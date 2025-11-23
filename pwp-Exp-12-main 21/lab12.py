import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency in Hz
duration = 1  # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)  # Time array

# Frequencies
f1 = 5  # Frequency of first sine wave in Hz
f2 = 10  # Frequency of second sine wave in Hz

# Generate the sine wave signals
signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)

# Add the two signals together
combined_signal = signal1 + signal2

# Plot the result
plt.figure(figsize=(12, 6))
plt.plot(t, combined_signal)
plt.title('Combined Sine Wave Signal (5 Hz + 10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 1)  # Display full 1 second
plt.grid(True)
plt.tight_layout()
plt.show()
