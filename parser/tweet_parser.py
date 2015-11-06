#!/usr/bin/env python

import string

class TweetParser:
    VALID_ASCII_CHARACTERS = string.digits + string.ascii_letters + string.punctuation + ' '
    unicode_count = 0

    @staticmethod
    def escape_replace(text):
        """Replace escape characters per the FAQ on Github"""
        remap = {
            ord('\t') : u' ',
            ord('\n') : u' '
        }
        return text.translate(remap)

    @staticmethod
    def clean_tweet(tweet):
        """Given a tweet return the contents of the text key with unicode stripped"""
        raw_tweet = tweet['text']
        escape_replaced_tweet = TweetParser.escape_replace(raw_tweet)
        filtered_tweet = escape_replaced_tweet.encode('ascii','ignore')

        if filtered_tweet != escape_replaced_tweet:
            TweetParser.unicode_count = TweetParser.unicode_count + 1

        return filtered_tweet
