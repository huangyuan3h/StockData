import app
from ml.data.verify import verify_models
from ml.lstm4.LSTM4Factory import LSTM4Factory
from ml.lstm4.VXXDataset import VXXDataset

if __name__ == '__main__':
    """
    lstm4_3 data vs lstm4_3 checkpoint
    """
    res = verify_models(Factory=LSTM4Factory, DataSet=VXXDataset, code_num=300, mask_size=3,
                  paths=['../../model_data/lstm4_3',
                         '../../model_data/lstm4_3_checkpoint_0330',
                         '../../model_data/lstm4_3_checkpoint_0402'])

    """
    lstm4_1 data vs lstm4_1 checkpoint
    """
    #  res = verify_models(Factory=LSTM4Factory, DataSet=VXXDataset,code_num=500, mask_size=1,
    #              paths=['../../model_data/lstm4_1',
    #                     '../../model_data/lstm4_1_checkpoint_0306',
    #                     '../../model_data/lstm4_1_checkpoint_0315'])

    # res = verify_models(Factory=LSTM4Factory, DataSet=VXXDataset, code_num=300, mask_size=5,
    #              paths=['../../model_data/lstm4_5',
    #                     '../../model_data/lstm4_5_checkpoint_0405',
    #                     '../../model_data/lstm4_5_checkpoint_0406',
    #                     ])

    print(res)
