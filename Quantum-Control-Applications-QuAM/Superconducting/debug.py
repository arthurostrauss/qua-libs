
# Single QUA script generated at 2024-11-01 15:26:30.938003
# QUA library version: 1.2.1a2

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(fixed, )
    v11 = declare(fixed, )
    v12 = declare(fixed, )
    v13 = declare(int, )
    align()
    set_dc_offset("q1.z", "single", 0.45)
    set_dc_offset("q2.z", "single", 0.4)
    set_dc_offset("q3.z", "single", 0.0)
    set_dc_offset("q4.z", "single", 0.0)
    set_dc_offset("q5.z", "single", 0.0)
    align()
    set_dc_offset("coupler_q1_q2", "single", 0.0)
    set_dc_offset("coupler_q2_q3", "single", 0.0)
    set_dc_offset("coupler_q3_q4", "single", 0.0)
    set_dc_offset("coupler_q4_q5", "single", 0.0)
    align()
    align()
    set_dc_offset("q1.z", "single", 0.09500470400796164)
    with for_(v1,0,(v1<10),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v12,-0.5,(v12<0.505),(v12+0.010000000000000009)):
            set_dc_offset("q1.z", "single", v12)
            align("q1.xy", "q1.z", "q1.resonator")
            with for_(v13,-11500000,(v13<=11400000),(v13+100000)):
                update_frequency("q1.resonator", (v13+-23012781.0), "Hz", False)
                measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v7))
                wait(250, "q1.resonator")
                r2 = declare_stream()
                save(v2, r2)
                r7 = declare_stream()
                save(v7, r7)
    align("q1.resonator", "q2.resonator", "q3.resonator", "q4.resonator", "q5.resonator")
    align()
    set_dc_offset("q1.z", "single", 0.45)
    set_dc_offset("q2.z", "single", 0.4)
    set_dc_offset("q3.z", "single", 0.0)
    set_dc_offset("q4.z", "single", 0.0)
    set_dc_offset("q5.z", "single", 0.0)
    align()
    set_dc_offset("coupler_q1_q2", "single", 0.0)
    set_dc_offset("coupler_q2_q3", "single", 0.0)
    set_dc_offset("coupler_q3_q4", "single", 0.0)
    set_dc_offset("coupler_q4_q5", "single", 0.0)
    align()
    align()
    set_dc_offset("q2.z", "single", 0.08333570267122505)
    with for_(v1,0,(v1<10),(v1+1)):
        save(v1, r1)
        with for_(v12,-0.5,(v12<0.505),(v12+0.010000000000000009)):
            set_dc_offset("q2.z", "single", v12)
            align("q2.xy", "q2.z", "q2.resonator")
            with for_(v13,-11500000,(v13<=11400000),(v13+100000)):
                update_frequency("q2.resonator", (v13+70304257.0), "Hz", False)
                measure("readout", "q2.resonator", None, dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v8))
                wait(250, "q2.resonator")
                r3 = declare_stream()
                save(v3, r3)
                r8 = declare_stream()
                save(v8, r8)
    align("q1.resonator", "q2.resonator", "q3.resonator", "q4.resonator", "q5.resonator")
    align()
    set_dc_offset("q1.z", "single", 0.45)
    set_dc_offset("q2.z", "single", 0.4)
    set_dc_offset("q3.z", "single", 0.0)
    set_dc_offset("q4.z", "single", 0.0)
    set_dc_offset("q5.z", "single", 0.0)
    align()
    set_dc_offset("coupler_q1_q2", "single", 0.0)
    set_dc_offset("coupler_q2_q3", "single", 0.0)
    set_dc_offset("coupler_q3_q4", "single", 0.0)
    set_dc_offset("coupler_q4_q5", "single", 0.0)
    align()
    align()
    set_dc_offset("q3.z", "single", 0.11550821181590695)
    with for_(v1,0,(v1<10),(v1+1)):
        save(v1, r1)
        with for_(v12,-0.5,(v12<0.505),(v12+0.010000000000000009)):
            set_dc_offset("q3.z", "single", v12)
            align("q3.xy", "q3.z", "q3.resonator")
            with for_(v13,-11500000,(v13<=11400000),(v13+100000)):
                update_frequency("q3.resonator", (v13+-86963877.0), "Hz", False)
                measure("readout", "q3.resonator", None, dual_demod.full("iw1", "iw2", v4), dual_demod.full("iw3", "iw1", v9))
                wait(250, "q3.resonator")
                r4 = declare_stream()
                save(v4, r4)
                r9 = declare_stream()
                save(v9, r9)
    align("q1.resonator", "q2.resonator", "q3.resonator", "q4.resonator", "q5.resonator")
    align()
    set_dc_offset("q1.z", "single", 0.45)
    set_dc_offset("q2.z", "single", 0.4)
    set_dc_offset("q3.z", "single", 0.0)
    set_dc_offset("q4.z", "single", 0.0)
    set_dc_offset("q5.z", "single", 0.0)
    align()
    set_dc_offset("coupler_q1_q2", "single", 0.0)
    set_dc_offset("coupler_q2_q3", "single", 0.0)
    set_dc_offset("coupler_q3_q4", "single", 0.0)
    set_dc_offset("coupler_q4_q5", "single", 0.0)
    align()
    align()
    set_dc_offset("q4.z", "single", 0.09822352841747865)
    with for_(v1,0,(v1<10),(v1+1)):
        save(v1, r1)
        with for_(v12,-0.5,(v12<0.505),(v12+0.010000000000000009)):
            set_dc_offset("q4.z", "single", v12)
            align("q4.xy", "q4.z", "q4.resonator")
            with for_(v13,-11500000,(v13<=11400000),(v13+100000)):
                update_frequency("q4.resonator", (v13+128375329.0), "Hz", False)
                measure("readout", "q4.resonator", None, dual_demod.full("iw1", "iw2", v5), dual_demod.full("iw3", "iw1", v10))
                wait(250, "q4.resonator")
                r5 = declare_stream()
                save(v5, r5)
                r10 = declare_stream()
                save(v10, r10)
    align("q1.resonator", "q2.resonator", "q3.resonator", "q4.resonator", "q5.resonator")
    align()
    set_dc_offset("q1.z", "single", 0.45)
    set_dc_offset("q2.z", "single", 0.4)
    set_dc_offset("q3.z", "single", 0.0)
    set_dc_offset("q4.z", "single", 0.0)
    set_dc_offset("q5.z", "single", 0.0)
    align()
    set_dc_offset("coupler_q1_q2", "single", 0.0)
    set_dc_offset("coupler_q2_q3", "single", 0.0)
    set_dc_offset("coupler_q3_q4", "single", 0.0)
    set_dc_offset("coupler_q4_q5", "single", 0.0)
    align()
    align()
    set_dc_offset("q5.z", "single", 0.030506361083241233)
    with for_(v1,0,(v1<10),(v1+1)):
        save(v1, r1)
        with for_(v12,-0.5,(v12<0.505),(v12+0.010000000000000009)):
            set_dc_offset("q5.z", "single", v12)
            align("q5.xy", "q5.z", "q5.resonator")
            with for_(v13,-11500000,(v13<=11400000),(v13+100000)):
                update_frequency("q5.resonator", (v13+21804454.0), "Hz", False)
                measure("readout", "q5.resonator", None, dual_demod.full("iw1", "iw2", v6), dual_demod.full("iw3", "iw1", v11))
                wait(250, "q5.resonator")
                r6 = declare_stream()
                save(v6, r6)
                r11 = declare_stream()
                save(v11, r11)
    align("q1.resonator", "q2.resonator", "q3.resonator", "q4.resonator", "q5.resonator")
    with stream_processing():
        r1.save("n")
        r2.buffer(230).buffer(101).average().save("I1")
        r7.buffer(230).buffer(101).average().save("Q1")
        r3.buffer(230).buffer(101).average().save("I2")
        r8.buffer(230).buffer(101).average().save("Q2")
        r4.buffer(230).buffer(101).average().save("I3")
        r9.buffer(230).buffer(101).average().save("Q3")
        r5.buffer(230).buffer(101).average().save("I4")
        r10.buffer(230).buffer(101).average().save("Q4")
        r6.buffer(230).buffer(101).average().save("I5")
        r11.buffer(230).buffer(101).average().save("Q5")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                    },
                },
                "1": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "2": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "3": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "4": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "5": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "6": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "7": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "8": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                    },
                },
                "6": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 5950000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4900000000.0,
                        },
                        "3": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4900000000.0,
                        },
                        "4": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4900000000.0,
                        },
                        "5": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4900000000.0,
                        },
                        "6": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4900000000.0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "downconverter_frequency": 5950000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "q1.xy": {
            "operations": {
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "saturation": "q1.xy.saturation.pulse",
            },
            "intermediate_frequency": 208089468.72514498,
            "thread": "a",
            "MWInput": {
                "port": ('con1', 6, 2),
                "upconverter": 1,
            },
        },
        "q1.z": {
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 1),
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": -23012781.0,
            "thread": "a",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
        },
        "q2.xy": {
            "operations": {
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "saturation": "q2.xy.saturation.pulse",
            },
            "intermediate_frequency": -62911194.0373852,
            "thread": "b",
            "MWInput": {
                "port": ('con1', 6, 3),
                "upconverter": 1,
            },
        },
        "q2.z": {
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": 70304257.0,
            "thread": "b",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
        },
        "q3.xy": {
            "operations": {
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "saturation": "q3.xy.saturation.pulse",
            },
            "intermediate_frequency": 246263353.0,
            "thread": "c",
            "MWInput": {
                "port": ('con1', 6, 4),
                "upconverter": 1,
            },
        },
        "q3.z": {
            "operations": {
                "const": "q3.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 2),
            },
        },
        "q3.resonator": {
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "intermediate_frequency": -86963877.0,
            "thread": "c",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
        },
        "q4.xy": {
            "operations": {
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "saturation": "q4.xy.saturation.pulse",
            },
            "intermediate_frequency": -225290795.89999962,
            "thread": "d",
            "MWInput": {
                "port": ('con1', 6, 5),
                "upconverter": 1,
            },
        },
        "q4.z": {
            "operations": {
                "const": "q4.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 3),
            },
        },
        "q4.resonator": {
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "intermediate_frequency": 128375329.0,
            "thread": "d",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
        },
        "q5.xy": {
            "operations": {
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180_Square": "q5.xy.x180_Square.pulse",
                "x90_Square": "q5.xy.x90_Square.pulse",
                "-x90_Square": "q5.xy.-x90_Square.pulse",
                "y180_Square": "q5.xy.y180_Square.pulse",
                "y90_Square": "q5.xy.y90_Square.pulse",
                "-y90_Square": "q5.xy.-y90_Square.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "saturation": "q5.xy.saturation.pulse",
            },
            "intermediate_frequency": -19824670.30000019,
            "thread": "e",
            "MWInput": {
                "port": ('con1', 6, 6),
                "upconverter": 1,
            },
        },
        "q5.z": {
            "operations": {
                "const": "q5.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 4),
            },
        },
        "q5.resonator": {
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "intermediate_frequency": 21804454.0,
            "thread": "e",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
        },
        "coupler_q1_q2": {
            "operations": {
                "const": "coupler_q1_q2.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 5),
            },
        },
        "coupler_q2_q3": {
            "operations": {
                "const": "coupler_q2_q3.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 6),
            },
        },
        "coupler_q3_q4": {
            "operations": {
                "const": "coupler_q3_q4.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 7),
            },
        },
        "coupler_q4_q5": {
            "operations": {
                "const": "coupler_q4_q5.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 8),
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "q1.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
        },
        "q1.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
        },
        "q1.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
        },
        "q1.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
        },
        "q1.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
        },
        "q1.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
        },
        "q1.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
        },
        "q1.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
        },
        "q1.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
        },
        "q1.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
        },
        "q1.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
        },
        "q2.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
        },
        "q2.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
        },
        "q2.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
        },
        "q2.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
        },
        "q2.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
        },
        "q2.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
        },
        "q2.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
        },
        "q2.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
        },
        "q2.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
        },
        "q2.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
        },
        "q3.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
        },
        "q3.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
        },
        "q3.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
        },
        "q3.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
        },
        "q3.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
        },
        "q3.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
        },
        "q3.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
        },
        "q3.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
        },
        "q3.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
        },
        "q3.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q3.z.const.wf",
            },
        },
        "q3.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
        },
        "q3.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
        },
        "q4.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
        },
        "q4.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
        },
        "q4.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
        },
        "q4.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
        },
        "q4.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
        },
        "q4.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
        },
        "q4.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
        },
        "q4.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
        },
        "q4.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
        },
        "q4.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q4.z.const.wf",
            },
        },
        "q4.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
        },
        "q4.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
        },
        "q5.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
        },
        "q5.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
        },
        "q5.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 16,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_Square.wf.I",
                "Q": "q5.xy.x180_Square.wf.Q",
            },
        },
        "q5.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_Square.wf.I",
                "Q": "q5.xy.x90_Square.wf.Q",
            },
        },
        "q5.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_Square.wf.I",
                "Q": "q5.xy.-x90_Square.wf.Q",
            },
        },
        "q5.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_Square.wf.I",
                "Q": "q5.xy.y180_Square.wf.Q",
            },
        },
        "q5.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_Square.wf.I",
                "Q": "q5.xy.y90_Square.wf.Q",
            },
        },
        "q5.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-y90_Square.wf.I",
                "Q": "q5.xy.-y90_Square.wf.Q",
            },
        },
        "q5.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
        },
        "q5.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q5.z.const.wf",
            },
        },
        "q5.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.resonator.readout.wf.I",
                "Q": "q5.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q5.resonator.readout.iw1",
                "iw2": "q5.resonator.readout.iw2",
                "iw3": "q5.resonator.readout.iw3",
            },
        },
        "q5.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
        },
        "coupler_q1_q2.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "coupler_q1_q2.const.wf",
            },
        },
        "coupler_q2_q3.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "coupler_q2_q3.const.wf",
            },
        },
        "coupler_q3_q4.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "coupler_q3_q4.const.wf",
            },
        },
        "coupler_q4_q5.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "coupler_q4_q5.const.wf",
            },
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.006938473070531523, 0.026575320436731595, 0.05557680821785938, 0.089024940270466, 0.12125829566060296, 0.14683725985313936, 0.16146704527579697, 0.16271994919256233, 0.15043392276080286, 0.12672133195073712, 0.09558969105422982, 0.06224317168956327, 0.03218811498910038, 0.010298207981334826, 1.0399376501033949e-17],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.01092463001658052, -0.020933821738006377, -0.029163145786415153, -0.03485965938251483, -0.03745652223413811, -0.03665820475184714, -0.032523540796892014, -0.02552656559024921, -0.016572258132298207, -0.006947614916055114, 0.001801889725233215, 0.008065870186655529, 0.010411426526756203, 0.007838167000187921, 2.810713702097524e-17],
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0071117628498714325, 0.027217362994405744, 0.0568403595149698, 0.09085866719668322, 0.12339021159475454, 0.14880999314295446] + [0.16272270068013356] * 2 + [0.14880999314295446, 0.12339021159475459, 0.09085866719668328, 0.056840359514969824, 0.027217362994405726, 0.0071117628498714325, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0071117628498714325, -0.027217362994405744, -0.0568403595149698, -0.09085866719668322, -0.12339021159475454, -0.14880999314295446] + [-0.16272270068013356] * 2 + [-0.14880999314295446, -0.12339021159475459, -0.09085866719668328, -0.056840359514969824, -0.027217362994405726, -0.0071117628498714325, 0.0],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 8.709397610390108e-19, 3.3331656472330614e-18, 6.960936434239257e-18, 1.1126977595721272e-17, 1.5110942767563078e-17, 1.8223968178365874e-17] + [1.992778345365384e-17] * 2 + [1.8223968178365874e-17, 1.5110942767563084e-17, 1.1126977595721281e-17, 6.96093643423926e-18, 3.3331656472330594e-18, 8.709397610390108e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.01092463001658052, 0.020933821738006377, 0.029163145786415157, 0.034859659382514833, 0.03745652223413812, 0.03665820475184715, 0.03252354079689202, 0.025526565590249222, 0.016572258132298217, 0.006947614916055122, -0.001801889725233209, -0.008065870186655525, -0.0104114265267562, -0.007838167000187921, -2.810713702097524e-17],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.006938473070531522, 0.026575320436731595, 0.05557680821785938, 0.089024940270466, 0.12125829566060296, 0.14683725985313936, 0.16146704527579697, 0.16271994919256233, 0.15043392276080286, 0.12672133195073712, 0.09558969105422982, 0.06224317168956327, 0.03218811498910038, 0.010298207981334826, 1.039937650103395e-17],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.354698805195054e-19, 1.6665828236165307e-18, 3.4804682171196286e-18, 5.563488797860636e-18, 7.555471383781539e-18, 9.111984089182937e-18] + [9.96389172682692e-18] * 2 + [9.111984089182937e-18, 7.555471383781542e-18, 5.5634887978606404e-18, 3.48046821711963e-18, 1.6665828236165297e-18, 4.354698805195054e-19, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0071117628498714325, 0.027217362994405744, 0.0568403595149698, 0.09085866719668322, 0.12339021159475454, 0.14880999314295446] + [0.16272270068013356] * 2 + [0.14880999314295446, 0.12339021159475459, 0.09085866719668328, 0.056840359514969824, 0.027217362994405726, 0.0071117628498714325, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.354698805195054e-19, 1.6665828236165307e-18, 3.4804682171196286e-18, 5.563488797860636e-18, 7.555471383781539e-18, 9.111984089182937e-18] + [9.96389172682692e-18] * 2 + [9.111984089182937e-18, 7.555471383781542e-18, 5.5634887978606404e-18, 3.48046821711963e-18, 1.6665828236165297e-18, 4.354698805195054e-19, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0071117628498714325, -0.027217362994405744, -0.0568403595149698, -0.09085866719668322, -0.12339021159475454, -0.14880999314295446] + [-0.16272270068013356] * 2 + [-0.14880999314295446, -0.12339021159475459, -0.09085866719668328, -0.056840359514969824, -0.027217362994405726, -0.0071117628498714325, 0.0],
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q1.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.38516042695567315,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.010324063270704151, 0.03953994133885332, 0.08268110886952187, 0.13242511881954014, 0.18035037931151743, 0.21837610832807786, 0.24013514085533222, 0.24204247693067574, 0.2238773073617527, 0.1887827117498417, 0.1426896934711177, 0.09327238133201989, 0.04862137333449968, 0.01586839419462579, 1.7518570245704744e-17],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.016031345139013987, -0.030974818090574553, -0.043745244996335766, -0.05329407968661518, -0.05869487210422391, -0.059281604536029146, -0.0548192506712861, -0.045667006460188043, -0.03288441231547024, -0.018232802130106703, -0.004040099148673168, 0.007076376497716886, 0.012601919373307643, 0.010572813015827744, 4.0205490885333685e-17],
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.010689140798121534, 0.04090831364069532, 0.08543234901067365, 0.13656263670442423, 0.1854582854756164, 0.22366479344868706] + [0.2445759082998639] * 2 + [0.22366479344868706, 0.1854582854756165, 0.13656263670442434, 0.08543234901067367, 0.04090831364069529, 0.010689140798121534, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.028099272145259434, -0.05133992486273004, -0.06570343816285948, -0.06870623010763355, -0.059829090690292394, -0.040606957962374124, -0.01436351330012944, 0.014363513300129423, 0.0406069579623741, 0.059829090690292366, 0.06870623010763355, 0.06570343816285949, 0.05133992486273003, 0.028099272145259434, 7.828039201518187e-17],
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.009931110484846163, -0.03809263715844657, -0.07986000361377403, -0.1283827090432651, -0.17571801269599083, -0.21414089689863283, -0.23741092245556797, -0.24178510577119772, -0.22661012675864076, -0.19439920934883784, -0.15038636124315247, -0.1016382648580709, -0.05587705191304346, -0.020213256253075986, -3.063334668498812e-17],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.027810204090780586, 0.05246043847259536, 0.07116307969980216, 0.08183950466200259, 0.08338671645077841, 0.07584290537913381, 0.06042708110908308, 0.039437810027664465, 0.016010011596869555, -0.006253948418212056, -0.02374377511377834, -0.033338674331668136, -0.03287706921136779, -0.02152809045597345, -7.03041814289914e-17],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.016031345139013987, 0.030974818090574556, 0.04374524499633577, 0.05329407968661519, 0.05869487210422392, 0.05928160453602916, 0.05481925067128612, 0.04566700646018806, 0.032884412315470256, 0.018232802130106713, 0.004040099148673176, -0.0070763764977168795, -0.01260191937330764, -0.010572813015827742, -4.0205490885333685e-17],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.01032406327070415, 0.03953994133885332, 0.08268110886952187, 0.13242511881954014, 0.18035037931151743, 0.21837610832807786, 0.24013514085533222, 0.24204247693067574, 0.2238773073617527, 0.1887827117498417, 0.1426896934711177, 0.09327238133201989, 0.04862137333449968, 0.01586839419462579, 1.7518570245704748e-17],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.028099272145259434, 0.05133992486273004, 0.06570343816285948, 0.06870623010763356, 0.05982909069029241, 0.04060695796237414, 0.014363513300129456, -0.014363513300129407, -0.04060695796237409, -0.05982909069029235, -0.06870623010763353, -0.06570343816285949, -0.05133992486273003, -0.028099272145259434, -7.828039201518187e-17],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.010689140798121532, 0.04090831364069532, 0.08543234901067365, 0.13656263670442423, 0.1854582854756164, 0.22366479344868706] + [0.2445759082998639] * 2 + [0.22366479344868706, 0.1854582854756165, 0.13656263670442434, 0.08543234901067367, 0.04090831364069529, 0.010689140798121536, 4.793291575869625e-33],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.028099272145259434, -0.05133992486273004, -0.06570343816285948, -0.06870623010763353, -0.05982909069029238, -0.04060695796237411, -0.014363513300129424, 0.014363513300129438, 0.04060695796237412, 0.05982909069029238, 0.06870623010763356, 0.06570343816285949, 0.05133992486273003, 0.028099272145259434, 7.828039201518187e-17],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.010689140798121536, -0.04090831364069532, -0.08543234901067365, -0.13656263670442423, -0.1854582854756164, -0.22366479344868706] + [-0.2445759082998639] * 2 + [-0.22366479344868706, -0.1854582854756165, -0.13656263670442434, -0.08543234901067367, -0.04090831364069529, -0.010689140798121532, 4.793291575869625e-33],
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q2.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q3.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q3.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q4.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q4.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.4,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
        },
        "q5.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q5.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q5.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q5.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q5.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q5.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q5.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q5.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "coupler_q1_q2.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "coupler_q2_q3.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "coupler_q3_q4.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "coupler_q4_q5.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(0.16944495714445007, 2000)],
            "sine": [(-0.9855396524231359, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.9855396524231359, 2000)],
            "sine": [(0.16944495714445007, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.9855396524231359, 2000)],
            "sine": [(-0.16944495714445007, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.24764598185183084, 2000)],
            "sine": [(-0.9688505909956615, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.9688505909956615, 2000)],
            "sine": [(-0.24764598185183084, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.9688505909956615, 2000)],
            "sine": [(0.24764598185183084, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {},
    "oscillators": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
                "1": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
                "6": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5950000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4900000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4900000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4900000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4900000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4900000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 5950000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "q1.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "saturation": "q1.xy.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "a",
            "MWInput": {
                "port": ('con1', 6, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 208089468.72514498,
        },
        "q1.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 2, 1),
            },
        },
        "q1.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "a",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -23012781.0,
        },
        "q2.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "saturation": "q2.xy.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "b",
            "MWInput": {
                "port": ('con1', 6, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -62911194.0373852,
        },
        "q2.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 1),
            },
        },
        "q2.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "b",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 70304257.0,
        },
        "q3.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "saturation": "q3.xy.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "c",
            "MWInput": {
                "port": ('con1', 6, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 246263353.0,
        },
        "q3.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q3.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 2),
            },
        },
        "q3.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "c",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -86963877.0,
        },
        "q4.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "saturation": "q4.xy.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "d",
            "MWInput": {
                "port": ('con1', 6, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": -225290795.89999962,
        },
        "q4.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q4.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 3),
            },
        },
        "q4.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "d",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 128375329.0,
        },
        "q5.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180_Square": "q5.xy.x180_Square.pulse",
                "x90_Square": "q5.xy.x90_Square.pulse",
                "-x90_Square": "q5.xy.-x90_Square.pulse",
                "y180_Square": "q5.xy.y180_Square.pulse",
                "y90_Square": "q5.xy.y90_Square.pulse",
                "-y90_Square": "q5.xy.-y90_Square.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "saturation": "q5.xy.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "e",
            "MWInput": {
                "port": ('con1', 6, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": -19824670.30000019,
        },
        "q5.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q5.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 4),
            },
        },
        "q5.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "e",
            "MWOutput": {
                "port": ('con1', 6, 1),
            },
            "MWInput": {
                "port": ('con1', 6, 1),
                "upconverter": 1,
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 21804454.0,
        },
        "coupler_q1_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q1_q2.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 5),
            },
        },
        "coupler_q2_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q2_q3.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 6),
            },
        },
        "coupler_q3_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q3_q4.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 7),
            },
        },
        "coupler_q4_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q4_q5.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 8),
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.x180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q1.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.x180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q2.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.x180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q3.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q3.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.x180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q4.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q4.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.x180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_Square.wf.I",
                "Q": "q5.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_Square.wf.I",
                "Q": "q5.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_Square.wf.I",
                "Q": "q5.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_Square.wf.I",
                "Q": "q5.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_Square.wf.I",
                "Q": "q5.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_Square.wf.I",
                "Q": "q5.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q5.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q5.resonator.readout.wf.I",
                "Q": "q5.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q5.resonator.readout.iw1",
                "iw2": "q5.resonator.readout.iw2",
                "iw3": "q5.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q5.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q1_q2.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "coupler_q1_q2.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q2_q3.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "coupler_q2_q3.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q3_q4.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "coupler_q3_q4.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q4_q5.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "coupler_q4_q5.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.006938473070531523, 0.026575320436731595, 0.05557680821785938, 0.089024940270466, 0.12125829566060296, 0.14683725985313936, 0.16146704527579697, 0.16271994919256233, 0.15043392276080286, 0.12672133195073712, 0.09558969105422982, 0.06224317168956327, 0.03218811498910038, 0.010298207981334826, 1.0399376501033949e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.01092463001658052, -0.020933821738006377, -0.029163145786415153, -0.03485965938251483, -0.03745652223413811, -0.03665820475184714, -0.032523540796892014, -0.02552656559024921, -0.016572258132298207, -0.006947614916055114, 0.001801889725233215, 0.008065870186655529, 0.010411426526756203, 0.007838167000187921, 2.810713702097524e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0071117628498714325, 0.027217362994405744, 0.0568403595149698, 0.09085866719668322, 0.12339021159475454, 0.14880999314295446] + [0.16272270068013356] * 2 + [0.14880999314295446, 0.12339021159475459, 0.09085866719668328, 0.056840359514969824, 0.027217362994405726, 0.0071117628498714325, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0071117628498714325, -0.027217362994405744, -0.0568403595149698, -0.09085866719668322, -0.12339021159475454, -0.14880999314295446] + [-0.16272270068013356] * 2 + [-0.14880999314295446, -0.12339021159475459, -0.09085866719668328, -0.056840359514969824, -0.027217362994405726, -0.0071117628498714325, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 8.709397610390108e-19, 3.3331656472330614e-18, 6.960936434239257e-18, 1.1126977595721272e-17, 1.5110942767563078e-17, 1.8223968178365874e-17] + [1.992778345365384e-17] * 2 + [1.8223968178365874e-17, 1.5110942767563084e-17, 1.1126977595721281e-17, 6.96093643423926e-18, 3.3331656472330594e-18, 8.709397610390108e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.01092463001658052, 0.020933821738006377, 0.029163145786415157, 0.034859659382514833, 0.03745652223413812, 0.03665820475184715, 0.03252354079689202, 0.025526565590249222, 0.016572258132298217, 0.006947614916055122, -0.001801889725233209, -0.008065870186655525, -0.0104114265267562, -0.007838167000187921, -2.810713702097524e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.006938473070531522, 0.026575320436731595, 0.05557680821785938, 0.089024940270466, 0.12125829566060296, 0.14683725985313936, 0.16146704527579697, 0.16271994919256233, 0.15043392276080286, 0.12672133195073712, 0.09558969105422982, 0.06224317168956327, 0.03218811498910038, 0.010298207981334826, 1.039937650103395e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.354698805195054e-19, 1.6665828236165307e-18, 3.4804682171196286e-18, 5.563488797860636e-18, 7.555471383781539e-18, 9.111984089182937e-18] + [9.96389172682692e-18] * 2 + [9.111984089182937e-18, 7.555471383781542e-18, 5.5634887978606404e-18, 3.48046821711963e-18, 1.6665828236165297e-18, 4.354698805195054e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0071117628498714325, 0.027217362994405744, 0.0568403595149698, 0.09085866719668322, 0.12339021159475454, 0.14880999314295446] + [0.16272270068013356] * 2 + [0.14880999314295446, 0.12339021159475459, 0.09085866719668328, 0.056840359514969824, 0.027217362994405726, 0.0071117628498714325, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.354698805195054e-19, 1.6665828236165307e-18, 3.4804682171196286e-18, 5.563488797860636e-18, 7.555471383781539e-18, 9.111984089182937e-18] + [9.96389172682692e-18] * 2 + [9.111984089182937e-18, 7.555471383781542e-18, 5.5634887978606404e-18, 3.48046821711963e-18, 1.6665828236165297e-18, 4.354698805195054e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0071117628498714325, -0.027217362994405744, -0.0568403595149698, -0.09085866719668322, -0.12339021159475454, -0.14880999314295446] + [-0.16272270068013356] * 2 + [-0.14880999314295446, -0.12339021159475459, -0.09085866719668328, -0.056840359514969824, -0.027217362994405726, -0.0071117628498714325, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q1.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.38516042695567315,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.010324063270704151, 0.03953994133885332, 0.08268110886952187, 0.13242511881954014, 0.18035037931151743, 0.21837610832807786, 0.24013514085533222, 0.24204247693067574, 0.2238773073617527, 0.1887827117498417, 0.1426896934711177, 0.09327238133201989, 0.04862137333449968, 0.01586839419462579, 1.7518570245704744e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.016031345139013987, -0.030974818090574553, -0.043745244996335766, -0.05329407968661518, -0.05869487210422391, -0.059281604536029146, -0.0548192506712861, -0.045667006460188043, -0.03288441231547024, -0.018232802130106703, -0.004040099148673168, 0.007076376497716886, 0.012601919373307643, 0.010572813015827744, 4.0205490885333685e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.010689140798121534, 0.04090831364069532, 0.08543234901067365, 0.13656263670442423, 0.1854582854756164, 0.22366479344868706] + [0.2445759082998639] * 2 + [0.22366479344868706, 0.1854582854756165, 0.13656263670442434, 0.08543234901067367, 0.04090831364069529, 0.010689140798121534, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.028099272145259434, -0.05133992486273004, -0.06570343816285948, -0.06870623010763355, -0.059829090690292394, -0.040606957962374124, -0.01436351330012944, 0.014363513300129423, 0.0406069579623741, 0.059829090690292366, 0.06870623010763355, 0.06570343816285949, 0.05133992486273003, 0.028099272145259434, 7.828039201518187e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.009931110484846163, -0.03809263715844657, -0.07986000361377403, -0.1283827090432651, -0.17571801269599083, -0.21414089689863283, -0.23741092245556797, -0.24178510577119772, -0.22661012675864076, -0.19439920934883784, -0.15038636124315247, -0.1016382648580709, -0.05587705191304346, -0.020213256253075986, -3.063334668498812e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.027810204090780586, 0.05246043847259536, 0.07116307969980216, 0.08183950466200259, 0.08338671645077841, 0.07584290537913381, 0.06042708110908308, 0.039437810027664465, 0.016010011596869555, -0.006253948418212056, -0.02374377511377834, -0.033338674331668136, -0.03287706921136779, -0.02152809045597345, -7.03041814289914e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.016031345139013987, 0.030974818090574556, 0.04374524499633577, 0.05329407968661519, 0.05869487210422392, 0.05928160453602916, 0.05481925067128612, 0.04566700646018806, 0.032884412315470256, 0.018232802130106713, 0.004040099148673176, -0.0070763764977168795, -0.01260191937330764, -0.010572813015827742, -4.0205490885333685e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.01032406327070415, 0.03953994133885332, 0.08268110886952187, 0.13242511881954014, 0.18035037931151743, 0.21837610832807786, 0.24013514085533222, 0.24204247693067574, 0.2238773073617527, 0.1887827117498417, 0.1426896934711177, 0.09327238133201989, 0.04862137333449968, 0.01586839419462579, 1.7518570245704748e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.028099272145259434, 0.05133992486273004, 0.06570343816285948, 0.06870623010763356, 0.05982909069029241, 0.04060695796237414, 0.014363513300129456, -0.014363513300129407, -0.04060695796237409, -0.05982909069029235, -0.06870623010763353, -0.06570343816285949, -0.05133992486273003, -0.028099272145259434, -7.828039201518187e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.010689140798121532, 0.04090831364069532, 0.08543234901067365, 0.13656263670442423, 0.1854582854756164, 0.22366479344868706] + [0.2445759082998639] * 2 + [0.22366479344868706, 0.1854582854756165, 0.13656263670442434, 0.08543234901067367, 0.04090831364069529, 0.010689140798121536, 4.793291575869625e-33],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.028099272145259434, -0.05133992486273004, -0.06570343816285948, -0.06870623010763353, -0.05982909069029238, -0.04060695796237411, -0.014363513300129424, 0.014363513300129438, 0.04060695796237412, 0.05982909069029238, 0.06870623010763356, 0.06570343816285949, 0.05133992486273003, 0.028099272145259434, 7.828039201518187e-17],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.010689140798121536, -0.04090831364069532, -0.08543234901067365, -0.13656263670442423, -0.1854582854756164, -0.22366479344868706] + [-0.2445759082998639] * 2 + [-0.22366479344868706, -0.1854582854756165, -0.13656263670442434, -0.08543234901067367, -0.04090831364069529, -0.010689140798121532, 4.793291575869625e-33],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q2.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q3.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q3.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q4.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q4.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.4,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.1175255713947627e-18, 8.103962877168999e-18, 1.6924202522078763e-17, 2.705314494215753e-17, 3.6739403974420595e-17, 4.4308137435288903e-17] + [4.8450642549593434e-17] * 2 + [4.4308137435288903e-17, 3.673940397442061e-17, 2.7053144942157555e-17, 1.692420252207877e-17, 8.103962877168993e-18, 2.1175255713947627e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.034581816942959656, 0.13234775745645672, 0.276393202250021, 0.4418113853070613, 0.6, 0.723606797749979] + [0.7912590402935223] * 2 + [0.723606797749979, 0.6000000000000002, 0.4418113853070617, 0.2763932022500211, 0.13234775745645663, 0.034581816942959656, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.017290908471479828, 0.06617387872822836, 0.1381966011250105, 0.22090569265353066, 0.3, 0.3618033988749895] + [0.39562952014676117] * 2 + [0.3618033988749895, 0.3000000000000001, 0.22090569265353086, 0.13819660112501056, 0.06617387872822832, 0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.0587627856973813e-18, 4.0519814385844994e-18, 8.462101261039382e-18, 1.3526572471078765e-17, 1.8369701987210297e-17, 2.2154068717644452e-17] + [2.4225321274796717e-17] * 2 + [2.2154068717644452e-17, 1.8369701987210304e-17, 1.3526572471078777e-17, 8.462101261039385e-18, 4.051981438584496e-18, 1.0587627856973813e-18, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.017290908471479828, -0.06617387872822836, -0.1381966011250105, -0.22090569265353066, -0.3, -0.3618033988749895] + [-0.39562952014676117] * 2 + [-0.3618033988749895, -0.3000000000000001, -0.22090569265353086, -0.13819660112501056, -0.06617387872822832, -0.017290908471479828, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q5.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q5.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229255,
        },
        "q5.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q5.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.05600920201614627,
        },
        "q5.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q5.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05600920201614627,
        },
        "q5.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.35,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "coupler_q1_q2.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "coupler_q2_q3.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "coupler_q3_q4.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "coupler_q4_q5.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(0.16944495714445007, 2000)],
            "sine": [(-0.9855396524231359, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.9855396524231359, 2000)],
            "sine": [(0.16944495714445007, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.9855396524231359, 2000)],
            "sine": [(-0.16944495714445007, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.24764598185183084, 2000)],
            "sine": [(-0.9688505909956615, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.9688505909956615, 2000)],
            "sine": [(-0.24764598185183084, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.9688505909956615, 2000)],
            "sine": [(0.24764598185183084, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {},
}


