// Probabilidades pré-jogo e odd justa de uma partida (plano ULTRA).
// Uso: node 02_probabilidades.mjs <match_id>
import { get } from "./client.mjs";

const matchId = process.argv[2];
if (!matchId) {
  console.error("Uso: node 02_probabilidades.mjs <match_id>");
  process.exit(1);
}

const { data: match } = await get(`/v1/matches/${matchId}`, { timezone: "America/Sao_Paulo" });
const { data: prediction } = await get(`/v1/matches/${matchId}/prediction`);

console.log(`${match.home_team.name} x ${match.away_team.name}  (${match.kickoff_at})\n`);

const labels = { home_win: "Mandante", draw: "Empate", away_win: "Visitante" };
for (const [key, label] of Object.entries(labels)) {
  const { probability, fair_odds: fairOdds } = prediction.result[key];
  console.log(`${label.padEnd(10)} ${(probability * 100).toFixed(1).padStart(5)}%  odd justa ${fairOdds.toFixed(2)}`);
}

console.log(`\nOver 2.5:     ${(prediction.over_under.over_2_5 * 100).toFixed(1)}%`);
console.log(`Ambos marcam: ${(prediction.btts_yes * 100).toFixed(1)}%`);
