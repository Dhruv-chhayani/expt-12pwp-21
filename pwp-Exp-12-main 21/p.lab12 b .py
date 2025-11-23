import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  # Sampling frequency in Hz
duration = 2  # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)  # Time array

# Frequencies
f1 = 5   # Frequency of sine wave in Hz
f2 = 10  # Frequency of cosine wave in Hz

# Generate the signals
sine_wave = np.sin(2 * np.pi * f1 * t)
cosine_wave = np.cos(2 * np.pi * f2 * t)

# Multiply the two signals element-wise
product_signal = sine_wave * cosine_wave

# Plot the result
plt.figure(figsize=(12, 6))
plt.plot(t, product_signal)
plt.title('Product of 5 Hz Sine Wave and 10 Hz Cosine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 2)  # Show full 2 seconds
plt.grid(True)
plt.tight_layout()
plt.show()
