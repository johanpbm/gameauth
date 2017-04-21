#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Course
import ProcessToDevelop
import AssessmentCriterion

class DGBLInstructionalDesign(object):
	def __init__(self):
		self.___grade = None
		"""@AttributeType string"""
		self.___description = None
		"""@AttributeType string"""
		self.___time = None
		"""@AttributeType string"""
		self._course = None
		# @AssociationType Course
		# @AssociationMultiplicity 1
		self._processToDevelop = []
		# @AssociationType ProcessToDevelop[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Aggregation
		self._assessmentCriterion = []
		# @AssociationType AssessmentCriterion[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Aggregation

