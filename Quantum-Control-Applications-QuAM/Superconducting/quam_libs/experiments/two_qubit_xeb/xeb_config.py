from dataclasses import dataclass, field
from typing import Literal, List, Union, Optional, Dict

import numpy as np
from qiskit.transpiler import CouplingMap

from .gateset import QUAGateSet
from .qua_gate import QUAGate
from ...components import Transmon, TransmonPair
from .macros import get_parallel_gate_combinations as gate_combinations


@dataclass
class XEBConfig:
    """
    Experiments parameters for running XEB

    Args:
        seqs (int): Number of random sequences to run per depth
        depths (np.ndarray): Array of depths to iterate through
        n_shots (int): Number of averages per sequence
        qubits (List[Transmon]): List of active qubits to be used in the experiment
        baseline_gate_name (str): Name of the baseline gate implementing a pi/2 rotation around the x-axis (default "sx")
        gate_set_choice (Union[str, Dict[int, QUAGate]]): Choice of gate set for XEB (choose "sw" or "t") or a custom gate set as a dictionary of QUAGate objects
        two_qb_gate (Optional[QUAGate]): Two-qubit gate to be used in the experiment
        qubit_pairs (List[TransmonPair]): List of active qubit pairs to be used in the experiment (for now only one pair is supported)
        readout_pulse_name (str): Name of the readout pulse, should be common to all resonators and should match the name in QuAM (default "readout")
        reset_method (str): Method used to reset the qubits (choose "active" or "cooldown")
        reset_kwargs (Optional[Dict[str, Union[float, str, int]]]): Keyword arguments for the reset method (default {"cooldown_time": 20, "max_tries": None, "pi_pulse_name": None})
        save_dir (str): Directory where the data will be saved
        should_save_data (bool): Whether to save the data
        generate_new_data (bool): Whether to generate new data
        disjoint_processing (bool): Whether to process the data in a disjoint manner (that is compute qubit states independently, relevant only when no two-qubit gate is provided)


    """

    seqs: int
    depths: Union[np.ndarray, List[int]]
    n_shots: int
    readout_qubits: List[Transmon]
    qubits: List[Transmon]
    baseline_gate_name: str = "sx"
    gate_set_choice: Union[Literal["sw", "t"], Dict[int, QUAGate]] = "sw"
    two_qb_gate: Optional[QUAGate] = None
    qubit_pairs: Optional[List[TransmonPair]] = field(default_factory=lambda: [])
    readout_pulse_name: str = "readout"
    reset_method: Literal["active", "cooldown"] = "cooldown"
    reset_kwargs: Optional[Dict[str, Union[float, str, int]]] = field(
        default_factory=lambda: {
            "cooldown_time": 20,
            "max_tries": None,
            "pi_pulse": None,
        }
    )
    save_dir: str = ""
    should_save_data: bool = True
    data_folder_name: Optional[str] = None
    generate_new_data: bool = True
    disjoint_processing: bool = False

    def __post_init__(self):
        if isinstance(self.depths, List):
            self.depths = np.array(self.depths)

        self.gate_set = QUAGateSet(self.gate_set_choice, self.baseline_gate_name)
        self.n_qubits = len(self.qubits)
        self.dim = 2**self.n_qubits
        # Create CouplingMap from QuAM qubit pairs
        qubit_dict = {qubit: i for i, qubit in enumerate(self.qubits)}
        coupling_map = CouplingMap()
        for qubit in range(len(self.qubits)):
            coupling_map.add_physical_qubit(qubit)
        for qubit_pair in self.qubit_pairs:
            if qubit_pair.qubit_control not in self.qubits or qubit_pair.qubit_target not in self.qubits:
                raise ValueError("Qubit pairs must be formed by qubits present in the qubits list")
            coupling_map.add_edge(qubit_dict[qubit_pair.qubit_control], qubit_dict[qubit_pair.qubit_target])
        self.coupling_map = coupling_map
        self.available_combinations = gate_combinations(self.coupling_map)

    def as_dict(self):
        """
        Return the XEBConfig object as a dictionary
        """
        config_dict = {
            "seqs": self.seqs,
            "depths": self.depths,
            "n_shots": self.n_shots,
            "qubits": [qubit.name for qubit in self.qubits],
            "baseline_gate_name": self.baseline_gate_name,
            "gate_set_choice": self.gate_set_choice,
            "two_qb_gate": self.two_qb_gate.name,
            "qubit_pairs": [pair.name for pair in self.qubit_pairs],
            "coupling_map": list(self.coupling_map.get_edges()),
            "available_combinations": self.available_combinations,
        }
        return config_dict
