import os


def rename_files(directory):
    # 获取目录下所有文件
    files = os.listdir(directory)

    # 遍历每个文件
    for filename in files:
        # 只处理以'.jpg'结尾的文件
        if filename.endswith('.jpg'):
            # 新文件名为去掉'R'后的名称
            new_filename = filename.replace('R.jpg', '.jpg')

            # 构建原文件路径和新文件路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            # 重命名文件
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} to {new_path}')


# 要重命名的目录
directory = '/mnt/d/program/ArtificialIntelligence/pj3/图像融合/VIF-Benchmark-ai_pj3-/datasets/test_imgs/ir/'

# 执行重命名操作
rename_files(directory)
