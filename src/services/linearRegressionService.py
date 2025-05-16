import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def train_linear_regression(df: pd.DataFrame):
    df = df.drop(columns=["id_turma"])
    df = pd.get_dummies(df, columns=['area_relacionada'])
    print(df.head())
    #print(df.corr())
    #X = df.drop(columns=["taxa_aprovacao","id_turma"])
    #Y = df["taxa_aprovacao"]

    #X = pd.get_dummies(X)

    #model = LinearRegression()
    #model.fit(X, Y)

    #y_pred = model.predict(X)

    #print(X)