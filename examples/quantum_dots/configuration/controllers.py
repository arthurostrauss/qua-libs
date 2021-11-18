"""
Created on 11/11/2021
@author barnaby
"""

controllers = {
    "con1": {
        "type": "opx1",
        "analog_outputs": {
            1: {"offset": 0.0, 'filter': {'feedback': [], 'feedforward': [1]}},
            2: {"offset": 0.0, 'filter': {'feedback': [], 'feedforward': [1]}},
            3: {"offset": 0.0, 'filter': {'feedback': [], 'feedforward': [1]}},
            4: {"offset": 0.0, 'filter': {'feedback': [], 'feedforward': [1]}}
        },
        "digital_outputs": {},
        "analog_inputs": {
            1: {"offset": 0.0}
        },
    }
}