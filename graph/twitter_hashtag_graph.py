#!/usr/bin/env python

MINUTE_IN_MS = 60000

class TwitterHashtagGraph:
    tweet_nodes = []
    average = 0

    def add_tweet(self, tweet):
        """Given a tweet, create a TweetNode and add it onto nodes if it has new edges, dequeuing outdated tweets"""
        node = TweetNode(tweet)

        if node.edge_list:
            self.tweet_nodes.append(node)
            self.remove_outdated_tweets()
            self.calculate_rolling_average()

    def remove_outdated_tweets(self):
        """Iterate over the nodes list, and remove entries that are > 60s from the last entry"""
        last_tweet_ms = self.tweet_nodes[-1].epoch

        for index, tweet in enumerate(self.tweet_nodes):
            time_difference = last_tweet_ms - tweet.epoch
            if time_difference <= MINUTE_IN_MS:
                self.tweet_nodes = self.tweet_nodes[index:]
                return

    def calculate_rolling_average(self):
        """Iterate over the nodes list, and find the degrees of all nodes divided by total # of nodes """
        hashtag_nodes = []
        edges = []

        for tweet_node in self.tweet_nodes:
            edges = edges + tweet_node.edge_list
            hashtag_nodes = hashtag_nodes + tweet_node.hashtags

        edges = list(TweetNode.dedupe(edges))
        hashtag_nodes = list(TweetNode.dedupe(hashtag_nodes))

        total_degrees = 0
        for hashtag_node in hashtag_nodes:
            for edge in edges:
                if hashtag_node in edge:
                    total_degrees = total_degrees + 1

        self.average = round(total_degrees / len(hashtag_nodes), 2)


import re
class TweetNode:
    def __init__(self, tweet):
        self.text = tweet['text']
        self.epoch = int(tweet['timestamp_ms'])
        self.edge_list = self.make_edge_list()

    def make_edge_list(self):
        """Given a tweet, normalize the hashtags and make a list of permutations between the hashtags"""

        all_hashtags = map(unicode.lower, re.findall(r"#(\w+)", self.text))
        unique_hashtags = list(TweetNode.dedupe(all_hashtags))
        self.hashtags = unique_hashtags

        out = []

        for index, hashtag in enumerate(unique_hashtags):
            for other_hashtag in unique_hashtags[index + 1:]:
                out.append((hashtag, other_hashtag))

        return out

    @staticmethod
    def dedupe(items):
        """Utility method via
        https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch01s10.html
        Useful for maintaining ordering for sane testing
        """
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)
