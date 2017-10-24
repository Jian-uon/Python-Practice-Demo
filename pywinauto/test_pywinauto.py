# -*- coding:utf-8 -*-
import time
from pywinauto import application


def run():
    app = application.Application().start('ScanPort.exe')
    dlg = app.window_(title_re = 'ScanPort')
    #dlg.print_control_identifiers()
    time.sleep(1)

    dlg['Edit12'].SetEditText(u'强行测试pywinauto.')
    time.sleep(1)

    dlg['Button2'].Click()

    time.sleep(0.5)

    dlgAbout = app.window_(title_re = u'关于')
    #dlgAbout.print_control_identifiers()
    time.sleep(1)

    dlgAbout.Button.Click()
    # or
    #dlgAbout[u'确定'].Click()
    time.sleep(1)

    dlg['Button3'].Click()
    pass

if __name__ == '__main__':
    run()