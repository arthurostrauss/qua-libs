# %%
import json
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np


def get_band(freq):
    if 50e6 <= freq < 5.5e9:
        return 1
    elif 4.5e9 <= freq < 7.5e9:
        return 2
    elif 6.5e9 <= freq <= 10.5e9:
        return 3
    else:
        raise ValueError(f"The specified frequency {freq} HZ is outside of the MW fem bandwidth [50 MHz, 10.5 GHz]")


path = "/Users/adamachuck/Documents/GitHub/ASQUM/qua-libs/Quantum-Control-Applications-QuAM/Superconducting/configuration/quam_state"
machine = QuAM.load()
u = unit(coerce_to_integer=True)

# %%
# Change active qubits
# machine.active_qubit_names = ["q0"]

# for i in range(len(machine.qubits.items())):
#     machine.qubits[f"q{i+1}"].grid_location = f"{i},0"

# Update frequencies
# rr_freq = np.array([5932987219.0, 6023928729.0, 5866936123.0, 6079048431.0, 5971697831.0]) #* u.GHz
# rr_LO = 5.95 * u.GHz
# rr_if = rr_freq - rr_LO
# rr_max_power_dBm = -20

# xy_freq = np.array([5108604110.9, 4834229255.6, 5146263353.0, 4674709204.1, 4880175329.7]) #* u.GHz
# xy_LO = np.array([6.0, 6.5, 6.5, 7.0, 7.04]) * u.GHz
# xy_LO = np.array([4.9]*5) * u.GHz
# xy_if = xy_freq - xy_LO
# xy_max_power_dBm = -2

# NOTE: be aware of coupled ports for bands
# for i, q in enumerate(machine.qubits):
#     ## Update qubit rr freq and power
#     machine.qubits[q].resonator.opx_output.full_scale_power_dbm = rr_max_power_dBm
#     machine.qubits[q].resonator.opx_output.upconverter_frequency = rr_LO
#     machine.qubits[q].resonator.opx_input.downconverter_frequency = rr_LO
#     machine.qubits[q].resonator.opx_input.band = get_band(rr_LO)
#     machine.qubits[q].resonator.opx_output.band = get_band(rr_LO)
#     machine.qubits[q].resonator.intermediate_frequency = rr_if[i]

#     ## Update qubit xy freq and power
#     machine.qubits[q].xy.opx_output.full_scale_power_dbm = xy_max_power_dBm
#     machine.qubits[q].xy.opx_output.upconverter_frequency = xy_LO[i]
#     machine.qubits[q].xy.opx_output.band = get_band(xy_LO[i])
#     machine.qubits[q].xy.intermediate_frequency = xy_if[i]

#     # Update flux channels
#     machine.qubits[q].z.opx_output.output_mode = "amplified"
#     machine.qubits[q].z.opx_output.upsampling_mode = "pulse"

#     ## Update pulses
#     # Readout
#     machine.qubits[q].resonator.operations["readout"].length = 2 * u.us
#     machine.qubits[q].resonator.operations["readout"].amplitude = 0.25
#     # Qubit saturation
#     machine.qubits[q].xy.operations["saturation"].length = 20 * u.us
#     machine.qubits[q].xy.operations["saturation"].amplitude = 0.5
#     # Single qubit gates - DragCosine
#     machine.qubits[q].xy.operations["x180_DragCosine"].length = 16
#     machine.qubits[q].xy.operations["x180_DragCosine"].amplitude = 0.8
#     machine.qubits[q].xy.operations["x90_DragCosine"].amplitude = (
#         machine.qubits[q].xy.operations["x180_DragCosine"].amplitude / 2
#     )
#     # Single qubit gates - Square
#     machine.qubits[q].xy.operations["x180_Square"].length = 40
#     machine.qubits[q].xy.operations["x180_Square"].amplitude = 0.1
#     machine.qubits[q].xy.operations["x90_Square"].amplitude = (
#         machine.qubits[q].xy.operations["x180_Square"].amplitude / 2
#     )

# %%
# for qp in machine.qubit_pairs.values():
#     qp.coupler.opx_output.output_mode = "amplified"
#     qp.coupler.opx_output.upsampling_mode = "pulse"

# %%
# machine.qubits["q1"].xy.thread = "a"
# machine.qubits["q2"].xy.thread = "b"
# machine.qubits["q3"].xy.thread = "c"
# machine.qubits["q4"].xy.thread = "d"
# machine.qubits["q5"].xy.thread = "e"

# machine.qubits["q1"].resonator.thread = "b"
# machine.qubits["q2"].resonator.thread = "c"
# machine.qubits["q3"].resonator.thread = "d"
# machine.qubits["q4"].resonator.thread = "e"
# machine.qubits["q5"].resonator.thread = "a"

# %%
q1 = machine.qubits["q1"]
q2 = machine.qubits["q2"]
q3 = machine.qubits["q3"]
q4 = machine.qubits["q4"]
q5 = machine.qubits["q5"]
print("\nsetting couplers's offset.........\n")

# q1.z.independent_offset = 0
# q2.z.independent_offset = 0
# q3.z.independent_offset = 0
# q4.z.independent_offset = 0
# q5.z.independent_offset = 0

(q4 @ q5).coupler.decouple_offset = -0.051 #-0.0515 
(q3 @ q4).coupler.decouple_offset = -0.053 #-0.0535
(q2 @ q3).coupler.decouple_offset = -0.03 #-0.0727
(q1 @ q2).coupler.decouple_offset = -0.01 #-0.0414 #to save q2's T2 #off:-0.0635 

# %%
# Add qubit pulses
# q1.z.operations["flux_pulse"] = pulses.SquarePulse(length=100, amplitude=0.1)
# q2.z.operations["flux_pulse"] = pulses.SquarePulse(length=100, amplitude=0.1)


# %%
# save into state.json
save_machine(machine, path)

# %%
# View the corresponding "raw-QUA" config
# with open("./Quantum-Control-Applications-QuAM/Superconducting/configuration/qua_config.json", "w+") as f:
#     json.dump(machine.generate_config(), f, indent=4)

# %%


