import os

dir = os.path.split(os.path.abspath(__file__))[0]

testdatas_path = dir.replace("Common", "TestDatas")

testreports_path = dir.replace("Common", "TestReports")


logs_pasth = dir.replace("Common", "Logs")


config_path = dir.replace("Common", "Configs")