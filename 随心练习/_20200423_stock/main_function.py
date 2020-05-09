import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDesktopWidget  # 创建任何应用程序都需要QApplication
from window_stock import *
import tushare as ts
import pandas as pd
pro = ts.pro_api('7fac027f24db4e9bddd02e3f998cd48f9f28551050860e2c402d87fc')
import datetime#获取今天日期

class LookUpStock(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('最新股票收盘价查询')
        self.setupUi(self)
        self.index = 1
        self.stock_info = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name')#获得流通股票代码和股票名称
        self.show_close_price(stock_code='000001.SZ')

    def setup_ui(self):
        pass

    #最新股票收盘价日期
    def new_date(self):
        today = datetime.date.today().strftime('%Y%m%d')
        yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')  # 获取昨天日期
        hour = int(datetime.datetime.now().strftime('%H'))
        if hour >= 15:
            date = today
        else:
            date = yesterday
        return date

    # 显示指定股票信息（名称，代码，收盘价）
    def show_close_price(self,stock_code):
        date=self.new_date()
        close_price = pro.daily(ts_code=stock_code, start_date=date, end_date=date)['close'].tolist()[0]
        self.label_stockclose.setText(str(close_price))#显示股票收盘价
        stock_name=self.stock_info.ix[self.stock_info['ts_code']==stock_code]['name'].tolist()[0]#获得股票名称
        self.label_stockname.setText(stock_name)#显示股票名称
        self.label_stockcode.setText(str(stock_code))#显示股票代码

    def move_up(self):
        """向上移动"""
        self.index += -1
        stock_code = self.stock_info['ts_code'].tolist()[self.index]##stock_code = stock_info['ts_code'][index]
        self.show_close_price(stock_code)

    def move_down(self):
        """向下移动"""
        self.index += 1
        stock_code = self.stock_info['ts_code'].tolist()[self.index]
        self.show_close_price(stock_code)

    def look_up_stock(self):
        if self.lineEdit_stockcode.text()=='':
            stock_code = self.label_stockcode.text()
        else:
            stock_code = self.lineEdit_stockcode.text()
        try:
            self.show_close_price(stock_code)
        except:
            self.label_stockclose.setText('不存在此股票,请重新输入')  # 显示股票收盘价
            self.label_stockname.setText('不存在此股票,请重新输入')  # 显示股票名称
            self.label_stockcode.setText('不存在此股票,请重新输入')  # 显示股票代码


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LookUpStock()
    main.show()  # 显示窗口
    sys.exit(app.exec_())




