#!/bin/zsh

mlx_lm.lora \
 --model mistralai/Mistral-7B-Instruct-v0.3 \
 --data ./data \
 --batch-size 1 \
 --lora-r 8 \
 --epochs 2