#!/bin/bash

set -eu

cat oomph-trace | cut -d\; -f2,3,4,11 | tr -d '[];' > clean-trace
