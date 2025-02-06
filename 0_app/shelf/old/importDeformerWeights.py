#*********************************************************************
# content	= Import specified deformer weights
# version	= 1.0.0
# date		= 2025-01-25
# 
# author	= Garvey Chi
#*********************************************************************

from maya import cmds
import os  


def importDeformerWeights():
	pass


def exportWeights(deformer_weight_type, name, path):
	'''
	Export deformer weights to file.
	'''
	cmds.deformerWeights('{0}.json'.format(name), im=True, deformer=deformer_weight_type, method=True, path='{0}'.format(path))
