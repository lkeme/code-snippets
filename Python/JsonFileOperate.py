import json

# 将字典类型数据写入json文件或读取json文件并转为字典格式输出


class FileOperate:
    '''
    需要传入文件所在目录，完整文件名。
    默认为只读，并将json文件转换为字典类型输出
    若为写入，需向dictData传入字典类型数据
    默认为utf-8格式
    '''

    def __init__(self, filepath, filename, way='r', dictData=None, encoding='utf-8'):
        self.filepath = filepath
        self.filename = filename
        self.way = way
        self.dictData = dictData
        self.encoding = encoding

    def operation_file(self):
        if self.dictData:
            self.way = 'w'
        with open(self.filepath + self.filename, self.way, encoding=self.encoding) as f:
            if self.dictData:
                print(self.dictData)
                f.write(json.dumps(self.dictData, ensure_ascii=False))
            else:
                if '.json' in self.filename:
                    data = json.loads(f.read())
                else:
                    data = f.read()
                return data


if __name__ == '__main__':
    # writer
    dict_data = {"a": "1"}
    FileOperate(dictData=dict_data, filepath='./data/',
                filename='test.json').operation_file()
    # reader
    dict_data1 = FileOperate(
        filepath='./data/', filename='test.json').operation_file()
