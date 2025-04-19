import re
import typing

from DataReader import get_tweet_data

# PreProcessing steps

# Step 1 : Remove hyperlinks
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

    return tweet

def remove_hyperlinks(tweet):

    tweet = re.sub(pattern=r'https?://\S+',repl='',string=tweet)
    # \S+ means it matches one or more occurrence of any non whitespace characters
    # ? means the preceding character is optional.

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




