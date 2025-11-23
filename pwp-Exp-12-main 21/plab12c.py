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

# Shift the signal by 0.1 seconds
time_shift = 0.1  # seconds
t_shifted = t + time_shift
shifted_signal = np.sin(2 * np.pi * f * t_shifted)

# Plot both signals
plt.figure(figsize=(12, 6))
plt.plot(t, original_signal, label='Original Signal')
plt.plot(t, shifted_signal, label='Shifted Signal (by 0.1 s)', linestyle='--')
plt.title('Comparison of Original and Time-Shifted 5 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 1)  # Show full 1 second
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
