import os
'''
for dataset in ['ucf101','dtd']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=2 bash scripts/plot/main_graph.sh {} rn50 end 16 {} 4 average '.format(dataset, shot)
        print(cmd)
        os.system(cmd)
'''
for data in ['food101']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=0 bash scripts/plot/main_graph_share.sh {} rn50 end 16 {} 4'.format(data,shot)
        print(cmd)
        os.system(cmd)