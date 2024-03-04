import os
import cv2
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\pytesseract\tesseract.exe'


current_file_path = os.path.abspath(__file__)
print("当前文件路径：", current_file_path)
 


 
file_path = "E:\\Maple\\python\\pythons\\python_plugin\\mapletools\\screenshot.png"
# 打开图像
image = Image.open(file_path)

# 使用 OpenCV 读取图像
image_cv = cv2.imread(file_path)

# 缩放图像
scale_factor = 4
enlarged_image = cv2.resize(image_cv, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

# 将图像转换为灰度图像
gray = cv2.cvtColor(enlarged_image, cv2.COLOR_BGR2GRAY)

# 使用 Tesseract 进行 OCR
 
text = pytesseract.image_to_string(gray, lang='eng+chi_tra', config='--oem 2 --psm 6')
# 去除逗号和句点
text = text.replace(",", "").replace(".", "")

# 将识别结果按行分割
OCR_result = text.split("\n")

# 打印识别结果
print(OCR_result)

print(result)
print(input("ssss="))
