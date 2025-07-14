# mdei_response.py - Gera respostas adaptativas com base na emoção
import json
from jinja2 import Template
from mdei_dynamics import MDEIDynamics

class MDEIResponseEngine:
    """
    Cria respostas que mudam de tom dependendo do estado emocional.
    Usa templates como "Se está calmo, responde direto; se está agitado, acolhe."
    """
    
    def __init__(self, dynamics: MDEIDynamics, template_path: str = "prompt_template.json"):
        """
        Configura o motor de respostas, carregando templates de um arquivo JSON.
        Exemplo: response_engine = MDEIResponseEngine(dynamics).
        """
        self.dynamics = dynamics
        self.template_path = template_path
        self.templates = self.load_templates()
    
    def load_templates(self) -> dict:
        """
        Carrega os templates de resposta, como "Laminar" para respostas lógicas.
        Se o arquivo JSON não existir, usa padrões.
        """
        try:
            with open(self.template_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "Laminar": {"tone": "LÓGICA, CLAREZA E OBJETIVIDADE", "simplify": False, "template": "{{base_response}}"},
                "Transição": {"tone": "VALIDAR SENTIMENTO E EQUILIBRADO", "simplify": False, "template": "Compreendo seu ponto. {{base_response}}"},
                "Turbulento": {"tone": "EMPATIA PROFUNDA E CALMA", "simplify": True, "template": "Entendo que está sendo desafiador. Vamos tentar uma abordagem mais simples: {{base_response}}"}
            }
    
    def generate_adaptive_response(self, base_response: str, context: str) -> dict:
        """
        Gera uma resposta ajustada, como "O que posso fazer?" com tom certo.
        Exemplo: Para Laminar, retorna {"tone": "LÓGICA...", "text": "O que posso fazer?"}.
        """
        state_class = self.dynamics.classify_state()
        template_data = self.templates.get(state_class, self.templates["Laminar"])
        template = Template(template_data["template"])
        response_text = template.render(base_response=base_response)
        return {
            "tone": template_data["tone"],
            "simplify": template_data["simplify"],
            "text": response_text
        }
