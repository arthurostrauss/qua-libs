# Importing the necessary from qm
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm.qua import math
from qm import LoopbackInterface
from qm import SimulationConfig
import numpy as np
import matplotlib.pyplot as plt
import time

## Definition of the sample for Gaussian pulse
gauss_pulse_len = 20 # nsec
Amp=0.2     #Pulse Amplitude
gauss_arg = np.linspace(-3, 3, gauss_pulse_len)
gauss_wf = np.exp(-gauss_arg**2/2)
gauss_wf = Amp * gauss_wf / np.max(gauss_wf)
t_max = 0.500 #Maximum pulse duration
dt = 0.001 #timestep
N_t = int(t_max / dt) #Number of timesteps
N_max=3
a_max = 0.500 #Maximum amplitude
da = 0.001 #amplitude sweeping step
N_a = int(a_max / da) #Number of steps

## Setting up the configuration of the experimental setup
## Embedded in a Python dictionary
config = {
    'version': 1,

    'controllers': {  # Define the QM device and its outputs, in this case:
        'con1': {  # 2 analog outputs for the in-phase and out-of phase components
            'type': 'opx1',  # of the qubit (I & Q), and 2 other analog outputs for the coupled readout resonator
            'analog_outputs': {
                1: {'offset': 0.032},
                2: {'offset': 0.041},
                3: {'offset': -0.024},
                4: {'offset': 0.115},
            },
            'analog_inputs' : {
                1: {'offset': +0.0},

            }

        }
    },

    'elements': {  # Define the elements composing the quantum system, i.e the qubit+ readout resonator (RR)
        'qubit': {
            'mixInputs': {
                'I': ('con1', 1),  # Connect the component to one output of the OPX
                'Q': ('con1', 2),
                'lo_frequency': 5.10e7,
                'mixer': 'mixer_qubit'  ##Associate a mixer entity to control the IQ mixing process
            },
            'intermediate_frequency': 5.15e3,  # Resonant frequency of the qubit
            'operations': {  # Define the set of operations doable on the qubit, each operation is related
                'gauss_pulse': 'gauss_pulse_in'  # to a pulse
            },
        },
        'RR': {
            'mixInputs': {
                'I': ('con1', 3),
                'Q': ('con1', 4),
                'lo_frequency': 6.00e7,
                'mixer': 'mixer_res'
            },
            'intermediate_frequency': 6.12e3,
            'operations': {
                'meas_pulse': 'meas_pulse_in',
            },
            'time_of_flight': 28,  # Measurement parameters
            'smearing': 0,
            'outputs': {
                'out1': ('con1', 1)
            }

        },
    },

    'pulses': {  # Pulse definition
        'meas_pulse_in': {
            'operation': 'measurement',
            'length': 20,
            'waveforms': {
                'I': 'exc_wf',
                'Q': 'zero_wf'
            },
            'integration_weights': {
                'integW1': 'integW1',
                'integW2': 'integW2',
            },
            'digital_marker': 'marker1'
        },
        'gauss_pulse_in': {
            'operation': 'control',
            'length': 20,
            'waveforms': {
                'I': 'gauss_wf',
                'Q': 'zero_wf'
            },
        }
    },

    'waveforms': {
        'zero_wf': {
            'type': 'constant',
            'sample': 0.0
        },
        'exc_wf': {
                'type': 'constant',
                'sample': 0.479
        },

        'gauss_wf': {
                'type': 'arbitrary',
                'samples': gauss_wf.tolist()
        }

    },

    'digital_waveforms': {
        'marker1': {
            'samples': [(1, 4), (0, 2), (1, 1), (1, 0)]
        }
    },

    'integration_weights': {#Define integration weights for measurement demodulation
        'integW1': {
            'cosine': [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                       4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                       4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                       4.0, 4.0, 4.0, 4.0, 4.0, 4.0],
            'sine': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        },
        'integW2': {
            'cosine': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            'sine': [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                     4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                     4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                     4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
        }
    },

    'mixers': {  #Potential corrections to be brought related to the IQ mixing scheme
        'mixer_res': [
            {'intermediate_frequency': 6.12e3, 'lo_frequency': 6.00e7, 'correction': [1.0, 0.0, 0.0, 1.0]}
        ],
        'mixer_qubit': [
            {'intermediate_frequency': 5.15e3, 'lo_frequency': 5.10e7, 'correction': [1.0, 0.0, 0.0, 1.0]}
        ],
    }
}
qmManager = QuantumMachinesManager("3.122.60.129") # Reach OPX's IP address
my_qm = qmManager.open_qm(config)  #Generate a Quantum Machine based on the configuration described above

with program() as time_powerRabiProg:  #Mix up of the power and time Rabi QUA program
    I = declare(fixed)      #QUA variables declaration
    Q = declare(fixed)
    t = declare(fixed) #Sweeping parameter over the set of durations
    a = declare(fixed) #Sweeping parameter over the set of amplitudes
    Nrep = declare(int)  #Number of repetitions of the experiment


    with for_(a, 0.00, a <= a_max, a + da): #Sweep for varying amplitudes
        with for_(t, 0.00, t <= t_max, t + dt):  # Sweep from 0 to 50 *4 ns the pulse duration
            with for_(Nrep, 0, Nrep < N_max, Nrep + 1):  # Do a 100 times the experiment to obtain statistics
                play('gauss_pulse'*amp(a), 'qubit',duration=t)
                align("qubit", "RR")
                measure('meas_pulse', 'RR', 'samples', ('integW1', I), ('integW2', Q))
                save(I, 'I')
                save(Q, 'Q')
            save(t, 't')
        save(a, 'a')



my_job = my_qm.simulate(time_powerRabiProg,
                   SimulationConfig(int(4000),simulation_interface=LoopbackInterface([("con1", 1, "con1", 1)])))
time.sleep(1.0)
my_timeRabi_results = my_job.result_handles
I1=my_timeRabi_results.I.fetch_all()['value']
Q1=my_timeRabi_results.Q.fetch_all()['value']
t1=my_timeRabi_results.t.fetch_all()['value']
a1=my_timeRabi_results.a.fetch_all()['value']
samples = my_job.get_simulated_samples()
samples.con1.plot()
#plt.plot(dat['timestamp'],dat['value'])
#plt.show()