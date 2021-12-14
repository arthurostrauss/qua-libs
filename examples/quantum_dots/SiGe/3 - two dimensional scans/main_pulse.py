from construct_do2d import construct_do0d
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.simulate import SimulationConfig, LoopbackInterface
from qm.qua import *

from examples.quantum_dots.SiGe.configuration import config


# define a measurement macro which performs the pulse before measuring
def measuerement_macro(x_element, y_element, measured_element,
                       I, I_stream, Q, Q_stream):

    # jump downwards diagonally to initialise the spin state
    play('jump' * amp(+0.05), x_element, duration=100)
    play('jump' * amp(-0.05), y_element, duration=100)

    # jump upwards diagonally to potentially move to the S-T_ avoided crossing
    play('jump' * amp(-0.05), x_element, duration=100)
    play('jump' * amp(+0.05), y_element, duration=100)

    align(x_element, y_element, measured_element)

    # wait for 1us before measuring
    wait(1000 // 4, measured_element)

    measure(
        "measure",
        measured_element,
        None,
        demod.full("measure_I", I),
        demod.full("measure_Q", Q),
    )
    save(I, I_stream)
    save(Q, Q_stream)


# creating the do0d program
do0d = construct_do0d(
    x_element='LB',
    x_amplitude=0.1,
    y_element='RB',
    y_amplitude=0.1,
    resolution=11,
    measured_element='rf',
    number_of_averages=10,
    measurement_macro=measuerement_macro
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
