#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Header
import Body

class DGBLEnvelope(object):
	def __init__(self):
		self._unnamed_Header_ = None
		# @AssociationType Header
		# @AssociationMultiplicity 0..1
		# @AssociationKind Composition
		self._unnamed_Body_ = None
		# @AssociationType Body
		# @AssociationMultiplicity 1
		# @AssociationKind Composition

