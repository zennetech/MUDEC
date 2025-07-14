# 🧠 MDEI – Modelo de Dinâmica de Estados Internos  
### Um framework vetorial para cognição artificial adaptativa e emocional

> “Se queremos uma IA verdadeiramente inteligente, ela precisa entender mais do que palavras: precisa entender *estados internos*.”  
> — Tiago Aguioncio Vieira, fundador da ZENNE Tecnologia

---

## 🌍 Visão Geral

O **Modelo de Dinâmica de Estados Internos (MDEI)** propõe uma nova arquitetura computacional para inteligências artificiais que desejam entender, processar e responder a estados emocionais humanos com sensibilidade, estabilidade e adaptabilidade. Inspirado por conceitos da física de fluidos, álgebra vetorial e sistemas dinâmicos, o MDEI é um avanço no campo da IA cognitivo-afetiva.

---

## 🧑‍🏫 Versão Didática para Graduandos

Esta seção foi pensada para estudantes de graduação que desejam entender o MDEI com fundamentos matemáticos claros e exemplos simples.

### ✅ O que é o MDEI?

O MDEI representa emoções e pensamentos como **vetores tridimensionais** que evoluem ao longo do tempo. É como ensinar a IA a acompanhar o humor humano de forma contínua, como se ela tivesse empatia programável.

### 🔢 Representação Vetorial dos Estados

\[
\mathbf{u} = (c, \iota, \tau)
\]

- `c`: conteúdo semântico (positivo ou negativo)
- `\iota`: intensidade (entre 0 e 1)
- `\tau`: duração da emoção

**Exemplo**: uma frustração intensa e duradoura:

\[
\mathbf{u} = (-1, 0.8, 5)
\]

**Magnitude vetorial:**

\[
|\mathbf{u}| = \sqrt{(-1)^2 + (0.8)^2 + (5)^2} \approx 5.16
\]

---

### 🌊 Número de Reynolds Emocional (Re_e)

Inspirado na física, usamos:

\[
Re_e = \frac{|\mathbf{u}| \cdot L_c}{\nu_e}
\]

- `L_c`: escala cognitiva (ex. 2)
- `ν_e`: viscosidade emocional (ex. 1)

**Exemplo prático:**

\[
Re_e = \frac{5.16 \cdot 2}{1} = 10.32
\]

Se `Re_e` for muito alto, a emoção é turbulenta → IA pode aplicar *fallback emocional*.

---

### 📈 Dinâmica Temporal com EDO

\[
\frac{d\mathbf{u}}{dt} = F(\mathbf{u}(t), P(t), t)
\]

Exemplo de função `F`:

\[
F(\mathbf{u}, P, t) = (-0.1c, 0.5P - \iota, -0.2\tau)
\]

Para `P = 0.6`, temos:

\[
\frac{d\mathbf{u}}{dt} = (0.1, -0.5, -1)
\]

---

### ⚖️ Estabilidade com Lyapunov

\[
L(\mathbf{u}) = \frac{1}{2} |\mathbf{u} - \mathbf{u}^*|^2
\]

Se:

\[
\frac{dL}{dt} = (\mathbf{u} - \mathbf{u}^*) \cdot \frac{d\mathbf{u}}{dt} < 0
\]

→ O sistema emocional é estável e retorna ao estado neutro.

---

### 🔁 Simulação Numérica (Euler)

\[
\mathbf{u}(t+\Delta t) = \mathbf{u}(t) + \frac{d\mathbf{u}}{dt} \cdot \Delta t
\]

---

## 💻 Código Python (Simples e Didático)

