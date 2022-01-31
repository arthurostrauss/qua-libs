from time import time
from typing import Dict

import numpy as np
import time

from qcodes.utils.helpers import abstractmethod
from qcodes.utils.validators import Numbers
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig

from qcodes import (
    Instrument,
    Parameter,
)


# noinspection PyAbstractClass
class OPX(Instrument):
    """
    Driver for interacting with QM OPX
    """

    def __init__(
        self, config: Dict, name: str = "OPX", host=None, port=None, **kwargs
    ) -> None:
        """
        Args:
            name: Name to use internally in QCoDeS
        """
        super().__init__(name, **kwargs)

        self.config = None
        self.result_handles = None
        self.job = None
        self.set_config(config=config)
        self._connect(host=host, port=port)

        self.add_parameter("results", label="results", get_cmd=self.get_res)

        self.add_parameter(
            "sim_time",
            unit="ns",
            label="sim_time",
            initial_value=100000,
            vals=Numbers(
                4,
            ),
            get_cmd=None,
            set_cmd=None,
        )

    def simulate_and_read(self, prog):
        self.simulate_prog(prog, duration=self.sim_time())
        self.result_handles.wait_for_all_values()
        return self.get_res()

    @abstractmethod
    def get_res(self):
        pass

    def execute_prog(self, prog):
        self.job = self.qm.execute(prog)
        self.result_handles = self.job.result_handles

    def simulate_prog(self, prog, duration=1000):
        self.job = self.qm.simulate(prog, SimulationConfig(duration))
        self.result_handles = self.job.result_handles

    def set_config(self, config):
        self.config = config

    def _connect(self, host=None, port=None):
        begin_time = time.time()
        self.qmm = QuantumMachinesManager(host=host, port=port)
        self.qmm.close_all_quantum_machines()
        self.qm = self.qmm.open_qm(self.config)
        idn = {"vendor": "Quantum Machines", "model": "OPX"}
        idn.update(self.qmm.version())
        if idn["server"][0] == "2":
            idn["model"] = "OPX+"
        t = time.time() - (begin_time or self._t0)

        con_msg = (
            "Connected to: {vendor} {model}, client ver. = {client}, server ver. ={server} "
            "in {t:.2f}s".format(t=t, **idn)
        )
        print(con_msg)
        self.log.info(f"Connected to instrument: {idn}")


# noinspection PyAbstractClass
class GeneratedSetPoints(Parameter):
    """
    A parameter that generates a setpoint array from start, stop and num points
    parameters.
    """

    def __init__(self, startparam, stopparam, numpointsparam, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._startparam = startparam
        self._stopparam = stopparam
        self._numpointsparam = numpointsparam

    def get_raw(self):
        return np.linspace(
            self._startparam(), self._stopparam(), self._numpointsparam()
        )
