# Training

## Run
```bash
cd training
conda activate ./envs
run_training
```

The new model will be stored at `models/graduate-admissions/linear-regression-v1.pkl`

## Development
### Run local without docker
First setup your environment
```bash
cd training
conda env create -f environment.yml --prefix ./envs
conda activate ./envs
python setup.py develop
```

### Deploy
```bash
python setup.py bdist_wheel
```