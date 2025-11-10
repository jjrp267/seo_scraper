import requests

url = "https://abogadosariza.es"

# Hacemos una petición HTTP indicando que aceptamos varios tipos de compresión
headers = {
    "Accept-Encoding": "gzip, deflate, br"
}

response = requests.get(url, headers=headers)

# Mostramos las cabeceras de respuesta
print("Cabeceras de respuesta:")
for k, v in response.headers.items():
    print(f"{k}: {v}")

# Comprobamos si la respuesta está comprimida
encoding = response.headers.get("Content-Encoding")
if encoding:
    print(f"\n✅ El servidor está usando compresión: {encoding}")
else:
    print("\n❌ El servidor NO está usando compresión (Content-Encoding ausente)")
