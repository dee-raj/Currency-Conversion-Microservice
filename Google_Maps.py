import requests
my_api_key = "process"

def google_maps(api_key, location):
   try:
      url = f'https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&address={location}'
      response = requests.get(url)
      data = response.json()

      if 'results' in data:
         for result in data['results']:
            formatted_address = result.get('formatted_address', 'N/A')
            geometry = result.get('geometry', {})
            location_type = geometry.get('location_type', 'N/A')
            location = geometry.get('location', {})
            print(f'Formatted Address: {formatted_address}\nLocation Type: {location_type}\nLocation: {location}\n{"-"*50}')
      else:
         print('No location details found.')

   except KeyError as e:
      print(f'Error: {e} - Invalid response format from Google Maps API.')

   except RuntimeError as e:
      print(f'Error: {e} - Runtime error during API request.')

my_location_info = ''
google_maps(my_api_key, my_location_info)
