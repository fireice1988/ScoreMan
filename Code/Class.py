#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 10:43
# @Author  : fireicezongzi
# @Site    : 
# @File    : Class.py
# @Software: PyCharm


class Class:
    def __init__(self, id, name):
        self.classid = id
        self.classname = name


    def getclassid(self):
        return self.classid

    def getclassname(self):
        return self.classname

    def setclassname(self,name):
        self.classname =name

    def setclassid(self,id):
        self.classid=id

class ClassList:
    def __init__(self):
        self.list=[]
    def addItem(self,item):
        self.append(item)
    def finditembyid(self,id):
        for item in self:
            if(item.classid ==id):
                return item
    