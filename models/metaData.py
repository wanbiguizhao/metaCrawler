
class NeeqTaskMetaData:
    """创建下载公告时的约定的参数"""
    beg_date=""
    end_date=""
    companyCD=""
    keywords="关键字"
    """正则式，根据公告的标题，过滤想要的公告"""
    filterRegex=""
    disclosure_type=""

    def __init__(self,dict_data):
        for key in dict_data:
            setattr(self,key,dict_data[key])
    """返回公告类型对应的参数值"""
    def get_disclosure_type(self):
        return {
            "临时公告":"1",
            "定期报告":"2"
        }.get(self.disclosure_type,"5")
    def get_beg_date(self):
        return self.beg_date
    def get_end_date(self):
        return self.get_end_date
    def get_companyCD(self):
        return self.companyCD
    def get_keywords(self):
        return self.keywords
    def get_filterRegex(self):
        return self.filterRegex

class NeeqWebDownloadResultData:
    """download成功后，返回的源数据"""
    """源数据，存放json格式的数据"""
    meta_data={}
    def get_company_name():
        pass
    def get_company_code():
        pass
    
    def get_disclosure_name():
        pass
    def get_disclosure_url():
        pass
    def toString():
        pass

class NeeqNoticeMetaModel:
    json_meta_data="原来的json原始数据"
    meta_str_data=""#metaData str格式的数据情况
    uuid="数据唯一的id"
    company_code="公司代码"
    company_name="公司名称"
    title="公告标题"
    pub_date="发布日期"

    pdf_link="pdf的下载链接"
    pdf_download_flag="下载标志位"
    pdf_local_path="本地下载路径"

    category="公告分类格式|类别1|类别2|类别3|"
    category_flag="是否分类"

    pdf2xml_flag="是否做完成pdf2xml"
    xml2txt_flag="xml2txt_flag"
    xml2wtable_flag="xml2wtable_flag"

    update_datetime="更新时间"
    createDatetime="创建时间"

    def load_meta_data(self,jsonData):
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
    #将json数据转化为str类型的数据。
    self.company_code=jsonData["companyCd"]
    self.company_name=jsonData["companyName"]
    self.title=jsonData["disclosureTitle"]
    self.pub_date=jsonData["publishDate"]
    pass

    def reset_download_flag(self):
        self.pdf_download_flag=False;
        self.save()

    def to_dict(self):#将数据转化为容易批量处理的存储的数据
        """把定义好的各个字段"""
        return {

        }
