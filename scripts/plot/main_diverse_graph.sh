#!/bin/bash

# custom config
DATA=./DATA
TRAINER=PLOT_Diverse_Graph

DATASET=$1
CFG=$2  # config file
CTP=$3  # class token position (end or middle)
NCTX=$4  # number of context tokens
SHOTS=$5  # number of shots (1, 2, 4, 8, 16)
N=$6  # number of proxy
alpha=$7

for SEED in 1 2 3
do
    DIR=output/PLOT_Diverse_Graph${alpha}/${DATASET}/${TRAINER}/${CFG}_${SHOTS}shots/nctx${NCTX}_csc${CSC}_ctp${CTP}/seed${SEED}
    if [ -d "$DIR" ]; then
        echo "Oops! The results exist at ${DIR} Resuming..."
        python train.py \
        --root ${DATA} \
        --seed ${SEED} \
        --trainer ${TRAINER} \
        --dataset-config-file configs/datasets/${DATASET}.yaml \
        --config-file configs/trainers/PLOT/${CFG}.yaml \
        --output-dir ${DIR} \
        --N 4 \
        MODEL.alpha ${alpha} \
        TRAINER.COOP.N_CTX ${NCTX} \
        TRAINER.COOP.CSC False \
        TRAINER.COOP.CLASS_TOKEN_POSITION ${CTP} \
        DATASET.NUM_SHOTS ${SHOTS}
    else
        echo "Run this job and save the output to ${DIR}"
        python train.py \
        --root ${DATA} \
        --seed ${SEED} \
        --trainer ${TRAINER} \
        --dataset-config-file configs/datasets/${DATASET}.yaml \
        --config-file configs/trainers/PLOT/${CFG}.yaml \
        --output-dir ${DIR} \
        --N 4 \
        MODEL.alpha ${alpha} \
        TRAINER.COOP.N_CTX ${NCTX} \
        TRAINER.COOP.CSC False \
        TRAINER.COOP.CLASS_TOKEN_POSITION ${CTP} \
        DATASET.NUM_SHOTS ${SHOTS}
    fi
done