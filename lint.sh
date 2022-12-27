#!/bin/bash

if [[ $1 = "fix" ]]; then
    black --exclude "migrations/" src/
fi
black --exclude "migrations/" --check --diff src/
flake8 src/
