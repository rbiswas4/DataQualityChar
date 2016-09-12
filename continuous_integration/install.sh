#!/usr/bin/env bash

# Build the install from scratch

## Obtain current path
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

## script to install conda pre-requisites
${DIR}/INSTALL_MINICONDAPACKAGES.sh --file conda_prerequisites
