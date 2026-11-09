import os
import sys

import requests

HOST = "futapi.p.rapidapi.com"
BASE_URL = f"https://{HOST}"


def _headers() -> dict:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Defina a variável de ambiente RAPIDAPI_KEY com sua chave da RapidAPI.")
    return {"x-rapidapi-host": HOST, "x-rapidapi-key": key}


def get(path: str, **params) -> dict:
    response = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
    if response.status_code != 200:
        error = response.json().get("error", {})
        sys.exit(f"{response.status_code} {error.get('code')}: {error.get('message')}")
    return response.json()


def get_all(path: str, **params) -> list:
    items, cursor = [], None
    while True:
        body = get(path, limit=100, cursor=cursor, **params)
        items.extend(body["data"])
        cursor = (body.get("paging") or {}).get("next_cursor")
        if not cursor:
            return items


def find_competition(name: str) -> dict:
    competitions = get("/v1/competitions")["data"]
    for competition in competitions:
        if competition["name"].lower() == name.lower():
            return competition
    names = ", ".join(sorted(item["name"] for item in competitions))
    sys.exit(f"Competição '{name}' não encontrada. Disponíveis: {names}")
