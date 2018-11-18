from peewee import *
from models import dataxdb
from datetime import date

class NeeqTaskMetaData:
    """创建下载公告时的约定的参数"""
    beg_date = ""
    end_date = ""
    companyCD = ""
    keywords = "关键字"
    """正则式，根据公告的标题，过滤想要的公告"""
    filterRegex = ""
    disclosure_type = ""

    def __init__(self, dict_data):
        for key in dict_data:
            setattr(self, key, dict_data[key])

    """返回公告类型对应的参数值"""

    def get_disclosure_type(self):
        return {
            "临时公告": "1",
            "定期报告": "2"
        }.get(self.disclosure_type, "5")

    def get_beg_date(self):
        year,month,day=self.beg_date.split("-")
        return date(year=int(year),month=int(month),day=int(day))

    def get_end_date(self):
        year,month,day=self.end_date.split("-")
        return date(year=int(year),month=int(month),day=int(day))

    def get_companyCD(self):
        return self.companyCD

    def get_keywords(self):
        return self.keywords

    def get_filterRegex(self):
        return self.filterRegex


class NeeqWebDownloadResultData:
    """download成功后，返回的源数据"""
    """源数据，存放json格式的数据"""
    meta_data = {}

    def get_company_name(self):
        pass

    def get_company_code(self):
        pass

    def get_disclosure_name(self):
        pass

    def get_disclosure_url(self):
        pass

    def toString(self):
        pass


class NeeqNoticeMetaModel(Model):
    json_meta_data = {}  # "原来的json原始数据"
    meta_str_data = CharField(max_length=500)  # metaData str格式的数据情况
    uuid = CharField()  # "数据唯一的id"
    company_code = CharField()  # "公司代码"
    company_name = CharField()  # "公司名称"
    title = CharField()  # "公告标题"
    pub_date = CharField()  # "发布日期"

    pdf_link = CharField()  # "pdf的下载链接"
    pdf_download_flag = CharField()  # "下载标志位"
    pdf_local_path = CharField()  # "本地下载路径"

    category = CharField()  # "公告分类格式|类别1|类别2|类别3|"
    category_flag = CharField()  # "是否分类"

    pdf2xml_flag = CharField()  # "是否做完成pdf2xml"
    xml2txt_flag = CharField()  # "xml2txt_flag"
    xml2wtable_flag = CharField()  # "xml2wtable_flag"

    update_datetime = CharField()  # "更新时间"
    createDatetime = CharField()  # "创建时间"

    class Meta:
        database = dataxdb  # this model uses the "people.db" database

    def load_meta_data(self, jsonData):
        """
        {
                    "companyCd":"835675",
                    "companyName":"蓝色方略",
                    "dKey":"",
                    "destFilePath":"/disclosure/2018/2018-11-16/1542353411_107874.pdf",
                    "disclosureCode":"97f8e58666d41c0c01671b04e42f3a24",
                    "disclosurePostTitle":"（更正后）",
                    "disclosureSubType":"",
                    "disclosureTitle":"[临时公告]蓝色方略:收购报告书之财务顾问报告",
                    "disclosureType":"9504",
                    "disclosureYear":0,
                    "fileExt":"pdf",
                    "filePath":"",
                    "isEmergency":1,
                    "isNewThree":1,
                    "modifyTimes":0,
                    "publishDate":"2018-11-16",
                    "publishOrg":"9601-1003",
                    "state":1,
                    "upDate":{
                        "date":16,
                        "day":5,
                        "hours":15,
                        "minutes":30,
                        "month":10,
                        "seconds":11,
                        "time":1542353411000,
                        "timezoneOffset":-480,
                        "year":118
                    },
                    "xxfcbj":"0"
                }
        """
        # 将json数据转化为str类型的数据。
        self.company_code = jsonData["companyCd"]
        self.company_name = jsonData["companyName"]
        self.title = jsonData["disclosureTitle"]
        self.pub_date = jsonData["publishDate"]


    def reset_download_flag(self):
        self.pdf_download_flag = False;
        self.save()

    def to_dict(self):  # 将数据转化为容易批量处理的存储的数据
        """把定义好的各个字段"""
        return {
            "meta_str_data":self.meta_str_data,
            "uuid":self.uuid
        }


if __name__ == "__main__":
    dataxdb.connect()
    dataxdb.create_tables([NeeqNoticeMetaModel, ])
    task_obj = NeeqTaskMetaData({"beg_date":"2015-10-09"})
    print(task_obj.beg_date)
