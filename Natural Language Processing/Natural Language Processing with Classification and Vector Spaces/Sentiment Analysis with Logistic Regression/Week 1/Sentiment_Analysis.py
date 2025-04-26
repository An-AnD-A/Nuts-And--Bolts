import os
import nltk
from nltk.corpus import twitter_samples

from Functions.DataReader import get_tweet_data
from Functions.FeatureEngineering import (word_freq_corpus_builder,
                                          compute_features,
                                          stem_tokens,
                                          tokenize_tweet,
                                          process_tweets)

def main():
    positive_tweets, negative_tweets, all_tweets = get_tweet_data()

    # create corpus
    freq_corpus = word_freq_corpus_builder()

    tweets = [tweet for tweet in all_tweets if tweet not in set(positive_tweets+negative_tweets)]

    feature_vector = []

    for tweet in tweets:

        processed_tweet = stem_tokens(tokenize_tweet(process_tweets(tweet)))
        filtered_tweet = [word for word in processed_tweet if word in freq_corpus.keys()]

        tweet_vector = compute_features(tweet=filtered_tweet ,
                                        freq_corpus=freq_corpus,
                                        process_tweet=False)


        feature_vector.append(tweet_vector)

    return feature_vector

if __name__ == '__main__':

    feat_vector = main()




