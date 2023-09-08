import requests
from bs4 import BeautifulSoup as bs


def main():
    url = "https://books.toscrape.com/"

    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    books = soup.findAll("article")

    results = []
    index_ = 0
    for book in books:
        index_ += 1
        index = str(index_)
        title = book.find("img")["alt"]
        price = book.find("p", class_="price_color").text[2:]
        result = {"index": index, "title": title, "price": price}
        results.append(result)
    return results


if __name__ == "__main__":
    main()
