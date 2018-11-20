from models.metaData import NeeqNoticeMetaModel


class PDFDBManager:
    """根据下载的命令下载数据，一次只下载一个pdf，并且返回pdf文件的下载路径，文件名"""

    @classmethod
    def get_undownload_pdf_list(cls, beg_date, end_date):
        """提供未下载的pdf的数据"""
        data_list = NeeqNoticeMetaModel.select().where(
            (NeeqNoticeMetaModel.pub_date >= beg_date) &
            (NeeqNoticeMetaModel.pub_date <= end_date) &
            (NeeqNoticeMetaModel.pdf_download_flag == False)
        )
        return data_list


if __name__ == "__main__":
    print("helloworld")
    print(
        len(PDFDBManager.get_undownload_pdf_list(beg_date="2018-10-09", end_date="2018-11-09"))
    )
