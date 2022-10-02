# Copyright (c) 2018-2022 curoky(cccuroky@gmail.com).
#
# This file is part of sidercar.
# See https://github.com/curoky/sidercar for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Refernce: https://github.com/apache/hadoop/blob/branch-3.3.1/hadoop-common-project/hadoop-common/src/main/conf/hadoop-env.sh

export HADOOP_OS_TYPE=${HADOOP_OS_TYPE:-$(uname -s)}

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

export HDFS_NAMENODE_USER=door
