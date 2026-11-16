-- Théorie Phi - Version discrète
-- Auteur : Grégory Lombardo - CC BY 4.0
-- Version 1.0

structure PhiSystem (E : Type) where
  Phi : ℕ → E → E
  I : E → ℝ
  Phi_zero : ∀ x, Phi 0 x = x
  Phi_add : ∀ m n x, Phi (m + n) x = Phi m (Phi n x)
  I_nonneg : ∀ x, 0 ≤ I x
  I_mono : ∀ n x, I (Phi (n+1) x) ≤ I (Phi n x)

def IsCoherent {E : Type} (S : PhiSystem E) (x : E) : Prop :=
  S.I x = 0

theorem I_decreasing {E : Type} (S : PhiSystem E) (x : E) (n m : ℕ) (h : n ≤ m) :
    S.I (S.Phi m x) ≤ S.I (S.Phi n x) := by
  sorry

theorem stabilization {E : Type} (S : PhiSystem E) [Finite E] (x : E) :
    ∃ a, IsCoherent S a ∧ ∃ N, ∀ n ≥ N, S.Phi n x = a := by
  sorry

-- Exemple : Comptage - E = ℕ, Phi n -> max(0, n-1), I(n) = n
def countingSystem : PhiSystem ℕ where
  Phi := fun n k => if k ≥ n then k - n else 0
  I := fun n => (n : ℝ)
  Phi_zero := by intro x; simp
  Phi_add := by intro m n x; sorry
  I_nonneg := by intro x; exact Nat.cast_nonneg x
  I_mono := by intro n x; sorry
