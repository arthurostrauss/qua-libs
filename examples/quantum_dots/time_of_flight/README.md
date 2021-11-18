# Time Of Flight

The RF element of the the element field has a field called `time_of_flight` , which when playing the measurement pulse delays the sampling of the reflected signal for `time_of_flight` ns so that the OPX begins sampling just as it arrives back. 

There is an important subtly in the value of the time of flight. It is not the time between when the OPX outputs the first ns of the measurement pulse out of a analogy input port and the pulse returning to its respective output port. This is because the OPXs FPGA processor is responsible coordinating timings. 

For illustrative purposes the OPX FPGA outputs the first at `t=0` it sends the first digital value of the measurement waveform. This waveform then passes through the digital filter which allows for compensation which can take as long as 13ns. Next the digital waveform is passed to the DACs which synthesis it into the analogy waveform which is sent to the fridge. Therefore, the waveform begins propagating towards the fridge at `t ≈ 180` ns. Then the reflected waveform would return to the OPX some time later. The time of flight program is: 

### The Program 

The `time_of_flight` program can be constructed with the following function. 

```python
from qm.qua import *

def construct_time_of_fight(
	measured_element: str, 
	number_of_averages: int= 1000, 
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
            if wait_time > 4:
            	wait(wait_time // 4, measured_element)

        with stream_processing():
            adc_st.input1().average().save("in1")
            
    return time_of_flight_program
```

The program constructed by this function plays the pulse `measure` to the element passed as `measured_element` the samples of the reflected waveform will be sampled `time_of_flight` ns later and saved to the `adc_stream`. As each sample in this stream corresponds to integrating the returned signal for 1ns, to improve the signal to noise we repeat this `number_of_averages` times averaging iteration together for a greatly improved signal to noise, resetting the phase of the oscillators before each measurement, using the command `reset_phase(measured_element).` We wait `wait_time` ns between iterations to promote a clear separation between the measurement pulses to make it easier to determine the time of flight. 

With this program it is a case of changing the `time_of_flight` in the configuration dictionary such that the OPX starts measuring precisely when the reflected tone arrives back. 

