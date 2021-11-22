"""
Created on 11/11/2021
@author barnaby
"""
import time

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.simulate import SimulationConfig, LoopbackInterface

from construct_frequency_sweep import construct_frequency_sweep

from examples.quantum_dots.configuration import config
import matplotlib.pyplot as plt
import numpy as np

simulation_duration = 10000  # ns

program = construct_frequency_sweep(
    measured_element='rf', # the measured element to sweep the frequency over
    start_frequency=90e6, # the starting frequency in Hz
    stop_frequency=130e6, # the stop frequency in Hz
    number_of_frequencies=1000, # the number of frequencies to sweep over
    perturbing_element='CSP', # the element to perturb the charge sensor with
    perturbation_amplitude=0.01, # how much to perturb the charge sensor by
    perturbation_wait_time=50, # how long to wait [ns] after perturbing the charge sensor before measuring
    number_of_averages=1000, # the number of averages to take for each frequency
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

run = False # set to true to run the program
if run:
    qm = qmm.open_qm(config)
    job = qm.execute(program=program)

    while job.result_handles.is_processing():
        time.sleep(0.01)

    frequency = job.result_handles.frequency.fetch_all()

    I = job.result_handles.I.fetch_all()
    Q = job.result_handles.Q.fetch_all()
    I_pert = job.result_handles.I_perturbed.fetch_all()
    Q_pert = job.result_handles.Q_perturbed.fetch_all()

    delta = np.sqrt((I - I_pert) ** 2 + (Q - Q_pert) **2)

    plt.figure('frequency_sweep results')
    plt.plot(frequency, delta)
    plt.xlabel('rf frequency [Hz]')
    plt.ylabel('Delta [V]')
    plt.show()


