# API Dados Futebol: exemplos em Python, JavaScript e Google Sheets

Exemplos prontos para usar a [API Dados Futebol](https://www.apidadosfutebol.com): jogos, tabela, estatísticas, xG, ratings e probabilidades pré-jogo de **37 competições**, incluindo Brasileirão Série A e B, Copa do Brasil, Libertadores, Premier League, La Liga, Serie A, Bundesliga e Champions League.

- Site e documentação: https://www.apidadosfutebol.com/docs
- Referência dos endpoints: https://www.apidadosfutebol.com/referencia
- Assinatura (plano grátis disponível): https://rapidapi.com/wagnyoliver/api/futapi

## O que a API entrega

| Recurso | Plano |
|---|---|
| Competições, temporadas, classificação geral, em casa e fora | BASIC (grátis) |
| Jogos do dia, calendário e resultados em qualquer fuso horário | BASIC (grátis) |
| Times, elencos, jogadores e estádios | BASIC (grátis) |
| Eventos, escalações e 35 estatísticas por time em cada partida | PRO |
| Médias e percentuais de temporada (escanteios, cartões, over, ambos marcam) | PRO |
| Probabilidades pré-jogo com odd justa, over/under, ambos marcam | ULTRA |
| xG e rating de jogadores, 62 métricas por jogador | ULTRA |

## Como começar

1. Assine o plano grátis em [rapidapi.com/wagnyoliver/api/futapi](https://rapidapi.com/wagnyoliver/api/futapi).
2. Copie sua chave (`x-rapidapi-key`) e defina a variável de ambiente:

```bash
# Linux e macOS
export RAPIDAPI_KEY="sua_chave"

# Windows (PowerShell)
$env:RAPIDAPI_KEY = "sua_chave"
```

## Python

```bash
cd python
pip install -r requirements.txt
python 01_tabela_brasileirao.py
```

| Arquivo | O que faz | Plano |
|---|---|---|
| [01_tabela_brasileirao.py](python/01_tabela_brasileirao.py) | Classificação do Brasileirão | BASIC |
| [02_jogos_do_dia.py](python/02_jogos_do_dia.py) | Jogos de hoje no horário de Brasília | BASIC |
| [03_probabilidades_e_value_bet.py](python/03_probabilidades_e_value_bet.py) | Probabilidades, odd justa e valor esperado contra odds do mercado | ULTRA |
| [04_estatisticas_dos_times.py](python/04_estatisticas_dos_times.py) | Médias de escanteios, cartões, gols e xG por time | PRO |
| [05_exportar_jogos_csv.py](python/05_exportar_jogos_csv.py) | Exporta todos os jogos de uma temporada para CSV | BASIC |

Exemplo de value bet, informando as odds do mercado para mandante, empate e visitante:

```bash
python 03_probabilidades_e_value_bet.py mt_C6lLw8fjh1nI 3.80 3.50 2.25
```

## JavaScript (Node.js 18+)

```bash
cd javascript
node 01_jogos_do_dia.mjs
```

| Arquivo | O que faz | Plano |
|---|---|---|
| [01_jogos_do_dia.mjs](javascript/01_jogos_do_dia.mjs) | Jogos de hoje no horário de Brasília | BASIC |
| [02_probabilidades.mjs](javascript/02_probabilidades.mjs) | Probabilidades e odd justa de uma partida | ULTRA |
| [03_tabela_casa_fora.mjs](javascript/03_tabela_casa_fora.mjs) | Classificação só com jogos em casa e fora | BASIC |

## Google Sheets

[google-sheets/Code.gs](google-sheets/Code.gs) monta uma planilha com a tabela do Brasileirão e pode ser atualizada todo dia com um acionador do Apps Script. As instruções estão no topo do arquivo.

## Conceitos rápidos

- Toda resposta tem o formato `{"data", "paging", "meta"}`; erros vêm como `{"error": {"code", "message"}}`.
- Ids são textos com prefixo: `cp_` competição, `mt_` partida, `tm_` time, `pl_` jogador.
- Use `season=2025` ou `season=2025/2026` para temporadas anteriores.
- Use `timezone=America/Sao_Paulo` para receber datas no horário de Brasília.
- Listas são paginadas com `limit` e `paging.next_cursor` (veja `get_all` em [python/client.py](python/client.py)).

Mais detalhes em [apidadosfutebol.com/docs/conceitos](https://www.apidadosfutebol.com/docs/conceitos).

## Guias

- [Como calcular a odd justa de uma aposta](https://www.apidadosfutebol.com/blog/como-calcular-odd-justa)
- [O que é xG e como ele é calculado](https://www.apidadosfutebol.com/blog/o-que-e-xg)
- [Value bet: o que é e como encontrar apostas de valor](https://www.apidadosfutebol.com/blog/value-bet)
- [Estatísticas por campeonato e por time](https://www.apidadosfutebol.com/estatisticas)

## Licença

Código dos exemplos sob licença [MIT](LICENSE). O uso dos dados segue os [termos da API](https://www.apidadosfutebol.com/termos).
