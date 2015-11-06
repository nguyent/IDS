#!/usr/bin/env python

import argparse
from parser.tweet_parser import TweetParser
from client.twitter_client import TwitterAPIClient

def main():
    args = parse_args()
    client = TwitterAPIClient(args.input)
    tweet_generator = client.get_tweets()

    output_file = open(args.output,'w')
    for tweet in tweet_generator:
        cleaned_tweet = TweetParser.clean_tweet(tweet)
        output_file.write("%s (timestamp: %s)\n" % (cleaned_tweet, tweet['created_at']))

    output_file.write("\n%d tweets contained unicode.\n" % TweetParser.unicode_count)
    output_file.close()

def parse_args():
    desc = "Read a file of Tweets and output cleaned tweets, timestamps and # of tweets with unicode"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input', type=str, help='path to tweets file')
    parser.add_argument('output', type=str, help='path to output file')

    return parser.parse_args()

if __name__ == '__main__':
    main()
