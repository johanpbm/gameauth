#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Subject

class Course(object):
	def __init__(self):
		self.___name = None
		"""@AttributeType string"""
		self.___description = None
		"""@AttributeType string"""
		self._subject = []
		# @AssociationType Subject[]
		# @AssociationMultiplicity 1..*
		# @AssociationKind Aggregation

