
Tu colles ça :

```python
# Théorie Phi - Système (E, Phi, I)
# Grégory Lombardo - CC BY 4.0
import math

class PhiSystem:
    def __init__(self, phi, I):
        self.phi = phi
        self.I = I

    def trajectory(self, x0, N):
        xs = 
        x = x0
        for n in range(N):
            x = self.phi(1, x)
            xs.append(x)
        return xs

    def incoherence(self, xs):
        return [self.I(x) for x in xs]

counting = PhiSystem(lambda n, x: max(0, x-n), lambda x: float(x))
ricci = PhiSystem(lambda n, g: g * math.exp(-2*n), lambda g: g**2)

if __name__ == "__main__":
    print("Comptage 12 ->", counting.trajectory(12, 12))
    print("Ricci 3.0 ->", ricci.trajectory(3.0, 5))
