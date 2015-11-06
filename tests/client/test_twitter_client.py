#!/usr/bin/env python

import pytest
from inspect import isgeneratorfunction
from client.twitter_client import TwitterAPIClient

def test_valid_get_tweets():
    valid_test_tweets = 'tests/client/test_tweets.txt'
    valid_test_client = TwitterAPIClient(valid_test_tweets)
    assert isgeneratorfunction(valid_test_client.get_tweets)

    tweet_generator = valid_test_client.get_tweets()
    tweet = tweet_generator.next()
    assert type(tweet) == type({})

def test_invalid_get_tweets():
    invalid_test_tweets = 'tests/client/invalid_tweets.txt'
    invalid_test_client = TwitterAPIClient(invalid_test_tweets)

    tweet_generator = invalid_test_client.get_tweets()

    with pytest.raises(SystemExit):
        tweet_generator.next()
