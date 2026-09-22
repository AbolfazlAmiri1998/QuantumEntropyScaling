import numpy as np
from scipy.linalg import eigh


class TimeEvolution:
    """
    Time evolution for a time-independent Hamiltonian.

    The Hamiltonian is diagonalized once:

        H = V diag(E) V^dagger

    and the state is evolved using

        |psi(t)> = V exp(-i E t) V^dagger |psi(0)>.
    """

    def __init__(self, H):
        H = np.asarray(H, dtype=complex)

        if H.ndim != 2:
            raise ValueError("H must be a two-dimensional matrix.")

        if H.shape[0] != H.shape[1]:
            raise ValueError("H must be a square matrix.")

        if not np.allclose(H, H.conj().T):
            raise ValueError("H must be Hermitian.")

        self.H = H

        # eigh is appropriate for Hermitian matrices.
        self.energies, self.eigenvectors = eigh(H)

    def evolve(self, psi0, t):
        """
        Evolve an initial state to time t.

        Parameters
        ----------
        psi0 : numpy.ndarray
            Initial state vector.
        t : float
            Time.

        Returns
        -------
        numpy.ndarray
            State vector |psi(t)>.
        """
        psi0 = np.asarray(psi0, dtype=complex)

        dimension = self.H.shape[0]

        if psi0.shape != (dimension,):
            raise ValueError(
                f"psi0 must have shape ({dimension},)."
            )

        coefficients = self.eigenvectors.conj().T @ psi0

        phases = np.exp(-1j * self.energies * t)

        psi_t = self.eigenvectors @ (coefficients * phases)

        return psi_t

    def evolve_many(self, psi0, times):
        """
        Evolve an initial state over an array of times.

        Returns
        -------
        numpy.ndarray
            Array with shape (len(times), dimension).
        """
        times = np.asarray(times, dtype=float)

        return np.array([
            self.evolve(psi0, t)
            for t in times
        ])