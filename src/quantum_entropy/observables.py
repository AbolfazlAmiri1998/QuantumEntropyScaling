import numpy as np


def von_neumann_entropy(rho, tolerance=1e-12):
    """
    Calculate the von Neumann entropy of a density matrix.

    S(rho) = -Tr(rho log(rho))
    """
    rho = np.asarray(rho, dtype=complex)

    if rho.ndim != 2:
        raise ValueError("rho must be a two-dimensional matrix.")

    if rho.shape[0] != rho.shape[1]:
        raise ValueError("rho must be a square matrix.")

    # Remove tiny numerical non-Hermiticity.
    rho = 0.5 * (rho + rho.conj().T)

    if not np.isclose(np.trace(rho), 1.0, atol=1e-10):
        raise ValueError("rho must have trace one.")

    eigenvalues = np.linalg.eigvalsh(rho)

    if np.any(eigenvalues < -tolerance):
        raise ValueError(
            "rho has significantly negative eigenvalues."
        )

    # Remove tiny negative eigenvalues caused by floating-point
    # roundoff.
    eigenvalues = np.clip(eigenvalues, 0.0, None)

    nonzero = eigenvalues > 0.0

    entropy = float(
        -np.sum(
            eigenvalues[nonzero]
            * np.log(eigenvalues[nonzero])
        )
    )

    # Numerical roundoff can produce values such as
    # -4.4e-16 instead of exactly zero.
    if entropy < 0.0 and abs(entropy) < tolerance:
        entropy = 0.0

    return entropy


def purity(rho):
    """
    Calculate the purity Tr(rho^2).

    A pure state has purity 1.
    A mixed state has purity less than 1.
    """
    rho = np.asarray(rho, dtype=complex)

    if rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        raise ValueError("rho must be a square matrix.")

    rho = 0.5 * (rho + rho.conj().T)

    return float(np.real(np.trace(rho @ rho)))


def expectation_value(psi, operator):
    """
    Calculate <psi|O|psi>.
    """
    psi = np.asarray(psi, dtype=complex)
    operator = np.asarray(operator, dtype=complex)

    if psi.ndim != 1:
        raise ValueError("psi must be a state vector.")

    if operator.shape != (len(psi), len(psi)):
        raise ValueError(
            "operator dimensions must match the state dimension."
        )

    return float(
        np.real(
            np.vdot(psi, operator @ psi)
        )
    )