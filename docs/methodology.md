# Methodology

## 1. Physical Model

The project studies a finite one-dimensional transverse-field Ising chain

\[
H =
J\sum_{i=1}^{N-1}\sigma_i^z\sigma_{i+1}^z
+
h\sum_{i=1}^{N}\sigma_i^x.
\]

The Hilbert-space dimension is

\[
d=2^N.
\]

The baseline calculation uses

\[
J=2,\qquad h=2.
\]

With the sign convention used in this project, positive \(J\) corresponds
to an antiferromagnetic nearest-neighbor interaction.

---

## 2. Initial State

The default initial state is

\[
|\psi(0)\rangle = |00\ldots0\rangle.
\]

The implementation also supports additional product-state classes for
robustness checks:

- \(|0101\ldots\rangle\)
- \(|+\rangle^{\otimes N}\)

where

\[
|+\rangle =
\frac{|0\rangle+|1\rangle}{\sqrt{2}}.
\]

---

## 3. Time Evolution

The Hamiltonian is Hermitian and is diagonalized as

\[
H=V\,\mathrm{diag}(E_n)V^\dagger.
\]

The state at time \(t\) is then calculated from

\[
|\psi(t)\rangle
=
V e^{-iEt}V^\dagger|\psi(0)\rangle.
\]

Because the Hamiltonian is time independent, its diagonalization is
performed once and reused for all requested time points.

---

## 4. Density Matrix

For a pure state,

\[
\rho(t)=|\psi(t)\rangle\langle\psi(t)|.
\]

The implementation checks that the state is normalized before constructing
the density matrix.

---

## 5. Reduced Density Matrix

For a subsystem \(A\), the reduced density matrix is

\[
\rho_A(t)
=
\mathrm{Tr}_{\bar A}\rho(t),
\]

where \(\bar A\) denotes the degrees of freedom outside the selected
subsystem.

The partial-trace implementation is generic and supports arbitrary
subsets of qubits rather than using separate hard-coded formulas for
different system sizes.

---

## 6. Entanglement Entropy

The main observable is the von Neumann entropy

\[
S_A(t)
=
-\mathrm{Tr}
\left[
\rho_A(t)\ln\rho_A(t)
\right].
\]

For the one-qubit subsystem used in the main analysis,

\[
0\leq S_A(t)\leq\ln 2.
\]

The entropy is calculated from the eigenvalues of the Hermitian reduced
density matrix.

Small negative eigenvalues caused by floating-point roundoff are clipped
to zero. Significantly negative eigenvalues are treated as numerical
errors.

---

## 7. Quantitative Metrics

Several complementary time-series metrics are calculated.

### 7.1 Maximum entropy

\[
S_{\max}=\max_t S_A(t).
\]

### 7.2 Normalized maximum entropy

For a one-qubit subsystem,

\[
\eta_{\max}
=
\frac{S_{\max}}{\ln 2}.
\]

### 7.3 Time-averaged entropy

The time-averaged entropy is defined as

\[
\overline{S}
=
\frac{1}{T}
\int_0^T S_A(t)\,dt.
\]

The integral is evaluated numerically using the trapezoidal rule.

### 7.4 Fraction above threshold

For a chosen entropy threshold \(S_{\mathrm{th}}\), the fraction

\[
f =
\frac{
\text{time for which }S_A(t)>S_{\mathrm{th}}
}{
\text{total observation time}
}
\]

is calculated numerically.

This quantity measures how persistently the subsystem remains substantially
entangled during the observation interval.

### 7.5 First local maximum

The first interior time point satisfying the local-maximum criterion is
identified as the first observed entropy peak.

### 7.6 Operational recurrence

A recurrence is defined using a finite threshold.

After the entropy first rises above the threshold, the first subsequent time
at which it returns below the threshold is recorded.

This is an operational numerical definition and should not be interpreted
as an exact mathematical recurrence time.

---

## 8. Numerical Validation

The project contains automated tests for:

