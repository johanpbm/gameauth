#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ILO

class Subject(object):
	def __init__(self):
		self.___name = None
		"""@AttributeType string"""
		self.___description = None
		"""@AttributeType string"""
		self._subject = []
		# @AssociationType Subject[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Aggregation
		self._ilo = []
		# @AssociationType ILO[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Aggregation

