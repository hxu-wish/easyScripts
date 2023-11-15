import os
from tabulate import tabulate


def drawTable(code_status_list):
    table = [['module name', 'code count', 'file count']]
    for item in code_status_list:
        if item.total_code_num() > 0:
            table.append([item.module_name, item.total_code_num(), item.total_file_num()])
    print(tabulate(table, headers='firstrow'))


def takeCodeNumber(element):
    return element.total_code_num()


def scan(path):
    dir_list = os.listdir(path)
    result = []
    for single_dir in dir_list:
        if os.path.isdir(path + single_dir):
            java_status, kt_status = run_cloc_under_directory(ANDROID_REPO_PATH + single_dir)
            result.append(ModuleCodeStatus(single_dir, java_status, kt_status))

    result.sort(key=takeCodeNumber, reverse=True)
    return result


def generate_code_status(single_line_dic):
    return CodeStatus(single_line_dic[FILE_NUM_INDEX], single_line_dic[CODE_NUM_INDEX])


def run_cloc_under_directory(path):
    tmp = os.popen(f'cloc {path}').readlines()
    java_code_status = CodeStatus(0, 0)
    kt_code_status = CodeStatus(0, 0)
    for single_line in tmp:
        if single_line.startswith(JAVA_PREFIX) and not single_line.startswith(JS_PREFIX):
            single_line_dic = single_line.split()
            java_code_status = generate_code_status(single_line_dic)
        if single_line.startswith(KT_PREFIX):
            single_line_dic = single_line.split()
            kt_code_status = generate_code_status(single_line_dic)

    return java_code_status,kt_code_status


ANDROID_REPO_PATH = '/Users/hxu/Work/repo/android/'
FILE_NUM_INDEX = 1
CODE_NUM_INDEX = 4
JAVA_PREFIX = 'Java'
KT_PREFIX = 'Kotlin'
JS_PREFIX = 'JavaScript'


class ModuleCodeStatus:
    def __init__(self, module_name, java_code_status, kt_code_status):
        self.module_name = module_name
        self.java_code_status = java_code_status
        self.kt_code_status = kt_code_status

    def total_file_num(self):
        return int(self.java_code_status.files_num) + int(self.kt_code_status.files_num)

    def total_code_num(self):
        return int(self.java_code_status.code_num) + int(self.kt_code_status.code_num)


class CodeStatus:
    def __init__(self, files_num, code_num):
        self.files_num = files_num
        self.code_num = code_num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    drawTable(scan(ANDROID_REPO_PATH))
