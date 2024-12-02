from qm.qua import *
from qualang_tools.bakery.bakery import Baking

from quam_libs.experiments.two_qubit_rb import TwoQubitRb, TwoQubitRbDebugger
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save
from quam_libs.macros import qua_declaration, readout_state

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Class containing tools to help handling units and conversions.
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)

# todo: make sure to install: cirq, xarray, tqdm

matplotlib.use("TKAgg")

machine = QuAM.load()
config = machine.generate_config()

# Get the relevant QuAM components
qubits = machine.active_qubits
num_qubits = len(qubits)

qc_index = 1  # i.e., qc = q1
qt_index = 2  # i.e., qt = q2
qc = machine.qubits[f"q{qc_index}"]
qt = machine.qubits[f"q{qt_index}"]

readout_qubits = [qubit for qubit in machine.qubits.values() if qubit not in [qc, qt]]


##############################
##  Two-qubit RB functions  ##
##############################
# single qubit generic gate constructor Z^{z}Z^{a}X^{x}Z^{-a}
# that can reach any point on the Bloch sphere (starting from arbitrary points)
def bake_phased_xz(baker: Baking, q, x, z, a):
    if q == 1:
        element = qc.xy.name
    else:
        element = qt.xy.name

    baker.frame_rotation_2pi(a / 2, element)
    baker.play("x180", element, amp=x)
    baker.frame_rotation_2pi(-(a + z) / 2, element)


# TODO: single qubit phase corrections in units of 2pi applied after the CZ gate
phi_to_flux_tune, phi_to_meet_with = 0, 0 #0.83, 0.52
qubit1_frame_update = phi_to_flux_tune #0.23  # example values, should be taken from QPU parameters
qubit2_frame_update = phi_to_meet_with #0.12  # example values, should be taken from QPU parameters


# defines the CZ gate that realizes the mapping |00> -> |00>, |01> -> |01>, |10> -> |10>, |11> -> -|11>
def bake_cz(baker: Baking, q1, q2):
    # print("q1,q2: %s,%s" %(q1,q2))
    qc_xy_element = qc.xy.name
    qt_xy_element = qt.xy.name
    
    try: coupler = (qc @ qt).coupler
    except: coupler = (qt @ qc).coupler
    
    ########### Pulsed Version
    # baker.wait(100 * u.ns)
    # baker.wait(24 * u.ns)
    baker.play(("cz%s_%s"%(qc.name,qt.name)).replace("q",""), qc.z.name)
    baker.play("cz", coupler.name)
    #############################
    
    # baker.wait(20 * u.ns)
    baker.align(qc.z.name, coupler.name, qc_xy_element, qt_xy_element)
    baker.frame_rotation_2pi(qubit1_frame_update, qc_xy_element)
    baker.frame_rotation_2pi(qubit2_frame_update, qt_xy_element)
    baker.align(qc.z.name, coupler.name, qc_xy_element, qt_xy_element)


def prep():
    machine.apply_all_flux_to_min()
    machine.apply_all_couplers_to_min()
    wait(machine.thermalization_time * u.ns)
    align()


def meas():
    # threshold1 = qc.resonator.operations["readout"].threshold  # threshold for state discrimination 0 <-> 1 using the I quadrature
    # threshold2 = qt.resonator.operations["readout"].threshold  # threshold for state discrimination 0 <-> 1 using the I quadrature

    # I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=len([qc, qt]))
    # state1 = declare(bool)
    # state2 = declare(bool)

    # for other_qubit in readout_qubits:
    #     other_qubit.resonator.play("readout")
    # multiplexed_readout([qc, qt], I, I_st, Q, Q_st)
        
    num_qubits = len(machine.qubits)

    state = [declare(int) for _ in range(num_qubits)]

    align()
    for i in range(num_qubits):
        readout_state(machine.qubits[f"q{i+1}"], state[i])

    return state[qc_index - 1], state[qt_index - 1]


##############################
##  Two-qubit RB execution  ##
##############################
# create RB experiment from configuration and defined functions
rb = TwoQubitRb(
    config=config,
    single_qubit_gate_generator=bake_phased_xz,
    two_qubit_gate_generators={"CZ": bake_cz},  # can also provide e.g. "CNOT": bake_cnot
    prep_func=prep,
    measure_func=meas,
    interleaving_gate=None,
    verify_generation=False,
)

qmm = machine.connect()

# run simpler experiment to verify `bake_phased_xz`, `prep` and `meas`
rb_debugger = TwoQubitRbDebugger(rb)
rb_debugger.run_phased_xz_commands(qmm, 280)
plt.show()

# run 2Q-RB experiment
# res = rb.run(qmm, circuit_depths=np.arange(1, 300, 5), num_circuits_per_depth=60, num_shots_per_circuit=30)
# circuit_depths ~ how many consecutive Clifford gates within one executed circuit
# (https://qiskit.org/documentation/apidoc/circuit.html)
# num_circuits_per_depth ~ how many random circuits within one depth
# num_shots_per_circuit ~ repetitions of the same circuit (averaging)

data = {}

res.plot_hist()
plt.show()

res.plot_with_fidelity()
plt.show()

A, alpha, B = res.fit_exponential()
fidelity = res.get_fidelity(alpha)
data["amplitude"] = A
data["decay_rate"] = alpha
data["mixed_state_probability"] = B
data["fidelity"] = fidelity
data["figure"] = plt.gcf()

node_save(machine, "two_qubit_randomized_benchmarking", data, additional_files=True)

# verify/save the random sequences created during the experiment
rb.save_sequences_to_file("sequences.txt")  # saves the gates used in each random sequence
# rb.save_command_mapping_to_file('commands.txt')  # saves mapping from "command id" to sequence
# rb.print_sequences()
# rb.print_command_mapping()
# rb.verify_sequences() # simulates random sequences to ensure they recover to ground state. takes a while...
