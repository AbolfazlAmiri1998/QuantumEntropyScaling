"""Quantum entropy scaling simulation package."""

from .hamiltonian import build_ising_chain
from .dynamics import TimeEvolution
from .observables import von_neumann_entropy, purity, expectation_value
from .quantum import state_to_density_matrix, partial_trace
from .simulation import simulate_entropy
from .states import (
    computational_basis_state,
    all_zero_state,
    alternating_state,
    plus_state,
)
from .metrics import (
    maximum_entropy,
    normalized_maximum_entropy,
    first_local_maximum,
    time_average_entropy,
    first_recurrence_time,
    fraction_above_threshold,
)

__all__ = [
    "build_ising_chain",
    "TimeEvolution",
    "von_neumann_entropy",
    "purity",
    "expectation_value",
    "state_to_density_matrix",
    "partial_trace",
    "simulate_entropy",
    "computational_basis_state",
    "all_zero_state",
    "alternating_state",
    "plus_state",
    "maximum_entropy",
    "normalized_maximum_entropy",
    "first_local_maximum",
    "time_average_entropy",
    "first_recurrence_time",
    "fraction_above_threshold",
]