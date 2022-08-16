#!/usr/bin/env bash

set -euo pipefail

version=latest
image=jupyter/tensorflow-notebook:${version}
container_name=tensorflow-notebook
port=10000

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
   --name ${container_name} \
   --user root \
   -e NB_UID=$(id -u) \
   -e NB_GID=$(id -g) \
   -v $(pwd):/home/jovyan/work \
   ${image}

>&2 echo ${container_name} listening on port ${port}
>&2 echo -e "Run the following to get the token:\ndocker exec ${container_name} jupyter notebook list"

>&2 echo Done
exit 0

