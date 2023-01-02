from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import requests

with open("data_loc.html") as html:
    soup = BeautifulSoup(html)


def process_a_elem_write_file(a_elem) -> None:
    GIMME_FILES = ["json", "csv", "zip", "xls", "docx", "txt", "kml", "xlsx"]
    href = a_elem["href"]
    if href.rsplit(".")[-1] in GIMME_FILES:
        resp = requests.get(href)
        open(f"data/{get_file_name(href)}", "w").write(resp.content.decode("utf8"))


def get_file_name(href: str) -> str:
    href = href.replace("https://", "")
    href = href.replace(" ", "_")
    href = href.replace("/", "_")
    href = href.replace(".", "_", href.count(".") - 1)
    return href


if __name__ == "__main__":
    for a_elem in soup.find_all("a"):
        process_a_elem_write_file(a_elem)
