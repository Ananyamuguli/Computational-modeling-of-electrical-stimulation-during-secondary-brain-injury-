import sys
from motif1_traces import *


if len(sys.argv)==3:
    if int(sys.argv[1]) == 1:
        glutamate_analysis_nostim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 2:
        glutamate_analysis_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 3:
        Ko_analysis_nostim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 4:
        Ko_analysis_acstim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 5:
        atp_analysis_nostim_traces(sys.argv[2])
        print('-------------Done---------------')
    if int(sys.argv[1]) == 6:
        atp_analysis_acstim_traces(sys.argv[2])
        print('-------------Done---------------')

else:
    print('Wrong number of inputs to the file')
