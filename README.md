# 🧠 MDEI - Modelo de Dinâmica de Estados Internos

**Repositório oficial do MDEI**, uma arquitetura computacional criada por **Tiago Aguioncio Vieira** para representar e simular estados cognitivo-afetivos em Inteligência Artificial, usando vetores tridimensionais, cálculo diferencial e dinâmicas emocionais inspiradas na física de fluidos.

> Desenvolvido por ZENNE Tecnologia · 2025

---

## 📌 Visão Geral

O MDEI modela emoções como vetores no espaço tridimensional (c, ι, τ), onde:
- `c` → componente conceitual (cognitiva);
- `ι` (iota) → intensidade emocional (normalizada);
- `τ` (tau) → duração temporal.

Com isso, é possível calcular o **Número de Reynolds Emocional (Reₑ)** e classificar o estado como:
- Laminar
- Transição
- Turbulento

Tudo isso permite que **modelos LLM** (como GPT, Gemini ou Claude) ajustem o tom e o estilo de resposta com base no estado emocional da interação.

---

## ⚙️ Funcionalidades

- 🧮 Vetorização emocional e cálculo de norma
- 🔁 Simulação dinâmica com EDOs (Euler/Runge-Kutta)
- 📉 Número de Reynolds Emocional (Reₑ)
- 🧠 Camada MDEILayer adaptativa para LLMs
- 🧯 Fallback emocional com tom controlado
- 🧾 Log em JSON com estados emocionais em tempo real

---

## 🚀 Exemplos de Aplicação

- 🤖 Assistentes com empatia adaptativa
- 💬 Chatbots afetivos (telemedicina, suporte, educação)
- 🧘 Plataformas de autocuidado emocional
- 🧑‍🏫 Educação personalizada por estado afetivo
- 🤝 Interação Homem-Máquina sensível ao estado interno

---

## 🧪 Exemplo rápido (main.py)

```python
from mdei_state import MDEIState

state = MDEIState(c=-0.8, iota=0.9, tau=5.0)
print("Estado inicial:", state.get_state())
