import os
this_dir_path = 'G:/数据集/2-飞行器高阶信息数据集/飞机图片/'
json_index = 0
jpg_index = 0
for file in os. listdir(this_dir_path):
    file_path = os.path.join(this_dir_path, file)
    if os.path.splitext(file_path)[-1] == ".jpg":
        new_file_path = "."+"/".join((os.path.splitext(file_path)[0].split("\\"))[:-1]) + "/{:0>5}.jpg".format(jpg_index)
        jpg_index += 1
        print(file_path+'---->'+new_file_path)
        os.rename(file_path, new_file_path)
    elif os.path.splitext(file_path)[-1] == ".json":
        new_file_path = "."+"/".join((os.path.splitext(file_path)[0].split("\\"))[:-1]) + "/{:0>5}.json".format(json_index)
        json_index += 1
        print(file_path+'---->'+new_file_path)
        os.rename(file_path, new_file_path)
