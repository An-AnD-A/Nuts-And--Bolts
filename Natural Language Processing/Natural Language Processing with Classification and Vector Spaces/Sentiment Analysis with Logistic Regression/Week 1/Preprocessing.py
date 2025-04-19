import re
import string
import typing
import nltk

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from DataReader import get_tweet_data

# PreProcessing steps

# Step 1 : tweet specific preprocessing - done
# Step 2 : Tokenize
# Step 3 : Remove stop words and punctuations
# Step 4 : Stemming and lowercase


def remove_handles(tweet):
    """
    Function to process tweets and remove handle names from the tweet.

    :param tweet: Unprocessed Tweet
    :return: Processed tweet with the handles removed
    """
    # Remove handles

    # Attempt 1 : Can remove anything that starts with @, But this breaks email address
    # tweet = re.sub(r'@\w+',repl='', string=tweet)
    # starts with @, follows by (a-z), (A-Z), [0-9], _ and + means one or more occurrence

    # Attempt 2 : Use a negative look behind
    tweet = re.sub(pattern=r'(?<!\w)@\w+',repl='',string=tweet)
    # Negative lookbehind - (?<!...)

    # Negated charater class - [^...] eg: [^\s]+ everything except the whitespace characters (\s captures all whitespace character

    return tweet

def remove_retweet_syntax(tweet):

    tweet = re.sub(pattern=r'^RT[\s]+', repl='', string=tweet)

    return tweet

def remove_hashtag(tweet):
    """
    Function to remove hashtag from a tweet.

    Improvements
    ------------
    - is there a better way to deal with hashtags?
    :param tweet: Tweet with hashtags
    :return: Processed tweet
    """

    tweet = re.sub(pattern=r'#', repl='', string=tweet)

    return tweet


def remove_hyperlinks(tweet):

    tweet = re.sub(pattern=r'https?://\S+',repl='',string=tweet)
    # \S+ means it matches one or more occurrence of any non whitespace characters
    # ? means the preceding character is optional.

    return tweet

def tokenize_tweet(tweet):
    """
    Function to tokenize tweets and remove stopwords and punctuations.

    Improvements
    ------------
    - refine the method to handle stopwords and punctuations.

    :param tweet:
    :return:
    """

    tweet_tokenizer = TweetTokenizer(preserve_case=True,
                                     reduce_len=False,
                                     strip_handles=False,
                                     match_phone_numbers=False)

    tweet_token = tweet_tokenizer.tokenize(tweet)

    tweet_token = list(set(tweet_token).difference(set(stopwords.words('english'))))

    tweet_token = list(set(tweet_token).difference(set(string.punctuation)))

    return tweet_token

def stem_tokens(tweet_token):

    stemmed_token = [PorterStemmer().stem(word) for word in tweet_token]

    return stemmed_token



def process_tweets(tweet,
                   process_handles=True,
                   process_hyperlinks=True,
                   process_hashtags=True,
                   process_retweets=True,
                   ):

    if process_handles:
        tweet = remove_handles(tweet)

    if process_hyperlinks:
        tweet = remove_hyperlinks(tweet)

    if process_hashtags:
        tweet = remove_hashtag(tweet)

    if process_retweets:
        tweet = remove_retweet_syntax(tweet)

    return tweet

def build_word_freq(text : str, label : str):
    """
    Function to count the frequency of word occurrence
    :param text:
    :param label:
    :return:
    """
    word_freq = {}
    for word in text.split(' '):
        if word in word_freq:
            word_freq[word] = word_freq[word]+1
        else:
            word_freq[word] = 1

    return word_freq


if __name__ == '__main__':

    positive_tweet, negative_tweet, all_tweet = get_tweet_data()

    # find all tweet with a handle.

    tweet_with_handle = [tweet for tweet in all_tweet if re.search('@\w+', tweet)]

    tweet_without_handles = {proc_tweet : remove_handles(proc_tweet) for proc_tweet in tweet_with_handle}

    for k, v in list(tweet_without_handles.items())[:3]:

        print('Tweet Preprocessing : Removing handles')
        print(f'{k}:{v}\n')

    tweet_with_hyperlinks = [tweet for tweet in all_tweet if re.search('https?://\S+', tweet)]

    tweet_without_hyperlinks = {proc_tweet: remove_hyperlinks(proc_tweet) for proc_tweet in tweet_with_hyperlinks}

    for k, v in list(tweet_without_hyperlinks.items())[:3]:
        print('Tweet Preprocessing : Removing hyperlinks')
        print(f'{k}: {v}\n')

    tweet_token = {tweet : tokenize_tweet(process_tweets(tweet)) for tweet in all_tweet}

    for k, v in list(tweet_token.items())[:3]:
        print('Tweet Preprocessing : Tweet processed and tokenized')
        print(f'{k}: {v}\n')

    stemmed_token = {tweet: stem_tokens(tweet_token[tweet]) for tweet in all_tweet}
    for k, v in list(stemmed_token.items())[:3]:
        print('Tweet Preprocessing : Tweet token stemmed')
        print(f'{k}: {v}\n')



