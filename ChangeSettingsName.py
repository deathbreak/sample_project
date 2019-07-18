__author__ = 'YMH'
import os

dir = '.'
production_name = 'production.py'
production_offline_name = 'production_offline.py'

def ChangeSettingsName(type=1):
    '''
    修改配置文件名称，方便开发。
    以后的开发中，配置文件将永远引用production，但是为了适配个人开发环境和128测试环境，特写此程序互换配置文件的文件名。
    以后只需要运行一下该程序，便可以在各种开发环境中切换。

    :param type:
    :return:
    '''
    setting_dir = os.path.join(os.path.abspath('.'), dir)
    production_setting = os.path.join(setting_dir, production_name)
    production_offline_setting = os.path.join(setting_dir, production_offline_name)
    if os.path.exists(production_setting) and os.path.exists(production_offline_setting):
        production_setting_tmp = os.path.join(setting_dir, 'tmp')
        if type == 1:  # 互换 production 和 production_offline的文件名
            ExChangeFileName(production_setting, production_offline_setting, production_setting_tmp)
        return 0
    else:
        return -1


def ExChangeFileName(file_name1, file_name2, tmp_name):
    os.rename(file_name1, tmp_name)
    os.rename(file_name2, file_name1)
    os.rename(tmp_name, file_name2)


if __name__ == "__main__":
    import sys
    type = 1
    arg_list = sys.argv
    arg_len = len(arg_list)
    if arg_len == 1:
        pass
    elif arg_len == 2:
        type = arg_list[1]
    else:
        print('错误的参数!')
        exit()
    result = ChangeSettingsName(int(type))
    if result == 0:
        print('修改完毕!')
    elif result == -1:
        print('缺少配置文件!')
