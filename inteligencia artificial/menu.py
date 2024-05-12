import tkinter as tk
from tkinter import scrolledtext, ttk
import speech_recognition as sr
import pyttsx3
from PIL import Image, ImageTk

class VoiceRecognitionApp:
    def __init__(self, master):
        self.master = master
        master.title("Reconhecimento de Voz")
        master.configure(bg="#25274d")

        self.label = tk.Label(master, text="Selecione o idioma e pressione 'Iniciar' para começar a falar:", font=("Arial", 12), bg="#25274d", fg="white")
        self.label.pack(pady=10)

        self.language_frame = tk.Frame(master, bg="#25274d")
        self.language_frame.pack()

        self.language_label = tk.Label(self.language_frame, text="Idioma:", font=("Arial", 10), bg="#25274d", fg="white")
        self.language_label.grid(row=0, column=0, padx=5, pady=5)

        self.language_var = tk.StringVar(master)
        self.language_var.set("pt-BR")
        self.language_menu = ttk.Combobox(self.language_frame, textvariable=self.language_var, values=["pt-BR", "en-US"], font=("Arial", 10), width=8)
        self.language_menu.grid(row=0, column=1, padx=5, pady=5)

        self.textbox = scrolledtext.ScrolledText(master, height=10, width=50, font=("Arial", 12), bg="#0d1b2a", fg="white")
        self.textbox.pack(pady=10)

        self.icon_frame = tk.Frame(master, bg="#25274d")
        self.icon_frame.pack()

        self.listening_icon = self.load_icon("C:/Users/PC/Desktop/inteligencia artificial/img/ouvindo.png")
        self.not_listening_icon = self.load_icon("C:/Users/PC/Desktop/inteligencia artificial/img/microfone.png")

        self.icon_label = tk.Label(self.icon_frame, image=self.not_listening_icon, bg="#25274d")
        self.icon_label.pack(pady=5)

        self.button_frame = tk.Frame(master, bg="#25274d")
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Iniciar", command=self.start_recognition, font=("Arial", 12), bg="#4a4e69", fg="white")
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(self.button_frame, text="Parar", command=self.stop_recognition, state=tk.DISABLED, font=("Arial", 12), bg="#4a4e69", fg="white")
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)

        self.r = sr.Recognizer()
        self.stop_listening = None
        self.engine = pyttsx3.init()

    def load_icon(self, filename):
        icon = Image.open(filename)
        icon = icon.resize((64, 64))
        return ImageTk.PhotoImage(icon)

    def start_recognition(self):
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.textbox.delete(1.0, tk.END)

        language = self.language_var.get()
        self.icon_label.config(image=self.listening_icon)

        self.stop_listening = self.r.listen_in_background(sr.Microphone(), lambda recognizer, audio: self.callback(recognizer, audio, language))

    def stop_recognition(self):
        if self.stop_listening:
            self.stop_listening(wait_for_stop=False)
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.icon_label.config(image=self.not_listening_icon)

    def callback(self, recognizer, audio, language):
        try:
            text = recognizer.recognize_google(audio, language=language)
            self.textbox.insert(tk.END, text + "\n")
            self.textbox.see(tk.END)
        except sr.UnknownValueError:
            pass

def main():
    root = tk.Tk()
    root.geometry("400x500")
    app = VoiceRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
