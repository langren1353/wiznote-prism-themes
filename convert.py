import os
from os.path import join

ori_dir = './ori_themes'
output_dir = './themes'

def convert_all():
    for filename in os.listdir(ori_dir):
        if filename.endswith('.css'):
            convert_one(filename)

def convert_one(filename):
    with open(join(ori_dir, filename), 'r') as file:
        file_content = file.read()

    # 替换文本
    file_content = file_content.replace('pre[class*="language-"]', '.code-block')
    keys = getReplaceKeys()
    for pre, after in keys:
        file_content = file_content.replace(pre, after)

    # 写入替换后的内容
    with open(join(output_dir, filename), 'w') as file:
        file.write(file_content)

def getReplaceKeys():
    list = ['token', 'block-comment', 'comment', 'prolog', 'doctype', 'cdata', 'punctuation', 'property', 'tag', 'boolean', 
            'number', 'function-name', 'constant', 'symbol', 'deleted', 'selector', 'attr-name', 'string', 'char', 'function', 
            'builtin', 'inserted', 'operator', 'entity', 'url', 'variable', 'atrule', 'attr-value', 'keyword', 'class-name', 
            'regex', 'important', 'bold', 'italic', 'namespace']
    return [(i, 'style-'+i) for i in list]

if __name__ == '__main__':
    convert_all()
