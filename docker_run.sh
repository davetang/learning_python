#!/usr/bin/env bash

set -euo pipefail

version=latest
image=jupyter/tensorflow-notebook:${version}
container_name=tensorflow-notebook
port=10000

docker run -d \
   --rm \
   -p ${port}:8888 \
   --name ${container_name} \
   -v $(pwd):/data \
   ${image}

>&2 echo ${container_name} listening on port ${port}
>&2 echo Run the following to get the token: docker exec ${container_name} jupyter notebook list

>&2 echo Done
exit 0

