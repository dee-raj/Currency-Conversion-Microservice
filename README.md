# Google Maps and Google Search API Scripts

These scripts provide simple interfaces for interacting with the Google Maps and Google Search APIs using Python's `requests` library.

## Google Maps API Script

### Description

The Google Maps API script retrieves location details using the Google Maps Geocoding API. It takes an API key and a location as input, then prints formatted address, location type, and coordinates.

### Usage

1. Replace the placeholder `process` in `my_api_key = "process"` with your actual Google Maps API key.

2. Update the `my_location_info` variable with the location for which you want to retrieve details.

3. Run the script:

   ```bash
   python google_maps.py
   ```

### Example Output

```
Formatted Address: 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA
Location Type: ROOFTOP
Location: {'lat': 37.4224764, 'lng': -122.0842499}
--------------------------------------------------
```


## Google Search API Script

### Description

The Google Search API script performs a custom search using the Google Custom Search API. It takes an API key and a search query as input, then prints search results including title, link, and snippet.


### Usage

1. Replace the placeholder `google api key` in `_api_key = "google api key"` with your actual Google Custom Search API key.

2. Update the `_search_query` variable with the query for which you want to perform a search.

3. Run the script:

   ```bash
   python google_search.py
   ```


### Example Output

```
Title: Google Search API | Google Developers
Link: https://developers.google.com/custom-search/docs/tutorial/creatingcse
Snippet: The JSON API can be used to integrate Bing Custom Search into applications, websites, or other products.
--------------------------------------------------
```

**Note:** 

Ensure that you have the `requests` library installed. If not, you can install it using:

```bash
pip install requests
```

Feel free to explore and customize these scripts according to your needs!
```
