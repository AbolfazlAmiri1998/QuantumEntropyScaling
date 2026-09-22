import numpy as np

from quantum_entropy.observables import (
    von_neumann_entropy,
    purity,
)


def test_entropy_of_pure_state_is_zero():
    rho = np.array(
        [[1.0, 0.0],
         [0.0, 0.0]],
        dtype=complex,
    )

    S = von_neumann_entropy(rho)

    assert np.isclose(S, 0.0)


def test_entropy_of_maximally_mixed_qubit_is_ln2():
    rho = 0.5 * np.eye(2, dtype=complex)

    S = von_neumann_entropy(rho)

    assert np.isclose(S, np.log(2))


def test_purity_of_pure_state_is_one():
    rho = np.array(
        [[1.0, 0.0],
         [0.0, 0.0]],
        dtype=complex,
    )

    P = purity(rho)

    assert np.isclose(P, 1.0)


def test_purity_of_maximally_mixed_qubit_is_one_half():
    rho = 0.5 * np.eye(2, dtype=complex)

    P = purity(rho)

    assert np.isclose(P, 0.5)


def test_entropy_is_zero_for_pure_state_without_negative_roundoff():
    rho = np.array(
        [[1.0, 0.0],
         [0.0, 0.0]],
        dtype=complex,
    )

    S = von_neumann_entropy(rho)

    assert S >= 0.0
    assert np.isclose(S, 0.0)