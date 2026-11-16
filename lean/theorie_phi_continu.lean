-- Théorie Phi - Version continue
-- Auteur : Grégory Lombardo - CC BY 4.0
-- Équation maîtresse : d/dt Phi_t(x) = - ∇ I(Phi_t(x))

import Mathlib.Topology.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic

open Real

structure PhiSystemCont (E : Type) [TopologicalSpace E] where
  Phi : ℝ → E → E
  I : E → ℝ
  Phi_zero : ∀ x, Phi 0 x = x
  Phi_add : ∀ s t x, Phi (s + t) x = Phi s (Phi t x)
  I_nonneg : ∀ x, 0 ≤ I x
  I_cont : Continuous I
  I_mono : ∀ t x, t ≥ 0 → I (Phi t x) ≤ I x

def IsAttractorCont {E : Type} [TopologicalSpace E] (S : PhiSystemCont E) (a : E) : Prop :=
  S.I a = 0 ∧ ∀ x, Filter.Tendsto (fun t => S.Phi t x) Filter.atTop (nhds a)

axiom attractor_existence {E : Type} [TopologicalSpace E] [CompactSpace E]
    (S : PhiSystemCont E) (x : E) :
    ∃ a, S.I a = 0 ∧ Filter.Tendsto (fun t => S.Phi t x) Filter.atTop (nhds a)

-- Exemple : Paysage I(g) = g^2, tout flot -> g = 0
def landscapeI : ℝ → ℝ := fun g => g ^ 2

theorem landscape_attractor (g0 : ℝ) :
    Filter.Tendsto (fun t => g0 * Real.exp (-2 * t)) Filter.atTop (nhds 0) := by
  sorry
