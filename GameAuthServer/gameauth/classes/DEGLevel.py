#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DEGMissions
import DEGLevels
import DEGFeedback

class DEGLevel(object):
	def __init__(self):
		self._degMissions = None
		# @AssociationType DEGMissions
		# @AssociationMultiplicity 1
		self._degLevels = []
		# @AssociationType DEGLevels[]
		# @AssociationMultiplicity 0..*
		self._feedback = []
		# @AssociationType DEGFeedback[]
		# @AssociationMultiplicity 0..*

