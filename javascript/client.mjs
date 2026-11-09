const HOST = "futapi.p.rapidapi.com";

function headers() {
  const key = process.env.RAPIDAPI_KEY;
  if (!key) {
    console.error("Defina a variável de ambiente RAPIDAPI_KEY com sua chave da RapidAPI.");
    process.exit(1);
  }
  return { "x-rapidapi-host": HOST, "x-rapidapi-key": key };
}

export async function get(path, params = {}) {
  const url = new URL(`https://${HOST}${path}`);
  for (const [name, value] of Object.entries(params)) {
    if (value !== undefined && value !== null) url.searchParams.set(name, value);
  }
  const response = await fetch(url, { headers: headers() });
  const body = await response.json();
  if (!response.ok) {
    console.error(`${response.status} ${body.error?.code}: ${body.error?.message}`);
    process.exit(1);
  }
  return body;
}

export async function getAll(path, params = {}) {
  const items = [];
  let cursor;
  do {
    const body = await get(path, { ...params, limit: 100, cursor });
    items.push(...body.data);
    cursor = body.paging?.next_cursor;
  } while (cursor);
  return items;
}

export async function findCompetition(name) {
  const { data } = await get("/v1/competitions");
  const competition = data.find((item) => item.name.toLowerCase() === name.toLowerCase());
  if (!competition) {
    console.error(`Competição '${name}' não encontrada. Disponíveis: ${data.map((item) => item.name).sort().join(", ")}`);
    process.exit(1);
  }
  return competition;
}
