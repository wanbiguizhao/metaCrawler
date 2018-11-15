from models.metaData import NeeqTaskMetaData,NeeqWebDownloadResultData
from actions.DownLoadActions import NeeqWebDownloadAction
from actions.StorageActions import PGDBStorage
from copy import copy

class MetaTaskManager：
"""
负责接收下载命令，调度下载和存储进度。
"""
    date_list=[]
    task_meta_data_obj=NeeqTaskMetaData()
    downloadActions_obj=NeeqWebDownloadAction()
    storge_obj=PGDBStorage()
    def run_task(self,taskMetaDataobj):
        self.analysis_task_meta()
        for date_day in self.date_list:
            new_task_data_obj=copy(taskMetaDataobj)
            new_task_data_obj.beg_date=date_day
            new_task_data_obj.end_date=date_day#将周期变成变天下载。

            download_data_set=self.downloadActions_obj.execute_action(new_task_data_obj)
            storge_obj.append_meta_data(download_data_set)
            
            storge_obj.save()
    def analysis_task_meta(self):
        pass
        """按照日子将天数拆分成数组，每天取一次数据"""

#各种命令行或者其他的接口
def all_commond_action():
    task=MetaTaskManager()
    taskMetaDataobj=""#根据参数生成命令
    task.run_task(taskMetaDataobj)
    pass
