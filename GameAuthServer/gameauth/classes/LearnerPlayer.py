#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DEGTracking
import User

class LearnerPlayer(User):
	def __init__(self):
		self.___gameLevel = None
		"""@AttributeType string"""
		self.___gameScore = None
		"""@AttributeType string"""
		self._tracking = None
		# @AssociationType DEGTracking
		# @AssociationMultiplicity 0..1

