#!/usr/bin/python3
# -*- coding: utf-8 -*-

class CoreHandler():

    def __init__(self, in_name):
        self.name = in_name
        self.emotionStatus = 0
        print ("CoreHandler established.")
        
    def procCall(self, content):
        #fetch commands
        commandList = {"测试": 'test', '讲个笑话': 'joke'}
        for k,v in commandList.items():
            if '/' + k in content:
                return eval('self._command_' + v + "()")
    
    def _command_test(self):
        return 'Pong~'
        
    def _command_joke(self):
        return '高考成绩出来了，老师长出一口气对我说：其实没考上，对你和大学都是一种幸福。'