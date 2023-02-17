import os
import pygame

# Import the Tkinter module for the GUI
from tkinter import *

# Initialize the pygame mixer
pygame.mixer.init()

# Create the main window for the app
root = Tk()
root.title("Audio App")

# Create a frame for the app
frame = Frame(root)
frame.pack()

# Function to play the audio file
def play_audio():
    # Load the audio file
    pygame.mixer.music.load("song.mp3")

    # Start playing the audio
    pygame.mixer.music.play()

# Function to pause the audio playback
def pause_audio():
    pygame.mixer.music.pause()

# Function to resume the audio playback
def resume_audio():
    pygame.mixer.music.unpause()

# Create a button to play the audio file
play_button = Button(frame, text="Play", command=play_audio)
play_button.pack(side=LEFT)

# Create a button to pause the audio playback
pause_button = Button(frame, text="Pause", command=pause_audio)
pause_button.pack(side=LEFT)

# Create a button to resume the audio playback
resume_button = Button(frame, text="Resume", command=resume_audio)
resume_button.pack(side=LEFT)

# Run the app
root.mainloop()
