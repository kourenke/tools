# import os
# import shutil
#
# # 假设txt_file_path是包含图片序号的.txt文件的路径
# txt_file_path = 'G:\挑战赛\Dataset-mask_6_30\最新数据集idx/V5_train.txt'
#
# # 假设source_dir是包含图片的源文件夹的路径
# source_dir = 'G:\挑战赛\Dataset-mask_6_30/mask'
#
# # 假设target_dir是目标文件夹的路径，用于存储复制的图片
# target_dir = 'G:\挑战赛\Dataset-mask_6_30\最新数据集idx/V5_train_mask'
#
# # 如果目标文件夹不存在，则创建它
# if not os.path.exists(target_dir):
#     os.makedirs(target_dir)
#
# # 读取.txt文件并获取序号列表
# with open(txt_file_path, 'r') as file:
#     image_numbers = [line.strip() for line in file]
#
# # 遍历源文件夹中的图片
# for filename in os.listdir(source_dir):
#     # 检查文件名是否包含.txt文件中的序号
#     for number in image_numbers:
#         if number in filename:
#             # 构建源文件的完整路径
#             source_file_path = os.path.join(source_dir, filename)
#             # 构建目标文件的完整路径
#             target_file_path = os.path.join(target_dir, filename)
#             # 复制文件
#             shutil.copy2(source_file_path, target_file_path)
#             print(f"Copied {source_file_path} to {target_file_path}")
#             # 如果你只想复制一次，可以在找到匹配项后跳出内部循环
#             break

import os
def get_image_names(folder_path):
    image_names = []
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否为图片
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                # 构建完整的文件路径（可选）
                full_path = os.path.join(root, file)
                # 只添加文件名到列表中（如果你只需要文件名）
                image_names.append(file)
                # 或者添加完整路径到列表中（如果你需要完整路径）
                # image_names.append(full_path)
    return image_names


# 使用函数并打印结果
folder_path = 'G:\挑战赛\Dataset-mask_6_30/V6_近岸舰船'  # 替换为你的图片文件夹路径
image_names = get_image_names(folder_path)
for name in image_names:
    print(name)


# import random
# def split_file(input_file, output_file1, output_file2, split_ratio=0.9):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#         # 计算每个文件应该有多少行
#     total_lines = len(lines)
#     first_file_lines = int(split_ratio * total_lines)
#     second_file_lines = total_lines - first_file_lines
#
#     # 打乱行的顺序
#     random.shuffle(lines)
#
#     # 写入第一个文件
#     with open(output_file1, 'w', encoding='utf-8') as file:
#         file.writelines(lines[:first_file_lines])
#
#         # 写入第二个文件
#     with open(output_file2, 'w', encoding='utf-8') as file:
#         file.writelines(lines[first_file_lines:])
#
#     # 使用函数
#
#
# input_file = 'G:\挑战赛\Dataset-mask_6_30/V3_space_no_target.txt'  # 原始txt文件
# output_file1 = 'G:\挑战赛\Dataset-mask_6_30/V3_train.txt'  # 含有90%内容的txt文件
# output_file2 = 'G:\挑战赛\Dataset-mask_6_30/V3_val.txt'  # 含有10%内容的txt文件
# split_file(input_file, output_file1, output_file2)


# from PIL import Image
# import os
#
#
# def get_image_resolution(folder_path):
#     """
#     遍历指定文件夹中的所有图片，并打印出它们的分辨率。
#     """
#     for filename in os.listdir(folder_path):
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
#             image_path = os.path.join(folder_path, filename)
#             with Image.open(image_path) as img:
#                 width, height = img.size
#                 # print(f"{filename}: {width}x{height}")
#                 print(f"{width}x{height}")
#
#             # 替换为你的文件夹路径
#
# folder_path = 'G:/挑战赛/Lightweight_9000/images_1000'
# get_image_resolution(folder_path)

# import os
#
# # 文件夹路径，这里替换为你的图片文件夹路径
# folder_path = 'G:\挑战赛\Dataset-mask_6_30\img_delate'
#
# # 遍历文件夹中的文件
# for filename in os.listdir(folder_path):
#     # 检查文件是否为图片（这里假设图片是.jpg或.png格式，你可以根据需要添加其他格式）
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')):
#         print(filename)  # 打印图片名字

# def read_and_compare_txt_files(file1_path, file2_path):
#     with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
#         # 读取第二个txt文件的所有行的前5个字符，并存储在集合中以加速查找
#         prefix_set = {line[:5].strip() for line in file2 if len(line) >= 5}
#
#         # 重置第一个文件的读取位置
#         file1.seek(0)
#
#         # 遍历第一个txt文件的每一行
#         for line in file1:
#             # 去除行首尾的空白字符
#             stripped_line = line.strip()
#             # 如果该行长度小于5或者其前5个字符不在第二个txt文件的集合中
#             if len(stripped_line) < 5 or stripped_line[:5] not in prefix_set:
#                 print(stripped_line)  # 打印不匹配的行
#
#
# # 替换为你的txt文件路径
# file1_path = 'G:\挑战赛\Dataset-mask_6_30/statistics_new_8804.txt'
# file2_path = 'G:\挑战赛\Dataset-mask_6_30/img_idx_new_8804.txt'
#
# # 调用函数
# read_and_compare_txt_files(file1_path, file2_path)


# def remove_and_save_non_matching_lines(file1_path, file2_path, output_path=None):
#     if output_path is None:
#         output_path = file1_path  # 如果没有指定输出路径，则覆盖原文件
#
#     # 读取第二个txt文件的所有行的前5个字符，并存储在集合中以加速查找
#     with open(file2_path, 'r', encoding='utf-8') as file2:
#         prefix_set = {line[:5].strip() for line in file2 if len(line) >= 5}
#
#         # 临时存储匹配的行
#     matching_lines = []
#
#     # 读取第一个txt文件并检查每一行
#     with open(file1_path, 'r', encoding='utf-8') as file1:
#         for line in file1:
#             stripped_line = line.strip()
#             if len(stripped_line) >= 5 and stripped_line[:5] in prefix_set:
#                 matching_lines.append(line)
#
#                 # 将匹配的行写入到输出文件
#     with open(output_path, 'w', encoding='utf-8') as output_file:
#         for line in matching_lines:
#             output_file.write(line)
#
#     print(f"不匹配的行已从 {file1_path} 中删除，剩余的行已保存到 {output_path}。")
#
#
# # 替换为你的txt文件路径
# file1_path = 'G:\挑战赛\Dataset-mask_6_30/statistics_8804.txt'
# file2_path = 'G:\挑战赛\Dataset-mask_6_30/trainval_7483.txt'
# # 如果你想要保存到新的文件，可以指定 output_path
# output_path = 'G:\挑战赛\Dataset-mask_6_30/statistics_trainval_7483.txt'  # 如果不需要，则注释或设置为 None
#
# # 调用函数
# remove_and_save_non_matching_lines(file1_path, file2_path, output_path)


# from PIL import Image, ImageShow
#
# # 打开图片
# img = Image.open('E:\Project/03903.png')  # 替换为你的图片文件名
#
# # 重新调整图片大小到256x256
# img_resized = img.resize((256, 256))
#
# # 显示图片
# # 注意：ImageShow模块可能不支持所有环境，例如某些IDE或服务器环境。
# # 在这种情况下，你可能需要将图片保存到文件并使用其他方式查看。
# ImageShow.show(img_resized)
#
# # 或者，你可以将图片保存到文件
# img_resized.save('E:\Project/resized_image.png')