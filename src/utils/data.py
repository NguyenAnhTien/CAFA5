"""
@author : Tien Nguyen
@date   : 2023-07-12
"""
from sklearn.model_selection import train_test_split

def split_train_test(
        data: list,
        test_size: float = 0.2,
        random_state: int = 42
    ):
    train_ids, test_ids = train_test_split(data, test_size=test_size,\
                                                    random_state=random_state)
    return train_ids, test_ids
