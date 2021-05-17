# -*- coding: utf-8 -*-
import os
import datetime
import xlrd


# def requests_by_duration(continue_time_seconds,concurrency_threads,info_level=1,headers_type="",header_array=[],api_address="",output_path=""):
#     cmd_list=[]
#     for threads in concurrency_threads.split("|"):
#         cmd_content="ab"+" -t "+str(continue_time_seconds)+" -c " +str(threads)
#         cmd_content=cmd_content+" -v "+str(info_level)
#         if len(headers_type)>0:
#             cmd_content = cmd_content + " -T " + headers_type
#         if len(header_array)>0:
#             for header in header_array:
#                 cmd_content=cmd_content+" -H "+str(header)
#         cmd_content=cmd_content+" "+str(api_address)
#         if len(output_path)>0:
#             cmd_content=cmd_content+" > "+os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/TestResultFloder/"+\
#                         datetime.datetime.strftime(datetime.datetime.now(), '%m%d%H%M')+"_"+\
#                         api_address.split("/")[-2]+"_"+api_address.split("/")[-1]+\
#                         "_"+str(continue_time_seconds)+"t_"+str(threads)+"c.txt"
#         # print (cmd_content.replace("\n",""))
#         cmd_list.append(cmd_content.replace("\n",""))
#         # print(os.popen(cmd_content).read())
#     return cmd_list

# def requests_by_sum(sum_requests_times,user_threads,info_level=1,api_address="",output_path=""):
#     cmd_content = "ab" + " -n " + str(sum_requests_times) + " -c " + str(user_threads)
#     cmd_content = cmd_content + " -v " + str(info_level)
#     cmd_content = cmd_content + " " + str(api_address)
#     if len(output_path) > 0:
#         cmd_content = cmd_content + " > " + str(output_path)+".txt"
#     print(cmd_content)
# print(os.popen(cmd_contentent).read())

def get_plan_data():
    date = xlrd.open_workbook("./TestPlan.xls")
    table = date.sheet_by_name("Sheet1")
    row_date_list = []
    all_date_list = []

    for row in range(1, table.nrows):
        for col in range(0, table.ncols):
            value = str(table.cell(row, col).value)
            value = value.replace(".0", "").replace("./",
                                                    os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/")
            row_date_list.append(value)
            # print(table.cell(row, col).value)
        all_date_list.append(row_date_list)
        row_date_list = []

    # for i in all_date_list:
    #     print(i)
    return all_date_list


def get_table_start_col():
    date = xlrd.open_workbook("./TestPlan.xls")
    date = xlrd.open_workbook("./TestPlan.xls")
    table = date.sheet_by_name("Sheet1")
    for row in range(0, table.nrows):
        i = 0
        for col in range(0, table.ncols):
            if str(table.cell(row, col).value) == "测试接口地址":
                table_start_col_flag = i
                return table_start_col_flag
            i += 1


def get_cmd_list(all_rows_list):
    cmd_list = []
    table_start_col_flag = get_table_start_col()
    for row in all_rows_list:
        concurrency_level = row[table_start_col_flag + 6].split("|")
        row_cmd_list = []
        for concurrency in concurrency_level:
            # 初始化
            row_cmd_content = ""
            # -t/-n -c
            if len(str(row[table_start_col_flag + 5])) < 1:
                row_cmd_content += "ab" + " -t " + str(row[table_start_col_flag + 4]) + " -c " + str(concurrency)
            else:
                row_cmd_content += "ab" + " -n " + str(row[table_start_col_flag + 5]) + " -c " + str(concurrency)
            # -v
            row_cmd_content += " -v " + str(row[table_start_col_flag + 8])
            # -k
            if len(str(row[table_start_col_flag + 7])) > 0:
                if str(row[table_start_col_flag + 7]).replace(" ", "") == "是":
                    row_cmd_content = row_cmd_content + " -k "
            # -T

            if len(str(row[table_start_col_flag + 2])) > 0:
                row_cmd_content += " -T " + str(row[table_start_col_flag + 2])
            # -p
            if len(str(row[table_start_col_flag + 1])) > 0:
                row_cmd_content += " -p "
                row_cmd_content += os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/JsonFile/"
                row_cmd_content += str(row[table_start_col_flag + 1])

            # -H
            if len(str(row[table_start_col_flag + 3])) > 0:
                header_str = ""
                for i in str(row[table_start_col_flag + 3]).split("|"):
                    header_str += " -H " + i
            row_cmd_content += header_str
            #
            row_cmd_content += " " + "\"" + str(row[table_start_col_flag + 0]) + "\""
            result_file_floder_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/ResultFloder/" + \
                                      datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d') + "/"
            if not os.path.exists(result_file_floder_path):
                os.makedirs(result_file_floder_path)

            result_file_name = ""
            if "?" in str(row[table_start_col_flag + 0]):
                api_adress_last_line = str(row[table_start_col_flag + 0]).split("?")[0]
            else:
                api_adress_last_line = str(row[table_start_col_flag + 0])
            result_file_name += str(api_adress_last_line.split("/")[-2]) + "_"
            result_file_name += str(api_adress_last_line.split("/")[-1]) + "_"
            if " -n " in row_cmd_content:
                result_file_name += str(row[table_start_col_flag + 5]) + "n_" + str(concurrency) + "c"
            else:
                result_file_name += str(row[table_start_col_flag + 4]) + "t_" + str(concurrency) + "c"
            if " -k " in row_cmd_content:
                result_file_name += "_k_"
            else:
                result_file_name += "_"

            result_file_name += datetime.datetime.strftime(datetime.datetime.now(), '%H%M') + ".txt"
            # result_file_name += "2155.txt"
            result_file_name += "sleep" + str(row[table_start_col_flag + 9])
            row_cmd_content = row_cmd_content + " > " + result_file_floder_path + result_file_name
            row_cmd_list.append(row_cmd_content)

        cmd_list.append(row_cmd_list)
    return cmd_list


def exec_cmd(cmd_str):
    print("执行命令：" + cmd_str)
    cmd_return_value = os.popen(cmd_str).read()
    return cmd_return_value


def get_post_data(cmd_str_list):
    json_file_path = ""
    json_line = "无post数据"
    for cmd in cmd_str_list:
        if "-p " in cmd:
            json_file_path = cmd.split("-p ")[1].split(" ")[0]
            # print(json_file_path)
            break
        break
    # json_file_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/JsonFile/"+json_file_path
    if len(json_file_path) > 0:
        json_line = ""
        for line in open(json_file_path):
            json_line += line + "</br>"
    return json_line

# class jmeter:
#     def requests(continue_time_seconds,user_threads,api_address):
#         cmd_content="jmeter"+\
#                     " -t "+str(continue_time_seconds)+\
#                     " -c "+str(user_threads)+\
#                     " "+api_address
#         print (cmd_content)
#         print(os.popen(cmd_content).popenread())

# if __name__ == '__main__':
# # 获取 excel 中表格数据
# plan=get_plan_data()
# # 生成测试命令
# cmd_list=get_cmd_list(plan)
# # 执行测试命令
# for cmd in cmd_list:
#     print("执行命令：\n"+cmd)
#     # os.popen(cmd)
#     #生成测试报告
#
#
#
#
#
# #     .read())
