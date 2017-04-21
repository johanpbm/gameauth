#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Fraction
import Fractions

class FractionAddition(object):
	def __init__(self):
		self.___summandsQuantity = None
		"""@AttributeType int"""
		self._resultantFraction = None
		# @AssociationType Fraction
		# @AssociationMultiplicity 0..1
		self._fractions = None
		# @AssociationType Fractions
		# @AssociationMultiplicity 1
		# @AssociationKind Aggregation

