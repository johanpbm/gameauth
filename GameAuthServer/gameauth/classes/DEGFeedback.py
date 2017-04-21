#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DEGGameObject

class DEGFeedback(object):
	def __init__(self):
		self.___name = None
		"""@AttributeType string"""
		self.___description = None
		"""@AttributeType string"""
		self.___message = None
		"""@AttributeType string"""
		self._gameObjects = []
		# @AssociationType DEGGameObject[]
		# @AssociationMultiplicity 0..*

