import numpy as np

from quantum_entropy.states import all_zero_state
from quantum_entropy.quantum import (
    state_to_density_matrix,
    partial_trace,
)


def test_all_zero_state_is_normalized():
    psi = all_zero_state(3)

    assert np.isclose(np.linalg.norm(psi), 1.0)


def test_density_matrix_is_hermitian():
    psi = all_zero_state(2)

    rho = state_to_density_matrix(psi)

    assert np.allclose(rho, rho.conj().T)


def test_density_matrix_has_trace_one():
    psi = all_zero_state(2)

    rho = state_to_density_matrix(psi)

    assert np.isclose(np.trace(rho), 1.0)


def test_partial_trace_preserves_trace():
    psi = all_zero_state(3)

    rho = state_to_density_matrix(psi)

    rho_A = partial_trace(
        rho,
        keep=(0,),
        N=3,
    )

    assert np.isclose(np.trace(rho_A), 1.0)


def test_product_state_has_zero_entropy():
    psi = all_zero_state(2)

    rho = state_to_density_matrix(psi)

    rho_A = partial_trace(
        rho,
        keep=(0,),
        N=2,
    )

    eigenvalues = np.linalg.eigvalsh(rho_A)

    assert np.allclose(
        eigenvalues,
        np.array([0.0, 1.0]),
    )