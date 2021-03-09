import argparse
import time
import os

def parse_option():
    parser = argparse.ArgumentParser('argument for training')

    # CUDA
    parser.add_argument('--CUDA', type=int, default=[0,1], nargs='+', help='CUDA_VISIBLE_DEVICES')

    # dadaset
    parser.add_argument('--dataset', type=str, default='nus', choices=['nus', 'coco', 'flickr'], help='dataset')

    # train parameters
    parser.add_argument('--alpha', type=float, default=1, help='alpha: used in calculate loss')
    parser.add_argument('--beta', type=float, default=1, help='beta: used in calculate loss')
    parser.add_argument('--gamma', type=float, default=0, help='phi: used in calculate loss')

    parser.add_argument('--w_c', type=float, default=0.01, help='weight of contrastive loss')  

    parser.add_argument('--epoch', type=int, default=10, help='epoch')
    parser.add_argument('--batch_size', type=int, default=100, help='batch size')
    parser.add_argument('--code_len', type=int, default=16, help='binary code length')

    parser.add_argument('--sem_emb_size', type=int, default=1024, help='semantic embedding size')
    parser.add_argument('--contrast', type=bool, default=False, help='enable contrastive loss')

    opt = parser.parse_args()

    return opt


def train(opt):
    # time.sleep(2)
    print('dataset: {}'.format(opt.dataset))
    print('batch size: {}'.format(opt.batch_size))
    print('epoch: {}'.format(opt.epoch))
    print('alpha: {}'.format(opt.alpha))
    print('beta: {}'.format(opt.beta))
    print('gamma: {}'.format(opt.gamma))
    print('code length: {}'.format(opt.code_len))
    print('contrast: {}'.format(opt.contrast))
    print('=' * 20)
    print('\n')


if __name__ == '__main__':
    # parameters   
    opt = parse_option()

    # CUDA
    os.environ["CUDA_VISIBLE_DEVICES"] = str(opt.CUDA)[1:-1]

    train(opt)