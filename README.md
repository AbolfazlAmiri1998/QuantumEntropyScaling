# Quantum Entropy Scaling

Exact-diagonalization study of subsystem entanglement dynamics in finite transverse-field Ising chains.

## Overview

This project investigates how increasing the number of interacting quantum spins changes the dynamics of a local subsystem.

**Central question:**

> How does increasing the number of degrees of freedom affect the transition from microscopic unitary dynamics to effectively irreversible subsystem behavior?

The study uses the transverse-field Ising Hamiltonian:

```
H = J Σ_{i=1}^{N-1} σᶻ_i σᶻ_{i+1}  +  h Σ_{i=1}^{N} σˣ_i
```

The main observable is the von Neumann entropy of a one-qubit subsystem:

```
S_A(t) = -Tr[ ρ_A(t) ln ρ_A(t) ]
```

**Important note:** The total quantum system remains closed and evolves unitarily. Therefore, the entropy discussed in this project is **subsystem entanglement entropy** and should not be interpreted as fundamental thermodynamic entropy.

## Main Results

For the finite systems studied here (N = 2, ..., 6) with J = h = 2.0:

### Time-Averaged Entropy

| N | ⟨S_A⟩_T | f(S > 0.5) |
|---|----------|-------------|
| 2 | 0.3461 | 0.3066 |
| 3 | 0.4371 | 0.4559 |
| 4 | 0.4645 | 0.5271 |
| 5 | 0.4859 | 0.6683 |
| 6 | 0.4843 | 0.6022 |

The time-averaged entropy increases from N=2 to N=5 and then slightly decreases at N=6. The fraction of time spent above S=0.5 follows a similar trend.

### Maximum Entropy

| N | S_max | S_max / ln2 |
|---|-------|-------------|
| 2 | 0.6795 | 0.9803 |
| 3 | 0.6908 | 0.9966 |
| 4 | 0.6850 | 0.9883 |
| 5 | 0.6870 | 0.9911 |
| 6 | 0.6854 | 0.9888 |

The maximum entropy remains close to ln2 for all system sizes, confirming that the one-qubit subsystem never exceeds its theoretical bound.

### Key Observations

- Subsystem entropy becomes strongly time-dependent as entanglement develops.
- The one-qubit entropy remains bounded by ln 2.
- Time-averaged entropy generally increases across the small system sizes studied.
- The fraction of the simulated time spent above a fixed entropy threshold also generally increases.
- The microscopic evolution remains unitary and reversible.
- No full recurrence (return to S < 10^-3) was observed within the simulation window [0, 5].

These observations should be interpreted as **finite-size numerical evidence**, not as a proof of a thermodynamic phase transition or fundamental irreversibility.

### Figures

- `figures/entropy_N2_N6_comparison.png`: Time evolution of subsystem entropy for N=2,...,6.
- `figures/maximum_entropy_vs_N.png`: Maximum one-qubit entropy vs system size.

## Model

The Hamiltonian is:

```
H = J Σ_{i=1}^{N-1} σᶻ_i σᶻ_{i+1}  +  h Σ_{i=1}^{N} σˣ_i
```

The convention used here has a plus sign in front of both terms. For J > 0, the nearest-neighbor interaction is antiferromagnetic.

**Note on sign conventions:** This differs from the standard TFIM convention

```
H = -J Σ σᶻ σᶻ  -  h Σ σˣ
```

The two are related by J → -J and h → -h.

The baseline parameters are:

```
J = 2.0
h = 2.0
```

## Method

### Hilbert space

```
dim(H) = 2^N
```

### Time evolution

The Hamiltonian is diagonalized once:

```
H = V diag(E) V†
```

The state is then evolved analytically in the eigenbasis:

```
|ψ(t)⟩ = V exp(-i E t) V† |ψ(0)⟩
```

### Subsystem entropy

The reduced density matrix of subsystem A:

```
ρ_A(t) = Tr_B[ |ψ(t)⟩ ⟨ψ(t)| ]
```

The von Neumann entropy from eigenvalues {λ_k} of ρ_A:

```
S_A(t) = -Σ_k λ_k ln λ_k
```

### Metrics

- **Time-averaged entropy:** ⟨S_A⟩_T = (1/T) ∫_0^T S_A(t) dt
- **Fraction above threshold:** f(S_0) = (1/T) ∫_0^T Θ[ S_A(t) - S_0 ] dt

## Installation

```bash
git clone https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling.git
cd QuantumEntropyScaling
pip install -e .
```

## Usage

### Basic example

```python
import numpy as np
from quantum_entropy.hamiltonian import build_ising_chain
from quantum_entropy.dynamics import TimeEvolution
from quantum_entropy.observables import von_neumann_entropy

N, J, h = 6, 2.0, 2.0

H = build_ising_chain(N, J, h)
evolution = TimeEvolution(H)

psi0 = np.ones(2**N, dtype=complex) / np.sqrt(2**N)
times = np.linspace(0.0, 10.0, 200)
states = evolution.evolve_many(psi0, times)
```

### Complete simulation

```python
from quantum_entropy.simulation import simulate_entropy

times = np.linspace(0.0, 5.0, 500)
times, entropy = simulate_entropy(
    N=6, J=2.0, h=2.0, times=times, keep=(0,)
)
```

### Reproducing all results

```bash
python scripts/run_simulation.py
```

This generates:

- `data/entropy_N*_J2_h2.csv` — entropy time series for each N
- `data/entropy_metrics_J2_h2.csv` — summary metrics table
- `figures/entropy_N2_N6_comparison.png` — entropy dynamics
- `figures/maximum_entropy_vs_N.png` — scaling plot

## Project Structure

```
QuantumEntropyScaling/
├── src/quantum_entropy/
│   ├── __init__.py
│   ├── hamiltonian.py      # Transverse-field Ising Hamiltonian
│   ├── dynamics.py         # Unitary time evolution
│   ├── observables.py      # von Neumann entropy, purity
│   ├── quantum.py          # Density matrix, partial trace
│   ├── states.py           # Initial states
│   ├── simulation.py       # Main simulation driver
│   └── metrics.py          # Time-averaged quantities
├── scripts/
│   └── run_simulation.py   # Reproduces all results
├── data/
│   ├── entropy_N*_J2_h2.csv
│   └── entropy_metrics_J2_h2.csv
├── figures/
│   ├── entropy_N2_N6_comparison.png
│   └── maximum_entropy_vs_N.png
├── tests/
├── docs/
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## Requirements

- Python >= 3.10
- numpy
- scipy
- matplotlib

See `requirements.txt` for exact versions.

## Testing

```bash
pip install -e ".[dev]"
pytest tests/
```

## Citation

If you use this code in your research, please cite:

```bibtex
@software{amiri2026quantum,
  author = {Amiri, Abolfazl},
  title = {Quantum Entropy Scaling},
  year = {2026},
  url = {https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling}
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.