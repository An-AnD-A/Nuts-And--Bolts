import pandas as pd

from Functions.DataReader import get_tweet_data

from Functions.Preprocessing import process_tweets, tokenize_tweet, stem_tokens

def token_corpus_check(token, freq_corpus):

    if token in freq_corpus:
        return True
    else:
        return False

def word_freq_builder(token, label, freq_corpus):


    if token_corpus_check(token=token, freq_corpus=freq_corpus) is True:
        freq_corpus[token][label] = freq_corpus[token][label] + 1
    else:
        freq_corpus[token] = {}
        freq_corpus[token]['Positive'] = 0
        freq_corpus[token]['Negative'] = 0

        freq_corpus[token][label] = freq_corpus[token][label] + 1

    return

def word_freq_corpus_builder():

    freq_corpus = dict()

    positive_tweets, negative_tweets, all_tweets = get_tweet_data()

    processed_positive_tweets = [stem_tokens(tokenize_tweet(process_tweets(tweet))) for tweet in positive_tweets]
    processed_negative_tweets = [stem_tokens(tokenize_tweet(process_tweets(tweet))) for tweet in negative_tweets]

    for tweet in processed_positive_tweets:
        for token in tweet:
            word_freq_builder(token=token, label='Positive', freq_corpus=freq_corpus)

    for tweet in processed_negative_tweets:
        for token in tweet:
            word_freq_builder(token=token, label='Negative', freq_corpus=freq_corpus)

    return freq_corpus

def tweet_preprocessing(tweet):

    processed_tweet = stem_tokens(tokenize_tweet(process_tweets(tweet)))

    return processed_tweet

def compute_features(tweet,
                     freq_corpus,
                     process_tweet=True):
    # Function for feature reduction for a single tweet
    if process_tweet:
        processed_tweet = tweet_preprocessing(tweet)
    else:
        processed_tweet = tweet

    n_positive_token_weight = [freq_corpus[word]['Positive'] for word in processed_tweet]
    n_negative_token_weight = [freq_corpus[word]['Negative'] for word in processed_tweet]

    n_positive_sum = sum(n_positive_token_weight)
    n_negative_sum = sum(n_negative_token_weight)

    tweet_feature = [1, n_positive_sum, n_negative_sum]

    return tweet_feature

def word_freq_df(freq_corpus):

    df = pd.DataFrame.from_dict(freq_corpus, orient='index').reset_index()
    df.rename(columns={'index': 'Word'}, inplace=True)
    return df



if __name__ == '__main__':

    freq_corpus = word_freq_corpus_builder()

    print(freq_corpus)
    positive_tweets, negative_tweets, all_tweets = get_tweet_data()

    print(f'{all_tweets[1]} : {compute_features(all_tweets[1], freq_corpus=freq_corpus)}')

    df = word_freq_df(freq_corpus)
    print(df)