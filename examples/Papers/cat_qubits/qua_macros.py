from qm.qua import *
from Examples.Papers.cat_qubits.exponential_suppression_bit_flip_errors.configuration import deflation_duration


def Ramsey(transmon, readout_res, revival_time, threshold, polarization, target_state, I):

    play("X90", transmon)
    wait(revival_time, transmon)
    with switch_(polarization, unsafe=True):  # Make sure cases handle all possible outcomes when using unsafe
        with case_(0):
            play("X90", transmon)
        with case_(1):
            play("X90" * amp(-1), transmon)

    align(transmon, readout_res)
    measure(
        "Readout_Op",
        readout_res,
        "raw",
        dual_demod.full("optimal_integW_1", "out1", "optimal_integW_2", "out2", I),
    )

    assign(target_state, I > threshold)


def deflate(buffer_drive_on, buffer_amp):
    align("ATS", "buffer")
    if buffer_drive_on:
        play("deflation" * amp(buffer_amp), "buffer")
        play("pump", "ATS", duration=deflation_duration // 4)
    if not buffer_drive_on:
        play("pump", "ATS", duration=deflation_duration // 4)


def g_one_to_g_zero():
    align("storage", "transmon")
    play("g1_to_g0_opt_con", "storage")
    play("g1_to_g0_opt_con", "transmon")


def g_odd_to_g_even():  # In case cavity has not been deflated prior to parity measurement
    align("storage", "transmon")
    play("g1_to_g0_opt_con", "storage")
    play("g1_to_g0_opt_con", "transmon")


def e_one_to_g_zero():
    align("storage", "transmon")
    play("e1_to_g0_opt_con", "storage")
    play("e1_to_g0_opt_con", "transmon")