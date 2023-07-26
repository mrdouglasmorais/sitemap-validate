import requests
from bs4 import BeautifulSoup

def fetch_page_with_googlebot(user_agent, url):
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching the page: {response.status_code}")
    return None

def check_seo(url):
    googlebot_user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    page_content = fetch_page_with_googlebot(googlebot_user_agent, url)
    if not page_content:
        return

    soup = BeautifulSoup(page_content, 'html.parser')

    # Check page title
    page_title = soup.title.text.strip() if soup.title else 'Title tag not found'
    print(f"Page Title: {page_title}")

    # Check meta description
    meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_desc_tag['content'].strip() if meta_desc_tag else 'Meta description not found'
    print(f"Meta Description: {meta_description}")

    # Check for H1 tag
    h1_tag = soup.find('h1')
    h1_content = h1_tag.text.strip() if h1_tag else 'H1 tag not found'
    print(f"H1 Tag: {h1_content}")

    # Check for images without alt attribute
    images_without_alt = soup.find_all('img', alt="")
    if images_without_alt:
        print("Images without alt attribute:")
        for img in images_without_alt:
            print(img)

    # Check for broken links (404 status)
    links = soup.find_all('a', href=True)
    if links:
        print("Checking for broken links...")
        for link in links:
            link_url = link['href']
            if not link_url.startswith('http'):
                link_url = url + link_url
            response = requests.get(link_url)
            if response.status_code == 404:
                print(f"Broken link: {link_url}")

def main():
    url_to_check = input("Enter the URL to check SEO: ")
    check_seo(url_to_check)

if __name__ == "__main__":
    main()
