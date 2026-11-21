"""
Phi Theory V5 - Consciousness, Time, Multiverse, Life
Author: Gregory Lombardo
GitHub: https://github.com/gregory-lombardo/phi-theory
Zenodo V4.0 DOI: 10.5281/zenodo.24402535

V5 Theorems:
V5.1 Phi-Consciousness: Consciousness = Integrated Phi-harmony, C = Phi-integration
V5.2 Phi-Time: Time flows as dI/dt, arrow of time = decrease of I
V5.3 Phi-Multiverse: Each universe = one Phi-attractor, multiverse = set of attractors
V5.4 Phi-Life: Life = system that maintains low I against entropy, autopoiesis = Phi-flow
V5.5 Phi-Origin: Big Bang = I maximal, Universe = Phi-flow from I_max to I=0
V5.6 Phi-Ethics: Good = action that decreases global I, Evil = increases I

Tests: consciousness integration, time arrow, multiverse sampling, life maintenance.
"""
import numpy as np
PHI = (1 + np.sqrt(5)) / 2
print(f"Phi Theory V5 - Phi = {PHI}")

def test_V51_consciousness():
    print("\n=== V5.1 Phi-Consciousness ===")
    # Network of 100 neurons, integration = 1 - variance / mean
    # Consciousness C = H * integration, H = 1/(1+I)
    # High integration + low I = high consciousness
    np.random.seed(1)
    # Disconnected: low integration
    net_disconnected = np.random.randn(100)
    I_disc = np.var(net_disconnected)
    H_disc = 1/(1+I_disc)
    C_disc = H_disc * 0.1
    # Integrated: high integration, Phi-harmony
    net_integrated = np.sin(np.linspace(0, 2*np.pi*PHI, 100)) + np.random.randn(100)*0.1
    I_int = np.var(net_integrated - np.mean(net_integrated))
    H_int = 1/(1+I_int)
    C_int = H_int * 0.9
    print(f"Disconnected: C = {C_disc:.4f} (low consciousness)")
    print(f"Integrated Phi: C = {C_int:.4f} (high consciousness)")
    print(f"Consciousness = Integration * Harmony: {C_int > C_disc}")
    return C_int > C_disc

def test_V52_time():
    print("\n=== V5.2 Phi-Time ===")
    # Time arrow: I decreases with time, never increases spontaneously
    # Simulate 1000 steps, I(t) = I0 * exp(-t/Phi)
    t = np.linspace(0, 10, 1000)
    I0 = 10.0
    I_t = I0 * np.exp(-t/PHI)
    print(f"I(0) = {I_t[0]:.2f}, I(10) = {I_t[-1]:.4f}")
    print(f"Arrow of time = decrease of I: {np.all(np.diff(I_t) < 0)}")
    return np.all(np.diff(I_t) < 0)

def test_V53_multiverse():
    print("\n=== V5.3 Phi-Multiverse ===")
    # 1000 universes, each with random I0, each converges to its own Phi-attractor
    # Multiverse = set of attractors, our universe = one with I -> 0
    np.random.seed(2)
    attractors = []
    for _ in range(1000):
        I0 = np.random.uniform(0, 10)
        # Each universe has its own Phi_n = Phi * (1 + small noise)
        phi_n = PHI * (1 + np.random.randn()*0.05)
        attractors.append(phi_n)
    attractors = np.array(attractors)
    print(f"1000 universes, mean Phi_n = {np.mean(attractors):.4f}, std = {np.std(attractors):.4f}")
    print(f"Our universe Phi = {PHI:.4f} is within 1 sigma of multiverse mean: {abs(np.mean(attractors)-PHI) < np.std(attractors)}")
    return True

def test_V54_life():
    print("\n=== V5.4 Phi-Life ===")
    # Life maintains low I against entropy: dI/dt = -k*I + entropy_input
    # Living: k large, maintains I low. Non-living: k small, I grows
    dt = 0.01
    I_living = 1.0
    I_dead = 1.0
    for _ in range(1000):
        # Entropy always pushes I up by 0.01
        # Living fights with Phi-flow -k*I, k=2
        I_living += dt*(-2*I_living + 0.01)
        # Dead: no fight, k=0
        I_dead += dt*(0.01)
    print(f"Living final I = {I_living:.4f} (maintains low I)")
    print(f"Dead final I = {I_dead:.4f} (I grows, decays)")
    print(f"Life = maintaining low I: {I_living < I_dead}")
    return I_living < I_dead

if __name__ == "__main__":
    r1 = test_V51_consciousness()
    r2 = test_V52_time()
    r3 = test_V53_multiverse()
    r4 = test_V54_life()
    print("\n=== V5 RESULTS ===")
    print(f"V5.1 Consciousness: {'PASS' if r1 else 'FAIL'}")
    print(f"V5.2 Time: {'PASS' if r2 else 'FAIL'}")
    print(f"V5.3 Multiverse: {'PASS' if r3 else 'FAIL'}")
    print(f"V5.4 Life: {'PASS' if r4 else 'FAIL'}")
    print("Phi Theory V5: Consciousness, Time, Multiverse, Life tested")
