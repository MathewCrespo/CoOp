import os
#['food101', 'dtd', 'ucf101', 'oxford_flowers', 'oxford_pets', 'fgvc_aircraft', 'stanford_cars', 'sun397', 'eurosat'
'''
for dataset in ['eurosat','fgvc_aircraft','food101','oxford_flowers']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=0 bash scripts/plot/main.sh {} rn50 end 16 {} 4'.format(dataset,shot)
        print(cmd)
        os.system(cmd)

for dataset in ['eurosat','fgvc_aircraft','food101','oxford_flowers']:
    
    cmd = 'CUDA_VISIBLE_DEVICES=0 bash scripts/plot/base2new_train.sh {} rn50 end 16 16 4'.format(dataset)
    print(cmd)
    os.system(cmd)

for dataset in ['stanford_cars','sun397']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=0 bash scripts/plot/main_graph.sh {} rn50 end 16 {} 4 average '.format(dataset, shot)
        print(cmd)
        os.system(cmd)
'''
for data in ['oxford_pets','eurosat','food101']:
    for shot in [1,2,4,8,16]:
        cmd = 'CUDA_VISIBLE_DEVICES=5 bash scripts/plot/main_diverse_graph.sh {} rn50 end 16 {} 4 0.2'.format(data,shot)
        print(cmd)
        os.system(cmd)