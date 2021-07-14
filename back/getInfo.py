from commentScrape import read_from_txt
from commentScrape import scrape_comment, parse_comment
from random import choice
from hentai import Hentai, Format

import re

def read_from_txt(txt) -> list:
    the_file = open(txt, "r")
    content = the_file.read()
    content_list = content.split("\n")
    content_list = content_list[:-1] #remove empty line at end
    return content_list

def get_url():
    """
    comment = scrape_comment()
    the_numbers = parse_comment(comment)
    print(f"Random Holy Link: {choice(the_numbers)}")
    """
    the_numbers = read_from_txt("./back/the_numbers.txt")
    #print(f"Random Wholesome Link: {choice(the_numbers)}")
    return choice(the_numbers)

def get_number(url):
    number = re.findall('[^/]+$', url)
    number = int(number[0])
    #print(number)
    return number

def get_doujin(num):
    doujin = Hentai(num)
    title = doujin.title(Format.Pretty)
    artists = [artist.name for artist in doujin.artist]
    tags = [tag.name for tag in doujin.tag]
    cover = doujin.image_urls[0]
    return {"title": title,
            "artists": artists,
            "cover":cover,
            "tags": tags}

if __name__ == "__main__":
    print(get_doujin(get_number(get_url())))