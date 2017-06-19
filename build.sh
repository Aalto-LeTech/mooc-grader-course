#!/bin/bash

# Upgrade submodules (a-plus-rst-tools)
git submodule init
git submodule update

# Touch *.rst to force re-compilation
make touchrst

# Compile to html
make html

