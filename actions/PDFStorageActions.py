import requests
import json
import os


class NeeqPDFDownloadActions:
    """根据下载的命令下载数据，一次只下载一个pdf，并且返回pdf文件的下载路径，文件名"""
    file_uri = ""
    local_dir_path = ""
    filename = ""
    pre_path=""#绝对路径

    def reset_action_commond(self, meta):
        """根据下载命令重置系统状态，私有方法"""
        """
        meta 的结构，pdf的uuid
        {
        "uuid":"",
        "origin_url":"http://www.neeq.com.cn",
        "download_link":"/disclosure/2018/2018-10-12/1539336345_253551.pdf",
        }
        """
        self.file_uri = meta["origin_url"] + meta["download_link"]
        file_name_list = meta["download_link"].split("/")
        self.local_dir_path = "/".join(file_name_list[1:-1])
        self.filename = file_name_list[-1]
        pass

    def execute_action(self, action_meta):
        """执行下载任务，返回下载结果"""
        self.reset_action_commond(action_meta)
        self.check_local_path()  # 做文件下载路径检查
        r = requests.get(self.file_uri, stream=True)
        with open(self.get_abs_file_name(), "wb") as fd:
            for chunk in r.iter_content(chunk_size=20):
                fd.write(chunk)
        return {
            "status": "200",
            "msg": "success",
            "local_file_path": self.get_abs_file_name(),
        }

    def check_local_path(self):
        """检查文件夹路径是否存在，如果不存在创建路径"""
        if not os.path.exists(self.get_local_path()):
            os.makedirs(self.get_local_path())


    def get_abs_file_name(self):
        return self.pre_path+self.local_dir_path+"/"+self.filename

    def get_local_path(self):
        return self.local_dir_path
if __name__ == "__main__":
    print("helloworld")
    action=NeeqPDFDownloadActions()
    action.execute_action({
        "uuid": "xxxxxxxx",
        "origin_url": "http://www.neeq.com.cn",
        "download_link": "/disclosure/2018/2018-10-12/1539336345_253551.pdf",
    })
