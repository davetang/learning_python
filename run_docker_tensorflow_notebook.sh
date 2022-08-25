#!/usr/bin/env bash

set -euo pipefail

# JupyterLab is now the default for all the Jupyter Docker stack images
# the latest version as of 2022-08-25 is
# 9c23551dec7e6c93d2363e8a17307d0a8bb847471e2b2fe959dd019daa370178, which
# keeps crashing when I try to start or open a new notebook, so I am using the
# older ubuntu-20.04 image
# version=latest
version=ubuntu-20.04
image=jupyter/tensorflow-notebook:${version}
container_name=tensorflow-notebook
port=10000

start_container () {

   # If you change the notebook username using the following:
   #
   #     -e NB_USER="my-username" \
   #
   # You will not be able to list currently running servers to obtain a token.
   # Therefore just use the username jovyan
   #
   # In addition, you need to run as root (`--user root`)
   # or else you will not be able to edit mounted files

   docker run -d \
      --rm \
      -p ${port}:8888 \
      --user root \
      -e NB_UID=$(id -u) \
      -e NB_GID=$(id -g) \
      -v $(pwd):/home/jovyan/work \
      --name ${container_name} \
      ${image}

   >&2 echo ${container_name} listening on port ${port}
   >&2 echo -e "Run the following to get the token:\ndocker exec ${container_name} jupyter server list"

}

check_container () {

   docker container inspect ${container_name} > /dev/null 2>&1
   # $? == 0 if container exists
   if [[ $? > 0 ]]; then
      start_container
   else
      >&2 echo ${container_name} already exists
      exit 1
   fi

}

# the || is necessary for preventing `set -e` immediately exiting
# if the container already exists
check_container || true

>&2 echo Done
exit 0

