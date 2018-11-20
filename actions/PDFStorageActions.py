import requests
import json
import os

class PDFDownloadActions:
    """根据下载的命令下载数据，一次只下载一个pdf"""
    file_uri=""
    local_path=""
    def reset_action_commond(self,meta):
        """根据下载命令重置系统状态，私有方法"""
        """
        meta 的结构，pdf的uuid
        {
        "uuid":"",
        "download_link":"下载连接",
        "local_path":"下载的路径",
        "filename":"下载文件名称",
        
        }
        """
        pass
    def execute_action(self,action_meta):
        """执行下载任务，返回下载结果"""
        self.reset_action_commond(action_meta)

    def check_local_path(self):
        """检查文件夹路径是否存在，如果不存在创建路径"""
        pass
