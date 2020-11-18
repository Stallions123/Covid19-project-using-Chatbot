import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data,ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    ##Splitting the data
    return data.iloc[train_indices],data.iloc[test_indices]


if __name__=="__main__":

    #Read the Data
    df = pd.read_csv('data.csv')
    train,test = data_split(df,0.2)
    X_train = train[['fever','bodypain','age','RunnyNose','DiffBreath']].to_numpy()
    X_test = test[['fever','bodypain','age','RunnyNose','DiffBreath']].to_numpy()
    
    Y_train = train[['Problem']].to_numpy()
    Y_test = train[['Problem']].to_numpy()

    clf = LogisticRegression()
    clf.fit(X_train,Y_train)

    #Open a file whhere you can store the data
    file = open('model.pkl','wb')

    #Dump Information to that file
    pickle.dump(clf,file)
    file.close()



