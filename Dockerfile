FROM quay.io/jupyter/scipy-notebook:python-3.11

# PRETTY_NAME="Ubuntu 22.04.4 LTS"
# NAME="Ubuntu"
# VERSION_ID="22.04"
# VERSION="22.04.4 LTS (Jammy Jellyfish)"
# VERSION_CODENAME=jammy
# ID=ubuntu
# ID_LIKE=debian
# HOME_URL="https://www.ubuntu.com/"
# SUPPORT_URL="https://help.ubuntu.com/"
# BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
# PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
# UBUNTU_CODENAME=jammy

MAINTAINER Dave Tang <me@davetang.org>

RUN python -m pip install --upgrade pip \
    && pip install scanpy celltypist

USER root
RUN printf "deb https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/\n" >> /etc/apt/sources.list
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
RUN apt-get clean all && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y r-base && \
    apt-get clean all && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/jovyan/work
