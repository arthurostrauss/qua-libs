import numpy as np
import matplotlib.pyplot as plt

N = 101
font_postion_correction = 0.06

plt.figure('Raster Scan')

X = np.arange(0, N ** 2).reshape(N, N)
plt.imshow(X.T, origin='lower')
for i, values in enumerate(X):
    for j, num in enumerate(values):
        plt.text(i - font_postion_correction, j - font_postion_correction, num)

plt.axis('off')
plt.show()

measurement_time = 1000

output_1 = np.full(shape = (N ** 2 + 2, measurement_time), fill_value=0.)
output_2 = np.full(shape = (N ** 2 + 2, measurement_time), fill_value=0.)
output_3 = np.full(shape = (N ** 2 + 2, measurement_time), fill_value=0.)

for i, values in enumerate(X):
    for j, num in enumerate(values):
        output_1[num + 1, :] = np.full(measurement_time, fill_value=(i - (N - 1) / 2) / (N - 1))
        output_2[num + 1, :] = np.full(measurement_time, fill_value=(j - (N - 1) / 2) / (N - 1))
        output_3[num + 1, :] = np.concatenate([
            np.zeros(200), np.sin(np.linspace(0, 50, 600)) / 2, np.zeros(200)
        ])

def high_pass(X, tau):
    waveform_fft = np.fft.fft(X, axis=-1)
    fft_frequencies = np.fft.fftfreq(X.shape[-1], d=1)

    fft_scaling = (2j * np.pi * tau * fft_frequencies) / (1 + 2j * np.pi * tau * fft_frequencies)
    fft_scaling = np.power(fft_scaling, 1)
    fft_scaling[np.logical_or(np.isnan(fft_scaling), np.isinf(fft_scaling))] = 0

    waveform_fft = waveform_fft * fft_scaling
    waveforms = np.fft.ifft(waveform_fft)
    return np.real(waveforms)

output_1 = high_pass(output_1.flatten(), 6.2e9)
output_2 = high_pass(output_2.flatten(), 6.2e9)
output_3 = high_pass(output_3.flatten(), 6.2e9)

plt.figure('Raster Waveform')
plt.plot(output_1.flatten()[::100] + 1.1, label = 'analogy output 1')
plt.plot(output_2.flatten()[::100], label = 'analogy output 2')
plt.plot(output_3.flatten()[::100] - 1.1, label = 'analogy output 3')
plt.xlabel('time (ns)')
plt.ylabel('output voltage (V)')
plt.legend()
plt.show()

def spiral(N: int):
    N = N if N % 2 == 1 else N + 1
    i, j = (N - 1) // 2, (N - 1) // 2
    order = np.zeros(shape=(N, N), dtype=int)

    sign = +1
    number_of_moves = 1
    total_moves = 0
    while total_moves < N ** 2 - N:
        for _ in range(number_of_moves):
            i = i + sign
            total_moves = total_moves + 1
            order[i, j] = total_moves

        for _ in range(number_of_moves):
            j = j + sign
            total_moves = total_moves + 1
            order[i, j] = total_moves
        sign = sign * -1
        number_of_moves = number_of_moves + 1

    for _ in range(number_of_moves - 1):
        i = i + sign
        total_moves = total_moves + 1
        order[i, j] = total_moves

    return order

plt.figure('Spiral Scan')
order = spiral(N)
plt.imshow(order.T, origin='lower')
for i, values in enumerate(order):
    for j, num in enumerate(values):
        plt.text(i - font_postion_correction, j - font_postion_correction, num)

plt.axis('off')
plt.show()

output_1 = np.full(shape = (N ** 2 + 1, measurement_time), fill_value=0.)
output_2 = np.full(shape = (N ** 2 + 1, measurement_time), fill_value=0.)
output_3 = np.full(shape = (N ** 2 + 1, measurement_time), fill_value=0.)

for i, values in enumerate(order):
    for j, num in enumerate(values):
        output_1[num, :] = np.full(measurement_time, fill_value=(i - (N - 1) / 2) / (N - 1))
        output_2[num, :] = np.full(measurement_time, fill_value=(j - (N - 1) / 2) / (N - 1))
        output_3[num, :] = np.concatenate([
            np.zeros(200), np.sin(np.linspace(0, 50, 600)) / 2, np.zeros(200)
        ])

output_1 = high_pass(output_1.flatten(), 6.2e9)
output_2 = high_pass(output_2.flatten(), 6.2e9)
output_3 = high_pass(output_3.flatten(), 6.2e9)

plt.figure('Spiral Waveform')
plt.plot(output_1.flatten()[::100] + 1.1, label = 'analogy output 1')
plt.plot(output_2.flatten()[::100], label = 'analogy output 2')
plt.plot(output_3.flatten()[::100] - 1.1, label = 'analogy output 3')
plt.xlabel('time (ns)')
plt.ylabel('output voltage (V)')
plt.legend()
plt.show()