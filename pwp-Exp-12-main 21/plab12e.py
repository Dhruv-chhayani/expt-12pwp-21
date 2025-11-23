import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  # Sampling frequency in Hz
duration = 1  # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)  # Time array

# Frequency
f = 5  # Frequency of the sine wave in Hz

# Generate the original sine wave
original_signal = np.sin(2 * np.pi * f * t)

# Reverse the signal in time
reversed_signal = original_signal[::-1]

# Plot both signals
plt.figure(figsize=(12, 6))
plt.plot(t, original_signal, label='Original Signal')
plt.plot(t, reversed_signal, label='Reversed Signal', linestyle='--')
plt.title('Original and Time-Reversed 5 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
