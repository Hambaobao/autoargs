import os
import numpy as np
from itertools import product


if __name__ == '__main__':
    alphas = np.arange(0, 3, 0.01)
    betas = np.arange(0, 3, 0.01)
    gammas = np .arange(0, 3, 0.01)

    prm_cbn = list(product(alphas, betas, gammas))

    for alpha, beta, gamma in prm_cbn:
        os.system('python foo.py --dataset {} --batch_size {} --epoch {} --CUDA {} --alpha {} --beta {} --gamma {} --contrast {}'.
            format('coco', '100', '200', '4', alpha, beta, gamma, 'True'))