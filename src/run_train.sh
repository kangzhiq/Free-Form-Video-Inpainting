#!/bin/bash

export TORCH_HOME=/mnt2/download
python train.py --config config.json --dataset_config dataset_configs/forensics_all_masks.json