import numpy as np

from quantum_entropy.hamiltonian import build_ising_chain
from quantum_entropy.states import all_zero_state
from quantum_entropy.dynamics import TimeEvolution


def test_energy_is_conserved():
    N = 3
    J = 2.0
    h = 2.0

    H = build_ising_chain(N, J, h)
    psi0 = all_zero_state(N)

    evolution = TimeEvolution(H)

    energy_initial = np.vdot(
        psi0,
        H @ psi0
    ).real

    times = np.linspace(0.0, 5.0, 20)

    for t in times:
        psi_t = evolution.evolve(psi0, t)

        energy_t = np.vdot(
            psi_t,
            H @ psi_t
        ).real

        assert np.isclose(
            energy_t,
            energy_initial,
            atol=1e-10,
        )