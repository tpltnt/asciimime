#!/usr/bin/env python3
"""
This is a simple mastodon bot. It pretends to be
a mime and mirrors the (sentiment of the) toots
of a user.
"""
import argparse
from mastodon import Mastodon
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

    if data.sentiment.polarity > 0.2:
        return ":)"

    # subjectivity: [0.0, 1.0] objective .. subjective
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
    PARSER.add_argument('--register', action='store_true',
                        help='register the app (only run once)')
    ARGS = PARSER.parse_args()

    if ARGS.register:
        register_app()
        exit(0)

    acess_token = Mastodon.log_in(username=ARGS.username,
                                  password=ARGS.password)
