import numpy as np


SX = np.array(
    [[0, 1],
     [1, 0]],
    dtype=complex
)

SZ = np.array(
    [[1, 0],
     [0, -1]],
    dtype=complex
)

IDENTITY = np.eye(2, dtype=complex)


def tensor_product(*operators):
    """Return the Kronecker product of multiple operators."""
    result = operators[0]

    for operator in operators[1:]:
        result = np.kron(result, operator)

    return result


def build_ising_chain(N, J, h):
    """
    Construct the transverse-field Ising Hamiltonian.

    H = J * sum_i sigma_z(i) sigma_z(i+1)
        + h * sum_i sigma_x(i)

    Parameters
    ----------
    N : int
        Number of spins.
    J : float
        Nearest-neighbor interaction strength.
    h : float
        Transverse-field strength.

    Returns
    -------
    numpy.ndarray
        Complex Hermitian Hamiltonian matrix of shape (2**N, 2**N).
    """
    if N < 2:
        raise ValueError("N must be at least 2.")

    if not isinstance(N, int):
        raise TypeError("N must be an integer.")

    dimension = 2**N

    H = np.zeros(
        (dimension, dimension),
        dtype=complex
    )

    # Nearest-neighbor interaction terms:
    # J * sigma_z(i) sigma_z(i+1)
    for i in range(N - 1):
        operators = [IDENTITY] * N
        operators[i] = SZ
        operators[i + 1] = SZ

        H += J * tensor_product(*operators)

    # Transverse-field terms:
    # h * sigma_x(i)
    for i in range(N):
        operators = [IDENTITY] * N
        operators[i] = SX

        H += h * tensor_product(*operators)

    return H