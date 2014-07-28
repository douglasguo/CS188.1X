#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: guoyinghao
# @Date:   2014-07-28 22:52:52
# @Last Modified by:   guoyinghao
# @Last Modified time: 2014-07-28 22:53:32
class Person:
    population = 0
    def __init__(self, myAge):
        self.age = myAge
        Person.population += 1
    def get_population(self):
        return Person.population
    def get_age(self):
        return self.age