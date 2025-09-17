---
language: python
license: mit
tags:
- python
- parser
- quake
- data-processing
- regex
---

# Quake 3 Arena Log Parser
![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg) ![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)

## 📜 Descrição do Projeto

Este repositório contém um script em Python desenvolvido para analisar (fazer o *parse*) de arquivos de log do jogo **Quake 3 Arena** (`games.log`). O parser extrai informações detalhadas sobre cada partida, incluindo a contagem total de mortes, a lista de jogadores e a pontuação individual.

Este projeto foi criado como um desafio técnico para demonstrar habilidades em:
-   Manipulação de arquivos e processamento de texto em Python.
-   Uso de expressões regulares (regex) para extração de dados.
-   Estrutura de dados e lógica de programação.
-   Desenvolvimento orientado a testes (TDD) com a biblioteca `unittest`.
-   Boas práticas de versionamento com Git.

-   **Linguagem:** Python
-   **Dependências:** Nenhuma biblioteca externa necessária.
-   **Desenvolvido por:** David Nascimento (David-Cunha)

## 🚀 Instalação e Uso

O script foi projetado para ser simples e direto, sem a necessidade de instalar pacotes externos.

**1. Clone o repositório:**
```bash
git clone [https://github.com/David-Cunha/quake-log-parser.git](https://github.com/David-Cunha/quake-log-parser.git)
cd quake-log-parser
```
**2. Coloque seu arquivo de log:**
Certifique-se de que o arquivo de log que você deseja analisar se chama games.log e está na mesma pasta que o script parser.py.

**3. Execute o script:**
```bash
python parser.py
```
O script irá processar o arquivo e imprimir no console um relatório JSON detalhado para cada partida e um ranking geral de jogadores.

## 💻 Lógica e Funcionalidades
- O parser implementa uma série de regras para garantir a correta contabilização dos dados de cada partida.
- Agrupamento de Partidas: Cada partida é identificada pelo evento InitGame e finalizada pelo evento ShutdownGame.
- Extração de Dados: Para cada partida, o script extrai:
  - total_kills: A contagem de todas as mortes ocorridas na partida.
  - players: Uma lista com o nome de todos os jogadores que participaram.
  - kills: Um dicionário com a pontuação de cada jogador.
  - kills_by_means: (Bônus) Um relatório que agrupa as mortes pela causa (ex: MOD_RAILGUN, MOD_FALLING).

- Regras de Pontuação:
  - Quando um jogador é morto pelo <world>, ele perde -1 kill.
  - O <world> não é considerado um jogador e não aparece nas listas de pontuação.
  - Suicídios também resultam na perda de -1 kill para o jogador.
 
## 📊 Exemplo de Saída
Ao executar o script, você receberá um relatório formatado no terminal.
Relatório por Partida (JSON):
```json
{
    "game_4": {
        "total_kills": 105,
        "players": [
            "Assasinu Credi",
            "Dono da Bola",
            "Isgalamido",
            "Zeh"
        ],
        "kills": {
            "Isgalamido": 19,
            "Dono da Bola": 5,
            "Zeh": 20,
            "Assasinu Credi": 11
        },
        "kills_by_means": {
            "MOD_TRIGGER_HURT": 9,
            "MOD_FALLING": 11,
            "MOD_ROCKET": 20,
            "MOD_RAILGUN": 8,
            "MOD_ROCKET_SPLASH": 51,
            "MOD_MACHINEGUN": 4,
            "MOD_SHOTGUN": 2
        }
    }
}
```
## Ranking Geral de Jogadores:
```
--- RANKING GERAL DE JOGADORES ---
1. Isgalamido: 129 kills
2. Zeh: 116 kills
3. Oootsimo: 102 kills
```

## 🧪 Executando os Testes
O projeto inclui uma suíte de testes unitários para validar a lógica principal do parser.
Para executar os testes, utilize o módulo unittest do Python:
```bash
python -m unittest test_parser.py
```
A saída esperada é a confirmação de que todos os testes foram executados e passaram com sucesso.

## 📝 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
