"""
@author : Tien Nguyen
@date   : 2023-07-12
"""
import tqdm

import utils
import constants
from configs import Configurer
from preprocessor import ProteinTranslator

class Preprocessor(object):
    def __init__(
            self,
            phase: str,
            configs: Configurer,
            translator: ProteinTranslator
        ):
        self.phase = phase
        self.configs = configs
        self.translator = translator

    def __call__(
            self
        ) -> tuple:
        data = []
        sequences = self.load_data(self.phase, self.configs)
        labels_df = self.load_labels(self.phase, self.configs)
        label_ids = list(set(labels_df[constants.TERM].values.tolist()))
        labels_ids = utils.create_series(label_ids)
        protien_ids = set(sequences.keys())
        for protien_id in tqdm.tqdm(protien_ids):
            sequence, embedding = self.translate_sequence(sequences[protien_id])
            labels = labels_df[labels_df[constants.PROTEIN_ID] == protien_id]
            labels = labels[constants.TERM].values.tolist()
            labels = labels_ids.isin(labels).values.astype(float)
            data.append({
                constants.ID: protien_id,
                constants.SEQUENCE: sequence,
                constants.EMBEDDING: embedding,
                constants.LABEL: labels
            })
        train_data, val_data = utils.split_data(data, self.configs.val_size)
        return train_data, val_data

    def translate_sequence(
            self,
            sequence: str
        ):
        sequence = str(sequence.seq)
        embedding = self.translator(sequence)
        return sequence, embedding

    def load_data(
            self,
            phase: str,
            configs: Configurer
        ) -> dict:
        fasta_file = self.load_data_file(phase, configs)
        sequences = utils.read_fasta(fasta_file)
        return sequences

    def load_labels(
            self,
            phase: str,
            configs: Configurer
        ):
        label_file = self.load_labels_file(phase, configs)
        labels_df = utils.read_csv(sep=configs.sep, csv_file=label_file)
        return labels_df
    
    def load_data_file(
            self,
            phase: str,
            configs: Configurer
        ) -> str:
        fasta_file = utils.join_path((configs.dataset_dir, phase,\
                                                        configs.train_data))
        return fasta_file
    
    def load_labels_file(
            self,
            phase: str,
            configs: Configurer
        ) -> str:
        label_file = utils.join_path((configs.dataset_dir, phase,\
                                                        configs.train_labels))
        return label_file
