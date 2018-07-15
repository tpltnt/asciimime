#!/usr/bin/env python3
"""
This is a simple mastodon bot. It pretends to be
a mime and mirrors the (sentiment of the) toots
of a user.
"""
import argparse
from bs4 import BeautifulSoup
from mastodon import Mastodon, MastodonIllegalArgumentError
from textblob import TextBlob

def text_to_emoticon(txt):
    """
    Convert a given text to an (hopefully)
    appropriate emoticon.

    :param txt: text to evaluate
    :type txt: str
    :returns: str (may be empty)
    """
    data = TextBlob(txt)

    # polarity: [-1.0, 1.0] -> :( .. :)
    if data.sentiment.polarity < -0.2:
        return ":("

    if data.sentiment.polarity == 0.0 and data.sentiment.subjectivity == 0:
        return ":|"

    if data.sentiment.polarity > 0.2:
        return ":)"

    # subjectivity: [0.0, 1.0] objective .. subjective
    #print(data.sentiment.polarity)
    #print(data.sentiment.subjectivity)
    return ""


def register_app():
    """
    Register the bot.

    :note: run only once
    """
    Mastodon.create_app(
        'asciimimebot',
        api_base_url='https://botsin.space',
        to_file='asciimime_clientcred.secret'
    )


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='A mastodon bot')
    PARSER.add_argument('--username', type=str, help='user name to use')
    PARSER.add_argument('--password', type=str, help='password to use')
    PARSER.add_argument('--atoken', type=str, help='access token to use')
    PARSER.add_argument('--register', action='store_true',
                        help='register the app (only run once)')
    ARGS = PARSER.parse_args()

    if ARGS.register:
        register_app()
        exit(0)

    mastodon = Mastodon(
        access_token=ARGS.atoken,
        api_base_url='https://botsin.space'
    )
    try:
        acess_token = mastodon.log_in(username=ARGS.username,
                                      password=ARGS.password,
                                      scopes=['read', 'write'])
    except MastodonIllegalArgumentError:
        print("given username and/or password are invalid")
    for toot in mastodon.timeline('home'):
        soup = BeautifulSoup(toot['content'], 'html.parser')
        txt = soup.text.replace('&apos;', "'")
        mime_reply = text_to_emoticon(txt)
        if not mime_reply:
            continue
        if ':(' != mime_reply:
            tid = toot['id']  # toot id
            print("{0} (id: {1})".format(txt, tid))
            print(" -> {0}".format(mime_reply))
            print("")
            mastodon.status_post(mime_reply, in_reply_to_id=tid)
