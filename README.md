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

$$
H = J \sum_{i=1}^{N-1} \sigma_i^z \sigma_{i+1}^z + h \sum_{i=1}^{N} \sigma_i^x
$$

The main observable is the von Neumann entropy of a one-qubit subsystem,

$$
S_A(t) = -\mathrm{Tr}\left[\rho_A(t) \ln \rho_A(t)\right]
$$

The total quantum system remains closed and evolves unitarily. Therefore,
the entropy discussed in this project is **subsystem entanglement entropy**
and should not be interpreted as fundamental thermodynamic entropy.

## Main Results

For the finite systems studied here ($N = 2, \ldots, 6$):

- Subsystem entropy becomes strongly time dependent as entanglement develops.
- The one-qubit entropy remains bounded by $\ln 2$.
- Time-averaged entropy generally increases across the small system sizes studied.
- The fraction of the simulated time spent above a fixed entropy threshold also generally increases.
- The microscopic evolution remains unitary and reversible.
- The results are consistent with increasingly persistent effective subsystem mixing caused by entanglement with the rest of the system.

These observations should be interpreted as **finite-size numerical evidence**,
not as a proof of a thermodynamic phase transition or fundamental
irreversibility.

## Model

The Hamiltonian is

$$
H = J \sum_{i=1}^{N-1} \sigma_i^z \sigma_{i+1}^z + h \sum_{i=1}^{N} \sigma_i^x
$$

The convention used here has a plus sign in front of both terms.
For $J > 0$, the nearest-neighbor interaction is antiferromagnetic.

> **Note on sign conventions:** This differs from the standard TFIM
> convention $H = -J\sum \sigma^z\sigma^z - h\sum \sigma^x$. The two are
> related by $J \to -J$ and $h \to -h$.

The baseline parameters are:

```text
J = 2.0
h = 2.0
```

## Method (Short Summary)

Phase-space variables and the relevant observables are computed via
exact diagonalization:

```text
H = J Σ σᶻσᶻ + h Σ σˣ
```

Time evolution is performed in the eigenbasis:

```text
|ψ(t)⟩ = V exp(-i E t) V† |ψ(0)⟩
```

The subsystem entropy is then evaluated as

$$
S_A(t) = -\sum_k \lambda_k \ln \lambda_k
$$

where $\{\lambda_k\}$ are the eigenvalues of the reduced density matrix
$\rho_A(t)$.

## Installation

```bash
git clone https://github.com/AbolfazlAmiri1998/QuantumEntropyScaling.git
cd QuantumEntropyScaling
pip install -e .
```

## Usage

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

## Project Structure

```text
QuantumEntropyScaling/
├── src/quantum_entropy/
│   ├── hamiltonian.py
│   ├── dynamics.py
│   └── observables.py
├── scripts/
├── tests/
├── data/
├── figures/
└── docs/
```

## License

See the [LICENSE](LICENSE) file for details.