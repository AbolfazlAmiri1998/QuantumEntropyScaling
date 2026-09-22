import numpy as np


def _validate_time_series(times, values):
    """
    Validate a one-dimensional time series.
    """
    times = np.asarray(times, dtype=float)
    values = np.asarray(values, dtype=float)

    if times.ndim != 1:
        raise ValueError("times must be one-dimensional.")

    if values.ndim != 1:
        raise ValueError("values must be one-dimensional.")

    if len(times) != len(values):
        raise ValueError(
            "times and values must have the same length."
        )

    if len(times) < 2:
        raise ValueError(
            "At least two time points are required."
        )

    if not np.all(np.isfinite(times)):
        raise ValueError("times must contain finite values.")

    if not np.all(np.isfinite(values)):
        raise ValueError("values must contain finite values.")

    if np.any(np.diff(times) <= 0):
        raise ValueError(
            "times must be strictly increasing."
        )

    return times, values


def maximum_entropy(entropy):
    """
    Return the maximum entropy in a time series.
    """
    entropy = np.asarray(entropy, dtype=float)

    if entropy.ndim != 1:
        raise ValueError(
            "entropy must be one-dimensional."
        )

    if len(entropy) == 0:
        raise ValueError(
            "entropy cannot be empty."
        )

    if not np.all(np.isfinite(entropy)):
        raise ValueError(
            "entropy must contain finite values."
        )

    return float(np.max(entropy))


def normalized_maximum_entropy(entropy):
    """
    Return the maximum entropy normalized by ln(2).

    This normalization is appropriate for a one-qubit
    subsystem, whose von Neumann entropy satisfies

        0 <= S_A <= ln(2).
    """
    return maximum_entropy(entropy) / np.log(2)


def first_local_maximum(times, entropy):
    """
    Return the time and value of the first local maximum.

    A local maximum is identified by

        S[i] >= S[i-1]
        S[i] >= S[i+1]

    for an interior point i.

    Returns
    -------
    tuple or None
        (time, entropy) for the first local maximum,
        or None if no local maximum exists.
    """
    times, entropy = _validate_time_series(
        times,
        entropy,
    )

    for i in range(1, len(entropy) - 1):
        if (
            entropy[i] >= entropy[i - 1]
            and entropy[i] >= entropy[i + 1]
        ):
            return (
                float(times[i]),
                float(entropy[i]),
            )

    return None


def time_average_entropy(times, entropy):
    """
    Calculate the time-averaged entropy.

    The definition is

        S_bar = (1 / T) integral S(t) dt,

    evaluated numerically using the trapezoidal rule.
    """
    times, entropy = _validate_time_series(
        times,
        entropy,
    )

    duration = times[-1] - times[0]

    if duration <= 0:
        raise ValueError(
            "The time interval must have positive duration."
        )

    integral = np.trapezoid(
        entropy,
        times,
    )

    return float(integral / duration)


def first_recurrence_time(
    times,
    entropy,
    threshold=1e-3,
):
    """
    Return the first operational recurrence time.

    A recurrence is defined as the first time after the
    entropy has risen above `threshold` at which

        S(t) <= threshold

    again.

    The initial condition at t=0 is therefore not counted
    as a recurrence.

    Returns
    -------
    float or None
        First recurrence time, or None if no recurrence is
        observed within the supplied time interval.
    """
    times, entropy = _validate_time_series(
        times,
        entropy,
    )

    if threshold <= 0:
        raise ValueError(
            "threshold must be positive."
        )

    above_threshold = entropy > threshold

    if not np.any(above_threshold):
        return None

    first_above_index = np.argmax(
        above_threshold
    )

    for i in range(
        first_above_index + 1,
        len(entropy),
    ):
        if entropy[i] <= threshold:
            return float(times[i])

    return None


def fraction_above_threshold(
    times,
    values,
    threshold,
):
    """
    Calculate the fraction of the total time interval
    during which the observable is above a threshold.

    The fraction is computed using the trapezoidal rule
    applied to the indicator function

        I(t) = 1  if values(t) > threshold
             = 0  otherwise.

    Returns
    -------
    float
        Fraction of the total time interval for which
        values > threshold.
    """
    times, values = _validate_time_series(
        times,
        values,
    )

    if not np.isfinite(threshold):
        raise ValueError(
            "threshold must be finite."
        )

    indicator = (
        values > threshold
    ).astype(float)

    duration_above = np.trapezoid(
        indicator,
        times,
    )

    total_duration = (
        times[-1] - times[0]
    )

    return float(
        duration_above / total_duration
    )