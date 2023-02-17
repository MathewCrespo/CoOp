import os
for dataset in ['food101', 'ucf101', 'oxford_flowers', 'oxford_pets', 'fgvc_aircraft', 'stanford_cars', 'sun397']:
    for shot in [1,2,4,8,16]:
        cmd = 'python parse_test_res.py output/Proxy4/{}/PLOT/rn50_{}shots/nctx16_csc_ctpend'.format(dataset,shot)
        print(cmd)
        os.system(cmd)