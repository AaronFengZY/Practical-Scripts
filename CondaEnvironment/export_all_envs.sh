#!/usr/bin/env bash

env_names=("GoalAct" "amlt9" "arctic_env" "chatglm" "combinatorics" \
           "hamer" "hands23" "hocap-toolkit" "hoimoge" "manopth" \
           "nanoGPT" "opensora" "wilor")

for env in "${env_names[@]}"; do
    echo "Exporting conda environment: $env"
    conda env export --name "$env" > "${env}_environment.yml"
done
