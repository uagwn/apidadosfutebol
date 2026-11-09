"""Exporta todos os jogos de uma temporada para CSV (plano BASIC).

Uso: python 05_exportar_jogos_csv.py ["Nome da competição"] [temporada]
Exemplo: python 05_exportar_jogos_csv.py "Premier League" 2025/2026
"""

import csv
import sys

from client import find_competition, get_all

name = sys.argv[1] if len(sys.argv) > 1 else "Brasileirão Série A"
season = sys.argv[2] if len(sys.argv) > 2 else None

competition = find_competition(name)
params = {"timezone": "America/Sao_Paulo"}
if season:
    params["season"] = season
matches = get_all(f"/v1/competitions/{competition['id']}/matches", **params)

filename = f"jogos_{competition['name']}_{season or 'atual'}.csv".replace(" ", "_").replace("/", "-")
with open(filename, "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["id", "rodada", "data", "status", "mandante", "visitante", "gols_mandante", "gols_visitante"])
    for match in matches:
        writer.writerow([
            match["id"], match["round"], match["kickoff_at"], match["status"],
            match["home_team"]["name"], match["away_team"]["name"],
            match["score"]["home"], match["score"]["away"],
        ])

print(f"{len(matches)} jogos salvos em {filename}")
