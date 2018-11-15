from Interface.IDownloadInterface import IDownloadAction
from models.metaData import NeeqTaskMetaData

class NeeqWebDownloadAction(IDownloadAction):
    downloadurl=""
    requestobj=None #下载对象
    action_task_meta_data="";#执行下载的参数
    current_response_data=""#爬取报文后得到的源数据。
    current_post_form_data=""#发送post的数据。
    current_header_data=""#发送post涉及的header
    download_data_set=[NeeqTaskMetaData()]#存储下载数据的list。

    """初始化化函数"""
    def __init__(self):
        pass

    """重新初始化下载参数"""
    def reset_action_common(self,NeeqTaskMetaDataObj):
        self.action_task_meta_data=NeeqTaskMetaDataObj
        self.download_data_set=[]

    def execute_action(self,NeeqTaskMetaDataObj):
        self.action_task_meta_data=NeeqTaskMetaDataObj
        self.download_data_set=[]
        while not self.in_stop_status():
            self.request_action()
            self.analysis_message_action()
        return self.download_data_set
        
    def request_action(self):
        """发送web请求，获得返回内容"""]
        paydata=make_form_data()
        #执行request函数

    def make_form_data(self):
        """生成web请求需要的form数据"""
        pass

    def analysis_message_action(self):
        """分析报文，对报文内容进行拆分，可以重新生成form data ，header，填充数据，"""
        split_message_action()


    def split_message_action(self,):
        """拆分获取的报文，将报文转化为转为为不同的状态"""
    pass

    def in_stop_status():
        pass