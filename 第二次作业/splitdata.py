import os
from sklearn.model_selection import train_test_split
import shutil

data_dir = '/home/chenan/qiuzx/data/fruit30'

train_dir ='/home/chenan/qiuzx/data/fruit/train'
test_dir = '/home/chenan/qiuzx/data/fruit/test'
classes = os.listdir(data_dir)
train_data = []
test_data = []

for cls in classes:
    cls_path = os.path.join(data_dir, cls)
    images = os.listdir(cls_path)
    # 划分训练集和测试集
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
    # 将训练集和测试集的图片路径保存到train_data和test_data中
    train_data.extend([os.path.join(cls_path, img) for img in train_images])
    test_data.extend([os.path.join(cls_path, img) for img in test_images])
    
print("训练集数量：", len(train_data))
print("测试集数量：", len(test_data))





# 创建训练集和测试集的文件夹
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for cls in os.listdir(data_dir):
    cls_path = os.path.join(data_dir, cls)
    train_cls_dir = os.path.join(train_dir, cls)
    test_cls_dir = os.path.join(test_dir, cls)
    # 创建训练集和测试集中类别对应的文件夹
    os.makedirs(train_cls_dir, exist_ok=True)
    os.makedirs(test_cls_dir, exist_ok=True)
    for img_path in train_data:
        if cls in img_path:
            # 将训练集中的图片复制到对应类别的文件夹中
            shutil.copy(img_path, os.path.join(train_cls_dir, os.path.basename(img_path)))
    for img_path in test_data:
        if cls in img_path:
            # 将测试集中的图片复制到对应类别的文件夹中
            shutil.copy(img_path, os.path.join(test_cls_dir, os.path.basename(img_path)))