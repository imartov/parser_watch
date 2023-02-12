import csv

import requests
from bs4 import BeautifulSoup
import json
import lxml
import os
from datetime import datetime


def get_all_pages():
    current_date = datetime.now().strftime("%d_%m_%Y")

    with open(f"info_watch_{current_date}.csv", "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (
                "title",
                "collection",
                "link"
            )
        )

    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    # }
    # url = "https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/"
    #
    #
    # r = requests.get(url=url, headers=headers, verify=False)
    #
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    #
    # with open(f"data/data_page_1.html", "w", encoding="utf-8") as file:
    #     file.write(r.text)
    #     file.close()

    with open("data/data_page_1.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_div_products = soup.find_all("div", {"class": "product-item carousel-item"})

    info_watch = []
    for item in all_div_products:
        href = "https://shop.casio.ru" + item.find("a", class_="product-item__link").get("href")
        title = item.find("img", class_="product-item__img").get("alt")
        collection = item.find("img", class_="product-item__brand-img").get("alt")

        info_watch.append(
            {
                "title": title,
                "collection": collection,
                "link": href
            }
        )

        with open(f"info_watch_{current_date}.csv", "a", encoding="utf-8=sig", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                (
                    title,
                    collection,
                    href
                )
            )

    with open(f"info_watch_{current_date}.json", "w", encoding="utf-8") as file:
        json.dump(info_watch, file, indent=4, ensure_ascii=False)
        file.close()


def main():
    get_all_pages()


if __name__ == "__main__":
    main()
