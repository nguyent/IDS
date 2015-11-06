#!/usr/bin/env python

import pytest
from graph.twitter_hashtag_graph import *

@pytest.fixture(scope='function')
def single_hashtag_fixture():
    return {
        'text': 'sds#bar sds',
        'timestamp_ms': '1'
    }

@pytest.fixture(scope='function')
def two_hashtag_fixture():
    return {
        'text': 'sdsd#foo sdsds #bar',
        'timestamp_ms': '2'
    }


@pytest.fixture(scope='function')
def three_hashtag_fixture():
    return {
        'text': '#foo #bar #knee',
        'timestamp_ms': '3'
    }

test_tweets = [
    (single_hashtag_fixture(), []),
    (two_hashtag_fixture(), [('foo','bar')]),
    (three_hashtag_fixture(), [('foo','bar'),
                               ('foo','knee'),
                               ('bar','knee')])
]

@pytest.mark.parametrize("tweet, expected_edges", test_tweets)
def test_tweet_node(tweet, expected_edges):
    node = TweetNode(tweet)
    assert node.edge_list == expected_edges

def test_add_tweet():
    graph = TwitterHashtagGraph()
    graph.add_tweet(two_hashtag_fixture())
    graph.add_tweet(three_hashtag_fixture())
    assert graph.average == 2

@pytest.fixture(scope='function')
def really_old_tweet_fixture():
    return {
        'text': '#baz #bay',
        'timestamp_ms': '10000000'
    }

def test_remove_outdated():
    graph = TwitterHashtagGraph()
    graph.add_tweet(single_hashtag_fixture())

    graph.add_tweet(two_hashtag_fixture())
    assert len(graph.tweet_nodes) == 2

    graph.add_tweet(three_hashtag_fixture())
    assert len(graph.tweet_nodes) == 3

    graph.add_tweet(really_old_tweet_fixture())
    assert len(graph.tweet_nodes) == 1
