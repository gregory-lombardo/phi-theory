-- Théorie Phi - Instanciation Ricci / Perelman
-- Auteur : Grégory Lombardo - CC BY 4.0
-- E = métriques, Phi = flot de Ricci, I = énergie de Perelman

structure RicciSystem where
  g : ℝ

def ricciPhi : ℝ → RicciSystem → RicciSystem :=
  fun t s => ⟨s.g * Real.exp (-2 * t)⟩

def ricciI : RicciSystem → ℝ :=
  fun s => s.g ^ 2

theorem ricci_flow_eq (g0 : ℝ) (t : ℝ) :
    ricciPhi t ⟨g0⟩ = ⟨g0 * Real.exp (-2 * t)⟩ := by
  rfl

theorem perelman_energy_decreasing (s : RicciSystem) (t : ℝ) (ht : t ≥ 0) :
    ricciI (ricciPhi t s) ≤ ricciI s := by
  sorry

theorem ricci_attractor (g0 : ℝ) :
    Filter.Tendsto (fun t => (ricciPhi t ⟨g0⟩).g) Filter.atTop (nhds 0) := by
  sorry

theorem phi_is_perelman :
    ∀ g0 : ℝ, ∃ a : RicciSystem, ricciI a = 0 ∧
    Filter.Tendsto (fun t => (ricciPhi t ⟨g0⟩).g) Filter.atTop (nhds a.g) := by
  intro g0
  use ⟨0⟩
  constructor
  · simp [ricciI]
  · simp
    exact ricci_attractor g0
