# mdei_state.py - Gerencia o vetor de estado emocional
import numpy as np
from typing import List

class MDEIState:
    """
    Cuida do vetor [c, iota, tau], representando semântica, intensidade e duração.
    Garante que iota esteja entre 0 e 1, com opções para normalizar e aplicar decaimento.
    """
    
    def __init__(self, c: float = 0.0, iota: float = 0.0, tau: float = 0.0):
        """
        Cria o vetor inicial. Iota deve ser entre 0 e 1, senão dá erro.
        Exemplo: state = MDEIState(c=-0.9, iota=0.85, tau=5.5) para usuário frustrado.
        """
        if not 0.0 <= iota <= 1.0:
            raise ValueError("iota deve estar entre 0 e 1.")
        self.state = np.array([c, iota, tau], dtype=float)
    
    def update(self, delta: List[float]) -> np.ndarray:
        """
        Atualiza o vetor com uma mudança, verificando se iota continua válido.
        Exemplo: delta = [0.1, -0.05, 0.2] para ajustar o estado.
        """
        if len(delta) != 3:
            raise ValueError("Delta precisa ter 3 valores [Δc, Δiota, Δtau].")
        new_state = self.state + np.array(delta, dtype=float)
        if not 0.0 <= new_state[1] <= 1.0:
            raise ValueError("Mudança levaria iota fora do intervalo [0,1].")
        self.state = new_state
        return self.state
    
    def normalize(self, max_norm: float = 1.0) -> np.ndarray:
        """
        Garante que o vetor não cresça demais, ajustando sua escala.
        Exemplo: Se o vetor for muito grande, reduz para max_norm=1.0.
        """
        norm = np.linalg.norm(self.state)
        if norm > max_norm:
            self.state /= (norm + 0.00001)  # Evita divisão por zero
        return self.state
    
    def apply_decay(self, decay_rate: float = 0.01) -> np.ndarray:
        """
        Reduz tau ao longo do tempo, simulando esquecimento emocional.
        Exemplo: decay_rate=0.01 reduz tau em 1% a cada passo.
        """
        self.state[2] *= (1.0 - decay_rate)
        if self.state[2] < 0:
            self.state[2] = 0.0
        return self.state
    
    def get_state(self) -> np.ndarray:
        """
        Mostra o vetor atual, útil para debug ou integração.
        Exemplo: Retorna [-0.9, 0.85, 5.5].
        """
        return self.state
