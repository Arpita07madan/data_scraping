import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_result_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    election_results = []

    # Example: Handling different page structures
    if 'PcResultGenJune2024' in url:  # Example for Parliamentary Constituencies page
        tables = soup.find_all('table')  # Adjust as per actual HTML structure
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 3:  # Assuming columns for candidate name, votes, party
                    candidate_name = cols[0].text.strip()
                    votes = cols[1].text.strip()
                    party = cols[2].text.strip()
                    election_results.append({
                        'candidate_name': candidate_name,
                        'votes': votes,
                        'party': party
                    })

    elif 'AcResultGenJune2024' in url:  # Example for Assembly Constituencies page
        # Implement scraping logic specific to Assembly Constituencies page
        # Adjust as per actual HTML structure
        pass  # Placeholder for actual scraping logic

    return election_results

if __name__ == "__main__":
    result_links = [
        'https://results.eci.gov.in/PcResultGenJune2024/index.htm',
        'https://results.eci.gov.in/AcResultGenJune2024/index.htm',
        # Add more URLs as needed
    ]

    for link in result_links:
        data = scrape_result_page(link)
        print(f"Data from {link}:")
        print(data)
        print()  # Separate outputs for clarity
