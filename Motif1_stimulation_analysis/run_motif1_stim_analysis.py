import sys
from motif1_stim_analysis import *


if len(sys.argv)==3:
    if int(sys.argv[1]) == 1:
        print('AC stim analysis with glutamate')
        glu_stim_ac(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 2:
        print('AC stim analysis with Ext. Potassium')
        Ko_stim_ac(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 3:
        print('AC stim analysis with Ext. Potassium')
        atp_stim_ac(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 4:
        print('AC stim analysis with synaptic weight variation')
        syn_stim_ac(sys.argv[2])
        print('-------------Done---------------') 
    if int(sys.argv[1]) == 5:
        print('AC stim analysis with mito potential')
        mito_stim_ac(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 6:
        print('DBS stim analysis with glutamate')
        glu_stim_dbs(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 7:
        print('DBS stim analysis with Ext. Potassium')
        Ko_stim_dbs(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 8:
        print('DBS stim analysis with Ext. Potassium')
        atp_stim_dbs(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 9:
        print('DBS stim analysis with synaptic weight')
        syn_stim_dbs(sys.argv[2])
        print('-------------Done---------------')  
else:
    print('Wrong number of inputs!!!!')
