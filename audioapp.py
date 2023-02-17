import tkinter as tk
from tkinter import filedialog
import pyaudio
import wave

def select_file():
    # Ask the user to select an audio file
    file_path = filedialog.askopenfilename()

    # Open the selected audio file
    audio = wave.open(file_path, 'rb')

    # Store the audio data in a list
    audio_data = []
    for i in range(audio.getnframes()):
        audio_data.append(audio.readframes(1))

    # Close the audio file
    audio.close()

    # Play the audio data using pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(audio.getsampwidth()),
                    channels=audio.getnchannels(),
                    rate=audio.getframerate(),
                    output=True)
    for data in audio_data:
        stream.write(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

# Create a GUI window
window = tk.Tk()
window.geometry('400x300')
window.title('Audio Player')

# Add a button for selecting an audio file
select_file_btn = tk.Button(window, text='Select Audio File', command=select_file)
select_file_btn.pack()

# Start the GUI event loop
window.mainloop()
