import numpy as np

from quantum_entropy.hamiltonian import build_ising_chain
from quantum_entropy.states import all_zero_state
from quantum_entropy.dynamics import TimeEvolution
from quantum_entropy.quantum import (
    state_to_density_matrix,
    partial_trace,
)
from quantum_entropy.observables import von_neumann_entropy


def exact_n2_state(J, h, t):
    """
    Exact analytical state for N=2 starting from |00>.
    """

    R = np.sqrt(J**2 + 4.0 * h**2)

    a = (
        np.cos(R * t)
        - 1j * (J / R) * np.sin(R * t)
    )

    b = (
        -1j * (2.0 * h / R) * np.sin(R * t)
    )

    phase = np.exp(-1j * J * t)

    c00 = (a + phase) / 2.0
    c11 = (a - phase) / 2.0

    c01 = b / 2.0
    c10 = b / 2.0

    return np.array(
        [c00, c01, c10, c11],
        dtype=complex,
    )


def exact_n2_entropy(J, h, t):
    """
    Exact analytical subsystem entropy for N=2.
    """

    psi = exact_n2_state(J, h, t)

    rho = np.outer(
        psi,
        psi.conj(),
    )

    rho_A = partial_trace(
        rho,
        keep=(0,),
        N=2,
    )

    return von_neumann_entropy(rho_A)


def test_exact_n2_state_is_normalized():
    J = 2.0
    h = 2.0

    times = np.linspace(0.0, 5.0, 20)

    for t in times:
        psi = exact_n2_state(J, h, t)

        assert np.isclose(
            np.linalg.norm(psi),
            1.0,
            atol=1e-10,
        )


def test_exact_n2_state_matches_numerical_evolution():
    J = 2.0
    h = 2.0

    H = build_ising_chain(
        N=2,
        J=J,
        h=h,
    )

    psi0 = all_zero_state(2)

    evolution = TimeEvolution(H)

    times = np.linspace(
        0.0,
        5.0,
        20,
    )

    for t in times:
        psi_numerical = evolution.evolve(
            psi0,
            t,
        )

        psi_exact = exact_n2_state(
            J,
            h,
            t,
        )

        assert np.allclose(
            psi_numerical,
            psi_exact,
            atol=1e-10,
        )


def test_exact_n2_entropy_matches_numerical_entropy():
    J = 2.0
    h = 2.0

    H = build_ising_chain(
        N=2,
        J=J,
        h=h,
    )

    psi0 = all_zero_state(2)

    evolution = TimeEvolution(H)

    times = np.linspace(
        0.0,
        5.0,
        20,
    )

    for t in times:
        psi_numerical = evolution.evolve(
            psi0,
            t,
        )

        rho_numerical = state_to_density_matrix(
            psi_numerical
        )

        rho_A_numerical = partial_trace(
            rho_numerical,
            keep=(0,),
            N=2,
        )

        entropy_numerical = von_neumann_entropy(
            rho_A_numerical
        )

        entropy_exact = exact_n2_entropy(
            J,
            h,
            t,
        )

        assert np.isclose(
            entropy_numerical,
            entropy_exact,
            atol=1e-10,
        )