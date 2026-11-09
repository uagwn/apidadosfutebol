// Classificação de uma liga em casa e fora (plano BASIC).
// Uso: node 03_tabela_casa_fora.mjs ["Nome da competição"]
import { findCompetition, get } from "./client.mjs";

const name = process.argv[2] ?? "Brasileirão Série A";
const competition = await findCompetition(name);

for (const venue of ["home", "away"]) {
  const { data } = await get(`/v1/competitions/${competition.id}/standings`, { venue });
  console.log(`\n${data.competition.name} ${data.season} - ${venue === "home" ? "em casa" : "fora"}`);
  for (const row of data.table.slice(0, 5)) {
    console.log(`${String(row.position).padStart(2)}  ${row.team.name.padEnd(24)} ${String(row.points).padStart(3)} pts`);
  }
}
