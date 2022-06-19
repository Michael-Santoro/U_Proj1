import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    dataset = os.listdir(source)
    np.random.shuffle(dataset)
  
    #80% 10% 10%
    train_set, test_set, val_set  = np.split(dataset, [int(.8*len(dataset)), int(.9*len(dataset))])
    # assigining 80 and 20 ration to train and val filenames
    train_dst = os.path.join(destination, 'train/')
    test_dst = os.path.join(destination, 'test/')
    val_dst = os.path.join(destination, 'val/')

    for trainfile in train_set:   
        shutil.move(source+f'{os.path.basename(trainfile)}', train_dst+f'{os.path.basename(trainfile)}')
    for testfile in test_set:   
        shutil.move(source+f'{os.path.basename(testfile)}', test_dst+f'{os.path.basename(testfile)}')
    for valfile in val_set:
        shutil.move(source+f'{os.path.basename(valfile)}', val_dst+f'{os.path.basename(valfile)}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
