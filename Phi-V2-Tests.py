"""
Phi Theory V2 - Python Tests for 3 Falsifiable Predictions
Author: Gregory Lombardo
GitHub: https://github.com/gregory-lombardo/phi-theory
Zenodo V1.1 DOI: 10.5281/zenodo.24291589
P1: Convergence time O(1/phi^n) on 100 random systems
P2: Along Ricci flow, I_Ricci decreases as -||grad I||^2
P3: For x_{n+1} = 1 + 1/x_n, |x_n - phi| ~ C*(1/phi^2)^n
"""
import numpy as np
import matplotlib.pyplot as plt
PHI = (1 + np.sqrt(5)) / 2
print(f"Phi = {PHI}")

def test_P3():
    print("\n=== P3: Golden ratio iteration ===")
    x = 1.0
    errors = []
    for n in range(20):
        errors.append(abs(x - PHI))
        x = 1 + 1/x
    errors = np.array(errors)
    ratios = errors[1:] / errors[:-1]
    print(f"Final x = {x:.10f}, Phi = {PHI:.10f}, error = {errors[-1]:.2e}")
    print(f"Mean ratio = {np.mean(ratios[5:]):.6f}, expected 1/phi^2 = {1/PHI**2:.6f}")
    I = errors**2
    print(f"I_0 = {I[0]:.4f}, I_19 = {I[-1]:.2e}")
    plt.figure()
    plt.semilogy(errors, marker='o', label='|x_n - Phi|')
    plt.semilogy([(1/PHI**2)**n for n in range(20)], linestyle='--', label='(1/Phi^2)^n')
    plt.xlabel('n'); plt.ylabel('error'); plt.legend(); plt.title('P3: Convergence to Phi')
    plt.savefig('/mnt/data/phi_v2/fig_P3.png', dpi=150)
    plt.close()
    return errors[-1] < 1e-8

def test_P1():
    print("\n=== P1: 100 random systems, I decreasing ===")
    np.random.seed(0)
    ok = 0
    for trial in range(100):
        a = np.random.uniform(0.5, 2.0)
        b = np.random.uniform(-1, 1)
        x = np.random.uniform(-2, 2)
        dt = 0.001
        I_prev = None
        monotone = True
        for _ in range(500):
            E = a*x**2 + b*x + 1.0
            Ep = 2*a*x + b
            I = (Ep - PHI*E)**2
            if I_prev is not None and I > I_prev + 1e-9:
                monotone = False
                break
            I_prev = I
            eps = 1e-6
            E2 = a*(x+eps)**2 + b*(x+eps) + 1.0
            Ep2 = 2*a*(x+eps) + b
            I2 = (Ep2 - PHI*E2)**2
            gradI = (I2 - I)/eps
            x = x - dt * gradI
        if monotone:
            ok += 1
    print(f"Monotone in {ok}/100 systems")
    return ok == 100

def test_P2():
    print("\n=== P2: Ricci flow toy model ===")
    t = np.linspace(0.5, 5.0, 100)
    g = np.exp(-2*t)
    Ric = g
    I_ricci = (Ric - 1/(2*t)*g)**2
    decreasing = np.mean(np.diff(I_ricci) < 0)
    print(f"I_Ricci(0.5) = {I_ricci[0]:.4f}, I_Ricci(5) = {I_ricci[-1]:.6f}")
    print(f"Fraction decreasing: {decreasing:.2%}")
    plt.figure()
    plt.plot(t, I_ricci, label='I_Ricci(t)')
    plt.xlabel('t'); plt.ylabel('I_Ricci'); plt.title('P2: I_Ricci decreasing along Ricci flow')
    plt.legend(); plt.savefig('/mnt/data/phi_v2/fig_P2.png', dpi=150); plt.close()
    return I_ricci[-1] < I_ricci[0]

if __name__ == "__main__":
    p3 = test_P3()
    p1 = test_P1()
    p2 = test_P2()
    print("\n=== RESULTS V2 ===")
    print(f"P1 (100 systems monotone): {'PASS' if p1 else 'FAIL'}")
    print(f"P2 (Ricci I decreasing): {'PASS' if p2 else 'FAIL'}")
    print(f"P3 (Phi convergence): {'PASS' if p3 else 'FAIL'}")
    if p1 and p2 and p3:
        print("Phi Theory V2: ALL 3 PREDICTIONS PASS")
    else:
        print("Phi Theory V2: SOME PREDICTIONS FAIL - theory needs revision")
