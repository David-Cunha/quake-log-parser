# parser.py
import json
import re
from collections import defaultdict

def parse_quake_log(log_file_path: str) -> dict:
    """
    Analisa (parse) um arquivo de log do Quake 3 Arena, agrupando os dados por partida.
    """
    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            log_content = f.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{log_file_path}' não foi encontrado.")
        return {}

    games = {}
    game_counter = 0
    kill_pattern = re.compile(r'Kill: .*?: (.*?) killed (.*?) by (.*)')

    for game_log in log_content.split('InitGame:')[1:]:
        game_counter += 1
        game_key = f"game_{game_counter}"

        total_kills = 0
        players = set()
        kills = defaultdict(int)
        kills_by_means = defaultdict(int)

        for line in game_log.splitlines():
            if 'Kill:' in line:
                match = kill_pattern.search(line)
                if not match:
                    continue

                killer, victim, means_of_death = match.groups()
                total_kills += 1

                if killer != '<world>':
                    players.add(killer)
                players.add(victim)

                if killer == '<world>' or killer == victim:
                    kills[victim] -= 1
                else:
                    kills[killer] += 1

                kills_by_means[means_of_death] += 1

        games[game_key] = {
            'total_kills': total_kills,
            'players': sorted(list(players)),
            'kills': dict(kills),
            'kills_by_means': dict(kills_by_means)
        }
    return games

def print_reports(all_games_data: dict):
    """
    Imprime os relatórios de cada jogo e o ranking geral de jogadores.
    """
    print("--- RELATÓRIO DE PARTIDAS ---")
    print(json.dumps(all_games_data, indent=4, ensure_ascii=False))

    print("\n--- RANKING GERAL DE JOGADORES ---")
    player_ranking = defaultdict(int)
    for game_data in all_games_data.values():
        for player, score in game_data['kills'].items():
            player_ranking[player] += score

    sorted_ranking = sorted(player_ranking.items(), key=lambda item: item[1], reverse=True)

    if not sorted_ranking:
        print("Nenhum jogador para rankear.")
    else:
        for rank, (player, score) in enumerate(sorted_ranking, 1):
            print(f"{rank}. {player}: {score} kills")

# Bloco de execução principal
if __name__ == "__main__":
    log_file = 'games.log'
    parsed_data = parse_quake_log(log_file)
    if parsed_data:
        print_reports(parsed_data)