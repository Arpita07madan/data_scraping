import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://results.eci.gov.in'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links to result pages
result_links = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if 'ResultGenJune2024' in href:
        full_url = urljoin(url, href)  # Construct full URL
        result_links.append(full_url)

# Print the collected links (for verification)
print("Found Result Links:")
for link in result_links:
    print(link)
