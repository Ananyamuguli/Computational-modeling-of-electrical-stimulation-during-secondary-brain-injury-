from motif2_final import ffi
import numpy as np
import PyDSTool as dst
from PyDSTool import *
import pickle as pkl
import gc
import os


def glutamate_analysis_nostim_traces(run):
    glu_e = [0, 0.06, 0.2, 0.29, 0.45]
    main_dict = {}

    print('Without stim')
    for g in glu_e:
        print('Glutamate: ', g)
        _, x_, pts = ffi(Istim=2, extrasyn_glu=g, forward_syn_weight=15)
        main_dict[g] = (_, x_, pts)
        del _,x_, pts
        gc.collect()

    print('Saving...........')
    with open('glutamate_params_no_stim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()
        



def glutamate_analysis_bn_acstim_traces(run):
    glu_e = [0.06, 0.29, 0.45]
    ac_stim_params_bn_set1 = [(60, 5.5)]
                        
    ac_stim_params_bn_set2 = [(25, 4.5),
                                (25, 2.5), 
                                (50, 4.5),]
    ac_stim_params_bn_set3 = [(25, 1.5), (30, 2.5)]
    main_dict = {}
    ode_results_set1 = {}
    for acp in ac_stim_params_bn_set1:
        f, ac = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[0], forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set1[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[glu_e[0]] = ode_results_set1
    



    ode_results_set2 = {}
    for acp in ac_stim_params_bn_set2:
        f, ac = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[1], forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set2[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[glu_e[1]] = ode_results_set2
    



    ode_results_set3 = {}
    for acp in ac_stim_params_bn_set3:
        f, ac = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[2], forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set3[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[glu_e[2]] = ode_results_set3
    


    print('Saving....................')
    with open('glutamate_params_bn_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)



def glutamate_analysis_inh_acstim_traces(run):
    glu_e = [0.06, 0.29]
    ac_stim_params_inh_set1 = [(30, 2.5)]
                        
    ac_stim_params_inh_set2 = [(25, 4.5),(25, 2.5), (50, 4.5)]

    main_dict = {}
    ode_results_set1 = {}
    for acp in ac_stim_params_inh_set1:
        f, ac = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[0], forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set1[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
        
    main_dict[glu_e[0]] = ode_results_set1
    



    ode_results_set2 = {}
    for acp in ac_stim_params_inh_set2:
        f, ac = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[1], forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set2[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()

    main_dict[glu_e[1]] = ode_results_set2
    


    print('Saving....................')
    with open('glutamate_params_inh_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)



def glutamate_analysis_bn_dbsstim_traces(run):
    glu_e = [ 0.29, 0.45]
                        
    stim_params_bn_set1 = [(75, 9.5),
                            (60, 9.5), ]
    stim_params_bn_set2 = [(100, 4.5), (75, 5.5)]
    main_dict = {}

    ode_results_set1 = {}
    for acp in stim_params_bn_set1:
        f, amp = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[0], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=1, stim_Vpost=1)
        ode_results_set1[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[glu_e[0]] = ode_results_set1
    

    ode_results_set2 = {}
    for acp in stim_params_bn_set2:
        f, amp = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[1], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=1, stim_Vpost=1)
        ode_results_set2[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[glu_e[1]] = ode_results_set2
    

    print('Saving....................')
    with open('glutamate_params_bn_dbsstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)



def glutamate_analysis_inh_dbsstim_traces(run):
    glu_e = [0.06, 0.29, 0.45]
    stim_params_bn_set1 = [(50, 5.5)]                    
    stim_params_bn_set2 = [(75, 5.5)]
    stim_params_bn_set3 = [(100, 4.5), (75, 5.5)]
    main_dict = {}
    ode_results_set1 = {}
    for acp in stim_params_bn_set1:
        f, amp = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[0], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set1[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()

    main_dict[glu_e[0]] = ode_results_set1
    

    ode_results_set2 = {}
    for acp in stim_params_bn_set2:
        f, amp = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[1], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set2[acp] = (_, x_, pts)
        del _, x_, pts
    main_dict[glu_e[1]] = ode_results_set2


    ode_results_set3 = {}
    for acp in stim_params_bn_set3:
        f, amp = acp
        _, x_, pts = ffi(Istim=2, extrasyn_glu = glu_e[2], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set3[acp] = pts
        del _, x_, pts
        gc.collect()

    main_dict[glu_e[2]] = ode_results_set3

    print('Saving....................')
    with open('glutamate_params_inh_dbsstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)





def Ko_analysis_nostim_traces(run):
    Ko = [4, 5.8, 8, 11]
    main_dict = {}

    print('Without stim')
    for k in Ko:
        print('Ko: ', k)
        _, x_, pts = ffi(Istim=2, Ko_rest=k, forward_syn_weight=15)
        main_dict[k] = (_, x_, pts)
        del _,x_, pts
        gc.collect()

    print('Saving...........')
    with open('Ko_params_no_stim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()




def Ko_analysis_bn_acstim_traces(run):
    Ko = [5.8, 8, 11]
    stim_params_set1 = [(1, 7.5), (5, 2.5)]
                        
    stim_params_set2 = [(15, 2.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}

    for params in stim_params_set1:
        f, ac = params
        _, x_, pts = ffi(Istim=2,Ko_rest = Ko[0] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set1[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[0]] = ode_results_set1


    for params in stim_params_set2:
        f, ac = params
        _, x_, pts = ffi(Istim=2,Ko_rest = Ko[1] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set2[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[1]] = ode_results_set2

    print('Saving...........')
    with open('Ko_params_bn_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()




def Ko_analysis_inh_acstim_traces(run):
    Ko = [5.8, 8, 11]
    stim_params_set1 = [(5, 2.5)]
                        
    stim_params_set2 = [(15, 2.5)]

    stim_params_set3 = [(60, 2.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}
    ode_results_set3 = {}

    for params in stim_params_set1:
        f, ac = params
        _, x_, pts = ffi(Istim=2, Ko_rest = Ko[0] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set1[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[0]] = ode_results_set1

    for params in stim_params_set2:
        f, ac = params
        _, x_, pts = ffi(Istim=2, Ko_rest = Ko[1] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set2[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[1]] = ode_results_set2


    for params in stim_params_set3:
        f, ac = params
        _, x_, pts = ffi(Istim=2, Ko_rest = Ko[2] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set3[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[2]] = ode_results_set3


    print('Saving...........')
    with open('Ko_params_inh_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()





def Ko_analysis_inh_dbsstim_traces(run):
    Ko = [5.8, 8, 11]
    stim_params_set1 = [(5, 2.5)]          

    main_dict = {}
    ode_results_set1 = {}
    for params in stim_params_set1:
        f, amp = params
        _, x_, pts = ffi(Istim=2, Ko_rest = Ko[2], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set1[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()

    main_dict[Ko[2]] = ode_results_set1
    main_dict[Ko[1]] = {}
    main_dict[Ko[0]] = {}

    print('Saving....................')
    with open('Ko_params_inh_dbsstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)



def atp_analysis_nostim_traces(run):
    atp_vals = [0.51, 1.01, 1.51, 2.01]
    main_dict = {}

    print('Without stim')
    for a in atp_vals:
        print('ATP: ', a)
        _, x_, pts = ffi(Istim=2, atp=a, forward_syn_weight=15)
        main_dict[a] = (_, x_, pts)
        del _,x_, pts
        gc.collect()

    print('Saving...........')
    with open('atp_params_no_stim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()




def atp_analysis_bn_acstim_traces(run):
    atp_vals = [0.51, 1.01, 1.51, 2.01]
    stim_params_set1 = []
                        
    stim_params_set2 = [ (2, 3.5), (25, 2.5), (30, 2.5)]
    stim_params_set3 = [(2, 3.5)]
    stim_params_set4 = [(30, 3.5), (50, 3.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}
    ode_results_set3 = {}
    ode_results_set4 = {}

    main_dict[atp_vals[0]] = ode_results_set1

    for params in stim_params_set2:
        f, ac = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[1] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set2[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[1]] = ode_results_set2


    for params in stim_params_set3:
        f, ac = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[2] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set3[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[2]] = ode_results_set3


    for params in stim_params_set4:
        f, ac = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[3] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=1, stim_Vpost=1)
        ode_results_set4[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[3]] = ode_results_set4

    print('Saving...........')
    with open('atp_params_bn_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()





def atp_analysis_inh_acstim_traces(run):
    atp_vals = [0.51, 1.01, 1.51, 2.01]
    stim_params_set1 = [(25, 2.5), (20, 2.5)]
                        
    stim_params_set2 = [ (15, 2.5), (30, 2.5)]
    stim_params_set3 = []
    stim_params_set4 = [(50, 3.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}
    ode_results_set3 = {}
    ode_results_set4 = {}

    main_dict[atp_vals[2]] = ode_results_set3

    for params in stim_params_set1:
        f, ac = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[0] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set1[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[0]] = ode_results_set1


    for params in stim_params_set2:
        f, ac = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[1] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set2[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[1]] = ode_results_set2


    for params in stim_params_set4:
        f, ac = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[3] , forward_syn_weight=15, neuromod='VE_sin(t)', freq_sin =f, Amp_sin=ac, stim_Vs=0, stim_Vpost=1)
        ode_results_set4[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[3]] = ode_results_set4

    print('Saving...........')
    with open('atp_params_inh_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()




def atp_analysis_bn_dbsstim_traces(run):
    atp_vals = [0.51, 1.01, 1.51, 2.01]
    stim_params_set1 = [(120, 8.5)]
                        
    stim_params_set2 = []
    stim_params_set3 = [(50, 2.5)]
    stim_params_set4 = [(60, 8.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}
    ode_results_set3 = {}
    ode_results_set4 = {}

    main_dict[atp_vals[1]] = ode_results_set2

    for params in stim_params_set1:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[0], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=1, stim_Vpost=1)
        ode_results_set1[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[0]] = ode_results_set1


    for params in stim_params_set3:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[2], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=1, stim_Vpost=1)
        ode_results_set3[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[2]] = ode_results_set3


    for params in stim_params_set4:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[3], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=1, stim_Vpost=1)
        ode_results_set4[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[3]] = ode_results_set4


    print('Saving...........')
    with open('atp_params_bn_dbsstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()




def atp_analysis_inh_dbsstim_traces(run):
    atp_vals = [0.51, 1.01, 1.51, 2.01]
    stim_params_set1 = [(120, 8.5)]
                        
    stim_params_set2 = [(75,2.5), (100, 3.5)]
    stim_params_set3 = [(60, 2.5)]
    stim_params_set4 = [(60, 8.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}
    ode_results_set3 = {}
    ode_results_set4 = {}




    for params in stim_params_set1:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[0], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set1[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[0]] = ode_results_set1


    for params in stim_params_set2:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[1], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set2[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[1]] = ode_results_set2


    for params in stim_params_set3:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[2], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set3[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_vals[2]] = ode_results_set3



    for params in stim_params_set4:
        f, amp = params
        _, x_, pts = ffi(Istim=2, atp = atp_vals[3], forward_syn_weight=15, neuromod='dbs_monophase(t)', dbs_freq =f, Amp_dbs=amp, stim_Vs=0, stim_Vpost=1)
        ode_results_set4[params] = (_, x_, pts)
        del _, x_, pts
        gc.collect()

    main_dict[atp_vals[3]] = ode_results_set4


    print('Saving...........')
    with open('atp_params_inh_dbsstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()
