"""
Created on 14/12/2021
@author barnaby
"""

from qm.qua import *
from typing import Union, Callable

def round_to_fixed(x, number_of_bits=12):
    """
    function which rounds 'x' to 'number_of_bits' of precision to help reduce the accumulation of fixed point arithmetic errors
    """
    return round((2 ** number_of_bits) * x) / (2 ** number_of_bits)


def default_measuerement_macro(x_element, y_element, measured_element,
                               I, I_stream, Q, Q_stream):
    measure(
        "measure",
        measured_element,
        None,
        demod.full("measure_I", I),
        demod.full("measure_Q", Q),
    )
    save(I, I_stream)
    save(Q, Q_stream)


def construct_do0d(x_element: str,
                   x_amplitude: float,
                   y_element: str,
                   y_amplitude: float,
                   resolution: int,
                   measured_element: str,
                   number_of_averages: int,
                   measurement_macro: Union[Callable, None] = None,
                   wait_time: int =16):
    """
    @param x_element: the qua element to sweep on the x axis
    @param x_amplitude: the amplitude of the x axis sweep
    @param y_element: the qua element to sweep on the y axis
    @param y_amplitude: the amplitude of the y axis sweep
    @param resolution: the resolution of the x and y axis sweeps, must be odd.
    @param measured_element: the element to measure
    @param number_of_averages: the number of averages to perform
    @param measurement_macro: a callable function which performs a measurement after performing a user specified pulse sequence
    @param wait_time: the time in ns to wait between moving and calling the measurement macro.
    @return: do0d program
    """
    assert resolution % 2 == 1, 'the resolution must be odd {}'.format(resolution)

    # if no measurement_macro is passed, default to the macro which just measures the I and Q components without pulsing beforehand
    if measurement_macro is None:
        measurement_macro = default_measuerement_macro

    x_step_size = round_to_fixed(2 * x_amplitude / (resolution - 1))
    y_step_size = round_to_fixed(2 * y_amplitude / (resolution - 1))

    with program() as do0d:
        i = declare(int)  # an index variable for the x index
        j = declare(int)  # an index variable for the y index

        x = declare(float)  # a variable to keep track of the x coordinate
        y = declare(float)  # a variable to keep track of the x coordinate

        average = declare(int)  # an index variable for the average
        moves_per_edge = declare(int)  # the number of moves per edge [1, resolution]
        completed_moves = declare(int)  # the number of completed move [0, resolution ** 2]
        movement_direction = declare(fixed)  # which direction to move {-1., 1.}

        # declaring the measured variables and their streams
        I, Q = declare(fixed), declare(fixed)
        I_stream, Q_stream = declare_stream(), declare_stream()

        with for_(average, 0, average < number_of_averages, average + 1):

            # initialising variables
            assign(moves_per_edge, 1)
            assign(completed_moves, 0)
            assign(movement_direction, +1)
            assign(x, 0.)
            assign(y, 0.)

            # for the first pixel it is unnecessary to move before measuring
            measurement_macro.__call__(
                x_element=x_element, y_element=y_element, measured_element=measured_element,
                I=I, I_stream=I_stream, Q=Q, Q_stream=Q_stream
            )

            with while_(completed_moves < resolution * (resolution - 1)):
                # for_ loop to move the required number of moves in the x direction
                with for_(i, 0, i < moves_per_edge, i + 1):
                    assign(x, x + movement_direction * x_step_size / 2)  # updating the x location
                    # playing the constant pulse to move to the next pixel
                    play('jump' * amp(movement_direction * x_step_size), x_element)

                    # if the x coordinate should be x, ramp to zero to remove fixed point arithmetic errors accumulating
                    with if_(x == 0.):
                        ramp_to_zero(x_element)

                    align(x_element, y_element, measured_element)
                    if wait_time > 4:  # if logic to enable wait_time = 0 without error
                        wait(wait_time // 4, measured_element)  # // 4 so that the wait time can be passed in ns
                    measurement_macro.__call__(
                        x_element=x_element, y_element=y_element, measured_element=measured_element,
                        I=I, I_stream=I_stream, Q=Q, Q_stream=Q_stream
                    )

                # for_ loop to move the required number of moves in the y direction
                with for_(j, 0, j < moves_per_edge, j + 1):
                    assign(y, y + movement_direction * y_step_size / 2)
                    play('jump' * amp(movement_direction * y_step_size), y_element)

                    with if_(y == 0.):
                        ramp_to_zero(y_element)

                    align(x_element, y_element, measured_element)
                    if wait_time > 4:  # if logic to enable wait_time = 0 without error
                        wait(wait_time // 4, measured_element)  # // 4 so that the wait time can be passed in ns
                    measurement_macro.__call__(
                        x_element=x_element, y_element=y_element, measured_element=measured_element,
                        I=I, I_stream=I_stream, Q=Q, Q_stream=Q_stream
                    )

                # updating the variables
                assign(completed_moves, completed_moves + 2 * moves_per_edge)  # * 2 because moves in both x and y
                assign(movement_direction, movement_direction * -1)  # *-1 as subsequent steps in the opposite direction
                assign(moves_per_edge, moves_per_edge + 1)  # moving one row/column out so need one more move_per_edge

        # filling in the final x row, which was not covered by the previous for_ loop
        with for_(i, 0, i < moves_per_edge - 1, i + 1):
            play('jump' * amp(movement_direction * x_step_size), x_element)

            align(x_element, y_element, measured_element)
            if wait_time > 4:  # if logic to enable wait_time = 0 without error
                wait(wait_time // 4, measured_element)

            measurement_macro.__call__(
                x_element=x_element, y_element=y_element, measured_element=measured_element,
                I=I, I_stream=I_stream, Q=Q, Q_stream=Q_stream
            )

        # aligning and ramping to zero to return to inital state
        align(x_element, y_element, measured_element)
        ramp_to_zero(x_element)
        ramp_to_zero(y_element)

        with stream_processing():
            for stream_name, stream in zip(['I', 'Q'], [I_stream, Q_stream]):
                stream.buffer(resolution ** 2).save(stream_name)

        return do0d
