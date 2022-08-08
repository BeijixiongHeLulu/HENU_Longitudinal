#!/usr/bin/env python
from argparse import ArgumentParser
import sys
from sklearn import datasets
from utils import *
from dataset import *
from EEG_processing import *
from direct_regression import *

def main():
    parser = ArgumentParser()
    parser.add_argument('--cfg', type=str, help='config file path')
    parser.add_argument('--eeg_data_path', type=str, default='../data/eed_data', help='eeg data path')
    parser.add_argument('--behavior_data_path', type=str, default='../data/behavior_data', help='behavior data path')
    args = parser.parse_args()
    config = load_config(config_path = args.cfg)
    dataset = SNDataset(config,args)
    folder_name = preprocessing_loop(dataset,config['PROCESSING']['PREPROCESSING'])
    feature_extraction_loop(folder_name,dataset,config['PROCESSING']['FEATURE_EXTRACTION'])
    EEG_social_network_loop(folder_name,dataset,config['PROCESSING']['EEG_SOCIAL_NETWORK'])
    direct_regression_survey_EEG(folder_name,dataset,config['REGRESSION']['SURVEY_EEG'])



        
    

if __name__ == '__main__':
    main()