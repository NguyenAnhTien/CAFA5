"""
@author : Tien Nguyen
@date   : 2023-07-11
"""
from configs import Configurer

class DatasetHandler(object):
    def __init__(
            self,
            configs: Configurer
        ):
        self.configs = configs

    def __getitem__(
            self,
            index: int
        ) -> dict:
        pass

    def __len__(
            self
        ) -> int:
        pass

    def load_data(
            self,
            configs: Configurer
        ):
        
