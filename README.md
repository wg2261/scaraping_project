The scraper uncovers from the website "https://boardgamegeek.com/browse/boardgame" games and it's name, rank, rating, and 
url.
This website is used because it seems obscure enough and people may want to have board game recommendations.

To run this:
1. Git clone
2. pip install -r requirements.txt
3. Run either 
    url = "https://boardgamegeek.com/browse/boardgame"
    1. get_boardgame_rec(url, [], n)
        # n = amount of recommendations you want
        # For neatly printed game informations
    2. games = scrape_board_games(url)
        # For all the games and relevant information