from actions.PDFDBActions import PDFDBManager
from actions.PDFStorageActions import NeeqPDFDownloadActions
from copy import copy
from datetime import datetime, date, timedelta


class PDFTaskManager:
    """负责接收下载命令，调度下载和存储进度。"""
    date_list = []
    task_meta_data_obj = None
    storage_obj = NeeqPDFDownloadActions()

    def run_task(self, beg_date, end_date):
        to_download_list = PDFDBManager.get_undownload_pdf_list(beg_date=beg_date
                                                                , end_date=end_date)
        for obj in to_download_list:
            result = self.storage_obj.execute_action(action_meta=
            {
                "uuid": obj.uuid,
                "origin_url": "http://www.neeq.com.cn",
                "download_link": obj.pdf_link,
            }
            )
            if result["status"] == "200":
                obj.pdf_download_flag = True
                obj.pdf_local_path = result["local_file_path"]
                obj.save()


if __name__ == "__main__":
    task = PDFTaskManager()
    taskMetaDataobj = ""  # 根据参数生成命令
    task.run_task(beg_date="2018-10-19",end_date="2018-11-20")