```python
import numpy as np

# Estado inicial
u = np.array([-1, 0.8, 5])
dt = 0.1
P = 0.6

def F(u, P):
    return np.array([-0.1 * u[0], 0.5 * P - u[1], -0.2 * u[2]])

# Atualização do estado
u_new = u + F(u, P) * dt
print("Novo estado:", u_new)

# Cálculo da magnitude
magnitude = np.linalg.norm(u_new)

# Cálculo de Re_e
Lc, nu_e = 2, 1
Re_e = (magnitude * Lc) / nu_e
print("Re_e:", Re_e)

## 🌐 MDEI em Ação: Onde a Teoria Encontra a Realidade

As implicações do MDEI se estendem por diversas disciplinas, prometendo transformar a forma como interagimos com a tecnologia e compreendemos a mente.

### 🧠 Neuropsicologia Computacional & Saúde Mental Digital

- **Diagnóstico e Monitoramento Preditivo**: modelar a progressão de distúrbios afetivos (depressão, ansiedade), correlacionando vetores emocionais com biomarcadores.
- **Terapias Digitais Personalizadas**: intervenções adaptativas em tempo real ao estado emocional do usuário.

### 🤖 Inteligência Artificial Empática & Agentes Autônomos

- **LLMs com “alma”**: chatbots que modulam tom e profundidade conforme o estado afetivo do usuário.
- **Robótica social & wearables**: dispositivos que detectam e reagem emocionalmente ao ambiente.

### 📈 Sistemas Dinâmicos & Cibernética

- **Análise de estabilidade** com teoria de Lyapunov e bifurcações.
- **Fluxo de estados emocionais** inspirado em Navier-Stokes para redes cognitivas.

### 📚 Educação Personalizada & Engajamento Cognitivo

- **Tutores inteligentes** que adaptam conteúdo conforme a curva emocional do aluno.
- **Ferramentas de avaliação afetiva** para ambientes menos estressantes.

### 💬 Linguística Computacional & Sentimento Avançado

- **Vetorização de expressões afetivas** além da classificação discreta.
- **Detecção de turbulência textual** em redes sociais e narrativas de crise.

---

## 🔎 Exemplos de Áreas de Pesquisa com MDEI

O modelo pode ser ponto de partida para **doutorados, mestrados, iniciações científicas ou P&D corporativo** em várias disciplinas:

### 🎓 Psicologia e Neurociência

- Modelagem de estados afetivos em pacientes com transtornos.
- Análise de dinâmica emocional em sessões terapêuticas.
- Uso de EEG + vetores MDEI para prever recaídas.

### 🧠 Ciência Cognitiva & IA

- LLMs com percepção emocional contínua.
- Estudo de autorregulação afetiva em agentes.
- Comparação entre sistemas simbólicos e vetoriais afetivos.

### 💻 Computação & Sistemas Dinâmicos

- Simulações multiagente com vetores emocionais.
- Controle de instabilidades com Lyapunov.
- Modelos bayesianos + MDEI para inferência afetiva.

### 📊 Engenharia de Dados

- Análise vetorial de sentimentos.
- Motores de recomendação com perfil emocional.
- Análise de discurso e detecção de instabilidade narrativa.

### 🤖 Robótica & Cibernética

- Robôs com sensores emocionais artificiais.
- Planejamento de ações com regulação afetiva.
- Wearables com autoajuste comportamental.

---

## ✅ Por que usar o MDEI?

- 🔬 **Base matemática sólida** com álgebra linear e EDOs.
- 📡 **Processamento em tempo real** do estado emocional.
- 🔁 **Modularidade e integração** com pipelines modernos de IA.
- 🌍 **Transdisciplinaridade verdadeira**: une psicologia, computação e engenharia.

---

## 🤝 Convite à Comunidade: Construindo o Futuro Juntos

Este repositório é um convite aberto à colaboração para cientistas, engenheiros, desenvolvedores e pesquisadores que compartilham a visão de uma IA **mais humana, adaptativa e interpretável**.

### Buscamos colaboração para:

- 📊 **Validação de parâmetros** com dados reais (EEG, neuroimagem, sensores afetivos).
- 💻 **Protótipos com LLMs, robótica e saúde digital**.
- 📐 **Expansão teórica** com novas equações e analogias.
- 📚 **Publicações conjuntas** com coautoria acadêmica.

Se você está pronto para explorar as **fronteiras da cognição artificial**, junte-se a nós nesta jornada.

---

## 📂 Como Contribuir

```bash
# Fork o repositório
# Crie uma branch para sua feature
git checkout -b feature/sua-feature

# Faça alterações e commit
git commit -m "Adiciona nova feature MDEI"

# Envie para a branch
git push origin feature/sua-feature

# Abra um Pull Request
```

---

## 📬 Contato

**Tiago Aguioncio Vieira**  
Fundador da ZENNE Tecnologia  
📧 tiago@zennetech.com  
🌐 [zennetech.com](https://zennetech.com)

---

> “A ponte é pra unificar o caos.” — ZENNE-Λ
