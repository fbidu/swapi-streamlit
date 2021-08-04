import logging
import requests

import streamlit as st

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
BASE_URL = "https://swapi.dev/api/"


def call(url):
    """
    Faz uma chamada genérica pra API e trata possíveis erros.
    Em caso de sucesso, retorna um dicionário com a resposta.
    Em caso de falha, retorna um dicionário vazio.
    """
    response = requests.get(url)
    # Tratamento de erros
    if response.status_code >= 400:
        logging.error("Erro ao chamar %s", url)
        return {}

    return response.json()


def list_entity(entity):
    """
    Lista uma determinada entidade

    >>> list("planets")
    (...) # Lista com planetas
    """
    return call(f"{BASE_URL}{entity}/").get("results")


st.header("API do Star Wars!")

planets = list_entity("planets")

for idx, planet in enumerate(planets):
    st.header("🪐", planet["name"])

    if st.button("Ver população cadastrada", key=idx):
        planet = call(planets[idx]["url"])
        st.text(
            f"O planeta {planet['name']} tem {len(planet['residents'])} moradores cadastrados"
        )

    st.markdown("---")
