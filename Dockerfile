FROM quay.io/jupyter/scipy-notebook:python-3.11

MAINTAINER Dave Tang <me@davetang.org>

RUN python -m pip install --upgrade pip \
    && pip install scanpy celltypist

WORKDIR /home/jovyan/work
