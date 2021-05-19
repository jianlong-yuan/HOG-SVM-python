#!/usr/bin/python
import os

# Link to the UIUC Car Database
# http://l2r.cs.uiuc.edu/~cogcomp/Data/Car/CarData.tar.gz
# dataset_url = "http://l2r.cs.uiuc.edu/~cogcomp/Data/Car/CarData.tar.gz"
# dataset_path = "../data/dataset/CarData.tar.gz"

# Fetch and extract the dataset
# if not os.path.exists(dataset_path):
#     os.system("wget {} -O {}".format(dataset_url, dataset_path))
#     os.system("tar -xvzf {} -C {}".format(dataset_path, os.path.split(dataset_path)[0]))

# Extract the features
# pos_path = "../data/dataset/CarData/pos"
# neg_path = "../data/dataset/CarData/neg"
# os.system("python ../object-detector/extract_features.py -p {} -n {}".format(pos_path, neg_path))

# Perform training
# pos_feat_path =  "../data/features/pos"
# neg_feat_path =  "../data/features/neg"
# os.system("python ../object-detector/train_classifier.py -p {} -n {}".format(pos_feat_path, neg_feat_path))

# Perform testing 
test_im_path = "../data/dataset/CarData/TestImages/test-18.pgm"
os.system("python ../object-detector/test_classifier.py -i {} -d {}".format(test_im_path,2))
