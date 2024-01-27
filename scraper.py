import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.britannica.com/topic/list-of-cities-and-towns-in-India-2033033'

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Attempt to find all city names
    city_names = []
    for anchor in soup.find_all('a'):
        if 'href' in anchor.attrs and '/place/' in anchor['href']:
            city_name = anchor.get_text().strip()
            city_names.append(city_name)

    # Remove duplicates
    city_names = list(set(city_names))

    # Print the city names
    for city in sorted(city_names):
        print(city.encode('utf-8'))
        
    with open('indian_cities.csv', 'w', encoding='utf-8') as file:
        for city in sorted(city_names):
            file.write(city + '\n')
else:
    print("Failed to retrieve data")
