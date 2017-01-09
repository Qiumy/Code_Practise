# -*- coding:utf-8 -*-

import xlrd
import xml.dom.minidom as md

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_xls_data(filename):
     book = xlrd.open_workbook(filename, "rb")
     sheet = book.sheet_by_index(0)
     content = {}
     for i in range(sheet.nrows):
         content[i+1] = sheet.row_values(i)[1:]
     return content


def write_to_xml(xlscontent):

    xmlfile = md.Document()		#创建新xml文件

    root = xmlfile.createElement('root')		#创建节点
    students = xmlfile.createElement('students')		#创建节点

    xmlfile.appendChild(root)		#在文件中添加root节点
    root.appendChild(students)		#在root下添加students节点

    comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')		#创建评论
    students.appendChild(comment)		#在students标签下添加comment

    xmlcontent = xmlfile.createTextNode(str(xlscontent))		#创建文本节点
    students.appendChild(xmlcontent)		#在students标签下添加文本内容

    with open('students.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding = 'utf-8'))		#写入文件


write_to_xml(get_xls_data('students.xls'))

## example 2
from xlrd import open_workbook
from xml.dom import minidom
def write_data_to_xml(dict_conent):
    '''
    将 dict 格式数据写入 xml 文件
    '''
    xml_doc = minidom.Document()
    root = xml_doc.createElement('root')
    xml_doc.appendChild(root)
    city = xml_doc.createElement('city')
    root.appendChild(city)
    comment = xml_doc.createComment('城市信息')
    city.appendChild(comment)
    content = xml_doc.createTextNode(str(dict_conent))
    city.appendChild(content)

    with open('city.xml', 'wb') as f:
        f.write(xml_doc.toprettyxml(encoding='utf-8'))

def load_data_as_dict(f_path):
    '''
    从 Excel 文件中读取数据，以 dict 格式返回
    '''
    dict_conent = {}
    workbook = open_workbook(f_path, encoding_override='utf-8')
    sheet = workbook.sheet_by_name('city')
    for row in xrange(sheet.nrows):
        dict_conent[str(row + 1)] = str(sheet.row_values(row)[1:])
    return dict_conent

f_path = 'city.xls'
dict_conent = load_data_as_dict(f_path)
write_data_to_xml(dict_conent)

#example 3
def write_data_to_xml3(list_content):
    '''
    将 dict 格式数据写入 xml 文件
    '''
    xml_doc = minidom.Document()
    root = xml_doc.createElement('root')
    xml_doc.appendChild(root)
    numbers = xml_doc.createElement('numbers')
    root.appendChild(numbers)
    comment = xml_doc.createComment('数字信息')
    numbers.appendChild(comment)
    content = xml_doc.createTextNode(str(list_content))
    numbers.appendChild(content)

    with open('numbers.xml', 'wb') as f:
        f.write(xml_doc.toprettyxml(encoding='utf-8'))


def load_data_as_list3(f_path):
    '''
    从 Excel 文件中读取数据，以 list 格式返回
    '''
    workbook = open_workbook(f_path)
    list_content = []
    sheet = workbook.sheet_by_name('numbers')
    for row in xrange(sheet.nrows):
        list_content.append(sheet.row_values(row)[:])
    return list_content

f_path = 'numbers.xls'
list_content = load_data_as_list3(f_path)
write_data_to_xml3(list_content)