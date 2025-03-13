# 通用模块, 其中 _ 前缀为内置模块，其它模块将不进行引用
def _get_size():
    pass

def _get_hash():
    pass

def _path_filename():
    pass

def _get_metadata():
    pass

# 文件模块
class File(dict):
    """
    此模块将用于描述一个文件
    
    应当具有以下属性，并均在初始化阶段完成
    1. 文件的 hash 值
    2. 文件的大小 
    3. 文件的名字
    4. 文件的存放路径
    5. 文件的元数据
    
    应当具有以下方法
    1. 获取文件的内容
    """

    def __init__(self, file_path):
        pass

    def fetch(self):
        """
        获取文件二进制内容
        """

