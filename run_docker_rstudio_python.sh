#!/usr/bin/env bash

set -euo pipefail

version=4.2.0
image=davetang/rstudio_python:${version}
container_name=$(whoami)_rstudio_python
port=8128

docker run \
   --rm \
   -d \
   -p ${port}:8787 \
   --name ${container_name} \
   -e PASSWORD=password \
   -e USERID=$(id -u) \
   -e GROUPID=$(id -g) \
   -v $(pwd):/home/rstudio/share \
   ${image}

>&2 echo ${container_name} listening on port ${port}

>&2 echo Done
exit 0

