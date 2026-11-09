/**
 * Planilha de futebol no Google Sheets com dados da API Dados Futebol.
 *
 * 1. Na planilha: Extensões > Apps Script e cole este arquivo.
 * 2. Em Configurações do projeto > Propriedades do script, crie RAPIDAPI_KEY com sua chave.
 * 3. Rode atualizarTabela() ou crie um acionador diário.
 */

const HOST = "futapi.p.rapidapi.com";
const COMPETICAO = "Brasileirão Série A";

function chamarApi(caminho) {
  const chave = PropertiesService.getScriptProperties().getProperty("RAPIDAPI_KEY");
  const resposta = UrlFetchApp.fetch(`https://${HOST}${caminho}`, {
    headers: { "x-rapidapi-host": HOST, "x-rapidapi-key": chave },
    muteHttpExceptions: true,
  });
  const corpo = JSON.parse(resposta.getContentText());
  if (resposta.getResponseCode() !== 200) throw new Error(`${corpo.error.code}: ${corpo.error.message}`);
  return corpo.data;
}

function atualizarTabela() {
  const competicao = chamarApi("/v1/competitions").find((item) => item.name === COMPETICAO);
  const tabela = chamarApi(`/v1/competitions/${competicao.id}/standings`);
  const linhas = tabela.table.map((linha) => [
    linha.position, linha.team.name, linha.played, linha.won, linha.drawn, linha.lost,
    linha.goals_for, linha.goals_against, linha.goal_difference, linha.points,
  ]);

  const aba = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Tabela")
    ?? SpreadsheetApp.getActiveSpreadsheet().insertSheet("Tabela");
  aba.clear();
  aba.getRange(1, 1, 1, 10).setValues([["#", "Time", "J", "V", "E", "D", "GP", "GC", "SG", "Pts"]]).setFontWeight("bold");
  aba.getRange(2, 1, linhas.length, 10).setValues(linhas);
  aba.getRange(linhas.length + 3, 1).setValue(`${tabela.competition.name} ${tabela.season} - atualizado em ${new Date().toLocaleString("pt-BR")}`);
}
