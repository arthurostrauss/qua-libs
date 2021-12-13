import numpy as np
import matplotlib.pyplot as plt

N = 5
font_postion_correction = 0.06


plt.figure('Raster Scan')

X = np.arange(0, N ** 2).reshape(N, N)
plt.imshow(X.T, origin='lower')
for i, values in enumerate(X):
    for j, num in enumerate(values):
        plt.text(i - font_postion_correction, j - font_postion_correction, num)

plt.axis('off')
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
