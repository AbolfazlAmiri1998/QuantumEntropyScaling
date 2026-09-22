import numpy as np


def computational_basis_state(bitstring):
    """
    Construct a computational-basis state from a bitstring.

    Examples
    --------
    "000" -> |000>
    "010" -> |010>
    "111" -> |111>

    Parameters
    ----------
    bitstring : str
        String containing only '0' and '1'.

    Returns
    -------
    numpy.ndarray
        Normalized state vector.
    """
    if not bitstring:
        raise ValueError("bitstring cannot be empty.")

    if any(bit not in "01" for bit in bitstring):
        raise ValueError("bitstring must contain only '0' and '1'.")

    N = len(bitstring)
    dimension = 2**N

    # Convert binary string to basis-state index.
    index = int(bitstring, 2)

    state = np.zeros(dimension, dtype=complex)
    state[index] = 1.0

    return state


def all_zero_state(N):
    """
    Return the product state |00...0> for N spins.
    """
    if not isinstance(N, int):
        raise TypeError("N must be an integer.")

    if N < 1:
        raise ValueError("N must be at least 1.")

    return computational_basis_state("0" * N)


def alternating_state(N):
    """
    Return the product state |0101...> for N spins.
    """
    if not isinstance(N, int):
        raise TypeError("N must be an integer.")

    if N < 1:
        raise ValueError("N must be at least 1.")

    bitstring = "".join(
        "0" if i % 2 == 0 else "1"
        for i in range(N)
    )

    return computational_basis_state(bitstring)


def plus_state(N):
    """
    Return the product state |+>^{tensor N},
    where |+> = (|0> + |1>) / sqrt(2).
    """
    if not isinstance(N, int):
        raise TypeError("N must be an integer.")

    if N < 1:
        raise ValueError("N must be at least 1.")

    single_qubit_plus = np.array(
        [1.0, 1.0],
        dtype=complex
    ) / np.sqrt(2)

    state = single_qubit_plus

    for _ in range(N - 1):
        state = np.kron(state, single_qubit_plus)

    return state