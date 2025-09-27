import json
import cv2
import numpy as np
import os
from pathlib import Path

def create_mask_from_json(json_path, image_path, output_path):
    """
    根据JSON标注文件和原始图像生成掩码图
    
    参数:
        json_path: JSON标注文件路径
        image_path: 原始图像路径
        output_path: 掩码图保存路径
    """
    try:
        # 读取原始图像获取尺寸
        image = cv2.imread(image_path)
        if image is None:
            print(f"警告: 无法读取图像 {image_path}，跳过处理")
            return False
        
        height, width = image.shape[:2]
        
        # 创建空白掩码（单通道）
        mask = np.zeros((height, width), dtype=np.uint8)
        
        # 读取JSON文件
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # 检查JSON格式
        if 'shapes' not in data:
            print(f"警告: JSON文件 {json_path} 缺少'shapes'字段，跳过处理")
            return False
        
        # 遍历JSON中的每个标注形状
        for shape in data['shapes']:
            if shape['shape_type'] == 'polygon':
                # 提取多边形坐标点并转换为NumPy数组
                points = np.array(shape['points'], dtype=np.int32)
                
                # 在掩码上填充多边形（填充值为255）
                cv2.fillPoly(mask, [points], color=255)
        
        # 保存掩码图
        cv2.imwrite(output_path, mask)
        return True
    except Exception as e:
        print(f"处理 {json_path} 时出错: {str(e)}")
        return False

def batch_process_folder(input_folder, output_folder):
    """
    批量处理文件夹中的所有图片和JSON文件
    
    参数:
        input_folder: 包含图片和JSON文件的输入文件夹路径
        output_folder: 保存掩码图的输出文件夹路径
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 支持的图片扩展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    
    # 统计处理结果
    processed = 0
    skipped = 0
    errors = 0
    
    # 遍历输入文件夹中的所有文件
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        
        # 只处理JSON文件
        if not file.lower().endswith('.json'):
            continue
        
        # 获取文件名（不含扩展名）
        base_name = Path(file).stem
        
        # 查找对应的图片文件
        image_path = None
        for ext in image_extensions:
            possible_image = os.path.join(input_folder, base_name + ext)
            if os.path.exists(possible_image):
                image_path = possible_image
                break
        
        if not image_path:
            print(f"警告: 找不到 {base_name} 对应的图片文件，跳过")
            skipped += 1
            continue
        
        # 设置输出路径
        output_path = os.path.join(output_folder, base_name + '_mask.png')
        
        # 处理当前文件对
        if create_mask_from_json(file_path, image_path, output_path):
            print(f"成功处理: {file} -> {os.path.basename(output_path)}")
            processed += 1
        else:
            errors += 1
    
    # 打印统计信息
    print("\n处理完成!")
    print(f"总文件对: {processed + skipped + errors}")
    print(f"成功处理: {processed}")
    print(f"跳过处理: {skipped}")
    print(f"处理错误: {errors}")

if __name__ == "__main__":
    # 直接在代码中指定路径
    input_folder = "C:/Users/36525/Desktop/target_library/tank/Tank_Simulation_dataset/photo"  # 修改为你的输入文件夹路径
    output_folder = "C:/Users/36525/Desktop/target_library/tank/Tank_Simulation_dataset/mask"           # 修改为你的输出文件夹路径
    
    # 执行批量处理
    batch_process_folder(input_folder, output_folder)