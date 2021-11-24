# Frequency Sweep

For RF charge sensing we drive the charge sensor ohmic with an RF tone and measure the reflection. Changes in the device perturb the state of the charge sensor leading the a change in the reflected signal. 

We aim to choose the RF frequency such that the reflected signal is maximally sensitive to the state of the charge sensor and thus the device. When charged particles such as electrons or holes, in this case, are loaded or unloaded on the device this perturbs the electrostatic potential of the charge sensor. If the charge sensor gate voltages are chosen such that the position ourselves on the side of the charge sensors Colomb peak this small electrostatic perturbation can lead to a significant change in the reflected RF tone, if the RF frequency is chosen correctly. 

It is possible to induce a similar electrostatic perturbation in the charge sensors potential by perturbing one of the device gate voltages. Therefore, by sweeping the RF frequency and comparing the difference between the RF tone of the unperturbed and perturbed charge sensor we can find the optimal RF frequency. Ie the frequency which: 
$$
\max_\omega \sqrt{(I(\omega) - I_{pert}(\omega)) ^ 2 + (Q(\omega) - Q_{pert}(\omega)) ^ 2}
$$
where the $I(\omega)$ and $I_{pert}(\omega)$ are the demodulated in-phase components of the reflected RF tone at frequency $\omega$, for the unperturbed and perturbed charge sensor. Likewise,  $Q(\omega)$ and $Q_{pert}(\omega)$ are the out of phase components. 

### The Program 

The program to create the frequency sweep program is: 

```python
def construct_frequency_sweep_difference(
    element: str,
    start_frequency: float,
    stop_frequency: float,
    number_of_frequencies: int,
    preturbing_element: str,
    pertubation_amplitude: float,
    pertubation_wait_time: int = 0,
    number_of_averages: int = 1,
    outer_loop_wait: int = 0,
    inner_loop_wait: int = 0,
):
    """
    A function to construct a program to perform a frequency sweep over 'element'.

    @param element: the element to run the frequency sweep over
    @param start_frequency: the lower limit for the frequency sweep
    @param stop_frequency: the upper limit for the frequency sweep
    @param number_of_frequencies: the number of frequencies to sweep over
    @param number_of_averages: the number of averages per frequency
    @param outer_loop_wait: the time [ns] to wait between performing a subsequent average
    @param inner_loop_wait: the time [ns] to wait between changing frequency and measuring
    @return: the frequency sweep program
    """

    # enforcing start_frequency < stop_frequency
    if start_frequency > stop_frequency:
        start_frequency, stop_frequency = stop_frequency, start_frequency

    # the frequency step
    delta_frequency = (stop_frequency - start_frequency) / number_of_frequencies

    # creating the context manager to be complied by qua
    with program() as frequency_sweep_program:

        I = declare(fixed)  # the in-phase demodulated variable
        Q = declare(fixed)  # the out of phase demodulated variable

        I_perturbed = declare(fixed)  # the in-phase demodulated variable
        Q_perturbed = declare(fixed)  # the out of phase demodulated variable

        frequency = declare(int)  # the frequency
        average = declare(int)  # the averaging index

        I_stream = declare_stream()  # the stream to take the I component
        Q_stream = declare_stream()  # the stream to take the Q component
        I_perturbed_stream = declare_stream() # the stream to take the perturbed I component
        Q_perturbed_stream = declare_stream() # the stream to take the perturbed Q component

        # outer loop to average consecutive frequency sweeps together
        with for_(average, 0, average < number_of_averages, average + 1):

            # the inner loop to sweep across frequencies
            with for_(
                frequency,
                start_frequency,
                frequency < stop_frequency,
                frequency + delta_frequency,
            ):
                # changing the frequency frequency, the phase is reset to avoid sitting in the rotating frame
                update_frequency(element, new_frequency=frequency, keep_phase=False)
                # waiting inner_loop_wait before measuring
                if inner_loop_wait > 4:
                    wait(inner_loop_wait // 4, element)

                # measuring by demodulating to obtain the I and Q components
                measure(
                    "measure",
                    element,
                    None,
                    demod.full("integW1", I),
                    demod.full("integW2", Q),
                )
                # saving the variables I and Q to the respective streams
                for variable, stream in zip([I, Q], [I_stream, Q_stream])
                	save(variable, stream)

                play("constant" * amp(pertubation_amplitude), preturbing_element)
                # measuring by demodulating to obtain the I and Q components

                # waiting inner_loop_wait before measuring
                if pertubation_wait_time > 4:
                    wait(pertubation_wait_time, element)

                update_frequency(element, new_frequency=frequency, keep_phase=False)
                measure(
                    "measure",
                    element,
                    None,
                    demod.full("integW1", I_perturbed),
                    demod.full("integW2", Q_perturbed),
                )
                
                for variable, stream in zip([I_perturbed, Q_perturbed], [I_perturbed_stream, Q_perturbed_stream])
                	save(variable, stream)
                

            # waiting outer_loop_wait before performing the next average
            if outer_loop_wait > 4:
                wait(outer_loop_wait // 4, element)

        # declaring how the data should be processed
        with stream_processing():
            # process very stream in stream_handler the same way
            for stream_name, stream in zip(
                ["I", "Q", "I_perturbed", "Q_perturbed"],
                [I_stream, Q_stream, I_perturbed_stream, Q_perturbed_stream],
            ):
                # averaging the subsequent averages together
                stream.buffer(number_of_frequencies).average().save(stream_name)
                
    # returning the frequency sweep program to executed
    return frequency_sweep_program
```

