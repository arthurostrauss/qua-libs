# SiGe Singlet - Triplet Qubits

This examples folder comprises documentation of the set of qua programs used to make a Singlet-Triplet qubit in the very device presented in [A singlet-triplet hole spin qubit in planar Ge](https://www.nature.com/articles/s41563-021-01022-2?proof=t%2529.). The OPX is connected as follows:



<img src="./_images/OPX connections.svg" alt="OPX connections"  />

The channels labelled LB and RB are connected to the left and right barriers by means of the capacitive node of a bias tee. Thus, allowing for the OPX to apply high frequency pulses to the gates while another instrument (A [Deflt IVVI)](http://qtwork.tudelft.nl/~schouten/ivvi/index-ivvi.htm) supplies a DC voltage. The channel labelled RF provides an RF tone of approximately 100MHz to an LC matching network which includes the charge sensor ohmic. The RF tone reflected off this matching network is directed to the OPX input channel labelled RF for demodulation and acquisition. 



## Program Overview 

The programs in this section are presented in the order in which they were used. Starting with the most basic time of flight calibration for the RF tone. Moving to fast two dimensional scans with which to tune a double quantum dot. Finally, finishing with Rabi pulse sequences. The programs are as follows:



| Program                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [time_of_flight](https://github.com/qua-platform/qua-libs/tree/barnaby/examples/quantum_dots/SiGe%20Singlet%20-%20Triplet/1%20-%20time_of_flight) | A program which plays an RF tone to analogy output RF then immediately starts measuring the raw ADC samples returned to the analogy input RF. Thus enabling the user to measure the time in ns between the RF tone being sent and received back at the OPX |
| [frequency_sweep](https://github.com/qua-platform/qua-libs/tree/barnaby/examples/quantum_dots/SiGe%20Singlet%20-%20Triplet/2%20-%20frequency_sweep) | A program which sweeps the frequency of the RF tone. Enabling the user to choose the optimal frequency. |
| [do2d](https://github.com/qua-platform/qua-libs/tree/barnaby/examples/quantum_dots/SiGe%20Singlet%20-%20Triplet/3%20-%20do2d) | A program which uses the LB and RB channels to play a pulse sequence performs a two dimensional sweep of the left and right barrier gate voltages, while measuring the state of the charge sensor, to produce an image. In the most simple case each pixel of the image corresponds to a measurement of the lowest energy state of the device for that particular set of gate voltages. However, it is possible to play pulse sequences prior to measuring to move the device into meta-stable states. This proved invaluable in the search for spin physics by means of the Singlet-Triplet Minus avoided crossing. |
| [rabi](https://github.com/qua-platform/qua-libs/tree/barnaby/examples/quantum_dots/SiGe%20Singlet%20-%20Triplet/4%20-%20rabi) | A program to perform a two dimensional Rabi measurement, where both the amplitude and the duration of the pulse is swept. |

