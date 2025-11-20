from motif1_final import ffe
import numpy as np
import PyDSTool as dst
from PyDSTool import *
import pickle as pkl
import gc


def glutamate_analysis_nostim_traces(run):
    extrasyn_glu = [0, 0.19, 0.2, 0.45, 0.6]

    main_dict = {}

    print('Without stim')
    for g in extrasyn_glu:
        print('Glutamate: ', g)
        ode, traj, pts = ffe(Istim1=2, extrasyn_glu=g, forward_syn_weight=10)
        main_dict[g] = (ode, traj, pts)
        del ode, traj, pts
        gc.collect()
        

    print('Saving...........')
    with open('glutamate_params_nostim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()



def glutamate_analysis_acstim_traces(run):
    glu_e = [0.2]
    ac_stim_params = [(20, 3.5), 
                     (10, 1.5), 
                     (120, 3.5), 
                     (60, 5.5)]
    main_dict = {}
    ode_results_set1 = {}
    for acp in ac_stim_params:
        f, ac = acp
        _, x_, pts = ffe(Istim1=2, extrasyn_glu = glu_e[0], forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
        ode_results_set1[acp] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[glu_e[0]] = ode_results_set1
    

    print('Saving....................')
    with open('glutamate_params_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)    
    

def Ko_analysis_nostim_traces(run):
    ko = [4, 6, 10]

    main_dict = {}

    print('Without stim')
    for k in ko:
        print('Ko: ', k)
        ode, traj, pts = ffe(Istim1=2, Ko_rest = k, forward_syn_weight=10)
        main_dict[k] = (ode, traj, pts)
        del ode, traj, pts
        gc.collect()
        

    print('Saving...........')
    with open('Ko_params_nostim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()



def Ko_analysis_acstim_traces(run):
    Ko = [6, 10]
    stim_params1 = [(15, 2.5), 
                     (50, 3.5) ]
    stim_params2 = [(15, 2.5), 
                     (5, 1.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}

    
    for param in stim_params1:
        f, ac = param
        _, x_, pts = ffe(Istim1=2, Ko_rest=Ko[0]  , forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
        ode_results_set1[param] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[0]] = ode_results_set1


    for param in stim_params2:
        f, ac = param
        _, x_, pts = ffe(Istim1=2, Ko_rest=Ko[1]  , forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
        ode_results_set2[param] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[Ko[1]] = ode_results_set2


    print('Saving....................')
    with open('Ko_params_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)




def atp_analysis_nostim_traces(run):
    atp_val = [0.51, 1.01, 2.01]

    main_dict = {}

    print('Without stim')
    for atp in atp_val:
        print('ATP: ', atp)
        ode, traj, pts = ffe(Istim1=2, atp = atp, forward_syn_weight=10)
        main_dict[atp] = (ode, traj, pts)
        del ode, traj, pts
        gc.collect()
        

    print('Saving...........')
    with open('atp_params_nostim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()


def atp_analysis_acstim_traces(run):
    atp_val = [0.51, 2.01]
    stim_params1 = [(0.5, 3.5), 
                    (1, 3.5), 
                    (15, 2.5),
                    (2, 3.5),
                    (5, 2.5) ]

    stim_params2 = [(1, 5.5), 
                    (15, 2.5),
                    (60,1.5)]
    main_dict = {}
    ode_results_set1 = {}
    ode_results_set2 = {}

    
    for param in stim_params1:
        f, ac = param
        _, x_, pts = ffe(Istim1=2, atp=atp_val[0]  , forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
        ode_results_set1[param] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_val[0]] = ode_results_set1


    for param in stim_params2:
        f, ac = param
        _, x_, pts = ffe(Istim1=2, atp=atp_val[1]  , forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
        ode_results_set2[param] = (_, x_, pts)
        del _, x_, pts
        gc.collect()
    main_dict[atp_val[1]] = ode_results_set2


    print('Saving....................')
    with open('atp_params_acstim_traces_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(main_dict, f)
    del main_dict
    gc.collect()



    