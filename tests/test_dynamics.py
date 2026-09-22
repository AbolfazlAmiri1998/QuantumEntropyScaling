import numpy as np

from quantum_entropy.hamiltonian import build_ising_chain
from quantum_entropy.states import all_zero_state
from quantum_entropy.dynamics import TimeEvolution


def test_time_evolution_preserves_norm():
    N = 3
    J = 2.0
    h = 2.0

    H = build_ising_chain(N, J, h)
    psi0 = all_zero_state(N)

    evolution = TimeEvolution(H)

    times = np.linspace(0.0, 5.0, 20)

    for t in times:
        psi_t = evolution.evolve(psi0, t)

        assert np.isclose(
            np.linalg.norm(psi_t),
            1.0,
            atol=1e-10,
        )


def test_evolution_at_zero_time_returns_initial_state():
    N = 3
    J = 2.0
    h = 2.0

    H = build_ising_chain(N, J, h)
    psi0 = all_zero_state(N)

    evolution = TimeEvolution(H)

    psi_t = evolution.evolve(psi0, 0.0)

    assert np.allclose(psi_t, psi0)


def test_evolve_many_returns_correct_shape():
    N = 3
    J = 2.0
    h = 2.0

    H = build_ising_chain(N, J, h)
    psi0 = all_zero_state(N)

    evolution = TimeEvolution(H)

    times = np.linspace(0.0, 1.0, 10)

    states = evolution.evolve_many(psi0, times)

    assert states.shape == (10, 2**N)