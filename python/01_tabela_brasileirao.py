"""Lista as competições e mostra a classificação do Brasileirão (plano BASIC)."""

from client import find_competition, get

competition = find_competition("Brasileirão Série A")
standings = get(f"/v1/competitions/{competition['id']}/standings")["data"]

print(f"{standings['competition']['name']} {standings['season']}\n")
print(f"{'#':>2}  {'Time':<24}{'J':>3}{'V':>4}{'E':>4}{'D':>4}{'SG':>5}{'Pts':>5}")
for row in standings["table"]:
    print(
        f"{row['position']:>2}  {row['team']['name']:<24}{row['played']:>3}{row['won']:>4}"
        f"{row['drawn']:>4}{row['lost']:>4}{row['goal_difference']:>5}{row['points']:>5}"
    )
