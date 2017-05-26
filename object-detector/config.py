'''
Set the config variable.
'''

import ConfigParser as cp
import json

config = cp.RawConfigParser()
config.read('../data/config/config.cfg')

min_wdw_sz = tuple(json.loads(config.get("hog","min_wdw_sz")))
step_size = tuple(json.loads(config.get("hog", "step_size")))
orientations = config.getint("hog", "orientations")
pixels_per_cell = json.loads(config.get("hog", "pixels_per_cell"))
cells_per_block = json.loads(config.get("hog", "cells_per_block"))
visualize = config.getboolean("hog", "visualize")
transform_sqrt = config.getboolean("hog", "transform_sqrt")
pos_feat_ph = config.get("paths", "pos_feat_ph")
neg_feat_ph = config.get("paths", "neg_feat_ph")
model_path = config.get("paths", "model_path")
threshold = config.getfloat("nms", "threshold")

