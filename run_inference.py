import os

for dataset in ['eurosat','fgvc_aircraft','food101','oxford_flowers','oxford_pets','stanford_cars','sun397','ucf101']:  
    cmd = 'CUDA_VISIBLE_DEVICES=0 bash scripts/plot/base2new_test.sh {} rn50 end 16 16 4'.format(dataset)
    print(cmd)
    os.system(cmd)