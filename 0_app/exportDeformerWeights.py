#*********************************************************************
# content	= Export specified deformer weights
# version	= 1.0.0
# date		= 2025-01-22
# 
# author	= Garvey Chi
#*********************************************************************

from maya import cmds
import os


#*********************************************************************
def exportDeformerWeights(deformer_type, folder_path=None):
	# Create file directory
	if not folder_path:

		filepath = cmds.file(sceneName=True, query=True)
		start_dir = os.path.dirname(filepath)
		file_name = os.path.splitext(os.path.basename(filepath))[0]
		folder_path = '{0}/{1}'.format(start_dir, file_name)

	if os.path.exists(folder_path):
		print('The {0} folder already exists, creation skipped.'.format(folder_path))
	else:
		os.makedirs(folder_path, exist_ok=True)
		print('The folder, {0} created for skinweights export.'.format(folder_path))

	deformer = cmds.ls(type=deformer_type)

	if not deformer:
		# No deformer of type requested in scene
		cmds.confirmDialog(
			title='Warning',
			message='No {0} found in scene'.format(deformer_type), 
			button=['Ok'])
	elif len(cmds.ls(sl=True)) == 0:
		# Return all requested deformers in the scene 
		print('No mesh selected, listing all {0} in scene file: {1}'.format(deformer_type, deformer))
		exportWeights(deformer, '{0}_{1}'.format(file_name, deformer_type), folder_path)
	else:
		# Return requested deformer of selected mesh(es)
		obj = cmds.listRelatives(s=True)
		shp_hist = cmds.listHistory(obj)
		deformer = cmds.ls(shp_hist, type=deformer_type)
		print(deformer)
		exportWeights(deformer, '{0}_{1}'.format(file_name, deformer_type), folder_path)


def exportWeights(deformer_weight_type, name, path):
	'''
	Export deformer weights to file.
	'''
	cmds.deformerWeights('{0}.json'.format(name), export=True, deformer=deformer_weight_type, method=True, path='{0}'.format(path))

