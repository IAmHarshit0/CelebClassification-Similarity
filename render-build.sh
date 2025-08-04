#!/usr/bin/env bash
apt-get update && apt-get install -y cmake g++ make
pip install --upgrade pip
pip install -r requirements.txt
