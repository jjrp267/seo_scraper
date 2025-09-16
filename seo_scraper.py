import sys
import requests
from bs4 import BeautifulSoup

def extraer_seo(url):
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Título
    title = soup.title.string.strip() if soup.title else "No encontrado"

    # Meta description
    description = soup.find("meta", attrs={"name": "description"})
    description = description["content"].strip() if description else "No encontrada"

    # Meta keywords
    keywords = soup.find("meta", attrs={"name": "keywords"})
    keywords = keywords["content"].strip() if keywords else "No encontradas"

    # H1 y H2
    h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
    h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

    # ALT de imágenes
    img_alts = [img.get("alt", "Sin alt").strip() for img in soup.find_all("img")]

    return {
        "title": title,
        "description": description,
        "keywords": keywords,
        "h1": h1_tags,
        "h2": h2_tags,
        "img_alts": img_alts
    }

if __name__ == "__main__":
    # Permite pasar URL como argumento: python seo_scraper.py https://miweb.com
    url = sys.argv[1] if len(sys.argv) > 1 else "https://restaurantecasaeva.com"
    data = extraer_seo(url)

    print("\n===== RESULTADO SEO =====")
    print(f"URL: {url}")
    print(f"\n▶ Title:\n   {data['title']}")
    print(f"\n▶ Meta Description:\n   {data['description']}")
    print(f"\n▶ Meta Keywords:\n   {data['keywords']}")

    print("\n▶ Encabezados H1:")
    if data['h1']:
        for i, h in enumerate(data['h1'], 1):
            print(f"   {i}. {h}")
    else:
        print("   No encontrados")

    print("\n▶ Encabezados H2:")
    if data['h2']:
        for i, h in enumerate(data['h2'], 1):
            print(f"   {i}. {h}")
    else:
        print("   No encontrados")

    print("\n▶ ALT de Imágenes:")
    if data['img_alts']:
        for i, alt in enumerate(data['img_alts'], 1):
            print(f"   {i}. {alt}")
    else:
        print("   No encontrados")

    print("\n=========================\n")
