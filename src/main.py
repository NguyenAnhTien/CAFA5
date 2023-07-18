"""
@author : Tien Nguyen
@date   : 2023-07-12
"""
import argparse

import utils
import constants
from configs import Configurer
from preprocessor import Preprocessor
from preprocessor import ProteinTranslator

def preprocess(
        args: argparse.Namespace,
        configs: Configurer
    ) -> None:
    accelerator = 'cuda' if args.gpu > -1 else 'cpu'
    translator = ProteinTranslator(configs, accelerator)
    preprocessor = Preprocessor(args.phase, configs, translator)
    train_data, val_data = preprocessor()
    utils.write_pkl(train_data, utils.join_path((configs.preprocess_dir,\
                                        constants.TRAIN, constants.TRAIN_DATA)))
    utils.write_pkl(val_data, utils.join_path((configs.preprocess_dir,\
                                        constants.VAL, constants.VAL_DATA)))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--configs', type=str, default='configs.yaml',\
                                                    help='configuration file')
    parser.add_argument('--phase', type=str, default='train')
    parser.add_argument('--command', help='CLI commands')
    parser.add_argument('--devices', type=int, default=1, help='number of devices')
    parser.add_argument('--gpu', type=int, help='GPU id')
    args = parser.parse_args()

    configs = Configurer(args.configs)
    eval(args.command)(args, configs)
