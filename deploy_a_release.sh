#!/usr/bin/env bash

echo "Building a new release of fmpsdk!"
echo
echo "Did you remember to run black???  e.g.  black fmpsdk --exclude \"venv|build\""
read -p "(y/n): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo
    echo "Did you remember to update the serial in pyproject.toml?"
    read -p "(y/n): " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        echo
        echo "Building package via poetry"
        poetry build
        echo
        echo "Publishing package"
        poetry publish
    fi
fi
