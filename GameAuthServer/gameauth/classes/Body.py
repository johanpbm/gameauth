#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DGBLInstructionalDesign
import DigitalEducationalGame

class Body(object):
	def __init__(self):
		self._dgblInstructionalDesign = []
		# @AssociationType DGBLInstructionalDesign[]
		# @AssociationMultiplicity 1..*
		# @AssociationKind Aggregation
		self._digitalEducationalGame = []
		# @AssociationType DigitalEducationalGame[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Aggregation

