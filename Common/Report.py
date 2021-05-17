# -*- coding: utf-8 -*-
import os
import subprocess
import datetime
import time
from collections import deque


#
def collect_date(report_file_path, last_line=50):
    file = open(report_file_path, "rb+")
    test_result = {}
    output = deque(file, last_line)
    list1 = list(output)
    result_data = ""
    # 给定默认值
    test_result['Server_Hostname'] = "NOT_GET_DATA"
    test_result['Server_Port'] = "NOT_GET_DATA"
    test_result['API_Path'] = "NOT_GET_DATA"
    test_result['Document_Length'] = "NOT_GET_DATA"
    test_result['User_Threads'] = "NOT_GET_DATA"
    test_result['Test_Time_Taken'] = "NOT_GET_DATA"
    test_result['Complete_Requests'] = "NOT_GET_DATA"
    test_result['Failed_Requests'] = "NOT_GET_DATA"
    test_result['Total_Transferred'] = "NOT_GET_DATA"
    test_result['Requests_Per_Second'] = "NOT_GET_DATA"
    test_result['Time_Per_Request_Sum'] = "NOT_GET_DATA"
    test_result['Time_Per_Request'] = "NOT_GET_DATA"
    test_result['Transfer_Rate'] = "NOT_GET_DATA"
    test_result['Transfer_Rate_total'] = "NOT_GET_DATA"
    test_result['Connect_Min'] = "NOT_GET_DATA"
    test_result['Connect_Mean'] = "NOT_GET_DATA"
    test_result['Connect_Sd'] = "NOT_GET_DATA"
    test_result['Connect_Median'] = "NOT_GET_DATA"
    test_result['Connect_Max'] = "NOT_GET_DATA"
    test_result['Processing_Min'] = "NOT_GET_DATA"
    test_result['Processing_Mean'] = "NOT_GET_DATA"
    test_result['Processing_Sd'] = "NOT_GET_DATA"
    test_result['Processing_Median'] = "NOT_GET_DATA"
    test_result['Processing_Max'] = "NOT_GET_DATA"
    test_result['Waiting_Min'] = "NOT_GET_DATA"
    test_result['Waiting_Mean'] = "NOT_GET_DATA"
    test_result['Waiting_Sd'] = "NOT_GET_DATA"
    test_result['Waiting_Median'] = "NOT_GET_DATA"
    test_result['Waiting_Max'] = "NOT_GET_DATA"
    test_result['Total_Min'] = "NOT_GET_DATA"
    test_result['Total_Mean'] = "NOT_GET_DATA"
    test_result['Total_Sd'] = "NOT_GET_DATA"
    test_result['Total_Median'] = "NOT_GET_DATA"
    test_result['Total_Max'] = "NOT_GET_DATA"
    test_result['50%'] = "NOT_GET_DATA"
    test_result['66%'] = "NOT_GET_DATA"
    test_result['75%'] = "NOT_GET_DATA"
    test_result['80%'] = "NOT_GET_DATA"
    test_result['90%'] = "NOT_GET_DATA"
    test_result['95%'] = "NOT_GET_DATA"
    test_result['98%'] = "NOT_GET_DATA"
    test_result['50%'] = "NOT_GET_DATA"
    test_result['99%'] = "NOT_GET_DATA"
    test_result['100%'] = "NOT_GET_DATA"

    for item in list1:
        item_str = str(item).replace("b'", "").replace("\\n'", "")
        if "Server Hostname:" in item_str:
            test_result['Server_Hostname'] = item_str.replace("Server Hostname:", "").replace(" ", "")
        if "Server Port:" in item_str:
            test_result['Server_Port'] = item_str.replace("Server Port:", "").replace(" ", "")
        if "Document Path:" in item_str:
            test_result['API_Path'] = item_str.replace("Document Path:", "").replace(" ", "")
        if "Document Length:" in item_str:
            test_result['Document_Length'] = item_str.replace("Document Length:", "").replace(" ", "").replace("bytes",
                                                                                                               "")
        if "Concurrency Level:" in item_str:
            test_result['User_Threads'] = item_str.replace("Concurrency Level:", "").replace(" ", "")
        # if "Time taken for tests:" in item_str :
        #     test_result['Test_Time_Taken']=item_str.replace("Time taken for tests:","").replace(" ","")
        if "Time taken for tests:" in item_str:
            test_result['Test_Time_Taken'] = item_str.replace("Time taken for tests:", "").replace("seconds",
                                                                                                   "").replace(" ", "")
        if "Complete requests" in item_str:
            test_result['Complete_Requests'] = item_str.replace("Complete requests:", "").replace(" ", "")
        if "Failed requests:" in item_str:
            test_result['Failed_Requests'] = item_str.replace("Failed requests:", "").replace(" ", "")
        if "Total transferred:" in item_str:
            test_result['Total_Transferred'] = item_str.replace("Total transferred:", "").replace("bytes", "").replace(
                " ", "")
        if "Requests per second:" in item_str:
            test_result['Requests_Per_Second'] = item_str.replace("Requests per second:", "").replace("[#/sec] (mean)",
                                                                                                      "").replace(" ",
                                                                                                                  "")
        if "Time per request:" in item_str and "(mean)" in item_str:
            test_result['Time_Per_Request_Sum'] = item_str.replace("Time per request:", "").replace("[ms] (mean)",
                                                                                                    "").replace(" ", "")
        if "Time per request:" in item_str and "across all concurrent requests)" in item_str:
            test_result['Time_Per_Request'] = item_str.replace("Time per request:", "").replace(
                "[ms] (mean, across all concurrent requests)", "").replace(" ", "")
        if "Transfer rate:" in item_str and "received" in item_str:
            test_result['Transfer_Rate'] = item_str.replace("Transfer rate:", "").replace("[Kbytes/sec] received",
                                                                                          "").replace(" ", "")
        if "kb/s total" in item_str:
            test_result['Transfer_Rate_total'] = item_str.replace("                        ", "").replace("kb/s total",
                                                                                                          "").replace(
                " ", "")

        if "Connect:" in item_str:
            item_str_list = item_str \
                .replace("        ", "|") \
                .replace("       ", "|") \
                .replace("      ", "|") \
                .replace("     ", "|") \
                .replace("    ", "|") \
                .replace("   ", "|") \
                .replace("  ", "|") \
                .replace(" ", "|").split("|")
            # print(item_str)
            test_result['Connect_Min'] = item_str_list[1]
            test_result['Connect_Mean'] = item_str_list[2]
            test_result['Connect_Sd'] = item_str_list[3]
            test_result['Connect_Median'] = item_str_list[4]
            test_result['Connect_Max'] = item_str_list[5]
        if "Processing:" in item_str:
            item_str_list = item_str \
                .replace("        ", "|") \
                .replace("       ", "|") \
                .replace("      ", "|") \
                .replace("     ", "|") \
                .replace("    ", "|") \
                .replace("   ", "|") \
                .replace("  ", "|") \
                .replace(" ", "|").split("|")
            test_result['Processing_Min'] = item_str_list[1]
            test_result['Processing_Mean'] = item_str_list[2]
            test_result['Processing_Sd'] = item_str_list[3]
            test_result['Processing_Median'] = item_str_list[4]
            test_result['Processing_Max'] = item_str_list[5]
        if "Waiting:" in item_str:
            item_str_list = item_str \
                .replace("        ", "|") \
                .replace("       ", "|") \
                .replace("      ", "|") \
                .replace("     ", "|") \
                .replace("    ", "|") \
                .replace("   ", "|") \
                .replace("  ", "|") \
                .replace(" ", "|").split("|")
            test_result['Waiting_Min'] = item_str_list[1]
            test_result['Waiting_Mean'] = item_str_list[2]
            test_result['Waiting_Sd'] = item_str_list[3]
            test_result['Waiting_Median'] = item_str_list[4]
            test_result['Waiting_Max'] = item_str_list[5]
        if "Total:" in item_str:
            item_str_list = item_str \
                .replace("        ", "|") \
                .replace("       ", "|") \
                .replace("      ", "|") \
                .replace("     ", "|") \
                .replace("    ", "|") \
                .replace("   ", "|") \
                .replace("  ", "|") \
                .replace(" ", "|").split("|")
            test_result['Total_Min'] = item_str_list[1]
            test_result['Total_Mean'] = item_str_list[2]
            test_result['Total_Sd'] = item_str_list[3]
            test_result['Total_Median'] = item_str_list[4]
            test_result['Total_Max'] = item_str_list[5]
        if "50%" in item_str:
            test_result['50%'] = item_str.replace("50%", "").replace(" ", "")
        if "66%" in item_str:
            test_result['66%'] = item_str.replace("66%", "").replace(" ", "")
        if "75%" in item_str:
            test_result['75%'] = item_str.replace("75%", "").replace(" ", "")
        if "80%" in item_str:
            test_result['80%'] = item_str.replace("80%", "").replace(" ", "")
        if "90%" in item_str:
            test_result['90%'] = item_str.replace("90%", "").replace(" ", "")
        if "95%" in item_str:
            test_result['95%'] = item_str.replace("95%", "").replace(" ", "")
        if "98%" in item_str:
            test_result['98%'] = item_str.replace("98%", "").replace(" ", "")
        if "99%" in item_str:
            test_result['99%'] = item_str.replace("99%", "").replace(" ", "")
        if "100%" in item_str:
            test_result['100%'] = item_str.replace("(longest request)", "").replace("100%", "").replace(" ", "")

        # result_data+=(str(item).replace("b'", "").replace("\\n'", ""))
    # print(result_data)
    # for key, value in test_result.items():
    #     print(key + ": " + str(value))
    return test_result


