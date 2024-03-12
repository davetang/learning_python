#!/usr/bin/env bash

set -euo pipefail

docker build -t davetang/scanpy:3.11 .

# docker login
# docker push davetang/mkdocs:${ver}