- Hamiltonian dimensions;
- Hamiltonian Hermiticity;
- known \(N=2\) eigenvalues;
- state normalization;
- density-matrix properties;
- partial-trace properties;
- entropy limits;
- purity;
- expectation values;
- norm preservation;
- energy conservation;
- exact \(N=2\) dynamics;
- time-series metrics.

The complete test suite is intended to verify both mathematical properties
and important numerical invariants of the implementation.

---

## 9. Finite-Size Analysis

The main numerical calculations consider

\[
N=2,3,4,5,6.
\]

The Hilbert-space dimension grows exponentially,

\[
d=2^N,
\]

which limits the system sizes accessible through direct exact
diagonalization.

The observed dependence on \(N\) is therefore interpreted as finite-size
dynamical behavior.

The calculations do not constitute a thermodynamic-limit extrapolation.

---

## 10. Interpretation of Irreversibility

The complete closed quantum system evolves unitarily according to

\[
|\psi(t)\rangle=e^{-iHt}|\psi(0)\rangle.
\]

Consequently, the numerical model does not introduce fundamental
irreversible dynamics.

Instead, entanglement transfers information and quantum correlations
between the selected subsystem and the rest of the chain. The subsystem can
therefore exhibit effectively irreversible or apparently irreversible
behavior even though the complete closed system remains unitary.

Accordingly, the results are interpreted in terms of

- effective subsystem irreversibility;
- apparent irreversibility;
- subsystem mixing through entanglement.

They are not interpreted as evidence for fundamental microscopic
irreversibility.

---

## 11. Parameter Robustness

The baseline calculations use

\[
J=h=2.
\]

Additional calculations were performed for different interaction strengths
to examine the sensitivity of the finite-size dynamics to the ratio
\(J/h\).

The results show that the detailed dynamics depends on the Hamiltonian
parameters. Therefore, the project does not claim a universal monotonic
scaling law valid for all parameter choices.

---

## 12. Initial-State Robustness

The main initial state is

\[
|00\ldots0\rangle.
\]

Additional product states were examined to determine whether the observed
finite-size behavior depends exclusively on this choice.

The detailed transient dynamics depends on the initial state, while the
general increase in time-averaged subsystem entropy over the small systems
studied is not restricted to a single initial-state construction.

---

## 13. Model Limitations

Several limitations must be kept in mind when interpreting the results.

### 13.1 Small system sizes

Only small \(N\) values are accessible with the present exact-diagonalization
implementation.

### 13.2 One-qubit subsystem

The principal observable concerns a single-qubit subsystem. Its entropy is
therefore bounded by \(\ln 2\), independently of the total system size.

### 13.3 Finite observation window

The numerical results are obtained over a finite time interval. Long-time
behavior can contain additional finite-size structure and recurrences.

### 13.4 Integrability

The transverse-field Ising model used in this project is integrable.
Therefore, the present calculations should not automatically be interpreted
as evidence for generic quantum chaos, generic thermalization, or
eigenstate thermalization hypothesis (ETH) behavior.

### 13.5 Thermodynamic limit

The available calculations do not establish a thermodynamic-limit
transition or a universal scaling law.

### 13.6 Entanglement entropy versus thermodynamic entropy

The entropy calculated here is the von Neumann entropy of a reduced
subsystem. It is not the total thermodynamic entropy of the closed quantum
system.

---

## 14. Scientific Interpretation

For the finite systems and parameters examined, increasing the number of
degrees of freedom modifies the temporal structure of subsystem
entanglement.

In particular, the time-averaged entropy and the fraction of the
observation interval spent above a fixed entropy threshold generally
increase over the small system sizes considered.

The microscopic dynamics nevertheless remains unitary and reversible.

The appropriate conclusion is therefore that increasing system size can
enhance persistent effective subsystem mixing, rather than that a
fundamental irreversible law has emerged.

---

## 15. Reproducibility

The main simulation can be reproduced from the project root using:

```bash
python scripts/run_simulation.py