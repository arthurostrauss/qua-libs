import numpy as np

pulse_len = 32
pulse_len2 = 100
readout_len = 400
qubit_IF = 0
coupler_IF = 0
rr_IF = 50e6
qubit_LO = 6.345e9
rr_LO = 4.755e9
coupler_LO = 4.755e9


def gauss(amplitude, mu, sigma, length):
    t = np.linspace(-length / 2, length / 2, length)
    gauss_wave = amplitude * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
    return [float(x) for x in gauss_wave]


def IQ_imbalance(g, phi):
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g ** 2) * (2 * c ** 2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


gauss_pulse = gauss(0.2, 0, 12, pulse_len)

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": +0.0},  # qe1-I
                2: {"offset": +0.0},  # qe1-Q
                3: {"offset": +0.0},  # qe2-I
                4: {"offset": +0.0},  # qe2-Q
                5: {"offset": +0.0},  # coupler-I
                6: {"offset": +0.0},  # coupler-Q
                7: {"offset": +0.0},  # rr1-I
                8: {"offset": +0.0},  # rr1-Q
                9: {"offset": +0.0},  # rr2-I
                10: {"offset": +0.0},  # rr2-Q
            },
            "digital_outputs": {
                1: {},
            },
            "analog_inputs": {
                1: {"offset": +0.0},
                2: {"offset": +0.0},
            },
        }
    },
    "elements": {
        "q0": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": qubit_LO,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "I": "IPulse",
                "X/2": "X/2Pulse",
                "X": "XPulse",
                "-X/2": "-X/2Pulse",
                "Y/2": "Y/2Pulse",
                "Y": "YPulse",
                "-Y/2": "-Y/2Pulse",
            },
        },
        "q1": {
            "mixInputs": {
                "I": ("con1", 3),
                "Q": ("con1", 4),
                "lo_frequency": qubit_LO,
                "mixer": "mixer_qubit",

            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "I": "IPulse",
                "X/2": "X/2Pulse",
                "X": "XPulse",
                "-X/2": "-X/2Pulse",
                "Y/2": "Y/2Pulse",
                "Y": "YPulse",
                "-Y/2": "-Y/2Pulse",
            },
        },
        "coupler": {
            "mixInputs": {
                "I": ("con1", 5),
                "Q": ("con1", 6),
                "lo_frequency": coupler_LO,
                "mixer": "mixer_coupler",
            },
            "intermediate_frequency": coupler_IF,
            "operations": {
                "CZ": "constPulse",
            },
        },
        "rr1": {
            "mixInputs": {
                "I": ("con1", 7),
                "Q": ("con1", 8),
                "lo_frequency": rr_LO,
                "mixer": "mixer_RR",
            },
            "intermediate_frequency": rr_IF,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {"out1": ("con1", 1),
                        "out2": ("con1", 2)},
            "time_of_flight": 28,
            "smearing": 0,
        },
        "rr2": {
            "mixInputs": {
                "I": ("con1", 9),
                "Q": ("con1", 10),
                "lo_frequency": rr_LO,
                "mixer": "mixer_RR",
            },
            "intermediate_frequency": rr_IF,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {"out1": ("con1", 1),
                        "out2": ("con1", 2)},
            "time_of_flight": 28,
            "smearing": 0,
        },
    },
    "pulses": {
        "IPulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "zero_wf", "Q": "zero_wf"},
        },
        "constPulse": {
            "operation": "control",
            "length": pulse_len2,
            "waveforms": {"I": "const_wf", "Q": "zero_wf"},
        },
        "XPulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "pi_wf", "Q": "zero_wf"},
        },
        "X/2Pulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "pi/2_wf", "Q": "zero_wf"},
        },
        "-X/2Pulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "-pi/2_wf", "Q": "zero_wf"},
        },
        "YPulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "zero_wf", "Q": "pi_wf"},
        },
        "Y/2Pulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "zero_wf", "Q": "pi/2_wf"},
        },
        "-Y/2Pulse": {
            "operation": "control",
            "length": pulse_len,
            "waveforms": {"I": "zero_wf", "Q": "-pi/2_wf"},
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {"I": "readout_wf", "Q": "zero_wf"},
            "integration_weights": {
                "integW1": "integW1",
                "integW2": "integW2",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_pulse},
        "pi_wf": {"type": "arbitrary", "samples": gauss(0.2, 0, 12, pulse_len)},
        "-pi/2_wf": {"type": "arbitrary", "samples": gauss(-0.1, 0, 12, pulse_len)},
        "pi/2_wf": {"type": "arbitrary", "samples": gauss(0.1, 0, 12, pulse_len)},
        "zero_wf": {"type": "constant", "sample": 0},
        "readout_wf": {"type": "constant", "sample": 0.3},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "integW1": {
            "cosine": [1.0] * int(readout_len / 4),
            "sine": [0.0] * int(readout_len / 4),
        },
        "integW2": {
            "cosine": [0.0] * int(readout_len / 4),
            "sine": [1.0] * int(readout_len / 4),
        },
    },
    "mixers": {
        "mixer_qubit": [
            {
                "intermediate_frequency": qubit_IF,
                "lo_frequency": qubit_LO,
                "correction": IQ_imbalance(0.0, 0.0),
            }
        ],
        "mixer_coupler": [
            {
                "intermediate_frequency": coupler_IF,
                "lo_frequency": coupler_LO,
                "correction": IQ_imbalance(0.0, 0.0),
            }
        ],
        "mixer_RR": [
            {
                "intermediate_frequency": rr_IF,
                "lo_frequency": rr_LO,
                "correction": IQ_imbalance(0.0, 0.0),
            }
        ],
    },
}