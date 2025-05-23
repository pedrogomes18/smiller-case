# 📦 Smiller Alocador de Pedidos

Este projeto resolve o **Desafio Tech Smiller - Maio/2025**, que propõe um sistema de **alocação diária de pedidos** de alinhadores ortodônticos, respeitando restrições de capacidade e otimizando a produção.

> ✅ Desenvolvido em Python, com foco em eficiência, clareza e otimização de três métricas principais.

---

## 🧠 Contexto do Desafio

A Smiller é uma empresa que fabrica alinhadores ortodônticos sob demanda. Diariamente, novos pedidos chegam e precisam ser distribuídos ao longo de uma linha de produção com **capacidade limitada**.

O desafio proposto consiste em **distribuir esses pedidos respeitando a capacidade de produção diária**, otimizando o processo produtivo e **melhorando o nível de serviço para clientes premium**, além de **reduzir atrasos e custos logísticos**.

### Regras do desafio:

- 🧩 Capacidade: até **325 placas por dia útil**
- ⏳ Prazos combinados com o cliente devem ser respeitados
- 🔐 Datas de produção só podem ser alteradas até **3 dias úteis antes**
- 💎 Clientes premium devem ser priorizados
- 🚛 Agrupamento de pedidos por cliente reduz custos de frete

---

## 📁 Estrutura do Projeto

```
.
├── src/
│   ├── alocador.py        # Algoritmo principal de alocação
│   ├── metricas.py        # Cálculo das métricas solicitadas
│   └── utils.py           # Função auxiliar para contar placas
│
├── data/
│   ├── input/             # Coloque aqui o arquivo CSV de entrada
│   └── output/            # A saída otimizada será salva aqui
│
├── main.py                # Script principal de execução
└── README.md              # Este arquivo
```

---

## ⚙️ Pré-requisitos

- Python 3.8+
- Pandas

```bash
pip install pandas
```

---

## 🚀 Como Executar

1. Coloque seu arquivo de dados em:
   ```
   data/input/dados.csv
   ```

2. Rode o programa:
   ```bash
   python main.py
   ```

3. A saída estará em:
   ```
   data/output/alocacao_otimizada_YYYYMMDD_HHMMSS.csv
   ```

4. As métricas serão exibidas no terminal ao final da execução.

---

## 📊 Métricas Avaliadas

| Métrica                                | Descrição                                                                 |
|----------------------------------------|---------------------------------------------------------------------------|
| **1️⃣ Atraso médio**                   | Quantos dias, em média, os pedidos foram produzidos além do prazo         |
| **2️⃣ Agrupamento por cliente/dia**   | Quantidade média de pedidos agrupados por cliente em um mesmo dia         |
| **3️⃣ Antecipação média VIPs**        | Quantos dias antes do prazo os pedidos de clientes premium foram feitos   |

---

## ✨ Destaques Técnicos

- 📅 Usa `pandas.bdate_range()` para considerar apenas dias úteis
- 🔁 Algoritmo **iterativo e greedy** para alocação
- 📌 Travamento de datas próximas para simular a restrição de replanejamento

---

## 📈 Sugestões de Melhoria

- Implementar uma interface gráfica ou dashboard interativa (Ex: Streamlit)
- Utilizar heurísticas como bin packing ou otimização por prioridade
- Modularizar para permitir testes unitários

---

## 👤 Autor

Pedro Henrique Gomes Oliveira — 2025 • Poli-USP
