from PIL import Image
import cv2
import numpy as np
import os
dis =20
def remove_background(image_path, output_path, color=(255, 255, 255)):  # 假设背景是白色
    with Image.open(image_path) as img:
        # 将图像转换为RGB模式
        img = img.convert("RGB")
        # 创建一个与原图大小相同的透明图像
        transparent = Image.new('RGBA', img.size, (255, 255, 255, 0))
        # 遍历像素，如果像素颜色接近背景色，则替换为透明
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                # print(x,y)
                if color_distance_rgb( (r, g, b),color)<dis:
                    transparent.putpixel((x, y), (255, 255, 255, 0))  # 设置为透明
                else:
                    transparent.putpixel((x, y), (r, g, b, 255))  # 保留原色
        print('ready')
        transparent.save(output_path)
        
def color_distance_rgb(color1, color2):
    return sum((c1 - c2)**2 for c1, c2 in zip(color1, color2)) ** 0.5

def remove_background_opencv(image_path, output_path, color=(255, 255, 255)):
    # 读取图像
    img = cv2.imread(image_path)
    
    # 转换为灰度图像（如果背景颜色是单色）
    # 对于彩色背景，直接在BGR图像上操作
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 如果背景是纯色，可以通过阈值化来创建掩码
    # 这里以白色为例，如果是其他颜色，可能需要调整阈值或使用其他方法
    _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
    
    # 应用掩码到原始图像
    img[mask != 255] = [0, 0, 0]  # 假设我们要移除的部分变为黑色，也可以直接处理为透明，但这在OpenCV中较为复杂
    
    # 保存处理后的图像
    cv2.imwrite(output_path, img)

# 批量处理
import os
folder_path = 'H:\CUB\Tools\dealImage'
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        input_path = os.path.join(folder_path, filename)
        print(input_path)
        output_path = os.path.join(folder_path, 'no_bg_' + filename+'.png')
        print(output_path)
        remove_background(input_path, output_path,color=(247, 188, 88))