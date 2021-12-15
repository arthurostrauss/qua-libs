"""
Created on 15/12/2021
@author barnaby
"""
import numpy as np

def spiral(N: int):

    # casting to int if necessary
    if not isinstance(N, int): N = int(N)
    # asserting that N is odd
    N = N if N % 2 == 1 else N + 1

    # setting i, j to be in the middle of the image
    i, j = (N - 1) // 2, (N - 1) // 2

    # creating array to hold the ordering
    order = np.zeros(shape=(N, N), dtype=int)

    sign = +1 # the direction which to move along the respective axis
    number_of_moves = 1 # the number of moves needed for the current edge
    total_moves = 0 # the total number of moves completed so far

    # spiralling outwards along x edge then y
    while total_moves < N ** 2 - N:
        for _ in range(number_of_moves):
            i = i + sign # move one step in left (sign = -1) or right (sign = +1)
            total_moves = total_moves + 1
            order[i, j] = total_moves # updating the ordering array

        for _ in range(number_of_moves):
            j = j + sign # move one step in down (sign = -1) or up (sign = +1)
            total_moves = total_moves + 1
            order[i, j] = total_moves
        sign = sign * -1 # the next moves will be in the opposite direction
        number_of_moves = number_of_moves + 1 # the next edges will require one more step

    # filling the final x edge, which cannot cleanly be done in the above while loop
    for _ in range(number_of_moves - 1):
        i = i + sign # move one step in left (sign = -1) or right (sign = +1)
        total_moves = total_moves + 1
        order[i, j] = total_moves

    return order