def generate_report_header(test_time, count_api):
    header_str = """<!--这里是头部内容-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no">
        <script type="text/javascript">
            function showOrHide(divID,textID){
                var targetDiv = document.getElementById(divID);
                if (targetDiv){
                    if (targetDiv.style.display=='block'){
                        var old_content=document.getElementById(textID).innerHTML;
                        document.getElementById(textID).innerHTML=old_content.replace("隐藏",'查看');
                        targetDiv.style.display='none';
                        }else{
                            var old_content=document.getElementById(textID).innerHTML;
                            document.getElementById(textID).innerHTML=old_content.replace('查看',"隐藏");
                            targetDiv.style.display='block';
                        }
                    }
            }
        </script>
            <title>测试报告</title>
    </head>
    
<!--这里是测试信息-->
<body>
<div class="box">
	<div class="table">
		<div class="table-header"><strong>互勾单接口测试报告</strong></div>
			<div class="table-box">
			<div class="table-header-item">
            <div class="table-header-item-title">测试信息</div>
            <div class="table-header-list">
                <div class="table-header-list-left">测试时间</div>
                <div class="table-header-list-right">""" + test_time + """</div>
            </div>
            <div class="table-header-list">
                <div class="table-header-list-left">测试目的</div>
                <div class="table-header-list-right">对""" + str(count_api) + """个接口进行并发测试，提取测试数据，作为后续接口调优参考</div>
            </div>
            <div class="table-header-list">
                <div class="table-header-list-left">测试方法</div>
                <div class="table-header-list-right">在相同时间内或在相同的总请求数下，并发数逐级递增后，接口的性能状况。</div>
            </div>
			</div>
        
<!--这里是需要插入的接口测试结果-->
			<div class="table-content">"""
    return header_str + "\n"


