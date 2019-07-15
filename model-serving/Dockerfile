FROM continuumio/miniconda3
ADD src/model_serving/ .
ADD conda.yml /
RUN conda env create -f conda.yml python=3.7

# Pull the environment name out of the environment.yml
RUN echo "source activate model-server-env" > ~/.bashrc
ENV PATH /opt/conda/envs/model-server-env/bin:$PATH

CMD [ "python", "./model_server.py" ]