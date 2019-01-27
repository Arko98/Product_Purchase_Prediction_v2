
def load_data():
    #Loading Data
    import pandas as pd
    import numpy as np
    df = pd.read_csv("Data.csv")

    #Converting to Categorical encoding
    df["job"] = df["job"].astype('category')
    df["marital"] = df["marital"].astype('category')
    df["education"] = df["education"].astype('category')
    df["default"] = df["default"].astype('category')
    df["housing"] = df["housing"].astype('category')
    df["loan"] = df["loan"].astype('category')
    df["contact"] = df["contact"].astype('category')
    df["month"] = df["month"].astype('category')
    df["day_of_week"] = df["day_of_week"].astype('category')
    df["poutcome"] = df["poutcome"].astype('category')
    df["y"] = df["y"].astype('category')
    
    df["job"] = df["job"].cat.codes
    df["marital"] = df["marital"].cat.codes
    df["education"] = df["education"].cat.codes
    df["default"] = df["default"].cat.codes
    df["housing"] = df["housing"].cat.codes
    df["loan"] = df["loan"].cat.codes
    df["contact"] = df["contact"].cat.codes
    df["month"] = df["month"].cat.codes
    df["day_of_week"] = df["day_of_week"].cat.codes
    df["poutcome"] = df["poutcome"].cat.codes
    df["y"] = df["y"].cat.codes
        
    #Changing the features to suitable datatype
    df["job"] = df["job"].astype('int64')
    df["marital"] = df["marital"].astype('int64')
    df["education"] = df["education"].astype('int64')
    df["default"] = df["default"].astype('int64')
    df["housing"] = df["housing"].astype('int64')
    df["loan"] = df["loan"].astype('int64')
    df["contact"] = df["contact"].astype('int64')
    df["month"] = df["month"].astype('int64')
    df["day_of_week"] = df["day_of_week"].astype('int64')
    df["poutcome"] = df["poutcome"].astype('int64')
    df["age"] = df["age"].astype('int64')
    df["duration"] = df["duration"].astype('float64')
    df["pdays"] = df["pdays"].astype('float64')
    df["previous"] = df["previous"].astype('float64')
    df["emp.var.rate"] = df["emp.var.rate"].astype('float64')
    df["cons.price.idx"] = df["cons.price.idx"].astype('float64')
    df["euribor3m"] = df["euribor3m"].astype('float64')
    df["nr.employed"] = df["nr.employed"].astype('float64')
    df["y"] = df["y"].astype('int64')
    
    #Converting Dataframe to Numpy array
    data = np.array(df)
    
    #Splitting Data into input and labels
    inputs = data[:,0:19]
    
    #Filling null values with mean and Scaling Labels
    labels = np.reshape(np.nan_to_num(data[:,20],copy = False),(data.shape[0],1))

    return inputs,labels 
