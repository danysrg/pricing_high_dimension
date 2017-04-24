# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:06:14 2017

@author: Dany
"""
import matplotlib.pyplot as plt
import numpy as np


def generate_data(size, dim):
    alpha_pos  =np.random.randint(0, 100, (dim))
    x_pos = np.random.dirichlet(alpha_pos, size)
    y_pos = np.ones(dim)
    print(x_pos.shape)
    
    alpha_neg  =np.random.randint(0, 100, (dim))
    x_neg = np.random.dirichlet(alpha_neg, size)
    y_neg = np.ones(dim)
    
    x, y = np.vstack((x_pos, x_neg)), np.vstack((y_pos, y_neg))
    
    z = np.random.normal(0, 1, (2*size, 1))
    return x, y, z
    
    
if __name__ == '__main__':
    x, y, z = generate_data(100, 10)
    cov = np.corrcoef(x)