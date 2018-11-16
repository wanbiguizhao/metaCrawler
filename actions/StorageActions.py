from models.metaData import NeeqNoticeMetaModel
class DBStorage:
    """将数据持久到数据库中，负责去重处理"""
    """ meta_data_obj 必须是NeeqNoticeMetaModel 实例化对象"""
    meta_data_list=[]
    def save():
        batch_data={}
        batch_insert_data=[meta_data_obj.to_dict() for meta_data_obj in meta_data_list]
        NeeqNoticeMetaModel.insert_many(batch_insert_data).execute()#执行批量存储
        meta_data_list=[]#释放数据
    def append_meta_data(meta_data_obj):
        """单个存储meta data"""
        if not isinstance(meta_data_obj,NeeqNoticeMetaModel):
            return "Error"
        if NeeqNoticeMetaModel.get_or_none(
            (NeeqNoticeMetaModel.uuid == '????') 
            ) is None:
            print "检查是否已经存在"
        else:
            self.meta_data_list.append(meta_data_obj)
        meta_data_list.append_meta_data(meta_data)
    def extend_meta_data(meta_data_list):
        """数组结构拓展队列"""
        for meta_data_obj in meta_data_list:
            self.append_meta_data(meta_data_obj)
        
