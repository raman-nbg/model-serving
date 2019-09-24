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
```bash
# create the conda environment with all dependencies
conda env create -f training/conda.yml

# run training script
python training/graduate_admission_training.py
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
docker build -t model-server .
```

### Run
```bash
docker run model-server
```

## Using Conda environment
Each subproject contains its own Conda environment file named `conda.yml`. You 
can apply the configuration using the following commands:
```bash
conda env create -f [subfolder]/conda.yml
conda activate [env-name]
```
You can find the name of the environment in the first line of the yaml file.

### Adding new dependencies
Just install the dependency using Conda. After that you have to export the changed
configuration to the yaml file using `conda env export > conda.yml`.

### Adding pip dependencies
If you want to add dependencies using pip you must not use your global pip installation.
Instead use pip from your activated conda environment.
```bash
cd /anaconda3/envs/[active-env-name]/bin
./pip install [dependency]
```
