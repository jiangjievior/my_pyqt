import base64
import os

class PictureProcess():
    """控制图片转化为txt"""
    def __init__(self):
        import base64
        import os

    def to_str(self, picture_path):
        """将图片转化为字符串"""
        f = open(picture_path, 'rb')
        str = base64.b64encode(f.read()).decode()  # 将图片由二进制转化为字符串
        f.close()
        return str

    def to_txt(self, picture_path, txt_path):
        """将图片转化为字符串并保存在指定文件,picture_path为图片路径，txt为txt文本路径"""
        str = self.to_str(picture_path)
        with open(txt_path, 'w+') as file:
            file.write(str)

    def to_picture(self, picture_path, txt_path):
        """将txt文本（txt_path）转化为图片（picture_path）"""

        with open(txt_path, 'r+') as file:
            str = file.read()

        with open(picture_path, 'wb') as file:
            file.write(base64.b64decode(str))

    def to_multi_txts(self, pictures_path, txts_path,picture_type=['.jpg','.png'],txt_type='.txt'):
        """将许多图片批量转化为txt文本,pictures_path为图片所在路径，txts_path为保存txt的路径,
        picture_type为指定修改的图片，默认为['.jpg','.png']；txt_type为将要保存的文本格式，默认为'.txt'
        注意：txt文本所在路径务必加r,如：txts_path = r'F:\python笔记\加密\txt文件'
        """

        filenames = os.listdir(pictures_path)
        # filename=filenames[0]
        for filename in filenames:
            try:
                if filename[-4:] in picture_type:
                    picture_path = os.path.join(pictures_path, filename)
                    txt_path = os.path.join(txts_path, filename[:-4] + txt_type)
                    self.to_txt(picture_path, txt_path)
                elif filename[-4:] =='.mp4':
                    picture_path = os.path.join(pictures_path, filename)
                    txt_path = os.path.join(txts_path, filename[:-4] + '.ini')
                    self.to_txt(picture_path, txt_path)
                print('已经完成' + str(round(filenames.index(filename) / len(filenames), 2) * 100) + '%')
            except:
                continue

    def to_multi_pictures(self, pictures_path, txts_path,txt_type='.txt'):
        """将许多txt文本批量转化为图片,pictures_path为图片所在路径，txts_path为保存txt的路径"""

        filenames = os.listdir(txts_path)
        # filename=filenames[0]
        for filename in filenames:
            try:
                if filename[-4:] == txt_type:
                    txt_path = os.path.join(txts_path, filename)
                    picture_path = os.path.join(pictures_path, filename[:-4] + '.jpg')
                    self.to_picture(picture_path, txt_path)
                elif filename[-4:] == '.ini':
                    txt_path = os.path.join(txts_path, filename)
                    picture_path = os.path.join(pictures_path, filename[:-4] + '.mp4')
                    self.to_picture(picture_path, txt_path)
                print('已经完成' + str(round(filenames.index(filename) / len(filenames), 2) * 100) + '%')
            except:
                continue

if __name__=='__main__':
    picture=PictureProcess()
    #转为txt

    picture.to_multi_txts(pictures_path=r'F:\python笔记\my_pyqt\随心练习\_20200508_更改图片为txt\原始图片',txts_path=r'F:\python笔记\my_pyqt\随心练习\_20200508_更改图片为txt\生成txt')
    #将txt转为图片
    picture.to_multi_pictures(r'F:\python笔记\my_pyqt\随心练习\_20200508_更改图片为txt\生成图片',r'F:\python笔记\my_pyqt\随心练习\_20200508_更改图片为txt\生成txt')







