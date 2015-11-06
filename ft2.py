#!/usr/bin/env python

import argparse
from graph.twitter_hashtag_graph import TwitterHashtagGraph
from client.twitter_client import TwitterAPIClient

def main():
    args = parse_args()
    client = TwitterAPIClient(args.input)
    tweet_generator = client.get_tweets()
    graph = TwitterHashtagGraph()

    output_file = open(args.output,'w')

    for tweet in tweet_generator:
        graph.add_tweet(tweet)
        output_file.write("%s\n" % graph.average)

    output_file.close()

def parse_args():
    desc = "Read a file of Tweets and output the rolling average for each tweet"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input', type=str, help='path to tweets file')
    parser.add_argument('output', type=str, help='path to output file')

    return parser.parse_args()

if __name__ == '__main__':
    main()
