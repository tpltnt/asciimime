#!/usr/bin/env python3
"""
This is a simple mastodon bot. It pretends to be
a mime and mirrors the (sentiment of the) toots
of a user.
"""
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
