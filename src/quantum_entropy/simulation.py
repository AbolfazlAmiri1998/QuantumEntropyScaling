import numpy as np

from .hamiltonian import build_ising_chain
from .states import all_zero_state
from .dynamics import TimeEvolution
from .quantum import state_to_density_matrix, partial_trace
from .observables import von_neumann_entropy


def simulate_entropy(
    N,
    J,
    h,
    times,
    keep=(0,),
    initial_state=None,
):
    """
    Simulate subsystem von Neumann entropy as a function of time.

    Parameters
    ----------
    N : int
        Number of spins.
    J : float
        Nearest-neighbor interaction strength.
    h : float
        Transverse-field strength.
    times : array-like
        Time points at which the entropy is evaluated.
    keep : tuple[int]
        Qubits retained in the subsystem.
    initial_state : numpy.ndarray or None
        Initial state. If None, |00...0> is used.

    Returns
    -------
    times : numpy.ndarray
        Time grid.
    entropy : numpy.ndarray
        Subsystem entropy at each time.
    """
    times = np.asarray(times, dtype=float)

    if times.ndim != 1:
        raise ValueError("times must be a one-dimensional array.")

    H = build_ising_chain(N, J, h)

    if initial_state is None:
        psi0 = all_zero_state(N)
    else:
        psi0 = np.asarray(initial_state, dtype=complex)

    evolution = TimeEvolution(H)

    entropy_values = []

    for t in times:
        psi_t = evolution.evolve(psi0, t)

        rho = state_to_density_matrix(psi_t)

        rho_subsystem = partial_trace(
            rho,
            keep=keep,
            N=N,
        )

        entropy = von_neumann_entropy(
            rho_subsystem
        )

        entropy_values.append(entropy)

    return times, np.array(entropy_values)