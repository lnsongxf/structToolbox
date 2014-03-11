#!/usr/bin/env python
''' Test cases
'''
# standard library
import numpy    as np
import cPickle  as pkl

import sys
import os

# testing library
from nose.core  import runmodule
from nose.tools import *

# Pythonpath
dir_ = os.path.dirname(os.path.realpath(__file__)).replace('/tests', '')
sys.path.insert(0, dir_)

from scripts.simulation import simulation
from scripts.estimation import estimation

# Set working directory.
dir_ = os.path.abspath(os.path.split(sys.argv[0])[0])
os.chdir(dir_)

class testCls(object):
    
    def test_case_1(self):
                
        simulation(initFile = '../dat/testA.ini', dataFile = 'testA.pkl')
        
        estimation(initFile = '../dat/testA.ini', dataFile = 'testA.pkl')
        
        rslt = pkl.load(open('rslt.struct.pkl', 'r'))
        
        assert_true(np.allclose(rslt['fun'], -0.583431) == True)

''' Execution of module as script.
'''
if __name__ == '__main__':
    
    runmodule()
