import imp
from bs4 import BeautifulSoup, SoupStrainer
from bs4.element import Tag
import urllib.request
import requests
import os

with open("data_loc.html") as html:
    soup = BeautifulSoup(html)


def process_a_elem_write_file(a_elem: Tag, already_got_files: list[str]) -> None:
    GIMME_FILES = ["json", "csv", "zip", "xls", "docx", "txt", "kml", "xlsx"]
    href = a_elem["href"]
    file_name = get_file_name(href)

    if file_name not in already_got_files:
        if href.rsplit(".")[-1] in GIMME_FILES:
            resp = requests.get(href)
            with open(f"data/{file_name}", "wb") as file:
                file.write(resp.content)
            print(f"downloaded: {href}")


def get_file_name(href: str) -> str:
    href = href.replace("https://", "")
    href = href.replace(" ", "_")
    href = href.replace("/", "_")
    href = href.replace(".", "_", href.count(".") - 1)
    return href


if __name__ == "__main__":
    already_got_files = os.listdir("data")
    for a_elem in soup.find_all("a"):
        try:
            process_a_elem_write_file(a_elem, already_got_files)
        except:
            print(f"issue with: {a_elem}")
