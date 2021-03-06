# Multiple Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("50_Startups.csv")

x = dataset.iloc[:,:4].values
y = dataset.iloc[:,4].values


# Encoding categorical data and also implementing dummy vairiable

# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))



# Avoiding Dummy Vairiable Trap
# We know that there are dummy vairiable column at index 0,1,2 to avoid dummy trap we need to remove any on eof the dummy vairiable column hence we are removing the column 0
# Although the linear regression take care of the dummy trap so we dont need to this manually but we did it to remind our self about dummy variable trap 
x = x[:,1:]


# We dont need to take care of the feature scaling manually as the liberary is taking care of it automatically.


# Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)



# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)



# Predicting the Test set result
y_pred = regressor.predict(x_test)



# This model is trained using ALL-IN Method hence its not so accurate
# This model is not the most optimal we can make it more accurate by using the BACKWARD ELIMNATION METHOD.
