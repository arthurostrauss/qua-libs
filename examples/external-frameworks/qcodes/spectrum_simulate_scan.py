from qcodes.utils.validators import Arrays
from qcodes import (
    ParameterWithSetpoints,
)
from OPX_driver import *
from qm.qua import *


# noinspection PyAbstractClass
class Spectrum(ParameterWithSetpoints):
    def get_raw(self):
        self.root_instrument.n_points.get_latest()

        return self.root_instrument.simulate_and_read(self.root_instrument.get_prog())


# noinspection PyAbstractClass
class OPXSpectrumScan(OPX):
    def __init__(self, config: Dict, name: str = "OPX", host=None, port=None, **kwargs):
        super().__init__(config, name, host=host, port=port, **kwargs)
        self.add_parameter(
            "f_start",
            initial_value=0,
            unit="Hz",
            label="f start",
            vals=Numbers(0, 1e3),
            get_cmd=None,
            set_cmd=None,
        )

        self.add_parameter(
            "f_stop",
            unit="Hz",
            label="f stop",
            vals=Numbers(1, 1e3),
            get_cmd=None,
            set_cmd=None,
        )

        self.add_parameter(
            "n_points",
            unit="",
            initial_value=10,
            vals=Numbers(1, 1e3),
            get_cmd=None,
            set_cmd=None,
        )
        self.add_parameter(
            "n_avg",
            unit="",
            initial_value=3,
            vals=Numbers(1, 1e3),
            get_cmd=None,
            set_cmd=None,
        )

        self.add_parameter(
            "freq_axis",
            unit="Hz",
            label="Freq Axis",
            parameter_class=GeneratedSetPoints,
            startparam=self.f_start,
            stopparam=self.f_stop,
            numpointsparam=self.n_points,
            vals=Arrays(shape=(self.n_points.get_latest,)),
        )

        self.add_parameter(
            "ext_v",
            unit="V",
            label="ext_v",
            vals=Numbers(0, 1e3),
            get_cmd=None,
            set_cmd=None,
        )

        self.add_parameter(
            "spectrum",
            unit="V",
            setpoints=(self.freq_axis,),
            label="Spectrum",
            parameter_class=Spectrum,
            vals=Arrays(shape=(self.n_points.get_latest,)),
        )

    def get_prog(self):
        df = (self.f_stop() - self.f_start()) / self.n_points()
        with program() as prog:
            r = Random()
            vn = declare(int)
            N = declare(int)
            f = declare(int)
            I = declare(fixed)
            result_str = declare_stream()
            # with for_(vn,0,vn<voltage_pts,vn+1):
            with for_(f, self.f_start(), f < self.f_stop(), f + df):
                update_frequency("qe1", f)
                with for_(N, 0, N < self.n_avg(), N + 1):
                    measure("readout", "qe1", None, demod.full("x", I))
                    assign(I, r.rand_fixed())
                    save(I, result_str)

            with stream_processing():
                result_str.buffer(self.n_avg()).map(FUNCTIONS.average()).save_all(
                    "data"
                )

        return prog

    def get_res(self):
        if (
            self.result_handles is None
            or self.result_handles.get("data").fetch_all() is None
        ):
            return None
        else:
            return self.result_handles.get("data").fetch_all()["value"]
