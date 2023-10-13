#!/bin/bash

echo '{"registry-mirrors": ["https://quay.io/"]}' | sudo tee -a /etc/docker/daemon.json
sudo systemctl reload docker
