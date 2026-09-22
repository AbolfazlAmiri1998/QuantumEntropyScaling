# Quantum Entropy Scaling

Exact-diagonalization study of subsystem entanglement dynamics in finite
transverse-field Ising chains.

## Overview

This project investigates how increasing the number of interacting quantum
spins changes the dynamics of a local subsystem.

The central question is:

> How does increasing the number of degrees of freedom affect the transition
> from microscopic unitary dynamics to effectively irreversible subsystem
> behavior?

The study uses the transverse-field Ising Hamiltonian

\[
H =
J\sum_{i=1}^{N-1}\sigma_i^z\sigma_{i+1}^z
+
h\sum_{i=1}^{N}\sigma_i^x.
\]

The main observable is the von Neumann entropy of a one-qubit subsystem,

\[
S_A(t) =
-\mathrm{Tr}\left[\rho_A(t)\ln\rho_A(t)\right].
\]

The total quantum system remains closed and evolves unitarily. Therefore,
the entropy discussed in this project is subsystem entanglement entropy and
should not be interpreted as fundamental thermodynamic entropy.

## Main Results

For the finite systems studied here (\(N=2,\ldots,6\)):

- subsystem entropy becomes strongly time dependent as entanglement develops;
- the one-qubit entropy remains bounded by \(\ln 2\);
- time-averaged entropy generally increases across the small system sizes
  studied;
- the fraction of the simulated time spent above a fixed entropy threshold
  also generally increases;
- the microscopic evolution remains unitary and reversible;
- the results are consistent with increasingly persistent effective
  subsystem mixing caused by entanglement with the rest of the system.

These observations should be interpreted as finite-size numerical evidence,
not as a proof of a thermodynamic phase transition or fundamental
irreversibility.

## Model

The Hamiltonian is

\[
H =
J\sum_{i=1}^{N-1}\sigma_i^z\sigma_{i+1}^z
+
h\sum_{i=1}^{N}\sigma_i^x.
\]

The convention used here has a plus sign in front of both terms. For
\(J>0\), the nearest-neighbor interaction is antiferromagnetic.

The baseline parameters are

```text
J = 2.0
h = 2.0