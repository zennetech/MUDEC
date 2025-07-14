# main.py - Mostra como usar tudo junto, passo a passo
import numpy as np
from mdei_state import MDEIState
from mdei_dynamics import MDEIDynamics
from mdei_response import MDEIResponseEngine
from emotion_logger import EmotionLogger

def example_F(state: np.ndarray, P: np.ndarray, t: float) -> np.ndarray:
    """
    Exemplo de como o estado muda: c e iota diminuem, tau cresce um pouco.
    """
    return np.array([-0.1 * state[0], -0.05 * state[1], 0.01 * state[2]])

def main():
    # Passo 1: Cria o estado inicial, como para um usuário frustrado
    state = MDEIState(c=-0.9, iota=0.85, tau=5.5)
    
    # Passo 2: Configura a dinâmica, com parâmetros padrão
    dynamics = MDEIDynamics(state=state)
    
    # Passo 3: Prepara para gerar respostas
    response_engine = MDEIResponseEngine(dynamics=dynamics)
    
    # Passo 4: Cria um diário para salvar tudo
    logger = EmotionLogger()
    
    # Passo 5: Simula uma interação, como usuário reclamando
    context = "Usuário reclamando várias vezes seguidas."
    base_response = "O que posso fazer?"
    
    # Passo 6: Atualiza o estado, simulando o tempo passando
    P = np.array([0.1, 0.2])  # Parâmetros fictícios, como contexto
    t, dt = 0.0, 0.1
    new_state = dynamics.dynamic_evolution(example_F, P, t, dt)
    
    # Passo 7: Ajusta o estado, normalizando e aplicando decaimento
    state.normalize(max_norm=10.0)
    state.apply_decay(decay_rate=0.01)
    
    # Passo 8: Registra tudo no diário
    logger.log_state(dynamics)
    
    # Passo 9: Valida cientificamente, vendo se Re_e está ok
    ree = dynamics.compute_emotional_reynolds()
    validation = dynamics.validate_empirical_thresholds(ree)
    
    # Passo 10: Gera uma resposta adaptada, como "O que posso fazer?" com tom certo
    response = response_engine.generate_adaptive_response(base_response, context)
    
    # Passo 11: Mostra tudo na tela para ver o que aconteceu
    print(f"Novo estado: {new_state}")
    print(f"Re_e: {ree:.2f}")
    print(f"Classificação: {dynamics.classify_state()}")
    print(f"Validação: {validation}")
    print(f"Resposta: {response}")
    
    # Passo 12: Salva o diário em JSON e CSV para analisar depois
    logger.save_to_json()
    logger.save_to_csv()

if __name__ == "__main__":
    main()
