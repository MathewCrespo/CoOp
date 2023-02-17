import os
for data in ['caltech101','eurosat','fgvc_aircraft']:
    for shot in [2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=3 bash scripts/plot/main_graph_share.sh {} rn50 end 16 {} 4'.format(data,shot)
        print(cmd)
        os.system(cmd)