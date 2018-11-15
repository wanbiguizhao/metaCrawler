



class NeeqTaskMetaData:
    """创建下载公告时的约定的参数"""
    beg_date=""
    end_date-""
    companyCD=""
    keywords=""
    """正则式，根据公告的标题，过滤想要的公告"""
    filterRegex=""
    disclosure_type=""
    disclosure_value=""
    disclosure_value_type_mapping={
        "":,
    }

    def __init__(self):
        pass
    """返回公告类型对应的参数值"""
    def get_disclosure_value(self):
        return {
            "临时公告":"1",
            "定期报告":"2"
        }.get(self.disclosure_type,"5")
    
    def get_beg_date(self):
        return self.beg_date

    def get_end_date(self):
        return self.get_end_date
    
    def get_companyCD(self):
        return self.keywords
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
