import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import logging
import os
from pathlib import Path
from . import config


def main():
    input_dataset = config.get("input-dataset")
    model_target_file = config.get("output-model-file")

    logger = logging.getLogger("training.graduate-admission-training")
    logger.info("Starting training for graduate admissions with Linear Regression")

    logger.info(f'Reading dataset from {input_dataset}')
    df = pd.read_csv(input_dataset)
    x = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    logger.info("Splitting dataset into training and test set with a test size of 0.2")
    test_size = config.get("training.test-size")
    random_state = config.get("training.random-state")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)

    logger.info("Fitting model with training dataset")
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    logger.info("Calculating score with test dataset")
    score = regressor.score(x_test, y_test)

    logger.info(f'Model accuracy score = {score}')

    path = Path(os.path.dirname(model_target_file))
    path.mkdir(parents=True, exist_ok=True)
    with open(model_target_file, 'wb') as file:
        pickle.dump(regressor, file)
