# Quantum Entropy Scaling

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-required-013243)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-required-8CAAE6)](https://scipy.org/)
[![Field](https://img.shields.io/badge/Field-Quantum%20Spin%20Chains-purple)](#model)
[![Method](https://img.shields.io/badge/Method-Exact%20Diagonalization-orange)](#method)
[![Status](https://img.shields.io/badge/Status-v1.0.0-success)](https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling/releases/tag/v1.0.0)
[![Type](https://img.shields.io/badge/Type-Research%20Project-purple)](https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

Exact-diagonalization study of subsystem entanglement dynamics in finite transverse-field Ising chains.

## Overview

This project investigates how increasing the number of interacting quantum spins affects the dynamics of a local subsystem while the full system remains closed and evolves unitarily.

**Central question:**

> How does increasing the number of degrees of freedom affect the emergence of effectively irreversible subsystem behavior while the global dynamics remains unitary?

The study uses the transverse-field Ising Hamiltonian

```text
H = J Σ_{i=1}^{N-1} σᶻ_i σᶻ_{i+1} + h Σ_{i=1}^{N} σˣ_i
```

with the baseline initial state

```text
|ψ(0)⟩ = |00...0⟩.
```

The main observable is the von Neumann entropy of a one-qubit subsystem:

```text
S_A(t) = -Tr[ρ_A(t) ln ρ_A(t)]
```

**Important:** The total quantum system remains closed and evolves unitarily. The entropy studied here is therefore **subsystem entanglement entropy**, not fundamental thermodynamic entropy.

---

## Main Results

For the finite systems studied here,

```text
N = 2, 3, 4, 5, 6
```

with

```text
J = 2.0
h = 2.0
```

the simulation produces the following results over the time interval

```text
t ∈ [0, 5].
```

### Time-Averaged Entropy

| N | ⟨S_A⟩_T | f(S > 0.5) |
|---|----------|-------------|
| 2 | 0.3461 | 0.3066 |
| 3 | 0.4371 | 0.4559 |
| 4 | 0.4645 | 0.5271 |
| 5 | 0.4859 | 0.6683 |
| 6 | 0.4843 | 0.6022 |

The time-averaged entropy increases from N=2 to N=5, followed by a slight decrease at N=6. Thus, the finite-size trend is not strictly monotonic.

The fraction of simulated time spent above the threshold S = 0.5 also shows a non-monotonic finite-size trend, increasing through N=5 and decreasing at N=6.

### Maximum Entropy

| N | S_max | S_max / ln(2) |
|---|-------|----------------|
| 2 | 0.6795 | 0.9803 |
| 3 | 0.6908 | 0.9966 |
| 4 | 0.6850 | 0.9883 |
| 5 | 0.6870 | 0.9911 |
| 6 | 0.6854 | 0.9888 |

The maximum entropy remains close to ln(2) for all system sizes.

Because the subsystem contains a single qubit,

```text
0 ≤ S_A ≤ ln(2),
```

so the observed values are consistent with the theoretical entropy bound.

### Key Observations

- Subsystem entropy becomes strongly time-dependent as entanglement develops.
- The one-qubit entropy remains bounded by ln(2).
- The time-averaged entropy increases from N=2 to N=5, followed by a slight decrease at N=6.
- The fraction of time spent above S = 0.5 shows a similar but non-monotonic finite-size trend.
- The microscopic evolution of the full system remains unitary and reversible.
- No recurrence below the operational threshold S < 10⁻³ was detected within the simulation window t ∈ [0, 5].

These observations should be interpreted as **finite-size numerical evidence**. They do not establish a thermodynamic-limit phase transition, generic thermalization, ETH, chaos, or fundamental irreversibility.

---

## Figures

The repository contains two main figures:

- `figures/entropy_N2_N6_comparison.png` — time evolution of subsystem entropy for N = 2, ..., 6.
- `figures/maximum_entropy_vs_N.png` — maximum one-qubit entropy as a function of system size.

---

## Model

The Hamiltonian is

```text
H = J Σ_{i=1}^{N-1} σᶻ_i σᶻ_{i+1} + h Σ_{i=1}^{N} σˣ_i.
```

The convention used in this project has a plus sign in front of both terms.

For J > 0, the nearest-neighbor interaction is antiferromagnetic under this convention.

### Sign Convention

A commonly used transverse-field Ising convention is

```text
H = -J Σ σᶻ_i σᶻ_{i+1} - h Σ σˣ_i.
```

The sign convention used here differs from that form. The physical interpretation of the coupling therefore depends on the chosen signs of J and h.

The baseline parameters are

```text
J = 2.0
h = 2.0
```

---

## Initial State

The baseline initial state is the computational-basis product state

```text
|ψ(0)⟩ = |00...0⟩.
```

The project also implements additional initial-state constructors for robustness studies, including:

- all-zero product state
- alternating product state
- equal-weight plus state

The main reported results use the all-zero state.

---

## Method

### Hilbert Space

For a chain of N spin-1/2 degrees of freedom, the Hilbert-space dimension is

```text
dim(H) = 2^N.
```

The calculations therefore use exact diagonalization and are restricted to small system sizes.

### Time Evolution

For a time-independent Hamiltonian, the Hamiltonian is diagonalized once:

```text
H = V diag(E) V†
```

The state is then evolved in the eigenbasis:

```text
|ψ(t)⟩ = V exp(-iEt) V† |ψ(0)⟩.
```

### Density Matrix

The pure-state density matrix is

```text
ρ(t) = |ψ(t)⟩⟨ψ(t)|.
```

### Reduced Density Matrix

For subsystem A,

```text
ρ_A(t) = Tr_B[ρ(t)].
```

The project implements a generic partial-trace routine that can retain arbitrary subsets of qubits.

### Subsystem Entropy

The von Neumann entropy is calculated from the eigenvalues {λ_k} of the reduced density matrix:

```text
S_A(t) = -Σ_k λ_k ln(λ_k).
```

Numerical calculations use Hermitian symmetrization and Hermitian eigensolvers for stable entropy evaluation.

---

## Metrics

The project calculates several quantitative measures of the entropy dynamics.

### Time-Averaged Entropy

```text
⟨S_A⟩_T = (1/T) ∫₀ᵀ S_A(t) dt
```

The numerical integral is evaluated using the simulated time grid.

### Maximum Entropy

```text
S_max = max_t S_A(t)
```

### Normalized Maximum Entropy

```text
S_max / ln(2)
```

For a one-qubit subsystem, this quantity is bounded by 1.

### Fraction Above a Threshold

For a chosen entropy threshold S₀,

```text
f(S₀) = (1/T) ∫₀ᵀ Θ[S_A(t) - S₀] dt
```

where Θ denotes the indicator function.

### First Local Maximum

The simulation also identifies the first detected local maximum of the entropy curve.

### Recurrence Criterion

Recurrence is treated operationally. A recurrence is detected when the entropy returns below a specified threshold after having previously exceeded that threshold.

For the baseline analysis,

```text
threshold = 10⁻³.
```

Therefore, the statement that no recurrence was observed refers specifically to this numerical criterion and finite simulation window.

---

## Validation

The project includes multiple layers of numerical validation.

### Hamiltonian Validation

Tests verify:

- correct matrix dimensions
- Hermiticity
- analytical N=2 eigenvalues

### Quantum-State Validation

Tests verify:

- state normalization
- density-matrix construction
- density-matrix Hermiticity
- unit trace
- partial-trace consistency

### Dynamical Validation

Tests verify:

- preservation of state normalization
- correct t = 0 evolution
- correct multi-time evolution output

### Energy Conservation

For the time-independent Hamiltonian,

```text
E(t) = ⟨ψ(t)|H|ψ(t)⟩
```

should remain constant. The test suite verifies this numerically.

### Entropy Validation

The implementation is tested against known cases including:

- pure states with zero entropy
- maximally mixed one-qubit states with entropy ln(2)
- numerical positivity of the entropy

### Analytical N=2 Benchmark

The N=2 dynamics has an analytical benchmark that is compared with the numerical time evolution.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling.git
cd QuantumEntropyScaling
```

Create and activate a virtual environment if desired:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project:

```bash
pip install -e .
```

For the exact dependency versions used for the v1.0.0 development environment:

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Example

The following example uses the same all-zero product state used in the baseline study:

```python
import numpy as np

from quantum_entropy.hamiltonian import build_ising_chain
from quantum_entropy.dynamics import TimeEvolution
from quantum_entropy.states import all_zero_state

N, J, h = 6, 2.0, 2.0

H = build_ising_chain(N, J, h)
evolution = TimeEvolution(H)

psi0 = all_zero_state(N)

times = np.linspace(0.0, 10.0, 200)
states = evolution.evolve_many(psi0, times)
```

### Complete Entropy Simulation

```python
import numpy as np

from quantum_entropy.simulation import simulate_entropy

times = np.linspace(0.0, 5.0, 500)

times, entropy = simulate_entropy(
    N=6,
    J=2.0,
    h=2.0,
    times=times,
    keep=(0,)
)
```

### Reproducing the Main Results

Run:

```bash
python scripts/run_simulation.py
```

The script generates:

```text
data/entropy_N2_J2_h2.csv
data/entropy_N3_J2_h2.csv
data/entropy_N4_J2_h2.csv
data/entropy_N5_J2_h2.csv
data/entropy_N6_J2_h2.csv
data/entropy_metrics_J2_h2.csv
```

and:

```text
figures/entropy_N2_N6_comparison.png
figures/maximum_entropy_vs_N.png
```

---

## Project Structure

```text
QuantumEntropyScaling/
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── src/
│   └── quantum_entropy/
│       ├── __init__.py
│       ├── hamiltonian.py      # Transverse-field Ising Hamiltonian
│       ├── dynamics.py         # Unitary time evolution
│       ├── quantum.py          # Density matrices and partial trace
│       ├── states.py           # Initial-state constructors
│       ├── observables.py      # Entropy, purity, expectation values
│       ├── metrics.py          # Dynamical summary metrics
│       └── simulation.py       # Main simulation routine
│
├── scripts/
│   └── run_simulation.py       # Reproduces the main numerical results
│
├── tests/
│   ├── test_hamiltonian.py
│   ├── test_quantum.py
│   ├── test_dynamics.py
│   ├── test_observables.py
│   ├── test_energy.py
│   ├── test_n2_exact.py
│   └── test_metrics.py
│
├── data/
│   ├── entropy_N2_J2_h2.csv
│   ├── entropy_N3_J2_h2.csv
│   ├── entropy_N4_J2_h2.csv
│   ├── entropy_N5_J2_h2.csv
│   ├── entropy_N6_J2_h2.csv
│   └── entropy_metrics_J2_h2.csv
│
├── figures/
│   ├── entropy_N2_N6_comparison.png
│   └── maximum_entropy_vs_N.png
│
└── docs/
    └── methodology.md
```

---

## Requirements

The project requires:

- Python 3.10 or later
- NumPy
- SciPy
- Matplotlib

Pytest is used for automated testing.

Exact package versions used for the v1.0.0 development environment are pinned in:

```text
requirements.txt
```

---

## Testing

Run the test suite with:

```bash
pytest -q
```

The current test suite contains 28 automated tests covering:

- Hamiltonian construction
- quantum-state preparation
- density matrices
- partial traces
- unitary time evolution
- energy conservation
- observables
- entropy metrics
- analytical N=2 dynamics

The v1.0.0 development version passes:

```text
28 passed
```

---

## Limitations

The results of this project should be interpreted within the following limitations:

- The calculations are restricted to small system sizes, N = 2, ..., 6.
- Exact diagonalization scales exponentially with system size because the Hilbert-space dimension is 2^N.
- The calculations do not establish a thermodynamic-limit result.
- The observed finite-size trends do not establish a phase transition.
- The subsystem considered in the main analysis is a single qubit, so its entropy is bounded by ln(2).
- The transverse-field Ising model studied here is integrable in the form implemented in this project. The results should therefore not be interpreted as evidence for generic chaotic dynamics or ETH.
- The simulations use a finite observation window, t ∈ [0, 5].
- The recurrence analysis uses an operational entropy threshold rather than exact return of the full many-body state.
- Subsystem entanglement entropy is not equivalent to thermodynamic entropy.
- The observed effective irreversibility is a subsystem-level phenomenon within globally unitary dynamics and does not imply fundamental irreversible microscopic dynamics.
- The finite-size behavior is not strictly monotonic for all observables, as illustrated by the N = 6 results.

---

## Scientific Interpretation

The numerical results are consistent with the following qualitative picture:

As the number of interacting degrees of freedom increases, a local subsystem can become more strongly entangled with the rest of the finite quantum system. This can produce persistent temporal mixing at the subsystem level even though the full state continues to evolve according to reversible unitary dynamics.

For the finite systems studied here, the time-averaged entropy and the fraction of time above a fixed entropy threshold generally increase over the smaller system sizes considered, while the maximum entropy remains close to the one-qubit bound ln(2).

However, the results should be understood as finite-size numerical evidence rather than as a demonstration of a new dynamical law, a thermodynamic phase transition, generic thermalization, ETH, or fundamental irreversibility.

---

## Related Literature

The theoretical context of this project is related to entanglement dynamics following quantum quenches and to entanglement evolution in one-dimensional spin systems, including integrable transverse-field Ising chains.

- Calabrese, P., & Cardy, J. (2005). Evolution of entanglement entropy in one-dimensional systems. *Journal of Statistical Mechanics*, P04010.  
  https://doi.org/10.1088/1742-5468/2005/04/P04010

- Calabrese, P., & Cardy, J. (2007). Quantum quenches in extended systems. *Journal of Statistical Mechanics*, P06008.  
  https://doi.org/10.1088/1742-5468/2007/06/P06008

- Calabrese, P., Essler, F. H., & Fagotti, M. (2012). Quantum quench in the transverse field Ising chain. *Journal of Statistical Mechanics*, P07022.  
  https://doi.org/10.1088/1742-5468/2012/07/P07022

- Latorre, J. I., & Riera, A. (2009). A short review on entanglement in quantum spin systems. *Journal of Physics A: Mathematical and Theoretical*, 42, 504002.  
  https://doi.org/10.1088/1751-8113/42/50/504002

- Schmitt, M., & Kehrein, S. (2016). Effective time reversal and echo dynamics in the transverse field Ising model. *Europhysics Letters*, 115, 50001.  
  https://iopscience.iop.org/article/10.1209/0295-5075/115/50001/meta

- Heyl, M. (2018). Dynamical quantum phase transitions: a review. *Reports on Progress in Physics*, 81, 054001.  
  https://doi.org/10.1088/1361-6633/aaaf9a

- Weinberg, P., & Bukov, M. (2017). QuSpin: a Python package for dynamics and exact diagonalisation of quantum many body systems part I. *SciPost Physics*, 2, 003.  
  https://arxiv.org/abs/1610.03042

- Weinberg, P., & Bukov, M. (2019). QuSpin: a Python package for dynamics and exact diagonalisation of quantum many body systems part II. *SciPost Physics*, 7, 020.  
  https://arxiv.org/abs/1804.06782

---

## Citation

If you use this code in your research, please cite:

```bibtex
@software{amiri2026quantum,
  author  = {Amiri, Abolfazl},
  title   = {Quantum Entropy Scaling},
  year    = {2026},
  url     = {https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling},
  version = {v1.0.0}
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Release

Current stable release:

**v1.0.0**

Repository:

https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling
