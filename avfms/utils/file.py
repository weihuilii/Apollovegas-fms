import os
import hashlib

file_path = 'test/test1.txt'

# 通用模块



def _get_path_filename(file_path):
    return os.path.dirname(file_path), os.path.basename(file_path)

def _get_metadata(file_path):
    return {
        'creation_time': os.path.getctime(file_path),
        'modification_time': os.path.getmtime(file_path),
        'access_time': os.path.getatime(file_path),
    }

# 文件模块
class File(dict):
    """
    此模块用于描述一个文件。
    
    具有以下属性，在初始化时完成：
    1. 文件的 hash 值
    2. 文件的大小 
    3. 文件的名字
    4. 文件的存放路径
    5. 文件的元数据
    
    具有以下方法：
    1. fetch() - 获取文件的二进制内容
    """
    
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件 {file_path} 不存在")
        
        self['file_path'] = file_path
        self['size'] = _get_size(file_path)
        self['hash'] = _get_hash(file_path)
        self['directory'], self['filename'] = _get_path_filename(file_path)
        self['metadata'] = _get_metadata(file_path)

    def _get_size(self):
        return os.path.getsize(self['file_path'])
    
    def _get_hash(self, algorithm='sha256'):
        hash_func = hashlib.new(algorithm)
        with open(self['file_path'], 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def _get_path_filename(self):
        return os.path.dirname(self['file_path']), os.path.basename(self['file_path'])

    def _get_metadata(self):
        return {
           'creation_time': os.path.getctime(self['file_path']),
           'modification_time': os.path.getmtime(self['file_path']),
           'access_time': os.path.getatime(self['file_path']),
        }
    
    def fetch(self):
        """
        获取文件二进制内容
        """
        with open(self['file_path'], 'rb') as f:
            return f.read()

# 示例用法
if __name__ == "__main__":
    file_path = 'test/test1.txt'
    try:
        file = File(file_path)
        print("文件信息:", file)
        content = file.fetch()
        print("文件内容:", content[:100])  # 只打印前 100 字节，防止太长
    except FileNotFoundError as e:
        print(e)
