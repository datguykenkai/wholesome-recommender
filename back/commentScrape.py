import praw
import re

def scrape_comment():
    reddit = praw.Reddit(
        user_agent="scraper",
        client_id="f-uJxcOqKLrt3iGYcHM4SA",
        client_secret="O1I0RCSlX-muoU-l6sSmd2vesccAlQ"
    )

    url = "https://www.reddit.com/r/nhentai/comments/inksnf/wholesome_hentai_list/"

    submission = reddit.submission(url=url)

    comment = submission.comments[1].body

    return comment

def parse_comment(comment):
    arr = comment.split("\r\n")

    filter_empty = [x for x in arr if x != '']

    num_list = []

    for x in filter_empty: 
        after_space = re.findall('(?<=\s).*', x)
        num_list.append(after_space[0])

    return num_list

def save_to_txt(the_numbers) -> None:
    with open('the_numbers.txt', 'w') as f:
        for item in the_numbers:
            f.write("%s\n" % item)

def read_from_txt(txt) -> list:
    the_file = open(txt, "r")
    content = the_file.read()
    content_list = content.split("\n")
    content_list = content_list[:-1] #remove empty line at end
    return content_list