FROM frolvlad/alpine-miniconda3:latest

COPY environment.yml ./

RUN conda env create -f environment.yml

RUN echo "source activate training" > ~/.bashrc
ENV PATH /opt/conda/envs/traiing/bin:$PATH
RUN conda config --add channels raman-nbg
RUN conda install model-serving-training

ENTRYPOINT ["run_training"]