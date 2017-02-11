#!/usr/bin/env python
#coding: utf-8

import pickle
import os

teacher_lst = []
course_lst = []

class Teacher:
    """
    创建老师角色
    """
    def __init__(self, name, sex, age):
        """
        创建教师角色类
        :param name: 教师名字
        :param sex: 性别
        :param age: 年龄
        """
        self.name = name
        self.gender = sex
        self.age = age

    def get_teacher_name(self):
        return self.name

class Course:
    """
    创建课程类
    """
    def __init__(self, course_name, time, cost, teacher):
        """
        初始化课程类
        :param course_name: 课程名称
        :param time: 上课时间
        :param cost: 课时费
        :param tercher: 代课老师对象
        """
        self.course_name = course_name
        self.start_course_time = time
        self.course_cost = cost
        self.teacher = teacher

def create_teacher():
    name = raw_input("请输入要创建教师的姓名：\n")
    gender = raw_input("请输入要创建教师的性别（M（男），F（女））\n")
    age = int(raw_input("请输入要创建教师的年龄：\n"))
    teacher = Teacher(name, gender, age)
    teacher_lst.append(teacher)

def create_course():
    course_name = raw_input("请输入要创建的课程名称：\n")
    course_start_time = raw_input("请输入课程上课时间：\n")
    course_cost = float(raw_input("请输入课时费：\n"))
    teacher_name = raw_input("请输入代课老师名称:\n")
    for teacher_obj in teacher_lst:
        if teacher_obj.get_teacher_name() == teacher_name:
            course = Course(course_name, course_start_time, course_cost, teacher_obj)
            course_lst.append(course)
            break
    else:
        print "没有相应的老师，请先创建教师！"


if __name__ == "__main__":
    if os.path.isfile("teacher.txt"):
        teacher_lst = pickle.load(open("teacher.txt", "rb"))
    if os.path.isfile("course.txt"):
        course_lst = pickle.load(open("course.txt", "rb"))
    if teacher_lst:
        for teacher_obj in teacher_lst:
            print teacher_obj.name, teacher_obj.gender, teacher_obj.age
    if course_lst:
        for course_obj in course_lst:
            print course_obj.course_name, course_obj.start_course_time, course_obj.course_cost, course_obj.teacher.get_teacher_name()

    while True:
        choice = raw_input("请输入要创建的内容：1.教师 2.课程 其他：退出\n")
        if choice == "1":
            create_teacher()

        elif choice == "2":
            create_course()

        else:
            choice_quit = raw_input("确定要退出？y/n\n")
            if choice_quit.upper().startswith("Y"):
                pickle.dump(teacher_lst, open("teacher.txt", "wb"))
                pickle.dump(course_lst, open("course.txt", "wb"))
                break
            else:
                continue
                pickle.dump(student_lst, open("student.txt", "wb"))