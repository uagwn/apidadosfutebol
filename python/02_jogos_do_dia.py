"""Jogos de hoje em todas as competições, no horário de Brasília (plano BASIC)."""

from client import get_all

matches = get_all("/v1/matches", timezone="America/Sao_Paulo")

if not matches:
    print("Nenhum jogo hoje.")

for match in matches:
    hour = (match["kickoff_at"] or "")[11:16]
    score = match["score"]
    result = f"{score['home']} x {score['away']}" if score["home"] is not None else "x"
    print(
        f"{hour}  {match['competition']['name']:<28} "
        f"{match['home_team']['name']} {result} {match['away_team']['name']}  [{match['status']}]"
    )
