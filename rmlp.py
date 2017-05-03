# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:06:14 2017

@author: Dany
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy
from numpy import linalg


def generate_data(size, dim):
    alpha_pos = np.random.randint(0, 100, (dim))
    x_pos = np.random.dirichlet(alpha_pos, size)
    y_pos = np.ones(dim)
    print(x_pos.shape)
    
    alpha_neg = np.random.randint(0, 100, (dim))
    x_neg = np.random.dirichlet(alpha_neg, size)
    y_neg = np.ones(dim)
    
    x, y = np.vstack((x_pos, x_neg)), np.vstack((y_pos, y_neg))
    
    z = np.random.normal(0, 1, (2*size, 1))
    return x, y, z
    
def nabla_likelihood(t,theta,p):
    vector = x[t]
    inner = np.inner(vector,theta)
    if y[t] == 1 :
        return -vector/(1-p+inner)
    else:
        return -vector/(p-inner)
      
def PI(theta, nu, t, p):
    result = theta - nu*nabla_likelihood(t,theta,p)
    return result/np.linalg.norm(result)

def phi(x):
    return 1
    
def phi_table(grid_number):
    dict_values = {}
        for i in range(grid_number):
            dict_values[i/grid_number]=phi(i/grid_number)
            dict_values[-i/grid_number]=phi(-i/grid_number)
    return dict_values

def phi_inverse(grid_number,x):
    dict_values = phi_table(grid_number)
    diff = np.Infinity
    inverse = -grid_number
    for i in range(-grid_number,grid_number):
        if (abs(dict_values[i/grid_number]- x) < diff):
            inverse = i
    return inverse
    
def PGSD(xt,nu):
    t = 0
    d = np.shape(xt)[1]
    p = 0
    theta = np.ones(d)
    nu = 1
    while true:
        theta = PI(theta, nu, t, p)
        p = func_g(theta,t)
    return p

if __name__ == '__main__':
    x, y, z = generate_data(100, 10)
    cov = np.corrcoef(x)

    