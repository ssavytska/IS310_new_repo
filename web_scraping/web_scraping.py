import requests
from bs4 import BeautifulSoup
import csv

with open('cleaned_pudding_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader]

results = []
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the script data using the appropriate HTML tags or CSS selectors
        script_data = soup.find('div', {'class': 'script-data'}).text
        
        # Append the first 1000 characters of the script data to the results list
        results.append([url, script_data[:1000]])
    except (requests.exceptions.RequestException, AttributeError) as e:
        print(f"Error accessing {url}: {e}")

    with open('pudding_movie_dialogue_results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
writer.writerow(['URL', 'Script Data'])
writer.writerows(results)



