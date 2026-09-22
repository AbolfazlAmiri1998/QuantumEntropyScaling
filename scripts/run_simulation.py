from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from quantum_entropy.simulation import simulate_entropy
from quantum_entropy.metrics import (
    maximum_entropy,
    normalized_maximum_entropy,
    first_local_maximum,
    time_average_entropy,
    first_recurrence_time,
    fraction_above_threshold,
)


def main():
    # --------------------------------------------------
    # Simulation parameters
    # --------------------------------------------------

    J = 2.0
    h = 2.0

    t_max = 5.0
    num_points = 500

    system_sizes = [2, 3, 4, 5, 6]

    recurrence_threshold = 1e-3
    entropy_threshold = 0.5

    # --------------------------------------------------
    # Output directories
    # --------------------------------------------------

    data_dir = Path("data")
    figures_dir = Path("figures")

    data_dir.mkdir(exist_ok=True)
    figures_dir.mkdir(exist_ok=True)

    # --------------------------------------------------
    # Storage
    # --------------------------------------------------

    results = {}
    metrics_rows = []

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    print("=" * 60)
    print("Quantum Entropy Scaling Simulation")
    print("=" * 60)

    print(f"J = {J}")
    print(f"h = {h}")
    print(f"Time interval = [0, {t_max}]")
    print(f"Number of time points = {num_points}")
    print(f"System sizes = {system_sizes}")
    print()

    # --------------------------------------------------
    # Run simulations
    # --------------------------------------------------

    for N in system_sizes:

        times = np.linspace(
            0.0,
            t_max,
            num_points,
        )

        times, entropy = simulate_entropy(
            N=N,
            J=J,
            h=h,
            times=times,
            keep=(0,),
        )

        results[N] = entropy

        # --------------------------------------------------
        # Save entropy time series
        # --------------------------------------------------

        entropy_file = (
            data_dir
            / f"entropy_N{N}_J{J:g}_h{h:g}.csv"
        )

        data = np.column_stack(
            [times, entropy]
        )

        np.savetxt(
            entropy_file,
            data,
            delimiter=",",
            header="time,entropy",
            comments="",
        )

        # --------------------------------------------------
        # Calculate metrics
        # --------------------------------------------------

        S_max = maximum_entropy(
            entropy
        )

        eta_max = normalized_maximum_entropy(
            entropy
        )

        first_peak = first_local_maximum(
            times,
            entropy,
        )

        S_average = time_average_entropy(
            times,
            entropy,
        )

        fraction_above = fraction_above_threshold(
            times,
            entropy,
            threshold=entropy_threshold,
        )


        recurrence = first_recurrence_time(
            times,
            entropy,
            threshold=recurrence_threshold,
        )

        # --------------------------------------------------
        # Extract first-peak information
        # --------------------------------------------------

        if first_peak is not None:
            peak_time, peak_entropy = first_peak
        else:
            peak_time = np.nan
            peak_entropy = np.nan

        # --------------------------------------------------
        # Store metrics
        # --------------------------------------------------

        metrics_rows.append(
    [
        N,
        S_max,
        eta_max,
        S_average,
        fraction_above,
        peak_time,
        peak_entropy,
        (
            recurrence
            if recurrence is not None
            else np.nan
        ),
    ]
)

        # --------------------------------------------------
        # Print results
        # --------------------------------------------------

        print("-" * 60)
        print(f"N = {N}")

        print(
            f"  Maximum entropy:       "
            f"{S_max:.8f}"
        )

        print(
            f"  Normalized maximum:    "
            f"{eta_max:.8f}"
        )

        print(
            f"  Time-average entropy:  "
            f"{S_average:.8f}"
        )

        print(
            f"  Fraction S > {entropy_threshold}: "
            f"{fraction_above:.8f}"
        )

        if first_peak is not None:
            print(
                f"  First peak time:       "
                f"{peak_time:.8f}"
            )

            print(
                f"  First peak entropy:    "
                f"{peak_entropy:.8f}"
            )
        else:
            print(
                "  First peak time:       None"
            )

        if recurrence is not None:
            print(
                f"  First recurrence time: "
                f"{recurrence:.8f}"
            )
        else:
            print(
                "  First recurrence time: None"
            )

        print(
            f"  Data saved to:         "
            f"{entropy_file}"
        )

    # --------------------------------------------------
    # Save metrics table
    # --------------------------------------------------

    metrics_file = (
        data_dir
        / f"entropy_metrics_J{J:g}_h{h:g}.csv"
    )

    metrics_array = np.array(
        metrics_rows,
        dtype=float,
    )

    np.savetxt(
        metrics_file,
        metrics_array,
        delimiter=",",
        header=(
            "N,"
            "S_max,"
            "eta_max,"
            "time_average,"
            "fraction_above_threshold,"
            "first_peak_time,"
            "first_peak_entropy,"
            "first_recurrence_time"
        ),
        comments="",
    )

    print("-" * 60)
    print(
        f"Metrics saved to: {metrics_file}"
    )

    # --------------------------------------------------
    # Plot entropy dynamics
    # --------------------------------------------------

    plt.figure(figsize=(10, 6))

    for N in system_sizes:
        plt.plot(
            times,
            results[N],
            label=f"N={N}",
            linewidth=2,
        )

    plt.axhline(
        y=np.log(2),
        linestyle="--",
        label=r"$\ln 2$",
    )

    plt.xlabel("Time $t$")
    plt.ylabel(r"Subsystem entropy $S_A(t)$")

    plt.title(
        "Entanglement Entropy Dynamics "
        "for the Transverse-Field Ising Chain"
    )

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 0.75)

    plt.tight_layout()

    dynamics_figure = (
        figures_dir
        / "entropy_N2_N6_comparison.png"
    )

    plt.savefig(
        dynamics_figure,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    print(
        f"Dynamics figure saved to: "
        f"{dynamics_figure}"
    )

    # --------------------------------------------------
    # Plot maximum entropy versus N
    # --------------------------------------------------

    N_values = metrics_array[:, 0]
    S_max_values = metrics_array[:, 1]

    plt.figure(figsize=(8, 5))

    plt.plot(
        N_values,
        S_max_values,
        marker="o",
        linewidth=2,
    )

    plt.axhline(
        y=np.log(2),
        linestyle="--",
        label=r"$\ln 2$",
    )

    plt.xlabel("System size $N$")
    plt.ylabel(r"$S_{\max}$")

    plt.title(
        "Maximum One-Qubit Entropy vs System Size"
    )

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    scaling_figure = (
        figures_dir
        / "maximum_entropy_vs_N.png"
    )

    plt.savefig(
        scaling_figure,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    print(
        f"Scaling figure saved to: "
        f"{scaling_figure}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()