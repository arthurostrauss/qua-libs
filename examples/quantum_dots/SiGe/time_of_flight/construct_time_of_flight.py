"""
Created on 11/11/2021
@author barnaby
"""

from qm.qua import *


def construct_time_of_fight(
        measured_element: str,
        number_of_averages: int = 1000,
        wait_time: int = 1000
):
    """
    @param measured_element: the element to measure the time of flight of
    @param number_of_averages: the number of averages to perform on the raw adc_trace
    @param wait_time: the time to wait between averages [ns]
    @return: time_of_flight_program
    """

    with program() as time_of_flight_program:
        n = declare(int)
        adc_st = declare_stream(adc_trace=True)
        with for_(n, 0, n < number_of_averages, n + 1):
            reset_phase(measured_element)
            measure('measure', measured_element, adc_st)
            if wait_time > 16:
                wait(wait_time // 4, measured_element)

        with stream_processing():
            adc_st.input1().average().save("in1")

    return time_of_flight_program
