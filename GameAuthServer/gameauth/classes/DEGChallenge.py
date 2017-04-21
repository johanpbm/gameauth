#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DEGLearningObject
import DEGDifficultyLevel
import ILOs
import DEGFeedback
import DEGActivity

class DEGChallenge(DEGActivity):
	def __init__(self):
		self._learningObjects = []
		# @AssociationType DEGLearningObject[]
		# @AssociationMultiplicity 0..*
		# @AssociationKind Aggregation
		self._difficultyLevel = []
		# @AssociationType DEGDifficultyLevel[]
		# @AssociationMultiplicity 0..*
		self._ilos = None
		# @AssociationType ILOs
		# @AssociationMultiplicity 0..1
		self._feedback = []
		# @AssociationType DEGFeedback[]
		# @AssociationMultiplicity 0..*

