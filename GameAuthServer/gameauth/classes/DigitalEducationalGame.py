#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Educator
import Developer
import Recorder
import LearnerPlayer
import DEGDataTypes
import DEGLevels

class DigitalEducationalGame(object):
	def __init__(self):
		self.___name = None
		"""@AttributeType string"""
		self.___description = None
		"""@AttributeType string"""
		self.___goal = None
		"""@AttributeType string"""
		self._authoredBy = []
		# @AssociationType Educator[]
		# @AssociationMultiplicity 0..*
		self._developedBy = []
		# @AssociationType Developer[]
		# @AssociationMultiplicity 1..*
		self._recorderedBy = []
		# @AssociationType Recorder[]
		# @AssociationMultiplicity 1..*
		self._player = []
		# @AssociationType LearnerPlayer[]
		# @AssociationMultiplicity 0..*
		self._dataTypes = []
		# @AssociationType DEGDataTypes[]
		# @AssociationMultiplicity 0..*
		self._degLevels = None
		# @AssociationType DEGLevels
		# @AssociationMultiplicity 1

