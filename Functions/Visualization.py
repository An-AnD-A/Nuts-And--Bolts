import matplotlib.pyplot as plt
import numpy as np

from Functions.FeatureEngineering import word_freq_df,word_freq_corpus_builder



def tweet_feature_visualizer(df):
    """

    Improvements
    ------------
    - Why are there negative values? - expected dehaviour
    -
    :param df:
    :return:
    """

    epsilon = 1e-6

    df['log_positive'] = np.log(df['Positive']+epsilon)
    df['log_negative'] = np.log(df['Negative'] + epsilon)

    plt.figure(figsize=(10,15))


    for i, row in df.iterrows():

        if (row['Positive'] > 100 & row['Negative'] > 10) | (row['Negative'] > 500 & row['Positive'] > 10):
            plt.scatter(row['log_positive'], row['log_negative'])
            plt.text(row['log_positive']+0.01,row['log_negative']+0.01, row['Word'], fontsize=9)

    plt.plot([3,9],[3,9], color='red')

    plt.xlabel('Log Positive count')
    plt.ylabel('Log Negative count')
    plt.title(' Visualizing Word Corpus')
    plt.show()

    return

if __name__ == '__main__':

    tweet_feature_visualizer(word_freq_df(word_freq_corpus_builder()))




