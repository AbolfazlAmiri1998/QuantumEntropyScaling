import numpy as np

from quantum_entropy.metrics import (
    maximum_entropy,
    normalized_maximum_entropy,
    first_local_maximum,
    time_average_entropy,
    first_recurrence_time,
    fraction_above_threshold,
)


def test_maximum_entropy():
    entropy = np.array(
        [0.0, 0.2, 0.5, 0.3]
    )

    assert np.isclose(
        maximum_entropy(entropy),
        0.5,
    )


def test_normalized_maximum_entropy():
    entropy = np.array(
        [0.0, np.log(2)]
    )

    assert np.isclose(
        normalized_maximum_entropy(entropy),
        1.0,
    )


def test_first_local_maximum():
    times = np.array(
        [0.0, 1.0, 2.0, 3.0, 4.0]
    )

    entropy = np.array(
        [0.0, 0.4, 0.8, 0.5, 0.2]
    )

    result = first_local_maximum(
        times,
        entropy,
    )

    assert result is not None

    peak_time, peak_entropy = result

    assert np.isclose(
        peak_time,
        2.0,
    )

    assert np.isclose(
        peak_entropy,
        0.8,
    )


def test_time_average_entropy():
    times = np.array(
        [0.0, 1.0, 2.0]
    )

    entropy = np.array(
        [0.0, 1.0, 2.0]
    )

    average = time_average_entropy(
        times,
        entropy,
    )

    assert np.isclose(
        average,
        1.0,
    )


def test_first_recurrence_time():
    times = np.array(
        [0.0, 1.0, 2.0, 3.0, 4.0]
    )

    entropy = np.array(
        [0.0, 0.5, 0.8, 0.4, 0.0]
    )

    recurrence = first_recurrence_time(
        times,
        entropy,
        threshold=1e-3,
    )

    assert np.isclose(
        recurrence,
        4.0,
    )


def test_no_recurrence_returns_none():
    times = np.array(
        [0.0, 1.0, 2.0, 3.0]
    )

    entropy = np.array(
        [0.0, 0.5, 0.8, 0.4]
    )

    recurrence = first_recurrence_time(
        times,
        entropy,
        threshold=1e-3,
    )

    assert recurrence is None


def test_fraction_above_threshold():
    times = np.array(
        [0.0, 1.0, 2.0, 3.0]
    )

    values = np.array(
        [0.0, 1.0, 1.0, 0.0]
    )

    fraction = fraction_above_threshold(
        times,
        values,
        threshold=0.5,
    )

    assert np.isclose(
        fraction,
        2.0 / 3.0,
    )


def test_fraction_above_threshold_is_zero():
    times = np.array(
        [0.0, 1.0, 2.0]
    )

    values = np.array(
        [0.1, 0.2, 0.3]
    )

    fraction = fraction_above_threshold(
        times,
        values,
        threshold=0.5,
    )

    assert np.isclose(
        fraction,
        0.0,
    )