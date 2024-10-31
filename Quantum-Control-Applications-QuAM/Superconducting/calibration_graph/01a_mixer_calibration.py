# %%

"""
A simple program to calibrate Octave mixers for all qubits and resonators
"""

from typing import Optional
from qualibrate import QualibrationNode, NodeParameters

from quam_libs.components import QuAM


# %% {Node_parameters}
class Parameters(NodeParameters):
    target_qubitsOptional[str] = None
    calibrate_resonator: bool = True
    calibrate_drive: bool = True

node = QualibrationNode(
    name="00_Mixer_Calibration",
    parameters=Parameters()
)

# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()
qm = qmm.open_qm(config)

if node.parameters.target_qubits is None or node.parameters.target_qubits == '':
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.target_qubits.replace(' ', '').split(',')]

for qubit in qubits:
    qubit.calibrate_octave(qm,
                           calibrate_drive=node.parameters.calibrate_drive,
                           calibrate_resonator=node.parameters.calibrate_resonator)

qm.close()
# %%
