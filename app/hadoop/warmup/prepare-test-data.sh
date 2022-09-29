#!/usr/bin/env bash
set -xeuo pipefail

/opt/hadoop/bin/hadoop fs -put /opt/hadoop/LICENSE.txt /LICENSE.txt