def get_current_datetime_str():
    return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')


def generate_report_footer():
    footer_str = """
		</div>
<!--这里是参考链接-->
			<div class="table-header-item table-margin-top-20">
				<div class="table-header-item-title">参考链接</div>
				<div class="table-header-list-auto">
					<label style="word-break:break-all;word-wrap:break-word">
					   1）<a href="https://www.drupal.org/docs/develop/profiling-drupal/apache-bench-ab" target=_blank>https://www.drupal.org/docs/develop/profiling-drupal/apache-bench-ab</a> </br>
					   2）<a href="https://www.cnblogs.com/gumuzi/p/5617232.html" target=_blank>https://www.cnblogs.com/gumuzi/p/5617232.html</a> </br>
					   3）<a href="http://www.devside.net/wamp-server/load-testing-apache-with-ab-apache-bench" target=_blank>http://www.devside.net/wamp-server/load-testing-apache-with-ab-apache-bench</a> </br>
					   4）<a href="http://www.it1352.com/708197.html" target=_blank>http://www.it1352.com/708197.html</a> </br>
					   5）<a href="https://www.w3ctech.com/topic/1746" target=_blank>https://www.w3ctech.com/topic/1746</a> </br>
					</label>
				</div>
			</div>
    </div>
</div>
</body>
<!--这里是css-->
<style>
html,body{
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
    overflow-y: scroll;
}
.box{
    width: 100%;
    height: 100%;
    display: block;
}
.table{
    display: flex;
    flex-direction: column;
    flex: 1;
    margin: 20px;
    border:1px solid black;
}
.table .table-header{
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: cornflowerblue;
    color: white;
    font-size:x-large;
}
.table .table-box{
    padding: 15px;
    display: flex;
    flex-direction: column;
    flex: 1;
    background-color: gainsboro;
}
.table .table-box .table-header-item{
    display: flex;
    flex-direction: column;
    height: auto;
}
.table-header-item-title {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 120px;
    background-color: cornflowerblue;
    border:1px solid black;
    color:white;
}
.table .table-box .table-header-item .table-header-list {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 40px;
    border:1px solid black;
}
.table-header-list-left {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 40px;
    width: 120px;
    border-right:1px double black;
}
.table-header-list-right{
    margin-left: 20px;
    margin-right: 20px;
    flex: 1;
}
.table .table-box .table-content {
    margin-top: 15px;
    flex: 1px;
}
.table-content-li {
    padding-bottom: 15px;
    display: block;
    width: 100%;
    overflow: scroll;
    border:1px solid black;
    background-color: white;
    display:none
}
.table-content-li-header {
    padding: 10px 20px 10px 20px;
    background-color: cornflowerblue;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    border:1px solid black;
    border-bottom: white;
    color: white;
}
.table-content-item {
    margin:0 15px 0 15px;
    height: auto;
	background-color: #f0f0f0;
    font-size:small
}
.table-content-item tr {
    text-align: center;
    width:fit-content;
}
.table-content-item tr td {
    padding: 5px;
}
.table-margin-top-20 {
    margin-top: 20px;
}
.table-header-list-auto {
    padding: 10px;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-wrap: wrap;
    height: auto;
    white-space: normal;
    border:1px solid black;
}
.table-tr-header {
    margin: 15px 15px 0 15px;
    padding: 5px 20px 5px 20px;
    width: fit-content;
    background-color: PowderBlue;
    border:1px solid black;
}
.table-tr-foot {
    margin: 0px 0px 0 15px;
    width: fit-content;
    border:1px solid black;
}
</style>
</html>"""
    return footer_str + "\n"


