import requests
import xml.etree.ElementTree as ET

def download_sitemap(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Erro ao fazer download do sitemap: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    return None

def validate_sitemap(xml_content):
    try:
        root = ET.fromstring(xml_content)
        if root.tag.endswith('sitemapindex'):
            print("O arquivo é um sitemapindex válido.")
            for child in root:
                if child.tag.endswith('sitemap'):
                    loc_element = child.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc_element is not None:
                        print(f"Sitemap: {loc_element.text}")
                    else:
                        print("Sitemap inválido - elemento <loc> não encontrado.")
        elif root.tag.endswith('urlset'):
            print("O arquivo é um urlset válido.")
            for child in root:
                if child.tag.endswith('url'):
                    loc_element = child.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc_element is not None:
                        print(f"URL: {loc_element.text}")
                    else:
                        print("URL inválida - elemento <loc> não encontrado.")
        else:
            print("Formato de sitemap desconhecido.")
    except ET.ParseError as e:
        print(f"Erro ao analisar o arquivo XML: {e}")

def main():
    sitemap_url = input("Digite a URL do sitemap: ")
    sitemap_content = download_sitemap(sitemap_url)
    if sitemap_content:
        validate_sitemap(sitemap_content)

if __name__ == "__main__":
    main()
