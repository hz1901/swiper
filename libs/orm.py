from datetime import date, time , datetime


def model_to_dict(model_obj, ignore=()):
    '''
    将一个model对象转换成字典

    '''
    att_dict = {}
    for field in model_obj._meta.fields:
        name = field.attname                 # 获取字段名
        value = getattr(model_obj, name)      #获取对象属性
        if name in ignore:
            continue
        # print(name,value)
        # 检查传入的数据能否被序列化
        if isinstance(value, (datetime, date,time)):
            att_dict[name] = str(value)
        else:
            att_dict[name] = value    # 生成字典
    return att_dict