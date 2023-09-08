import requests
from bs4 import BeautifulSoup as bs
from domain.book import Book
from get_datas import main


books = main()

results = []
for item in books:
    data = Book(item["index"], item["title"], item["price"])
    # print(data)
    results.append(data)
    # print(item)

for _ in results:
    print(_)
    with open("repo.json", "a") as f:
        f.write(str(_))
