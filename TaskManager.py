from models.metaData import NeeqTaskMetaData,NeeqWebDownloadResultData
from actions.DownLoadActions import NeeqWebDownloadAction
from actions.StorageActions import DBStorage
from copy import copy
from datetime import  datetime,date,timedelta

class MetaTaskManager:
    """负责接收下载命令，调度下载和存储进度。"""
    date_list=[]
    task_meta_data_obj=None
    downloadActions_obj=NeeqWebDownloadAction()
    storge_obj=DBStorage()
    def run_task(self,taskMetaDataobj):
        self.task_meta_data_obj=copy(taskMetaDataobj)
        self.analysis_task_meta()
        for date_day in self.date_list:
            new_task_data_obj=copy(taskMetaDataobj)
            new_task_data_obj.beg_date=date_day.strftime("%Y-%m-%d")
            new_task_data_obj.end_date=date_day.strftime("%Y-%m-%d")#将周期变成变天下载。

            download_data_set=self.downloadActions_obj.execute_action(new_task_data_obj)
            self.storge_obj.extend_meta_data(download_data_set)
            
            self.storge_obj.save()
    def analysis_task_meta(self):
        """按照日子将天数拆分成数组，每天取一次数据"""
        beg_date=self.task_meta_data_obj.get_beg_date()
        end_date=self.task_meta_data_obj.get_end_date()
        x=(end_date-beg_date).days
        self.date_list=[beg_date+timedelta(days=dd) for dd in range(x)]
        print(self.date_list)




#各种命令行或者其他的接口
def all_commond_action():
    task=MetaTaskManager()
    taskMetaDataobj=""#根据参数生成命令
    task.run_task(taskMetaDataobj)
    pass

if __name__ == "__main__":
    task_obj = NeeqTaskMetaData({"beg_date":"2018-10-09","end_date":"2018-10-19","keywords":"国"})
    task = MetaTaskManager()
    taskMetaDataobj = ""  # 根据参数生成命令
    task.run_task(task_obj)
    print(task_obj.beg_date)
