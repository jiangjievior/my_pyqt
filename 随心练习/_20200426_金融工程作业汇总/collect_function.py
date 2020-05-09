from docx import Document
from docx.shared import Inches
import os
import re
import win32com.client as win32
import pandas as pd

def combine_docx(path,path_last,path_save):
    os.chdir(path)

    #读取指定文件夹内的文件名字
    file_name = []
    for root, dirs, files in os.walk(path_last):
        for file in files:
            file_name.append(os.path.join(root, file))

    #将多个word文档合并并保存在指定路径
    word = win32.gencache.EnsureDispatch('Word.Application')# 打开word软件
    word.Visible = False# 非可视化运行
    output = word.Documents.Add()  # 新建合并后空白文档
    files =file_name # 需要合并的文档路径
    files_error=[]
    for file in files:
        try:
            file_path_=os.path.join(path,file)
            output.Application.Selection.Range.InsertFile(file_path_)  # 拼接文档
        except:
            files_error.append(file)
            continue
    doc = output.Range(output.Content.Start, output.Content.End)# 获取合并后文档的内容
    output.SaveAs(path_save)  # 保存
    output.Close()
    return files_error

def to_excle(path_excel, path_excel_save):
    data = pd.read_excel(path_excel)
    text = data.columns[0]
    info = re.findall(r'\n姓名：(.{1,5})\n学号：.{8}\n得分：(.{0,3})\n', text)
    model_data = pd.DataFrame([0, 0], index=['姓名', '分数'])
    for i in range(len(info)):
        name = info[i][0]
        score = info[i][1]
        model_data[i] = [name, score]
    model_data.to_excel(path_excel_save)


if __name__=='__main__':
    os.chdir('E:\课件\研一下\金融工程')
    path='E:\课件\研一下\金融工程'#至倒数第三层文件路径
    path_last='第三周作业'#文件倒数第二层路径
    path_save='E:\课件\研一下\金融工程\合并文档_第三周作业.docx'#目标保存路径
    combine_docx(path, path_last, path_save)

    #将新生成的word文档内容粘贴至Excel表格的第一个单元格中
    path_excel='E:\课件\研一下\金融工程\合并文档.xlsx'#excel表格所载路径
    path_excel_save='E:\课件\研一下\金融工程\合并文档1.xlsx'#新生成的excel表格所载路径
    to_excle(path_excel, path_excel_save)








import os

work_path=os.getcwd()#文件总路径
file_path='第二周作业'
file_names=os.listdir(file_path)
import numpy as np
import seaborn as sns
gamma=np.random.gamma(8,30,2000)
ax=sns.distplot(gamma, bins=100, kde=True, color='b', hist_kws={"linewidth": 15, 'alpha': 0.4})#将数据分为100组，绘制概率分布图，kde=True可以绘制出概率密度曲线
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
















