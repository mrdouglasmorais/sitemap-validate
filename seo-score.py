import requests

def get_google_search_results(query, api_key, cx):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching search results: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
    return None

def score_content_ranking(search_results, target_url):
    if not search_results or 'items' not in search_results:
        print("No search results found.")
        return

    ranked_urls = [item['link'] for item in search_results['items']]
    if target_url not in ranked_urls:
        print(f"Target URL ({target_url}) not found in the search results.")
        return

    target_ranking = ranked_urls.index(target_url) + 1
    print(f"Target URL ({target_url}) is ranked at position {target_ranking} on Google.")

def main():
    api_key = 'YOUR_API_KEY'
    cx = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'
    target_url = 'https://www.imovit.com.br/'  # Replace this with the URL you want to check

    query = input("Enter the search query: ")
    search_results = get_google_search_results(query, api_key, cx)
    score_content_ranking(search_results, target_url)

if __name__ == "__main__":
    main()
