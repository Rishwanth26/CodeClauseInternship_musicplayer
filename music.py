import os
import pygame
from tkinter import Tk, Label, Button, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        self.current_file = None

        self.label = Label(master, text="Simple Music Player")
        self.label.pack()

        self.choose_button = Button(master, text="Choose Music", command=self.choose_music)
        self.choose_button.pack()

        self.play_button = Button(master, text="Play", command=self.play_music)
        self.play_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.quit_button = Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack()

    def choose_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.current_file = file_path
            self.label.config(text=f"Selected: {os.path.basename(file_path)}")

    def play_music(self):
        if self.current_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
        else:
            self.label.config(text="No music selected.")

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()