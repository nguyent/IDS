#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from parser.tweet_parser import TweetParser

test_tweets = [
    ({'text': u'a clean tweet'}, 'a clean tweet', 0),
    ({'text': u'uñicode tweet'}, 'uicode tweet', 1),
    ({'text': u'\'tweet\twith \"escape\nchars'}, """'tweet with "escape chars""", 1)
]

@pytest.mark.parametrize("tweet, expected_text, expected_unicode_count", test_tweets)
def test_clean_tweet(tweet, expected_text, expected_unicode_count):
    assert TweetParser.clean_tweet(tweet) == expected_text
    assert TweetParser.unicode_count == expected_unicode_count
