"""
@author : Tien Nguyen
@date   : 2023-07-15
"""
import torch

from transformers import T5Tokenizer
from transformers import T5EncoderModel

class ProteinTranslator(object):
    def __init__(
            self,
            configs
        ) -> None:
        self.configs = configs
        self.define_translator()

    @torch.no_grad()
    def __call__(
            self,
            sequence: str
        ):
        seq_len = len(sequence)
        sequence = ' '.join(list(sequence))
        sequence = (sequence, )
        ids = self.tokenizer.batch_encode_plus(sequence,\
                                                    add_special_tokens=True,\
                                                            padding="longest")
        input_ids = torch.tensor(ids['input_ids'])
        attention_mask = torch.tensor(ids['attention_mask'])
        embedding = self.translator(input_ids=input_ids,\
                                    attention_mask=attention_mask)
        embedding = embedding[0, : seq_len]
        embedding = embedding.mean(dim=0)
        return embedding

    def define_translator(
            self
        ):
        local_files_only = self.configs.t5_local_files_only
        self.tokenizer = T5Tokenizer.from_pretrained(\
                                        self.configs.t5_checkpoint,\
                                            local_files_only=local_files_only,\
                                                        do_lower_case=False)
        self.translator = T5EncoderModel.from_pretrained(\
                                    self.configs.t5_checkpoint,\
                                        local_files_only=local_files_only)
        self.translator.eval()
