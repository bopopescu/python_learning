# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/04/08 22:46:15
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：测试
'''
import unittest
from random import randint
from s1_dog import dog
from s2_students import Student
from tools import random_name
from s3_dictclass import dictclass
from s4_student_private import Student4
# here put the import lib

class dogTest(unittest.TestCase):

    dog1=dog()
    nums=[20,30,40]
    color=["white","black","pink"]

    def test_sold(self):
        n=randint(2,3)
        q=randint(0,2)
        for j in range(n):
            w=randint(1,6)
            self.dog1.sold(self.color[q],w)
            self.nums[q]-=w
        for e in range(3):
            self.assertEqual(self.nums[e],self.dog1.members[e]["number"])

class studentTest(unittest.TestCase):
    def setUp(self):
        self.name=random_name()
        self.age=randint(18,22)
        self.score=[]
        for i in range(3):
            self.score.append(randint(60,100))
        self.stu=Student(self.name,self.age,self.score[0],self.score[1],self.score[2])

    def tearDown(self):
        for i in self.score:
            self.score.remove(i)

    def test_name(self):
        self.assertEqual(self.name,self.stu.getname())

    def test_age(self):
        self.assertEqual(self.age,self.stu.getage())

    def test_score(self):
        self.assertEqual(max(self.score),self.stu.get_course())

class student4Test(unittest.TestCase):
    sex=["男","女"]
    def setUp(self):
        self.name=random_name()
        self.age=randint(18,22)
        self.sexnum=randint(0,1)
        self.score=[]
        for i in range(3):
            self.score.append(randint(60,100))
        self.stu=Student4(self.name,self.age,self.sex[self.sexnum],self.score[0],self.score[1],self.score[2])

    def tearDown(self):
        for i in self.score:
            self.score.remove(i)

    def test_score(self):
        self.assertEqual(sum(self.score),self.stu.sum_score())
        self.assertEqual(sum(self.score)/len(self.score),self.stu.average_score())
        self.stu.print_data()

if __name__ == "__main__":
    suite=unittest.TestSuite()
    for i in range(100):
        # suite.addTest(dogTest('test_sold'))
        # suite.addTests([studentTest('test_name'),studentTest('test_age'),studentTest('test_score')])
        suite.addTest(student4Test('test_score'))
    unittest.TextTestRunner().run(suite)