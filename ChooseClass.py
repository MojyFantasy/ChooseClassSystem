#!/usr/bin/env python
#coding: utf-8

import pickle
import os

from ClassManager import Course, Teacher

student_lst = []

class Student:
    """
    创建一个学生类
    """
    def __init__(self, name, sex, passwd, age):
        """
        初始化一个学生类
        :param name: 学生姓名
        :param passwd: 用户名密码
        :param sex: 学生性别
        :param age: 学生年龄
        """
        self.name = name
        self.gender = sex
        self.passwd = passwd
        self.age = age
        self.course_lst = []

def register(name, sex, passwd, age):
    student_lst.append(Student(name, sex, passwd, age))

def login(name, passwd):
    """
    学生登录
    :param name: 学生姓名
    :param passwd: 密码
    :return: 是否登录成功
    """
    for student_obj in student_lst:
        if student_obj.name == name and student_obj.passwd == passwd:
            return True, "", student_obj
        else:
            return False, "密码错误，请重试！", None
    else:
        return False, "用户名不存在！", None

if __name__ == "__main__":
    if os.path.isfile("student.txt"):
        student_lst = pickle.load(open("student.txt"))

    while True:
        choice_login = raw_input("请选择：\n1.登录\n2.注册\n其他.退出\n")
        if choice_login == "1":
            name = raw_input("请输入用户名：\n")
            passwd = raw_input("请输出密码：\n")
            ret, msg, student_obj = login(name, passwd)
            if ret == True:
                student_now = student_obj
                while True:
                    for course_obj in student_now.course_lst:
                        print course_obj.course_name
                    print "选课列表："
                    course_lst = pickle.load(open("course.txt", "rb"))
                    for course_obj in course_lst:
                        print course_obj.course_name
                    choice_course = raw_input("请输入要选择的课程：\n")
                    for course_obj in course_lst:
                        if choice_course == course_obj.course_name:
                            student_now.course_lst.append(course_obj)
                            break
                    else:
                        print "选课失败！"
                    choice = raw_input("继续选课？y/n")
                    if choice.upper().startswith("Y"):
                        pass
                    else:
                        break
            else:
                print msg
                continue
        elif choice_login == "2":
            name = raw_input("请输入用户名：\n")
            passwd = raw_input("请输入密码：\n")
            gender = raw_input("请选择性别（M:男，F:女）：\n")
            age = int(raw_input("请输入年龄：\n"))
            if name and passwd and gender and age:
                student_lst.append(Student(name, gender, passwd, age))
            else:
                print "注册失败，不能为空！"
                continue
        else:
            pickle.dump(student_lst, open("student.txt", "wb"))
            exit(0)


    