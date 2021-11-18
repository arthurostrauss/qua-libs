"""
Created on 11/11/2021
@author barnaby
"""

from .pulses import pulses


def get_length(pulse):
    return int(pulses.get(pulse).get('length') // 4)


integration_weights = {
    "measure_I": {"cosine": [1] * (get_length('measure')),
                  "sine": [0] * (get_length('measure'))},

    "measure_Q": {"cosine": [0] * (get_length('measure')),
                  "sine": [1] * (get_length('measure'))}
}