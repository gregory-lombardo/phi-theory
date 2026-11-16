# Visualisations des attracteurs - Théorie Phi
# Grégory Lombardo - CC BY 4.0
import matplotlib.pyplot as plt
import numpy as np

def plot_ricci():
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    for g0 in [3.0, -2.0, 1.5, -1.0, 0.7]:
        ns = np.arange(0, 24)
        gs = g0 * np.exp(-0.5 * ns)
        ax[0].plot(ns, gs, marker='o', markersize=3, label=f'g0={g0}')
        ax[1].plot(ns, gs**2, marker='o', markersize=3)
    ax[0].set_title("Ricci jouet 1D : g -> attracteur 0")
    ax[0].set_xlabel("pas n : Phi_n(g)")
    ax[0].set_ylabel("g : courbure")
    ax[0].axhline(0, color='black', linestyle='--', linewidth=0.8)
    ax[0].legend()
    ax[1].set_title("Incohérence I(g) = g^2 -> 0")
    ax[1].set_xlabel("pas n")
    ax[1].set_ylabel("I(g)")
    ax[0].grid(True); ax[1].grid(True)
    plt.tight_layout()
    plt.savefig("figures/fig1_ricci_toy.png", dpi=150)
    plt.show()

def plot_counting():
    fig, ax = plt.subplots(figsize=(8, 4))
    for n0 in [8, 5, 12]:
        ns = np.arange(0, n0 + 1)
        xs = np.maximum(0, n0 - ns)
        ax.plot(ns, xs, marker='o', label=f'n0={n0} : I(n)=n -> 0')
    ax.set_title("Comptage décroissant : tout entier -> attracteur 0")
    ax.set_xlabel("pas n")
    ax.set_ylabel("état")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.savefig("figures/fig2_counting.png", dpi=150)
    plt.show()

if __name__ == "__main__":
    plot_ricci()
    plot_counting()
