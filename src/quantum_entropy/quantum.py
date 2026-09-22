import numpy as np


def state_to_density_matrix(psi):
    """
    Construct the density matrix |psi><psi|.

    Parameters
    ----------
    psi : numpy.ndarray
        State vector.

    Returns
    -------
    numpy.ndarray
        Density matrix.
    """
    psi = np.asarray(psi, dtype=complex)

    if psi.ndim != 1:
        raise ValueError("psi must be a one-dimensional state vector.")

    norm = np.linalg.norm(psi)

    if not np.isclose(norm, 1.0, atol=1e-10):
        raise ValueError(
            "psi must be normalized before constructing the density matrix."
        )

    return np.outer(psi, psi.conj())


def partial_trace(rho, keep, N):
    """
    Compute the reduced density matrix by tracing out all
    qubits except those listed in `keep`.

    Parameters
    ----------
    rho : numpy.ndarray
        Full density matrix of dimension 2**N x 2**N.
    keep : list[int] or tuple[int]
        Qubit indices to retain.
    N : int
        Total number of qubits.

    Returns
    -------
    numpy.ndarray
        Reduced density matrix for the retained subsystem.

    Notes
    -----
    Qubit indices follow the tensor-product ordering used
    throughout this project:

        |q0 q1 ... q(N-1)>
    """
    rho = np.asarray(rho, dtype=complex)

    dimension = 2**N

    if rho.shape != (dimension, dimension):
        raise ValueError(
            f"rho must have shape ({dimension}, {dimension})."
        )

    keep = list(keep)

    if len(keep) == 0:
        raise ValueError("At least one qubit must be kept.")

    if len(set(keep)) != len(keep):
        raise ValueError("keep contains duplicate qubit indices.")

    if any(q < 0 or q >= N for q in keep):
        raise ValueError("Qubit index in keep is out of range.")

    traced = [q for q in range(N) if q not in keep]

    # Put axes in the order:
    #
    # kept row indices
    # traced row indices
    # kept column indices
    # traced column indices
    #
    # This makes the partial trace a simple trace over
    # the second and fourth groups of indices.

    permutation = (
        keep
        + traced
        + [q + N for q in keep]
        + [q + N for q in traced]
    )

    rho_tensor = rho.reshape([2] * (2 * N))
    rho_tensor = np.transpose(rho_tensor, permutation)

    dimension_keep = 2 ** len(keep)
    dimension_trace = 2 ** len(traced)

    rho_tensor = rho_tensor.reshape(
        dimension_keep,
        dimension_trace,
        dimension_keep,
        dimension_trace,
    )

    rho_reduced = np.trace(
        rho_tensor,
        axis1=1,
        axis2=3,
    )

    return rho_reduced