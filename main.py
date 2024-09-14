import requests
from bs4 import BeautifulSoup
import random

# fetching web content and extracting table with the top 100 games
def scrape_board_games(url):
    print(f"Scraping: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    games_table = soup.find('table', {'class': 'collection_table'})
    if not games_table:
        print("No table found on the page.")
        return []

    rows = games_table.find_all('tr', {'id': 'row_'}) #the rows have ids such as 'row_x'
    games = []

    for row in rows:
        game_rank = row.find('td', {'class': 'collection_rank'}).text.strip()
        game_name = row.find('td', {'class': 'collection_objectname'}).text.strip()
        game_rating = row.find('td', {'class': 'collection_bggrating'}).text.strip()
        game_url = 'https://boardgamegeek.com' + row.find('td', {'class': 'collection_objectname'}).find('a')['href']

        games.append({
            'rank': game_rank,
            'name': game_name,
            'rating': game_rating,
            'url': game_url
        })

    return games

def get_boardgame_rec(url = "https://boardgamegeek.com/browse/boardgame", games = [], num = 5):
    if games == []:
        games = scrape_board_games(url)
    selection = random.sample(games, min(num, len(games)))

    print("Our randomly selected boardgame recommendations:")

    for game in selection:
        name = game['name'].split('\n')
        print(f"Name: {name[0]} {name[1]}\n" +
            f"Description: {name[4].strip()}\n"+
            f"Rank: {game['rank']}\n" +
            f"Rating: {game['rating']}\n" +
            f"Url: {game['url']}\n")
            

# chose not to use
# def top_music_scrape(url, num_info=20):
#     print(f"scraping, {url}")
#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"Failed to get the webpage: {response.status_code}")
#             return []
#         soup = BeautifulSoup(response.text, 'html.parser')

#         info_list = soup.find_all('a', href=lambda href: href and 'artist' in href)

#         info = [item.text.strip() for item in info_list]

#         print(info)
        
#         return info[:num_info]
    
#     except Exception as e:
#         print(f"Error: {e}")
#         return []
#

def main():
    # url = "https://www.acclaimedmusic.net/year/alltime_songs.htm"
    # info = top_music_scrape(url)
    # print(info)

    url = "https://boardgamegeek.com/browse/boardgame"
    games = scrape_board_games(url)

    get_boardgame_rec("", games, 5)

if __name__ == "__main__":
    main()