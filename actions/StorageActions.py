from models.metaData import NeeqNoticeMetaModel

class DBStorage():
    """将数据持久化到数据库中
    1 将json对象转化为数据库的model。
    2 对数据进行去重，避免重复存储到数据库中。
    """
    """ meta_data_obj 必须是NeeqNoticeMetaModel 实例化对象"""
    meta_data_list=[]
    def save(self):
        batch_data={}
        batch_insert_data=[meta_data_obj.to_dict() for meta_data_obj in self.meta_data_list]
        if len(batch_insert_data)>0:
            NeeqNoticeMetaModel.insert_many(batch_insert_data).execute()#执行批量存储
        self.meta_data_list=[]#释放数据
    def append_meta_data(self,meta_data_obj):
        """单个存储meta data"""
        if not isinstance(meta_data_obj,NeeqNoticeMetaModel):
            return "Error"
        if NeeqNoticeMetaModel.get_or_none(
            NeeqNoticeMetaModel.uuid == meta_data_obj.uuid
            ) is None :
            self.meta_data_list.append(meta_data_obj)
        else:
            print(meta_data_obj.to_dict(),"检查是否已经存在")
    def extend_meta_data(self,meta_data_list):
        """数组结构拓展队列"""
        for meta_data_obj in meta_data_list:
            self.append_meta_data(meta_data_obj)
        
