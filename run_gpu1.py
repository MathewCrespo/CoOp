import os
#['food101', 'dtd', 'ucf101', 'oxford_flowers', 'oxford_pets', 'fgvc_aircraft', 'stanford_cars', 'sun397', 'eurosat'
'''
for dataset in ['oxford_pets','stanford_cars','sun397','ucf101']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=1 bash scripts/plot/main.sh {} rn50 end 16 {} 4'.format(dataset,shot)
        print(cmd)
        os.system(cmd)

for dataset in ['oxford_pets','stanford_cars','sun397','ucf101']:
    
    cmd = 'CUDA_VISIBLE_DEVICES=1 bash scripts/plot/base2new_train.sh {} rn50 end 16 16 4'.format(dataset)
    print(cmd)
    os.system(cmd)

for shot in [8,16]:
    cmd = 'CUDA_VISIBLE_DEVICES=1 bash scripts/plot/main_views.sh caltech101 rn50_views end 16 {} 4 4'.format(shot)
    print(cmd)
    os.system(cmd)

for dataset in ['dtd', 'ucf101', 'oxford_flowers', 'oxford_pets', 'fgvc_aircraft', 'stanford_cars', 'sun397', 'eurosat']:
    cmd = 'CUDA_VISIBLE_DEVICES=1 bash scripts/plot/main_graph_share.sh {} rn50 end 16 1 4'.format(dataset)
    print(cmd)
    os.system(cmd)
'''
for alpha in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=1 bash scripts/plot/main_graph_share_alpha.sh caltech101 rn50 end 16 {} 4 {}'.format(shot,alpha)
        print(cmd)
        os.system(cmd)