#!/bin/bash
set -e

# docs 目录及文件
mkdir -p docs
touch docs/system_design.md
touch docs/requirements.md
touch docs/mid_term_report.md

# client 目录及文件
mkdir -p client/src
touch client/src/main.py
touch client/src/config.py
mkdir -p client/tests
touch client/tests/test_client.py
touch client/Dockerfile
touch client/requirements.txt

# edge 目录及文件
mkdir -p edge/src
touch edge/src/server.py
touch edge/src/cache_manager.py
touch edge/src/config.py
mkdir -p edge/tests
touch edge/tests/test_edge.py
touch edge/Dockerfile
touch edge/requirements.txt

# data_center 目录及文件
mkdir -p data_center/src
touch data_center/src/server.py
touch data_center/src/data_manager.py
touch data_center/src/config.py
mkdir -p data_center/tests
touch data_center/tests/test_data_center.py
touch data_center/Dockerfile
touch data_center/requirements.txt

# common 目录及文件
mkdir -p common/utils
touch common/utils/logging_util.py
touch common/utils/network_util.py
mkdir -p common/models
touch common/models/caching_model.py
touch common/models/ml_model.py
mkdir -p common/config
touch common/config/default_config.yaml

# scripts 目录及文件
mkdir -p scripts
touch scripts/setup.sh
touch scripts/deploy.sh

# 根目录下其他文件
touch docker-compose.yml
touch README.md

echo "目录结构已在 $(pwd) 下生成。"
