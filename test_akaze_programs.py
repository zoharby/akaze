import sys
import os
import subprocess

# ===============================================================================
# Populate AKAZE-based programs
programs = ['AKAZE_features', 'AKAZE_match', 'AKAZE_compare']
for i in range(len(programs)):
  programs[i] = './bin/Release/' + programs[i]
if sys.platform == 'win32':
  for i in range(len(programs)):
    programs[i] = programs[i] + '.exe'

# ===============================================================================
# Helper functions
def extract_AKAZE_features(imagePath):
  command = " ".join([programs[0], ' -i ', imagePath])
  os.system(command)

def match_AKAZE_features(imagePath1, imagePath2, gdTruthHomography):
  command = " ".join(
    [programs[1], ' -L ', imagePath1, ' -R ', imagePath2, ' -H ', gdTruthHomography] )
  os.system(command)

def compare_AKAZE_BRISK_ORB(imagePath1, imagePath2, gdTruthHomography):
  command = " ".join(
    [programs[2], ' -L ', imagePath1, ' -R ', imagePath2, ' -H ', gdTruthHomography] )
  os.system(command)

# ===============================================================================
# Example datasets
imagePath1 = './datasets/iguazu/img1.pgm'
imagePath2 = './datasets/iguazu/img4.pgm'
gdTruthHomography = './datasets/iguazu/H1to4p'

# Go!
extract_AKAZE_features(imagePath1)
match_AKAZE_features(imagePath1, imagePath2, gdTruthHomography)
compare_AKAZE_BRISK_ORB(imagePath1, imagePath2, gdTruthHomography)
