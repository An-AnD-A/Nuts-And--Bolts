import nltk
from nltk.corpus import twitter_samples

def get_tweet_data(download=False):
    if download:
        nltk.download('twitter_samples',
                      download_dir=os.path.join(os.getcwd(),'Data'))

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    all_tweets = twitter_samples.strings()

    return  positive_tweets, negative_tweets, all_tweets