def generate_row_html(cmd_str, result_file_path_list, json_str, index):
    index = str(index)
    result_dic = collect_date(result_file_path_list[0])
    # print(result_file_path_list[0])
    # print(result_dic)
    # print(result_dic['API_Path'])
    if result_dic['API_Path'] == "NOT_GET_DATA":
        div_id = "NO_GET_DATA"
    else:
        div_id = result_dic['API_Path'].split("/")[-2] + "_" + result_dic['API_Path'].split("/")[-1]
    api_info = result_dic['Server_Hostname'] + result_dic['API_Path']
    test_cmd_list_str = cmd_str

    part_one_api_info = """
    <!--part_one_api_info-->   
    <!--这里是接口信息-->
                <div id='interface_info' class="table-content-li-header" onclick="showOrHide('""" + div_id + """_""" + index + """','interface_info')">(点击查看)接口信息:""" + api_info + """</div>
                <div id=\"""" + div_id + """_""" + index + """\" class="table-content-li" display="none">
                    <div id='cmd_title' class="table-tr-header" onclick="showOrHide('cmd_""" + div_id + """','cmd_title')">(点击查看)测试命令及Post数据</div>
                        <div id='cmd_""" + div_id + """' style="display:none">
                            <table class="table-content-item" border="1" cellspacing="0">
                            <tbody>
                                <tr>
                                    <td rowspan=4 colspan=16 align="left">
                                        """ + test_cmd_list_str.replace("/Users/panpan/Desktop/DDStudy/APItest/",
                                                                        "./") + """
                                    </td>
                                </tr>
                                <tr></tr><tr></tr><tr></tr>
                                <tr>
                                    <td rowspan=4 colspan=16 align="left">
                                        POST 参数数据 ：""" + json_str + """
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                """

    key_result_title = """
    <!--key_result_title-->	
    <!--这里是关键数据结果-->				
                    <div class="table-tr-header">关键数据结果</div>
                    <table class="table-content-item" border="1" cellspacing="0">
                        <tr>
                            <td> </td>
                            <td>总请求数</td>
                            <td>失败数量</td>
                            <td>测试时长</td>
                            <td style="background-color:LightSteelBlue">Requests per second</td>
                            <td style="background-color:LightSteelBlue">Time per request1</td>
                            <td>Time per request2</td>
                            <td>Document Length</td>
                            <td>Total transferred</td>
                            <td>Transfer rate(total)</td>
                        </tr>
                        
                    """

    key_result_value = """"""
    for file_path in result_file_path_list:
        test_result = collect_date(file_path)  # return dic
        table_title = test_result['Test_Time_Taken'].split(".")[0] + """秒""" + test_result['User_Threads'] + """并发"""
        if "ab -n" in cmd_str:
            table_title = test_result['Complete_Requests'].split(".")[0] + """次""" + test_result[
                'User_Threads'] + """并发"""
        key_result_value += """
    <!--key_result_value-->  
                            <tr>
                                <td>""" + table_title + """</td>
                                <td>""" + test_result['Complete_Requests'] + """个</td>
                                <td>""" + test_result['Failed_Requests'] + """个</td>
                                <td>""" + test_result['Test_Time_Taken'] + """秒</td>
                                <td style="background-color:LightSteelBlue">""" + test_result['Requests_Per_Second'] + """个请求/每秒</td>
                                <td style="background-color:LightSteelBlue">""" + test_result['Time_Per_Request_Sum'] + """毫秒</td>
                                <td>""" + test_result['Time_Per_Request'] + """毫秒</td>
                                <td>""" + test_result['Document_Length'] + """ bytes</td>
                                <td>""" + test_result['Total_Transferred'] + """ bytes/秒</td>
                                <td>""" + test_result['Transfer_Rate'] + """ bytes/秒</td>
                            </tr>
                        """
    key_result_memo = """
    <!--key_result_memo-->  
    					<tr>
    						<td colspan=10 align="left">
    							1、Document Length：服务器处理请求后返回的响应数据长度</br>
    							2、Requests per second(RPS)：RPS，即服务器每秒处理的请求数量</br>
    							3、Time per request1：</br>
    							    &nbsp;&nbsp;a、从用户角度看，完成一个请求所需要的时间</br>
    							    &nbsp;&nbsp;b、体现1个连接（含多个请求）耗费的总时长，当于1个用户同时发送个多个并发请求给服务器并发处理后，得到这多个请求的响应数据的总时长</br>
    							4、Time per request2：
    							    &nbsp;&nbsp;a、服务器完成一个请求的时间。</br>
    							    &nbsp;&nbsp;b、体现1个连接多个请求中平均每一次请求的耗费时长，Time per request2=Time per request1/当前并发数。</br>
    							5、Transfer rate：网络传输速率，即平均每秒网络传输的数据量。该项有三个子项，received、sent、total(目前仅记录total)</br></td>
    					</tr>
    				</table>
                    """
    response_pct_title = """
    <!--response_pct_title-->  
    <!--这里是响应时间百分比分布-->                
                    <div class="table-tr-header">响应时间百分比分布</div>
                    <table class="table-content-item" border="1" cellspacing="0">
                        <tr>
                            <td> </td>
                            <td>Average</td>
                            <td>Min</td>
                            <td>50%</td>
                            <td>75%</td>
                            <td>80%</td>
                            <td style="background-color:LightSteelBlue">90%</td>
                            <td>95%</td>
                            <td>99%</td>
                            <td>Max</td>
                        </tr>
                        """
    response_pct_value = """"""
    for file_path in result_file_path_list:
        test_result = collect_date(file_path)  # return dic
        table_title = test_result['Test_Time_Taken'].split(".")[0] + """秒""" + test_result['User_Threads'] + """并发"""
        if "ab -n" in cmd_str:
            table_title = test_result['Complete_Requests'].split(".")[0] + """次""" + test_result[
                'User_Threads'] + """并发"""
        test_result = collect_date(file_path)  # return dic
        response_pct_value += """
    <!--response_pct_value-->   
                        <tr>
                            <td>""" + table_title + """</td>
                            <td>""" + test_result['Total_Mean'] + """毫秒</td>
                            <td>""" + test_result['Total_Min'] + """毫秒</td>
                            <td>""" + test_result['50%'] + """毫秒</td>
                            <td>""" + test_result['75%'] + """毫秒</td>
                            <td>""" + test_result['80%'] + """毫秒</td>
                            <td style="background-color:LightSteelBlue">""" + test_result['90%'] + """毫秒</td>
                            <td>""" + test_result['95%'] + """毫秒</td>
                            <td>""" + test_result['99%'] + """毫秒</td>
                            <td>""" + test_result['100%'] + """毫秒</td>
                        </tr>
                        """
    response_pct_memo = """
    <!--response_pct_memo-->   
    					<tr>
    						<td colspan=17 align="left">
    							1、一般较为关注90%的用户的响应时长，表示90%用户的请求所等待的时间不会超过的时间</br>
    							2、例如：当前接口中，90%的用户最长的等待时间不会超过""" + test_result['90%'] + """毫秒</br>
    							3、将所有请求的响应时间从小到大排序后，取列表中前百分比的所有请求时间，并取最大值。</br>
    						</td>
    					</tr>
                    </table>
                    
                    """
    connect_time_title = """
    <!--connect_time_title-->   
    <!--这里是响应时间分解表-->                
                    <div class="table-tr-header">响应时间分解表</div>
                    <table class="table-content-item" border="1" cellspacing="0">
                        <tr>
                            <td rowspan=2> </td>
                            <td colspan=5>Connect</td>
                            <td colspan=5>Processing</td>
                            <td colspan=5>Waiting</td>
                            <td colspan=5  style="background-color:LightSteelBlue">Total</td>
                        </tr>
                        <tr>
                            <td>min</td>
                            <td>mean</td>
                            <td>+/-sd</td>
                            <td>median</td>
                            <td>max</td>
                            <td>min</td>
                            <td>mean</td>
                            <td>+/-sd</td>
                            <td>median</td>
                            <td>max</td>
                            <td>min</td>
                            <td>mean</td>
                            <td>+/-sd</td>
                            <td>median</td>
                            <td>max</td>
                            <td style="background-color:LightSteelBlue">min</td>
                            <td style="background-color:LightSteelBlue">mean</td>
                            <td style="background-color:LightSteelBlue">+/-sd</td>
                            <td style="background-color:LightSteelBlue">median</td>
                            <td style="background-color:LightSteelBlue">max</td>
                        </tr>
                    
                    """
    connect_time_value = """"""
    for file_path in result_file_path_list:
        test_result = collect_date(file_path)  # return dic
        table_title = test_result['Test_Time_Taken'].split(".")[0] + """秒""" + test_result['User_Threads'] + """并发"""
        if "ab -n" in cmd_str:
            table_title = test_result['Complete_Requests'].split(".")[0] + """次""" + test_result[
                'User_Threads'] + """并发"""
        test_result = collect_date(file_path)  # return dic
        connect_time_value += """
    <!--connect_time_value-->   
                        <tr>
                            <td>""" + table_title + """</td>
                            <td>""" + test_result['Connect_Min'] + """毫秒</td>
                            <td>""" + test_result['Connect_Mean'] + """毫秒</td>
                            <td>""" + test_result['Connect_Sd'] + """毫秒</td>
                            <td>""" + test_result['Connect_Median'] + """毫秒</td>
                            <td>""" + test_result['Connect_Max'] + """毫秒</td>
                            <td>""" + test_result['Processing_Min'] + """毫秒</td>
                            <td>""" + test_result['Processing_Mean'] + """毫秒</td>
                            <td>""" + test_result['Processing_Sd'] + """毫秒</td>
                            <td>""" + test_result['Processing_Median'] + """毫秒</td>
                            <td>""" + test_result['Processing_Max'] + """毫秒</td>
                            <td>""" + test_result['Waiting_Min'] + """毫秒</td>
                            <td>""" + test_result['Waiting_Mean'] + """毫秒</td>
                            <td>""" + test_result['Waiting_Sd'] + """毫秒</td>
                            <td>""" + test_result['Waiting_Median'] + """毫秒</td>
                            <td>""" + test_result['Waiting_Max'] + """毫秒</td>
                            <td style="background-color:LightSteelBlue">""" + test_result['Total_Min'] + """毫秒</td>
                            <td style="background-color:LightSteelBlue">""" + test_result['Total_Mean'] + """毫秒</td>
                            <td style="background-color:LightSteelBlue">""" + test_result['Total_Sd'] + """毫秒</td>
                            <td style="background-color:LightSteelBlue">""" + test_result['Total_Median'] + """毫秒</td>
                            <td style="background-color:LightSteelBlue">""" + test_result['Total_Max'] + """毫秒</td>
                        </tr>
                        
                        """
    connect_time_memo = """
    					<tr>
    						<td colspan=21 align="left">
    							1、Connect：表示网络延时加上与远程服务器建立连接所耗费的时间</br>
    							2、Processing：表示第一个字节发出去至接受到第一个响应字节之间所耗费的时间, 这里大致可以推断出服务器的处理能力。</br>
    							3、Waiting：表示最后一个字节发送完至接受到第一个字节到响应时间间隔。</br>
    							4、Total：表示从建立连接开始至接受到第一个字节响应的总时间。</br>
    							5、mean：平均值。即一个页请求平均花费了多长时间。</br>
    							6、[+/-sd]：标准偏差。描述结果数据的波动大小。</br>
    							7、Total并不等于前三行数据相加，因为前三行的数据并不是在同一个请求中采集到的，所以Total是从整个请求所需要的时间的角度来统计的。</br>
    					</tr>
                    </table>
    			</div>
    			
    			"""

    return part_one_api_info + \
           key_result_title + key_result_value + key_result_memo + \
           response_pct_title + response_pct_value + response_pct_memo \
           + connect_time_title + connect_time_value + connect_time_memo


def get_report_file_list(cmd_str_list):
    report_file_list = []
    for cmd in cmd_str_list:
        report_file_list.append(cmd.split("> ")[1].split("sleep")[0])
    return report_file_list


def write_html(html_content):
    # report_file_name="Daily_单接口压测报告_"+datetime.datetime.strftime(datetime.datetime.now(), 'z%Y%m%d%_H%M%S')+".html"
    report_file_name = "Daily_单接口压测报告_" + time.strftime('%Y%m%d%H%M', time.localtime()) + ".html"
    report_file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/ReportFile/"
    with open(report_file_path + report_file_name, 'w', encoding="utf-8") as file:
        file.write(html_content)

# if __name__ == '__main__':
# HtmlReport.collect_date("/Users/panpan/Desktop/DDStudy/OcrDemo/1.txt",40)
# generate_report()
