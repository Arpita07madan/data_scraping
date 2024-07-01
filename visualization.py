# Assuming you have already scraped and cleaned the data
import matplotlib.pyplot as plt

# Example: Visualizing top parties by vote count
top_parties = [
    {'candidate_name': 'Bharatiya Janata Party - BJP', 'votes': 240},
    {'candidate_name': 'Indian National Congress - INC', 'votes': 99},
    {'candidate_name': 'Samajwadi Party - SP', 'votes': 37},
    # Add more parties as per your data
]

parties = [party['candidate_name'] for party in top_parties]
votes = [int(party['votes']) for party in top_parties]

plt.figure(figsize=(10, 6))
plt.barh(parties, votes, color='skyblue')
plt.xlabel('Votes')
plt.title('Top Parties by Vote Count')
plt.gca().invert_yaxis()  # Invert y-axis to show highest votes on top
plt.show()
