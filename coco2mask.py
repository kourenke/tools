import json
import os
import numpy as np
import cv2
from pycocotools.coco import COCO
import matplotlib.pyplot as plt

def coco_to_masks(coco_annotation_file, image_dir, output_dir, target_category_ids=None):
    """
    将 COCO 数据集格式转换为 mask 图像
    
    参数:
    - coco_annotation_file: COCO 标注文件的路径
    - image_dir: 原始图像所在的目录
    - output_dir: 输出 mask 图像的目录
    - target_category_ids: 需要转换的类别 ID 列表，如果为 None 则转换所有类别
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 加载 COCO 标注
    coco = COCO(coco_annotation_file)
    
    # 获取所有图像 ID
    img_ids = coco.getImgIds()
    
    # 如果没有指定类别，则使用所有类别
    if target_category_ids is None:
        target_category_ids = coco.getCatIds()
    
    # 处理每张图像
    for img_id in img_ids:
        # 获取图像信息
        img_info = coco.loadImgs(img_id)[0]
        img_name = img_info['file_name']
        img_path = os.path.join(image_dir, img_name)
        
        # 读取原始图像
        img = cv2.imread(img_path)
        if img is None:
            print(f"无法读取图像: {img_path}")
            continue
        
        # 获取图像尺寸
        img_height, img_width = img.shape[:2]
        
        # 创建空白 mask（与图像相同大小）
        mask = np.zeros((img_height, img_width), dtype=np.uint8)
        
        # 获取该图像的所有标注
        ann_ids = coco.getAnnIds(imgIds=img_id, catIds=target_category_ids)
        annotations = coco.loadAnns(ann_ids)
        
        print(f"图像 {img_name} 有 {len(annotations)} 个标注")
        
        # 为每个标注创建 mask
        for i, ann in enumerate(annotations):
            # 使用多边形创建 mask
            if 'segmentation' in ann and ann['segmentation']:
                # 处理多边形分割标注
                for segmentation in ann['segmentation']:
                    try:
                        # 将坐标转换为多边形点集
                        points = np.array(segmentation, dtype=np.float32).reshape((-1, 2))
                        
                        # 确保坐标在图像范围内
                        points[:, 0] = np.clip(points[:, 0], 0, img_width - 1)
                        points[:, 1] = np.clip(points[:, 1], 0, img_height - 1)
                        
                        # 转换为整数坐标
                        points = points.astype(np.int32)
                        
                        # 在 mask 上绘制多边形，填充值为255
                        cv2.fillPoly(mask, [points], color=255)
                        
                        print(f"标注 {i} 的多边形已绘制")
                    except Exception as e:
                        print(f"处理标注 {i} 时出错: {e}")
                        continue
        
        # 检查 mask 是否有非零值
        if np.any(mask > 0):
            print(f"Mask 包含目标区域，非零像素数量: {np.sum(mask > 0)}")
        else:
            print(f"警告: Mask 全为背景!")
            
        # 保存 mask 图像（单通道，背景为0，目标为255）
        mask_name = os.path.splitext(img_name)[0] + '_mask.png'
        mask_path = os.path.join(output_dir, mask_name)
        cv2.imwrite(mask_path, mask)
        
        # 可视化结果（可选）
        # plt.figure(figsize=(12, 6))
        # plt.subplot(1, 2, 1)
        # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # plt.title('原始图像')
        # plt.axis('off')
        # 
        # plt.subplot(1, 2, 2)
        # plt.imshow(mask, cmap='gray')  # 使用灰度颜色映射
        # plt.title('生成的 Mask')
        # plt.axis('off')
        # 
        # plt.savefig(os.path.join(output_dir, f"visualization_{img_name}"))
        # plt.close()
        # 
        # print(f"已处理: {img_name} -> {mask_name}")
# 
# 使用示例
if __name__ == "__main__":
    # 设置路径
    coco_annotation_file = "C:/Users/36525/Desktop/target_library/ship/swir_instanceSeg_dataset/swir_instanceSeg_dataset/annotations.json"  # 替换为你的 COCO 标注文件路径
    image_dir = "C:/Users/36525/Desktop/target_library/ship/swir_instanceSeg_dataset/swir_instanceSeg_dataset/images"  # 替换为你的图像目录
    output_dir = "C:/Users/36525/Desktop/target_library/ship/swir_instanceSeg_dataset/swir_instanceSeg_dataset/masks"  # 替换为输出目录
    
    # 可选：指定要处理的类别 ID（如果为 None 则处理所有类别）
    target_category_ids = [1]  # 例如，只处理类别 ID 为 1 的对象
    
    # 转换 COCO 格式到 mask
    coco_to_masks(coco_annotation_file, image_dir, output_dir, target_category_ids)