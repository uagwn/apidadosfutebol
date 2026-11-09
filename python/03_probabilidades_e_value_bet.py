"""Probabilidades pré-jogo, odd justa e valor esperado (plano ULTRA).

Uso: python 03_probabilidades_e_value_bet.py <match_id> [odd_mandante odd_empate odd_visitante]
"""

import sys

from client import get


def expected_value(probability: float, odds: float) -> float:
    return probability * odds - 1


if len(sys.argv) < 2:
    sys.exit(__doc__)

match_id = sys.argv[1]
market = [float(value.replace(",", ".")) for value in sys.argv[2:5]]

match = get(f"/v1/matches/{match_id}", timezone="America/Sao_Paulo")["data"]
prediction = get(f"/v1/matches/{match_id}/prediction")["data"]

print(f"{match['home_team']['name']} x {match['away_team']['name']}  ({match['kickoff_at']})\n")
print(f"Gols esperados: {prediction['expected_goals']['home']} x {prediction['expected_goals']['away']}\n")

labels = {"home_win": "Mandante", "draw": "Empate", "away_win": "Visitante"}
for index, (key, label) in enumerate(labels.items()):
    outcome = prediction["result"][key]
    line = f"{label:<10} {outcome['probability']:>7.1%}  odd justa {outcome['fair_odds']:>5.2f}"
    if len(market) == 3:
        ev = expected_value(outcome["probability"], market[index])
        line += f"  odd mercado {market[index]:>5.2f}  EV {ev:+.1%}{'  <- valor' if ev > 0 else ''}"
    print(line)

print(f"\nOver 2.5:     {prediction['over_under']['over_2_5']:.1%}")
print(f"Ambos marcam: {prediction['btts_yes']:.1%}")
print("Placares mais prováveis:", ", ".join(
    f"{item['score']} ({item['probability']:.1%})" for item in prediction["most_likely_scores"][:3]
))
