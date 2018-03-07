# coding=utf-8
# uliontse

import os
import string
import random
import numpy
from random import randint

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:
    import Image, ImageDraw, ImageFilter, ImageFont


def generate(number=4,bgSize=(200,80),font=None,colorAll=('white','blue','red'),pool=None,
               drawLine=True,foggy=True,saveDirPath=None,showImg=True):
    '''
    :param number: int,random.sample(pool, number)
    :param bgSize: tuple,backgroundSize(width,height). The `height` affects `fontSize` & `lineWidth`.
    :param font: str,Default font 'arial'. Windows :file:`C:\...\arial.ttf` directory.
    :param colorAll: tuple,(bgColor,fontColor,lineColor)
    :param pool: set,random.sample(set(pool), number)
    :param drawLine: boolean,
    :param foggy: boolean,
    :param saveDirPath: str,
    :param showImg: boolean,
    :return:
    '''

    if not font: font = r'arial.ttf'
    if not pool: pool = list(string.ascii_letters) + [str(x) for x in range(10)]
    text = ''.join(random.sample(set(pool), number))
    font = ImageFont.truetype(font,bgSize[1])

    if not foggy:
        image = Image.new(mode='RGBA', size=bgSize, color=colorAll[0])
    else:
        rawArray = numpy.zeros((bgSize[1],bgSize[0], 3), dtype=numpy.uint8)
        sh = rawArray.shape
        for i in range(sh[0]):
            for j in range(sh[1]):
                for k in range(sh[2]):
                    rawArray[i][j][k] = random.randint(0, 255)
        image = Image.fromarray(rawArray)

    draw = ImageDraw.Draw(image)
    textInd = ((bgSize[0]-font.getsize(text)[0])/2,(bgSize[1]-font.getsize(text)[1])/2)
    draw.text(xy=textInd,text=text,font=font,fill=colorAll[1])
    if drawLine:
        lineInd = [(textInd[0],randint(int(textInd[1]+1),bgSize[1]-int(textInd[1]-1))),
                    (bgSize[0]-textInd[0],randint(int(textInd[1]+1),bgSize[1]-int(textInd[1]-1)))]
        draw.line(xy=lineInd,fill=colorAll[2],width=int(bgSize[1]//10))
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    if showImg: image.show()
    if not saveDirPath:
        image.save('vcode.png')
        return 'Save OK! \nsaveDirPath: {}'.format(os.getcwd())
    else:
        try:
            image.save(saveDirPath + r'/vcode.png')
        except:
            image.save(saveDirPath + r'\\vcode.png')
        finally:
            return 'Save OK! \nsaveDirPath: {}'.format(saveDirPath)

