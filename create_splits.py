import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    move_dir='/home/workspace/data/'
    val_ratio=0.1
    test_ratio=0.1
    allFileNames=os.listdir(data_dir)
    np.random.shuffle(allFileNames)
    train_FileNames,val_FileNames,test_FileNames=np.split(np.array(allFileNames),[int(len(allFileNames)*(1-(val_ratio+test_ratio))),int(len(allFileNames)*(1-test_ratio))])
    train_FileNames=[data_dir+'/'+name for name in train_FileNames.tolist()]
    val_FileNames=[data_dir+'/'+name for name in val_FileNames.tolist()]
    test_FileNames=[data_dir+'/'+name for name in test_FileNames.tolist()]
    os.mkdir(move_dir+'train')
    os.mkdir(move_dir+'val')
    os.mkdir(move_dir+'test')
    for name in train_FileNames:
        shutil.move(name,move_dir+'train/')
    for name in val_FileNames:
        shutil.move(name,move_dir+'val/')
    for name in test_FileNames:
        shutil.move(name,move_dir+'test/')
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)