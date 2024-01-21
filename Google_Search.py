import requests
_api_key = "your google cloud api key"

def google_search(api_key, search_query):
   try:
      url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&q={search_query}'

      response = requests.get(url)
      data = response.json()

      if 'items' in data:
         for item in data['items']:
            title = item.get('title', 'N/A')
            link = item.get('link', 'N/A')
            snippet = item.get('snippet', 'N/A')

            print(f'Title: {title}\nLink: {link}\nSnippet: {snippet}\n{"-"*50}')
      else:
         print('No search results found.')
   except KeyError as e:
      print(f'Error: {e} - Invalid response format from Google Search API.')
   except RuntimeError as e:
      print(f'Error: {e} - Runtime error during API request.')

_search_query = ''
google_search(_api_key, _search_query)
