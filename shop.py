
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: guoyinghao
# @Date:   2014-07-28 21:09:34
# @Last Modified by:   guoyinghao
# @Last Modified time: 2014-07-28 21:34:49

class FruitShop:
	"""name: Name for the fruit shop

		fruitPrices: Dictionary with keys as fruit
		strings and prices for values e.g.
		{'apples': 2.00, 'oranges':1.50, 'pears', 1.75}
	"""
	def __init__(self, name, fruitPrices):
		self.fruitPrices=fruitPrices
		self.name=name
		print 'Welcome to %s fruit shop' % (name)

	def getCostPerPound(self, fruit):
		if fruit not in self.fruitPrices:
			print "sorry we don't have %s" % (fruit)
			return None
		return self.fruitPrices[fruit]

	def getPriceOfOrder(self, orderList):
		totalCost=0.0
		for fruit, numPounds in orderList:
			costPerPound = self.getCostPerPound(fruit)
			if costPerPound!=None:
				totalCost+= numPounds*costPerPound
		return totalCost

	def getName(self):
		return self.name


