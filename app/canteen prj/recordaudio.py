# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import pyttsx3
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

SpeakText("start now")
# Sampling frequency
freq = 44100

# Recording duration
duration = 4

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
# write("recording0.wav", freq, recording)

# Convert the NumPy array to audio file
wv.write("myaudio.wav", recording, freq, sampwidth=2)
SpeakText("Audio saved")