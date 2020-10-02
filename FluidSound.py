import librosa as lr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

song = './test/maadcity.wav'
audio, sfreq = lr.load(song, sr=10000)
time = np.arange(0, len(audio)) / sfreq
onset_env = lr.onset.onset_strength(audio, sr=sfreq)
tempo = lr.beat.tempo(onset_env, sr=sfreq)
print(tempo)

# fig, ax = plt.subplots()
# ax.plot(time, audio)

# ax.set(xlabel='Time(s)', ylabel='Sound Amplitude')
# plt.show()

