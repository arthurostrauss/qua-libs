import numpy as np

from construct_do2d import construct_do0d
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.simulate import SimulationConfig, LoopbackInterface
from qm.qua import *

from examples.quantum_dots.SiGe.configuration import config
from examples.quantum_dots.SiGe.do2d.spiral_order import spiral


# define a measurement macro which performs the pulse before measuring
def measuerement_macro(x_element, y_element, measured_element,
                       I, I_stream, Q, Q_stream):

    # jump downwards diagonally to initialise the spin state
    play('jump' * amp(+0.05), x_element, duration=100)
    play('jump' * amp(-0.05), y_element, duration=100)

    # jump upwards diagonally to potentially move to the S-T_ avoided crossing
    play('jump' * amp(-0.1), x_element, duration=100)
    play('jump' * amp(+0.1), y_element, duration=100)

    # return to initial value
    play('jump' * amp(+0.05), x_element, duration=100)
    play('jump' * amp(-0.05), y_element, duration=100)

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


# creating the do2d program
do0d = construct_do0d(
    x_element='LB',
    x_amplitude=0.1,
    y_element='RB',
    y_amplitude=0.1,
    resolution=11,
    measured_element='rf',
    number_of_averages=1,
    measurement_macro=measuerement_macro
)

import matplotlib.pyplot as plt

simulation_duration = 400000  # ns

qmm = QuantumMachinesManager()

job = qmm.simulate(
    config=config,
    program=do0d,
    simulate=SimulationConfig(
        duration=int(simulation_duration // 4),
        include_analog_waveforms=True,
        simulation_interface=LoopbackInterface(
            latency=280,
            connections=[('con1', 3, 'con1', 1)]  # connecting output 4 to input 1
        )
    )
)
# plotting the waveform outputted by the OPX
plt.figure('simulated output samples')
output_samples = job.get_simulated_samples()
output_samples.con1.plot()
plt.show()

# fetching the data
result_handles = job.result_handles
I_handle, Q_handle = result_handles.I, result_handles.Q
I, Q = I_handle.fetch_all(), Q_handle.fetch_all()

# reshaping the data into the correct order and shape
order = spiral(np.sqrt(I.size))
I = I[order]
Q = Q[order]
