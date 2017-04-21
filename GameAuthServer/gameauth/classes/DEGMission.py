#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DEGMissions
import DEGChallenges
import ILOs
import DEGFeedback
import DEGActivity

class DEGMission(DEGActivity):
	def __init__(self):
		self._degMissions = []
		# @AssociationType DEGMissions[]
		# @AssociationMultiplicity 0..*
		self._degChallenges = None
		# @AssociationType DEGChallenges
		# @AssociationMultiplicity 1
		self._ilos = None
		# @AssociationType ILOs
		# @AssociationMultiplicity 0..1
		self._feedback = []
		# @AssociationType DEGFeedback[]
		# @AssociationMultiplicity 0..*

