# -*- coding: utf-8 -*-
import json

def findColor(h, s, b):
  hsb = [
      { 'name': '红色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 60, 'max': 100 }, 'b': { 'min': 60, 'max': 100 } },
      { 'name': '深色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 60, 'max': 100 }, 'b': { 'min': 20, 'max': 59 } },
      { 'name': '粉红色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 10, 'max': 59 }, 'b': { 'min': 100, 'max': 90 } },
      { 'name': '红色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 10, 'max': 59 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 10, 'max': 59 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '粉红色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '浅灰色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 0, 'max': 16 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '白色', 'h': { 'min': 0, 'max': 360 }, 's': { 'min': 0, 'max': 0 }, 'b': { 'min': 97, 'max': 100 } },
      { 'name': '浅灰色', 'h': { 'min': 0, 'max': 360 }, 's': { 'min': 0, 'max': 0 }, 'b': { 'min': 90, 'max': 96 } },
      { 'name': '灰色', 'h': { 'min': 0, 'max': 360 }, 's': { 'min': 0, 'max': 0 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 0, 'max': 360 }, 's': { 'min': 0, 'max': 0 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '黑色', 'h': { 'min': 0, 'max': 360 }, 's': { 'min': 0, 'max': 360 }, 'b': { 'min': 0, 'max': 19 } },
      { 'name': '蓝色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 60, 'max': 100 }, 'b': { 'min': 60, 'max': 100 } },
      { 'name': '深色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 60, 'max': 100 }, 'b': { 'min': 20, 'max': 59 } },
      { 'name': '粉蓝色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 16, 'max': 59 }, 'b': { 'min': 100, 'max': 76 } },
      { 'name': '深色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 16, 'max': 59 }, 'b': { 'min': 20, 'max': 75 } },
      { 'name': '灰蓝色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 5, 'max': 15 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 5, 'max': 15 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 5, 'max': 15 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '浅灰色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 224, 'max': 240 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '蓝色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 60, 'max': 100 }, 'b': { 'min': 50, 'max': 100 } },
      { 'name': '深蓝色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 60, 'max': 100 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '粉蓝', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 30, 'max': 59 }, 'b': { 'min': 80, 'max': 100 } },
      { 'name': '蓝色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 30, 'max': 59 }, 'b': { 'min': 40, 'max': 79 } },
      { 'name': '灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 30, 'max': 59 }, 'b': { 'min': 20, 'max': 39 } },
      { 'name': '深色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 30, 'max': 59 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '粉蓝色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 20, 'max': 29 }, 'b': { 'min': 80, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 20, 'max': 29 }, 'b': { 'min': 50, 'max': 79 } },
      { 'name': '深色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 20, 'max': 29 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '粉蓝', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '浅灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '浅灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 196, 'max': 223 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '紫色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 50, 'max': 100 }, 'b': { 'min': 40, 'max': 100 } },
      { 'name': '深色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 50, 'max': 100 }, 'b': { 'min': 20, 'max': 39 } },
      { 'name': '粉紫色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 10, 'max': 49 }, 'b': { 'min': 80, 'max': 100 } },
      { 'name': '紫色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 10, 'max': 49 }, 'b': { 'min': 80, 'max': 89 } },
      { 'name': '紫色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 20, 'max': 49 }, 'b': { 'min': 50, 'max': 79 } },
      { 'name': '深色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 20, 'max': 49 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '紫色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 70, 'max': 79 } },
      { 'name': '灰色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 50, 'max': 69 } },
      { 'name': '深色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '粉紫色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '浅灰色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '绿色', 'h': { 'min': 90, 'max': 150 }, 's': { 'min': 20, 'max': 100 }, 'b': { 'min': 20, 'max': 100 } },
      { 'name': '亮绿', 'h': { 'min': 90, 'max': 150 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '绿色', 'h': { 'min': 90, 'max': 150 }, 's': { 'min': 10, 'max': 19 }, 'b': { 'min': 20, 'max': 89 } },
      { 'name': '亮绿', 'h': { 'min': 90, 'max': 150 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 80, 'max': 100 } },
      { 'name': '绿色', 'h': { 'min': 90, 'max': 150 }, 's': { 'min': 5, 'max': 9 }, 'b': { 'min': 20, 'max': 79 } },
      { 'name': '亮绿', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 90, 'max': 100 } },
      { 'name': '灰色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 50, 'max': 89 } },
      { 'name': '深色', 'h': { 'min': 270, 'max': 300 }, 's': { 'min': 1, 'max': 4 }, 'b': { 'min': 20, 'max': 49 } },
      { 'name': '浅灰色', 'h': { 'min': 0, 'max': 360 }, 's': { 'min': 0, 'max': 4 }, 'b': { 'min': 80, 'max': 95 } },
      { 'name': '米白色', 'h': { 'min': 30, 'max': 60 }, 's': { 'min': 4, 'max': 9 }, 'b': { 'min': 96, 'max': 100 } },
      { 'name': '卡其色', 'h': { 'min': 30, 'max': 50 }, 's': { 'min': 20, 'max': 60 }, 'b': { 'min': 60, 'max': 80 } }
    ]
  targetColor = []
  for color in hsb:
    if h >= color['h']['min'] and h <= color['h']['max'] and s >= color['s']['min'] and s <= color['s']['max'] and b >= color['b']['min'] and b <= color['b']['max']:
      targetColor.append(color)
  return targetColor

if __name__ == '__main__':
  color = findColor(0, 6, 100)
  if len(color) == 0:
    print('深色衣物')
  else:
    print(color[0]['name'])