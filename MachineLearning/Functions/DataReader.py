import os
import pandas as pd


def read_data(dataset='train'):

    if dataset=='train':
        path = os.path.abspath(os.path.join(os.getcwd(),'..','..','Data','RegressionData','train.csv'))
    elif dataset=='test':
        path = os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'Data', 'RegressionData', 'test.csv'))

    df = pd.read_csv(path)

    return df

if __name__ == '__main__':

    df = read_data(dataset='train')
    print(df.info)
    print(df.columns)