from MachineLearning.Functions.DataReader import read_data


def get_sample_data(sample_size=0.1):

    df = read_data(dataset='train')

    df_sample = df.sample(frac=sample_size, random_state=42)

    return df_sample

def get_training_example(j,
                         df_train,
                         np_array=False):

    training_ex_j = df_train.iloc[j]

    j_array = training_ex_j.to_numpy()

    if np_array:
        return j_array
    else:
        return training_ex_j


if __name__ == '__main__':

    df = get_sample_data(sample_size=0.01)

    j_element = get_training_example(j=2, df_train=df, np_array=True)

    print(j_element)
    print(type(j_element))
