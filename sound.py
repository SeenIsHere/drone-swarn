import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
import scipy.io.wavfile as wav
import json

NOTES_MAP = json.load(open("notes_map.json", "r"))

WAVE_LOCATION = "trimmed_hotlinebling.wav"
DURATION = 3  # Seconds
wav_file = open(WAVE_LOCATION, "rb")
SAMPLE_RATE, data = wav.read(wav_file)

# Plot the time domain
t = 1 * np.arange(SAMPLE_RATE*DURATION)

# print(t, data[:SAMPLE_RATE*DURATION])

yf = fft(data[:SAMPLE_RATE*DURATION])
xf = fftfreq(SAMPLE_RATE*DURATION, 1 / SAMPLE_RATE)

print(yf, xf)

for i in zip(xf, yf):
    

# plt.plot(xf, np.abs(yf))
# plt.xlim([0, 3e3])
# plt.show()

"""
yf = fft(data[:SAMPLE_RATE*DURATION])
xf = fftfreq(SAMPLE_RATE*DURATION, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.xlim([0, 3e3])
plt.show()
"""