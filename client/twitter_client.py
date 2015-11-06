#!/usr/bin/env python
import json
import sys

class TwitterAPIClient:
    def __init__(self, tweets_file):
        self.tweets_file = tweets_file

    def get_tweets(self):
        """given a file one tweet per line return a generator of serialized tweets"""
        with open(self.tweets_file, 'r') as tweets:
            for tweet in tweets:
                try:
                    yield json.loads(tweet)
                except:
                    sys.exit("File has malformed JSON")
