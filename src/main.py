# coding=utf-8
import config
import numpy as np

ABEO_file = config.source_matrix / 'ABEO_ARCA.npy'

if __name__ == '__main__':
    print('Kaushy')
    abeo = np.load(ABEO_file)
    print(abeo)