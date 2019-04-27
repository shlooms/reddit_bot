import praw
import config
import time
import os

def bot_login():
    print ("logging in...")
    r =  praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Alpaca test of an alpaca comment responder bot v0.1")
    print ("logged in.")

    return r


def run_bot(r, comments_replied_to):
    print ("obtaining comments")

    for comment in r.subreddit('test').comments(limit=25):
        if "alpaca" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print ("String with \"alpaca\" found " + comment.id)
            #comment.reply("alapacas are the best, llamas are the worst!")
            print ("replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print("sleeping for 10 seconds...")
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(r, comments_replied_to)
