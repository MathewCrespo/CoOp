import os
for dataset in ['food101','oxford_flowers']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=1 bash scripts/plot/main_graph.sh {} rn50 end 16 {} 4 average '.format(dataset, shot)
        print(cmd)
        os.system(cmd)