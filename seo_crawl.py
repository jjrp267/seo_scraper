import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()
to_visit = set()

def crawl_site(base_url):
    domain = urlparse(base_url).netloc
    to_visit.add(base_url)

    while to_visit:
        url = to_visit.pop()

        # Evitar agregar URLs que terminan en "/" excepto la base
        if url != base_url and url.endswith("/"):
            continue

        if url in visited:
            continue

        visited.add(url)
        print("Visitando:", url)

        try:
            response = requests.get(url, timeout=10)
            if "text/html" not in response.headers.get("Content-Type", ""):
                continue
        except:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            href = link.get("href")
            absolute_url = urljoin(url, href)
            parsed = urlparse(absolute_url)

            if parsed.netloc == domain:
                # Evitar URLs terminadas en "/"
                if absolute_url != base_url and absolute_url.endswith("/"):
                    continue

                if absolute_url not in visited:
                    to_visit.add(absolute_url)

    return visited


if __name__ == "__main__":
    website = "https://lariart.es"  # Cambia por tu sitio
    pages = crawl_site(website)

    print("\nPáginas encontradas:")
    for p in sorted(pages):
        print(p)
