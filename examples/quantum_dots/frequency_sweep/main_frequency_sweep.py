"""
Created on 11/11/2021
@author barnaby
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.simulate import SimulationConfig, LoopbackInterface

from construct_frequency_sweep import construct_frequency_sweep

from examples.quantum_dots.configuration import config
import matplotlib.pyplot as plt

simulation_duration = 10000  # ns

program = construct_frequency_sweep(
    measured_element='rf', # the measured element to sweep the frequency over
    start_frequency=100e6, # the starting frequency in Hz
    stop_frequency=110e6, # the stop frequency in Hz
    number_of_frequencies=100, # the number of frequencies to sweep over
    perturbing_element='CSP', # the element to perturb the charge sensor with
    perturbation_amplitude=0.01, # how much to perturb the charge sensor by
    perturbation_wait_time=50, # how long to wait [ns]
    number_of_averages=1, # the number of averages to take for each frequency
)

qmm = QuantumMachinesManager()

job = qmm.simulate(
    config=config,
    program=program,
    simulate=SimulationConfig(
        duration=int(simulation_duration // 4),
        include_analog_waveforms=True,
        simulation_interface=LoopbackInterface(
            latency = 280,
            connections = [('con1', 4, 'con1', 1)]  # connecting output 4 to input 1
        )
    )
)

# plotting the waveform outputted by the OPX
plt.figure('simulated output samples')
output_samples = job.get_simulated_samples()
output_samples.con1.plot()
plt.show()
