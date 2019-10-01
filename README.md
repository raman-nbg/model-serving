# Machine Learning end to end development

This repo contains a blueprint of the end to end process for the training, 
deployment and monitoring of machine learning models.

## Scenario
For the blueprint we will use the [Graduate Admission Dataset from Kaggle](https://www.kaggle.com/mohansacharya/graduate-admissions/downloads/graduate-admissions.zip/2). We want to create some models which should be served in parallel. Also we want to be able to monitor the model performance and hot plug new models and retire old models.

## Prerequisites
- Optional: Install PyCharm
- Install Anaconda
- Install Docker
- Install Docker-Compose (only on Linux)

## Training
### Build
```bash
cd training
conda env create -f environment.yml --prefix ./envs
conda activate ./envs
python setup.py [develop|install]
```

### Run
```bash
cd training
conda activate ./envs
run_training
```

The new model will be stored at `models/graduate-admissions/linear-regression-v1.pkl`

## Serving

### Setup
Start Kafka cluster including Zookeeper, Kafka REST Proxy, Schema Registry 
and Admin Web UIs. See 
[infrastructure/kafka/README.md](infrastructure/kafka/README.md) for details.

### Build
```bash
cd model-serving
conda env create -f environment.yml --prefix ./envs
conda activate ./envs
python setup.py [develop|install]
docker build -t model-server .
```

### Run
```bash
conda activate ./envs
docker run model-server
```

## Using Conda environment
Each subproject contains its own Conda environment file named `conda.yml`. You 
can apply the configuration using the following commands:
```bash
cd [subfolder]
conda env create -f environment.yml --prefix ./envs
conda activate ./[env-name]
```
You can find the name of the environment in the first line of the yaml file.

### Adding new dependencies
Just add the dependency to the `environment.yml` manually. Afterwards you
can import the new dependency using 
`conda env update -f environment.yml --prefix ./envs`
