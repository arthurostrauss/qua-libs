# Kerr-Cat qubit
*Author: Kevin Villegas Rosales*

_Demonstrated in QuLab, the laboratory of Prof. Michel Devoret, at Yale University. https://qulab.eng.yale.edu/_

_Demonstrated in the experiment of Rodrigo G. Cortiñas (https://www.linkedin.com/in/rodrigo-g-corti%C3%B1as-133a78164/)_


## The goal

In this use-case we show data related to the stabilization of a Kerr-Cat qubit with
a squeezing drive and three wave mixing.

## The device
The device that was used was as SNAIL with a planar resonator for readout, and
both of these inside of a 3D cavity.

## Kerr-cat qubit

The Kerr-cat Hamiltonian is the following in the frame rotating at the SNAIL frequency, $\hat{H}_{cat}/\hbar = -K\hat{a}^{\dagger2}\hat{a}^{2} + \epsilon\_{2}(\hat{a}^{\dagger2}+\hat{a}^{2})$,
where $K$ is the Kerr-nonlinearity and $\epsilon\_{2}$ is the amplitude of the squeezing drive.
The simulated energy landscape can be seen in Fig. 1c (left figure). There are two local minima
separated by an energy barrier. The two coherent states existing in these minima are |$\alpha$> and
|$-\alpha$>, and the superposition of these coherent states form cat states. The Bloch sphere of this 
driven Hamiltonian can be seen in Fig. 1b. When there is no squeezing drive applied to the SNAIL, the
Hamiltonian is the one of a simple transmon that can encode the first two Fock states. The Bloch
sphere and simulated energy potential of the undriven Hamiltonian can be seen in Fig. 1a and 1c. Figure
1 appearing in this use-case is the identical Figure 1 appearing in Grimm and Frattini \textit{et al.}, Nature \bf{584}, 205 (2020) [1].

![Grimm_Frattini_Fig1](Grimm_Frattini_Fig1.png)