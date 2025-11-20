import sys
from motif2_traces import *


if len(sys.argv)==3:
    if int(sys.argv[1]) == 1:
        glutamate_analysis_nostim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 2:
        glutamate_analysis_bn_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 3:
        glutamate_analysis_inh_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 4:
        glutamate_analysis_bn_dbsstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 5:
        glutamate_analysis_inh_dbsstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 6:
        Ko_analysis_nostim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 7:
        Ko_analysis_bn_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 8:
        Ko_analysis_inh_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 9:
        Ko_analysis_inh_dbsstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 10:
        atp_analysis_nostim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 11:
        atp_analysis_bn_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 12:
        atp_analysis_inh_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 13:
        atp_analysis_bn_dbsstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 14:
        atp_analysis_inh_dbsstim_traces(sys.argv[2])
        print('-------------Done---------------')

else:
    print('Wrong number of inputs')
