#!/usr/bin/env bash

set -euo pipefail

# for debugging
# docker build --progress=plain -t davetang/scanpy:3.11 .

docker build -t davetang/scanpy:3.11 .

# docker login
# docker push davetang/mkdocs:${ver}
