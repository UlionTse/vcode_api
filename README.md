## **[vcode_api]()** ##


- *Usage:*

```python
>>>from vcode_api import vcode

>>>vcode.generate()

'Save OK!'
```

- *Tips:*
```python
generate(number=4, bgSize=(200, 80), font=None, colorAll=('white', 'blue', 'red'), pool=None, 
         drawLine=True, foggy=True,saveDirPath=None, showImg=True)
    :param number: int,random.sample(pool, number)
    :param bgSize: tuple,backgroundSize(width,height). The `height` affects `fontSize` & `lineWidth`.
    :param font: str,Default font 'arial'. Windows :file:`C:\...rial.ttf` directory.
    :param colorAll: tuple,(bgColor,fontColor,lineColor)
    :param pool: set,random.sample(set(pool), number)
    :param drawLine: boolean,
    :param foggy: boolean,
    :param saveDirPath: str,
    :param showImg: boolean,
    :return: str,
```
