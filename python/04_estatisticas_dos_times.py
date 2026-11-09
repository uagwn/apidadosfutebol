"""Médias de escanteios, cartões, gols e xG de todos os times do Brasileirão (plano PRO)."""

from client import find_competition, get

competition = find_competition("Brasileirão Série A")
rows = get(f"/v1/competitions/{competition['id']}/teams/stats", venue="all")["data"]
rows.sort(key=lambda row: row["averages"].get("corners_total") or 0, reverse=True)

print(f"{competition['name']} {rows[0]['season']} - médias por jogo\n")
print(f"{'Time':<24}{'J':>3}{'Escanteios':>12}{'Amarelos':>10}{'Gols pró':>10}{'xG':>7}{'Over 2.5':>10}")
for row in rows:
    averages, percentages = row["averages"], row["percentages"]
    xg = averages.get("xg_for")
    print(
        f"{row['team']['name']:<24}{row['matches']:>3}{averages['corners_total']:>12.2f}"
        f"{averages['yellow_cards']:>10.2f}{averages['goals_for']:>10.2f}"
        f"{(f'{xg:.2f}' if xg is not None else '-'):>7}{percentages['over_2_5']:>9.0f}%"
    )
