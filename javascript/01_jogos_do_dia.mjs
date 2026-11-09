// Jogos de hoje em todas as competições, no horário de Brasília (plano BASIC).
import { getAll } from "./client.mjs";

const matches = await getAll("/v1/matches", { timezone: "America/Sao_Paulo" });

if (matches.length === 0) console.log("Nenhum jogo hoje.");

for (const match of matches) {
  const hour = (match.kickoff_at ?? "").slice(11, 16);
  const { home, away } = match.score;
  const result = home === null ? "x" : `${home} x ${away}`;
  console.log(
    `${hour}  ${match.competition.name.padEnd(28)} ${match.home_team.name} ${result} ${match.away_team.name}  [${match.status}]`,
  );
}
