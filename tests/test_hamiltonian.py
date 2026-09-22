import numpy as np

from quantum_entropy.hamiltonian import build_ising_chain


def test_hamiltonian_shape():
    N = 2
    H = build_ising_chain(N, J=2.0, h=2.0)

    assert H.shape == (4, 4)


def test_hamiltonian_is_hermitian():
    N = 3
    H = build_ising_chain(N, J=2.0, h=2.0)

    assert np.allclose(H, H.conj().T)


def test_n2_exact_eigenvalues():
    J = 2.0
    h = 2.0

    H = build_ising_chain(N=2, J=J, h=h)

    numerical = np.linalg.eigvalsh(H)

    R = np.sqrt(J**2 + 4 * h**2)

    exact = np.array([
        -R,
        -J,
        J,
        R,
    ])

    assert np.allclose(numerical, exact)