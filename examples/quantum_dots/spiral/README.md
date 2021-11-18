# Spiral Measurements 

For Semiconducting qubits it is often necessary to perform two dimensional sweeps with the voltage on a pair of gates. 

Traditionally in the field of semiconducting qubits these measurements have been performed by changing the DC voltage provided to the gate by the restrictive node of the bias tee, measuring then changing the voltage again to move to the next point. 

Typically the response time of the DC voltage sources is on the order of 10ms, meaning that only a small number of points can be measured per second. As a result these measurements garnered the name slow measurements. 

Groups have developed the capabilities to go much faster by using an AWG to apply a pair of sawtooth waves, a fast and slow wave. If the desired resolution of the scan is $N\times M$ and the measurement time for each pixel is $\tau_{int}$ then the period of the fast and slow sawtooth waves are
$$
\tau_{fast} = N\tau_{int} \\
\tau_{slow} = M \tau_{fast} =MN\tau_{int}
$$
So that the gate voltages are swept in a raster pattern. Such raster scans have two significant disadvantages: 

1. The raster scan jumps back to the beginning of the next line, leading to large fast changes in the device voltages. If such jumps are sufficiently large and fast they can damage the device. 
2. If $\tau_{slow}$ becomes significantly large the the sawtooth ceases to be sufficiently high frequency to pass through the capacitive node of the bias tee. This places a limit on either the resolution of the scans or the time spent measuring at the one point. 

It should be noted that 2. does not place a hard limit on the signal to noise ratio of these measurements, because it is possible to average subsequent scans together meaning that the effective integration time can be made an arbitrary integer multiple of $\tau_{int}$. 

### Spiral Measurements

With the OPX it is possible sweep the gate voltages in a spiral pattern - starting at the central pixel and the spiralling outwards until every pixel has been visited. Navigating the two dimensional gate voltage space in this manor avoids both of the disadvantages above. There are no large jumps and period of the slowest waveform is $2N \tau_{int}$, meaning there is much more headroom before the high pass filtering introduced by the bias tee becomes significant. 

The ramifications of this headroom are much greater than just allowing for greater resolutions. It is possible to run qubit pulse sequences at each pixel prior to measuring. Allowing for many of the measurements necessary to identify and characterise and tune semiconducting qubits orders of magnitude faster. 













