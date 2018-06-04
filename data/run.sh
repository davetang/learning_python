#!/bin/bash

R --vanilla --quiet -e 'write.csv(iris, "iris.csv", quote = FALSE, row.names = FALSE)'

