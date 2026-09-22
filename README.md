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

```text
H = J Σ_{i=1}^{N-1} σᶻ_i σᶻ_{i+1}  +  h Σ_{i=1}^{N} σˣ_i
```

The main observable is the von Neumann entropy of a one-qubit subsystem,

```text
S_A(t) = -Tr[ ρ_A(t) ln ρ_A(t) ]
```

The total quantum system remains closed and evolves unitarily. Therefore,
the entropy discussed in this project is subsystem entanglement entropy and
should not be interpreted as fundamental thermodynamic entropy.

## Main Results

For the finite systems studied here (N = 2, ..., 6):

- subsystem entropy becomes strongly time dependent as entanglement develops;
- the one-qubit entropy remains bounded by ln 2;
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

```text
H = J Σ_{i=1}^{N-1} σᶻ_i σᶻ_{i+1}  +  h Σ_{i=1}^{N} σˣ_i
```

The convention used here has a plus sign in front of both terms. For J > 0,
the nearest-neighbor interaction is antiferromagnetic.

**Note on sign conventions:** This differs from the standard TFIM
convention

```text
H = -J Σ σᶻ σᶻ  -  h Σ σˣ
```

The two are related by J → -J and h → -h.

The baseline parameters are:

```text
J = 2.0
h = 2.0
```

## Method

### Phase-space and initial state

The initial state is taken as a product state. The full Hilbert space has
dimension

```text
dim(H) = 2^N
```

### Time evolution

The Hamiltonian is diagonalized once:

```text
H = V diag(E) V†
```

The state is then evolved analytically in the eigenbasis:

```text
|ψ(t)⟩ = V exp(-i E t) V† |ψ(0)⟩
```

### Subsystem entropy

The reduced density matrix of subsystem A is obtained by tracing out the
complement:

```text
ρ_A(t) = Tr_B[ |ψ(t)⟩ ⟨ψ(t)| ]
```

The von Neumann entropy is then computed from the eigenvalues {λ_k} of ρ_A:

```text
S_A(t) = -Σ_k λ_k ln λ_k
```

### Observables and averages

Time-averaged entropy over a window [0, T]:

```text
⟨S_A⟩_T = (1/T) ∫_0^T S_A(t) dt
```

Fraction of time spent above a threshold S_0:

```text
f(S_0) = (1/T) ∫_0^T Θ[ S_A(t) - S_0 ] dt
```

where Θ is the Heaviside step function.

## Installation

Clone the repository and install in editable mode:

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