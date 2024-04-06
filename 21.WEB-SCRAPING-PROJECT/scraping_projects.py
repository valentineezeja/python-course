# http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Now scraping {BASE_URL}{url}.....")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "biolink": quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(1)

    return all_quotes

# # Write the scraped data to a file
# with open("scraped_quotes.txt", "w", encoding="utf-8") as file:
#     for quote in all_quotes:
#         file.write(f"Text: {quote['text']}\n")
#         file.write(f"Author: {quote['author']}\n")
#         file.write(f"Bio link: {BASE_URL}{quote['biolink']}\n")
#         file.write("\n")

def start_game(quotes):
    quote = choice(quotes)
    remaining_quesses = 4
    print("Here is a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower and remaining_quesses > 0:
        guess = input(f"who said this quote? Guesses remaining: {remaining_quesses} \n")
        remaining_quesses -= 1
        if guess == quote["author"]:
            print("That's correct, my boy!!!")
            break
        if remaining_quesses == 3:
            res = requests.get(f"{BASE_URL}{quote['biolink']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here is a hint: The author was born on {birth_date} at {birth_place}")
        elif remaining_quesses == 2:
            print(f"Here is a hint: The author's first name starts with {quote['author'][0]}")
        elif remaining_quesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with {last_initial} ")
        else:
            print(f"sorry, you run out of guesses, the answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        print("OK you play again!")
        return start_game(quotes)
    else:
        print("Okay, goodbye")

quotes = scrape_quotes()
start_game(quotes)