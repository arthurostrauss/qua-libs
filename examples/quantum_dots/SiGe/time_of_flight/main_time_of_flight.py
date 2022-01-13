"""
Created on 11/11/2021
@author barnaby
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.simulate import SimulationConfig, LoopbackInterface

from construct_time_of_flight import construct_time_of_fight
from examples.quantum_dots.SiGe.configuration import config
import matplotlib.pyplot as plt

simulate = False
simulation_duration = 10000 # ns

program = construct_time_of_fight(
    measured_element='rf',
    wait_time=500,
    number_of_averages=5
)

qmm = QuantumMachinesManager()

if not simulate:
    pass
else:
    job = qmm.simulate(
        config=config,
        program=program,
        simulate=SimulationConfig(
            duration=int(simulation_duration // 4),
            include_analog_waveforms=True,
            simulation_interface=LoopbackInterface(
                latency = 280,
                connections = [('con1', 3, 'con1', 1)]  # connecting output 3 to input 1
            )
        )
    )

    # plotting the waveform outputted by the OPX
    plt.figure('simulated output samples')
    output_samples = job.get_simulated_samples()
    output_samples.con1.plot()
    plt.show()

    # plotting the sampled reflection
    plt.figure('simulated input samples')
    results_handles = job.result_handles
    input_samples = results_handles.in1.fetch_all()
    plt.plot(input_samples)
    plt.xlabel('Time [ns]')
    plt.ylabel('Amplitude [V]')
    plt.show()