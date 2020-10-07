import librosa as lr
import numpy as np
import matplotlib.pyplot as plt
import timeit


#Reading file
song = './wav/starwars3.wav'
audio, sr = lr.load(song)

#Find BPM
tempo, beat_frames = lr.beat.beat_track(y=audio, sr=sr)
print(tempo)

#Find first chord


#Amplitude to time graph
time = np.arange(0, len(audio)) / sr
fig, ax = plt.subplots()
ax.plot(time, audio)

ax.set(xlabel='Time(s)', ylabel='Sound Amplitude')
plt.show()

