import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import logging
import os

inputDataset = "./../data/graduate-admissions/Admission_Predict_Ver1.1.csv"
modelTargetFile = "./../models/graduate-admissions/linear-regression-v1.pkl"

logger = logging.getLogger("training.graduate-admission-training")
logger.info("Starting training for graduate admissions with Linear Regression")

logger.info(f'Reading dataset from {inputDataset}')
df = pd.read_csv(inputDataset)
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

logger.info("Splitting dataset into training and test set with a test size of 0.2")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

logger.info("Fitting model with training dataset")
regressor = LinearRegression()
regressor.fit(x_train, y_train)

logger.info("Calculating score with test dataset")
score = regressor.score(x_test, y_test)

logger.info(f'Model accuracy score = {score}')

os.makedirs(os.path.dirname(modelTargetFile), exist_ok=True)
with open(modelTargetFile, 'xb') as file:
    pickle.dump(regressor, file)
