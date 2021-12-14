from construct_do2d import construct_do0d
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.simulate import SimulationConfig, LoopbackInterface

from examples.quantum_dots.SiGe.configuration import config

# creating the do0d program
do0d = construct_do0d(
    x_element='LB',
    x_amplitude=0.1,
    y_element='RB',
    y_amplitude=0.1,
    resolution=11,
    measured_element='rf',
    number_of_averages=10
)

import matplotlib.pyplot as plt

simulation_duration = 200000  # ns

qmm = QuantumMachinesManager()

job = qmm.simulate(
    config=config,
    program=do0d,
    simulate=SimulationConfig(
        duration=int(simulation_duration // 4),
        include_analog_waveforms=True,
        simulation_interface=LoopbackInterface(
            latency=280,
            connections=[('con1', 4, 'con1', 1)]  # connecting output 4 to input 1
        )
    )
)
# plotting the waveform outputted by the OPX
plt.figure('simulated output samples')
output_samples = job.get_simulated_samples()
output_samples.con1.plot()
plt.show()
