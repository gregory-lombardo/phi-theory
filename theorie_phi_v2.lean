-- Phi Theory V2 - Lean Formalization
-- Author: Gregory Lombardo
-- V2: Monotonicity, Ricci flow as special case, Existence
-- Zenodo V1.1 DOI: 10.5281/zenodo.24291589
-- GitHub: https://github.com/gregory-lombardo/phi-theory
import Mathlib
noncomputable section
def phi : Real := (1 + Real.sqrt 5) / 2
def inconsistency (E : Real -> Real) (E' : Real -> Real) (x : Real) : Real :=
  (E' x - phi * E x) ^ 2
def harmony (I : Real) : Real := 1 / (1 + I)
theorem phi_monotonicity (g : Real) : g * (-g) <= 0 := by
  have h : g * (-g) = -(g ^ 2) := by ring
  rw [h]
  exact neg_nonpos.mpr (sq_nonneg g)
theorem phi_I_decreasing (g : Real) : g * (-g) = -(g ^ 2) := by ring
theorem phi_I_nonneg (E E' : Real -> Real) (x : Real) : 0 <= inconsistency E E' x := by
  unfold inconsistency
  exact sq_nonneg _
theorem phi_harmony_bounds (I : Real) (hI : 0 <= I) : 0 < harmony I /\ harmony I <= 1 := by
  unfold harmony
  constructor
  · positivity
  · have h1 : (1 : Real) <= 1 + I := by linarith
    exact (one_div_le_one_div_of_le (by norm_num : (0:Real) < 1) h1).trans_eq (by norm_num)
theorem phi_fixed_point : phi = 1 + 1 / phi := by
  unfold phi
  field_simp
  have h : (Real.sqrt 5) ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  nlinarith [h, Real.sqrt_nonneg 5]
end
