import Common.Report
import Common.Exceter
import time


def wai_for_time(hours_min):
    while (True):
        h_m = time.strftime('%H%M', time.localtime());
        if h_m.__eq__(hours_min):
            print('等待时间%a到了，开始执行...', hours_min)
            break
        print('等待时间%a未到，继续等待5秒...', hours_min);
        time.sleep(5)


if __name__ == '__main__':
    for i in range(0, 1):
        # wai_for_time("1612")
        repo = Common.Report
        exector = Common.Exceter
        # 获取 excel 中表格数据
        plan = exector.get_plan_data()
        # 生成测试命令
        cmd_list = exector.get_cmd_list(plan)
        result_file_path_list = []
        html = """"""
        html += repo.generate_report_header(repo.get_current_datetime_str(), len(cmd_list))  # html头
        index = 0
        for row_cmd in cmd_list:
            # 一个接口的提取Post数据
            post_data_str = exector.get_post_data(row_cmd)
            # 获取测试间隔时长
            sleep_time = row_cmd[0].split("sleep")[1].replace(" ", "")
            cmd_report_str = """"""
            for cmd in row_cmd:
                # 去除附带的sleep
                cmd = cmd.split("sleep")[0]
                # 执行一个接口(一行)不同并发的测试命令
                exector.exec_cmd(cmd)
                cmd_report_str += cmd.split("sleep")[0] + "</br>\n"
                # 等待指定的间隔时长
                if len(sleep_time) > 0:
                    print("等待" + sleep_time + "秒...")
                    time.sleep(int(sleep_time))
            # 获取一个接口的每个测试结果
            report_file_list = repo.get_report_file_list(row_cmd)
            # 一个接口的html代码
            index += 1
            html += repo.generate_row_html(cmd_report_str, report_file_list, post_data_str, index)
        html += Common.Report.generate_report_footer()
        # 生成测试报告
        repo.write_html(html)
        # print(html)
        print('####################')
        print('###第' + str(i+1) + '次测试完成###')
        print('####################')
