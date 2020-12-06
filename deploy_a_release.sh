#!/bin/bash

echo "Building a new release of fmpsdk!"
echo
echo "Did you remember to run black???  e.g.  black fmpsdk --exclude \"venv|build\""
read -p "(y/n): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo
    echo "Did you remember to update the serial in setup.py?"
    read -p "(y/n): " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        echo
        echo "Clean up old build"
        rm -Rf build
        rm -Rf dist
        rm -Rf fmcapi.egg-info
        echo
        echo "Make a new build"
        python3 setup.py bdist_wheel
        python3 setup.py sdist
        twine upload dist/*
    fi
fi
