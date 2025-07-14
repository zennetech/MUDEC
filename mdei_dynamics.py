# mdei_dynamics.py - Simula como o estado emocional muda ao longo do tempo
import numpy as np
from typing import Callable
from scipy.integrate import odeint
from mdei_state import MDEIState

class MDEIDynamics:
    """
    Cuida da evolução do estado, calculando Re_e e classificando emoções.
    Usa equações diferenciais para simular mudanças e valida com ciência.
    """
    
    def __init__(self, state: MDEIState, Lc: float = 2.0, nu_e: float = 1.0, ree_critical: float = 2100.0):
        """
        Configura a dinâmica. Lc é como "tamanho" cognitivo, nu_e é viscosidade emocional.
        Exemplo: dynamics = MDEIDynamics(state, Lc=2.0, nu_e=1.0).
        """
        if Lc <= 0 or nu_e <= 0:
            raise ValueError("Lc e nu_e devem ser positivos.")
        self.state = state
        self.Lc = Lc
        self.nu_e = nu_e
        self.ree_critical = ree_critical
    
    def compute_norm(self) -> float:
        """
        Calcula o "tamanho" do vetor, útil para Re_e.
        Exemplo: Para [-0.9, 0.85, 5.5], retorna cerca de 5.65.
        """
        return np.linalg.norm(self.state.get_state())
    
    def compute_emotional_reynolds(self) -> float:
        """
        Calcula Re_e, que mede se o estado é calmo (baixo) ou turbulento (alto).
        Fórmula: Re_e = (norma do vetor * Lc) / nu_e.
        Exemplo: Para norma 5.65, Lc=2.0, nu_e=1.0, Re_e ≈ 11.30.
        """
        norm = self.compute_norm()
        return (norm * self.Lc) / self.nu_e
    
    def classify_state(self) -> str:
        """
        Classifica o estado: Laminar (<1050), Transição (1050-2100), Turbulento (>2100).
        Exemplo: Re_e=11.30 → "Laminar".
        """
        ree = self.compute_emotional_reynolds()
        if ree < self.ree_critical * 0.5:
            return "Laminar"
        elif ree < self.ree_critical:
            return "Transição"
        else:
            return "Turbulento"
    
    def dynamic_evolution(self, F: Callable, P: np.ndarray, t: float, dt: float) -> np.ndarray:
        """
        Simula como o estado muda ao longo do tempo usando equações diferenciais.
        Exemplo: F pode ser uma função como example_F no main.py.
        """
        def ode_func(state, t):
            return F(state, P, t)
        new_state = odeint(ode_func, self.state.get_state(), [t, t + dt], tfirst=True)[-1]
        if not 0.0 <= new_state[1] <= 1.0:
            raise ValueError("Mudança levou iota fora do intervalo [0,1].")
        self.state.state = new_state
        return new_state
    
    def validate_empirical_thresholds(self, ree: float) -> dict:
        """
        Verifica se Re_e está dentro de limites científicos (2100 ± 150).
        Exemplo: Para Re_e=11.30, retorna {"ree": 11.30, "is_within_threshold": False, ...}.
        """
        lower_bound = self.ree_critical - 150
        upper_bound = self.ree_critical + 150
        return {
            "ree": ree,
            "is_within_threshold": lower_bound <= ree <= upper_bound,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound
        }
