import requests
from bs4 import BeautifulSoup

def obtener_encabezados(url):
    try:
        # Descargar el contenido de la página
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return []

    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar encabezados (h1 hasta h6)
    encabezados = []
    for i in range(1, 7):
        for tag in soup.find_all(f'h{i}'):
            encabezados.append((f"h{i}", tag.get_text(strip=True)))

    return encabezados


if __name__ == "__main__":
    url = "https://miweb.com"  # Cambia por la web que quieras
    estructura = obtener_encabezados(url)

    print("Estructura de encabezados encontrada:\n")
    for nivel, texto in estructura:
        print(f"{nivel}: {texto}")
