#!/usr/bin/env python3
"""
This is a simple mastodon bot. It pretends to be
a mime and mirrors the (sentiment of the) toots
of a user.
"""
from textblob import TextBlob



data = TextBlob("great fun :)")

# polarity: [-1.0, 1.0] -> :( .. :)
if data.sentiment.polarity > 0.2:
    print(":)")
if data.sentiment.polarity < -0.2:
    print(":)")
# subjectivity: [0.0, 1.0] objective .. subjective
