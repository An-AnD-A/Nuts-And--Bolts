import matplotlib.pyplot as plt

from MachineLearning.Functions.DataReader import read_data

def plot_feature_scatter(df, feature_name):

    fig = plt.figure(figsize=(10,16))
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x=df[feature_name], y=df['SalePrice'])

    return plt.show()

if __name__ == '__main__':

    df = read_data(dataset='train')

    plot_feature_scatter(df=df, feature_name='LotArea')
