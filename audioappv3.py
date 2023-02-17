import pyaudio
import wave

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open an audio stream
stream = p.open("song.wav", format=pyaudio.paInt16, channels=1, rate=16000, output=True)

# Start the audio playback
stream.start_stream()

# Open the audio file
with wave.open("song.wav", "rb") as f:
    # Read the audio data from the file
    data = f.readframes(1024)

    # Play the audio data using the stream
    while data:
        stream.write(data)
        data = f.readframes(1024)

# Pause the audio playback
stream.stop_stream()

# Resume the audio playback
stream.start_stream()

# Close the audio stream
stream.close()
