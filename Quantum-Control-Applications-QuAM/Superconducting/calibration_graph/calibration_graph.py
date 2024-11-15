from typing import List, Optional
from qualibrate import QualibrationLibrary, QualibrationGraph, GraphParameters
from qualibrate.orchestration.basic_orchestrator import BasicOrchestrator


# Define graph target parameters
class Parameters(GraphParameters):
    qubits: Optional[List[str]] = None


library = QualibrationLibrary.get_active_library()

# Create the QualibrationGraph
graph = QualibrationGraph(
    name="Full-Calibration",  # Unique graph name
    parameters=Parameters(
        qubits="q1,q2,q3,q4,q5"
    ),  # Instantiate graph parameters
    nodes={  # Specify nodes used in the graph
        "close_qms": library.nodes["00_Close_other_QMs"],
        # "res_spec": library.nodes["02a_Resonator_Spectroscopy"],
        "res_spec_vs_flux_with_min": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(
            frequency_span_in_mhz=20,
            update_flux_min=False
        ),
        "res_spec_vs_flux": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(
            frequency_span_in_mhz=20,
            update_flux_min=False
        ),
        "qubit_spec": library.nodes["03a_Qubit_Spectroscopy"].copy(
            operation_amplitude_factor=0.01
        ),
        "qubit_spec_vs_flux": library.nodes["03b_Qubit_Spectroscopy_vs_Flux"].copy(
            operation_amplitude_factor=0.01,
            frequency_span_in_mhz=80,
            frequency_step_in_mhz=0.5,
            min_flux_offset_in_v=-0.02,
            max_flux_offset_in_v=0.02,
        ),
        "power_rabi_1": library.nodes["04_Power_Rabi"],
        "ramsey_1": library.nodes["05_Ramsey"].copy(
            max_wait_time_in_ns=5000,
            log_or_linear_sweep='linear'
        ),
        "power_rabi_2": library.nodes["04_Power_Rabi"].copy(),
        "ramsey_2": library.nodes["05_Ramsey"].copy(
            max_wait_time_in_ns=5000,
            log_or_linear_sweep='linear'
        ),
        "power_rabi_3": library.nodes["04_Power_Rabi"].copy(),
        "ramsey_3": library.nodes["05_Ramsey"].copy(
            max_wait_time_in_ns=5000,
            log_or_linear_sweep='linear'
        ),
        "power_rabi_4": library.nodes["04_Power_Rabi"].copy(
            num_averages=20,
            max_number_rabi_pulses_per_sweep=15
        ),
        "ramsey_4": library.nodes["05_Ramsey"].copy(
            max_wait_time_in_ns=5000,
            log_or_linear_sweep='linear'
        ),
        "readout_freq_opt": library.nodes["06a_Readout_Frequency_Optimization"],
        "readout_power_opt": library.nodes["06b_Readout_Power_Optimization"],
        "iq_blobs_1": library.nodes["07_IQ_Blobs"].copy(),
        "power_rabi_state_x180_1": library.nodes["09_Power_Rabi_State"].copy(
            operation_x180_or_any_90="x180",
            reset_type_thermal_or_active="thermal"
        ),
        "power_rabi_state_x90_1": library.nodes["09_Power_Rabi_State"].copy(
            operation_x180_or_any_90="x90",
            reset_type_thermal_or_active="thermal"
        ),
        "power_rabi_state_x180_2": library.nodes["09_Power_Rabi_State"].copy(
            operation_x180_or_any_90="x180",
            max_number_rabi_pulses_per_sweep=400,
            min_amp_factor=0.95,
            max_amp_factor = 1.05,
            amp_factor_step=0.001,
            reset_type_thermal_or_active="thermal"
        ),
        "power_rabi_state_x90_2": library.nodes["09_Power_Rabi_State"].copy(
            operation_x180_or_any_90="x90",
            max_number_rabi_pulses_per_sweep=400,
            min_amp_factor=0.95,
            max_amp_factor=1.05,
            amp_factor_step=0.001,
            reset_type_thermal_or_active="thermal"
        ),
        "power_rabi_state_x180_3": library.nodes["09_Power_Rabi_State"].copy(
            operation_x180_or_any_90="x180",
            max_number_rabi_pulses_per_sweep=1000,
            min_amp_factor=0.98,
            max_amp_factor=1.02,
            amp_factor_step=0.0005,
            reset_type_thermal_or_active="thermal"
        ),
        "power_rabi_state_x90_3": library.nodes["09_Power_Rabi_State"].copy(
            operation_x180_or_any_90="x90",
            max_number_rabi_pulses_per_sweep=1000,
            min_amp_factor=0.98,
            max_amp_factor=1.02,
            amp_factor_step=0.0005,
            reset_type_thermal_or_active="thermal"
        ),
        "iq_blobs_2": library.nodes["07_IQ_Blobs"].copy(),
        # "stark_detuning_x180_1": library.nodes["09a_Stark_Detuning"].copy(
        #     operation_x180_or_any_90="x180",
        #     reset_type_thermal_or_active="thermal"
        # ),
        # "stark_detuning_x90_1": library.nodes["09a_Stark_Detuning"].copy(
        #     operation_x180_or_any_90="x90",
        #     reset_type_thermal_or_active="thermal"
        # ),
        # "stark_detuning_x180_2": library.nodes["09a_Stark_Detuning"].copy(
        #     operation_x180_or_any_90="x180",
        #     reset_type_thermal_or_active="thermal",
        #     max_number_pulses_per_sweep=200,
        #     frequency_span_in_mhz=2,
        #     frequency_step_in_mhz = 0.002
        # ),
        # "stark_detuning_x90_2": library.nodes["09a_Stark_Detuning"].copy(
        #     operation_x180_or_any_90="x90",
        #     reset_type_thermal_or_active="thermal",
        #     max_number_pulses_per_sweep=200,
        #     frequency_span_in_mhz=2,
        #     frequency_step_in_mhz=0.002
        # ),
        "drag_calibration_x180_1": library.nodes["09c_DRAG_Calibration_180_90"].copy(
            operation_x180_or_any_90="x180",
            reset_type_thermal_or_active="thermal",
            num_averages=1000,
            max_number_pulses_per_sweep=100,
            min_amp_factor=0.5,
            max_amp_factor=1.5,
            amp_factor_step=0.05,
        ),
        "drag_calibration_x90_1": library.nodes["09c_DRAG_Calibration_180_90"].copy(
            operation_x180_or_any_90="x90",
            reset_type_thermal_or_active="thermal",
            num_averages=1000,
            max_number_pulses_per_sweep=100,
            min_amp_factor=0.5,
            max_amp_factor=1.5,
            amp_factor_step=0.05,
        ),
        "drag_calibration_x180_2": library.nodes["09c_DRAG_Calibration_180_90"].copy(
            operation_x180_or_any_90="x180",
            reset_type_thermal_or_active="thermal",
            num_averages=1000,
            max_number_pulses_per_sweep=100,
            min_amp_factor=0.9,
            max_amp_factor=1.1,
            amp_factor_step=0.005,
        ),
        "drag_calibration_x90_2": library.nodes["09c_DRAG_Calibration_180_90"].copy(
            operation_x180_or_any_90="x90",
            reset_type_thermal_or_active="thermal",
            num_averages=1000,
            max_number_pulses_per_sweep=100,
            min_amp_factor=0.9,
            max_amp_factor=1.1,
            amp_factor_step=0.005,
        ),
        "randomized_benchmarking": library.nodes["11a_Randomized_Benchmarking"]
    },
    # Specify directed relationships between graph nodes
    connectivity=[
        # ("close_qms", "res_spec"),

        ("close_qms", "res_spec_vs_flux_with_min"),
        ("res_spec_vs_flux_with_min", "res_spec_vs_flux"),
        ("res_spec_vs_flux", "qubit_spec"),

        ("qubit_spec", "qubit_spec_vs_flux"),
        ("qubit_spec_vs_flux", "power_rabi_1"),
        ("power_rabi_1", "ramsey_1"),
        ("ramsey_1", "power_rabi_2"),
        ("power_rabi_2", "ramsey_2"),
        ("ramsey_2", "power_rabi_3"),
        ("power_rabi_3", "ramsey_3"),
        ("ramsey_3", "power_rabi_4"),
        ("power_rabi_4", "ramsey_4"),
        ("ramsey_4", "readout_freq_opt"),
        ("readout_freq_opt", "readout_power_opt"),
        ("readout_power_opt", "iq_blobs_1"),
        ("iq_blobs_1", "power_rabi_state_x180_1"),
        ("power_rabi_state_x180_1", "power_rabi_state_x180_2"),
        ("power_rabi_state_x180_2", "power_rabi_state_x180_3"),
        ("power_rabi_state_x180_3", "power_rabi_state_x90_1"),
        ("power_rabi_state_x90_1", "power_rabi_state_x90_2"),
        ("power_rabi_state_x90_2", "power_rabi_state_x90_3"),
        ("power_rabi_state_x90_3", "iq_blobs_2"),

        # ("iq_blobs_2", "stark_detuning_x180_1"),
        # ("stark_detuning_x180_1", "stark_detuning_x90_1"),
        # ("stark_detuning_x90_1", "stark_detuning_x180_2"),
        # ("stark_detuning_x180_2", "stark_detuning_x90_2"),

        ("iq_blobs_2", "drag_calibration_x180_1"),
        ("drag_calibration_x180_1", "drag_calibration_x90_1"),
        ("drag_calibration_x90_1", "drag_calibration_x180_2"),
        ("drag_calibration_x180_2", "drag_calibration_x90_2"),
        ("drag_calibration_x90_2", "randomized_benchmarking"),
    ],
    # Specify orchestrator used to run the graph
    orchestrator=BasicOrchestrator(skip_failed=True),
)

# Run the calibration graph for qubits q1, q2, and q3
graph.run(qubits=None)
