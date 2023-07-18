"""
@author : Tien Nguyen
@date   : 2023-07-11
"""

import utils
import constants
from configs import Configurer

class DatasetHandler(object):
    def __init__(
            self,
            phase: str,
            configs: Configurer
        ):
        self.phase = phase
        self.configs = configs
        self.keys, self.sequences = self.load_data(phase, configs)

    def __getitem__(
            self,
            index: int
        ) -> dict:
        key = self.keys[index]
        sequence = self.sequences[key]
        return {
            constants.KEY: key,
            constants.SEQUENCE: sequence
        }

    def __len__(
            self
        ) -> int:
        return len(self.keys)
