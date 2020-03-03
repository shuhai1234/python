import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from Common import dirconfig
from Common.configreader import ReadConfig
from Common.read_excel import ReadExcel
def get_excel_data():
    # 获取测试数据
    filepath = dirconfig.testdatas_path + "/zkkeeper_api_datas.xlsx"
    conp = dirconfig.config_path + "/config.conf"
    mode = ReadConfig().read_config(conp, "MODE", "mode")
    case_id = ReadConfig().read_config(conp, "MODE", "case_id")

    r = ReadExcel(filepath)
    all_case_datas = r.get_case_datas(mode, case_id)
    return all_case_datas

#print(type(get_excel_data()))
#print(get_excel_data())