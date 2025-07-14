# emotion_logger.py - Registra tudo para análise futura
import json
import csv
from datetime import datetime
from typing import List
from mdei_dynamics import MDEIDynamics

class EmotionLogger:
    """
    Guarda um diário emocional: estado, Re_e, classificação, com data e hora.
    Salva em JSON ou CSV para você analisar depois, como em gráficos.
    """
    
    def __init__(self, log_file: str = "emotional_log.json"):
        """
        Começa um novo diário, salvando em emotional_log.json por padrão.
        Exemplo: logger = EmotionLogger().
        """
        self.history = []
        self.log_file = log_file
    
    def log_state(self, dynamics: MDEIDynamics) -> None:
        """
        Registra o estado atual, como "Às 14h, estado foi [-0.9, 0.85, 5.5], Re_e=11.30, Laminar".
        Exemplo: logger.log_state(dynamics).
        """
        state = dynamics.state.get_state()
        ree = dynamics.compute_emotional_reynolds()
        classification = dynamics.classify_state()
        timestamp = datetime.now().isoformat()
        self.history.append({
            "timestamp": timestamp,
            "state": state.tolist(),
            "ree": ree,
            "classification": classification
        })
    
    def save_to_json(self) -> None:
        """
        Salva o diário em um arquivo JSON, organizado e legível.
        Exemplo: logger.save_to_json() cria emotional_log.json.
        """
        with open(self.log_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def save_to_csv(self, csv_file: str = "emotional_log.csv") -> None:
        """
        Salva o diário em CSV, bom para abrir no Excel ou analisar em planilhas.
        Exemplo: logger.save_to_csv() cria emotional_log.csv.
        """
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "c", "iota", "tau", "ree", "classification"])
            writer.writeheader()
            for entry in self.history:
                writer.writerow({
                    "timestamp": entry["timestamp"],
                    "c": entry["state"][0],
                    "iota": entry["state"][1],
                    "tau": entry["state"][2],
                    "ree": entry["ree"],
                    "classification": entry["classification"]
                })
