
from models.metaData import NeeqTaskMetaData
import requests
import json
class NeeqWebDownloadAction:
    downloadurl="http://www.neeq.com.cn/disclosureInfoController/infoResult.do"
    action_task_meta_data="";#执行下载的参数
    current_status="init"#init,runing,stop
    current_response_json_data=""#爬取报文后得到的源数据。
    current_post_form_data={
    "disclosureType": "5",
    "page": "0",
    "companyCd":"" ,
    "isNewThree": "1",
    "startTime": "2018-10-17",
    "endTime": "2018-11-16",
    "keyword": "关键字",
    "xxfcbj": ""
    }
    current_header_data=""#发送post涉及的header
    download_data_list=[]#存储下载数据的list。

    """初始化化函数"""
    def __init__(self):
        pass

    """重新初始化下载参数"""
    def reset_action_commond(self,NeeqTaskMetaDataObj):
        self.current_post_form_data["disclosureType"]=NeeqTaskMetaDataObj.get_disclosure_type()
        self.current_post_form_data["companyCd"]=NeeqTaskMetaDataObj.get_companyCD()
        self.current_post_form_data["keyword"]=NeeqTaskMetaDataObj.get_keywords()
        self.current_post_form_data["startTime"]=NeeqTaskMetaDataObj.get_beg_date().strftime("%Y-%m-%d")
        self.current_post_form_data["endTime"]=NeeqTaskMetaDataObj.get_end_date().strftime("%Y-%m-%d")

    def execute_action(self,NeeqTaskMetaDataObj):
        if not isinstance(NeeqTaskMetaDataObj,NeeqTaskMetaData):
            return []
        self.reset_action_commond(NeeqTaskMetaDataObj)
        self.download_data_set=[]
        while not self.in_stop_status():
            self.request_action()
            self.analysis_message_action()
        return self.download_data_list
        
    def request_action(self):
        """发送web请求，获得返回内容"""
        #paydata=self.make_form_data()
        response=requests.post(self.downloadurl,data=self.current_post_form_data)
        self.current_response_json_data=json.loads(response.text[5:-1],encoding="utf-8")[0]#获得json函数。
        #执行request函数

    def make_form_data(self):
        """生成web请求需要的form数据"""
        self.current_post_form_data["page"]=0
        return self.current_post_form_data
        

    def analysis_message_action(self):
        """分析报文，对报文内容进行拆分，可以重新生成form data ，header，填充数据，"""
        firstPage=self.current_response_json_data['listInfo']['firstPage']
        lastPage=self.current_response_json_data['listInfo']['lastPage']
        number=self.current_response_json_data['listInfo']['number']
        size=self.current_response_json_data['listInfo']['size']
        totalElements=self.current_response_json_data['listInfo']['totalElements']
        totalPages=self.current_response_json_data['listInfo']['totalPages']
        numberOfElements = self.current_response_json_data['listInfo']['numberOfElements']

        if lastPage==True:
            self.current_status="stop"
        if numberOfElements<size:
            self.current_status="stop"
        self.current_post_form_data["page"]=number+1
        self.download_data_list.extend(self.current_response_json_data['listInfo']['content']) 


    def in_stop_status(self):
        return self.current_status=="stop"

if __name__ == "__main__":
    task_obj=NeeqTaskMetaData()
    task_obj.beg_date