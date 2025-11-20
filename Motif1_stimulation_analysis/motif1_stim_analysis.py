from motif1_final import ffe
import numpy as np
from scipy.signal import find_peaks
import PyDSTool as dst
from PyDSTool import *
import pickle as pkl
import gc



#Firing rate fuction
# %%


def firing_rate_cal_func(pts, threshold=5):
    peak_indx_1 = find_peaks(pts['Vs'], height=threshold, prominence=60) #prominences makes sure, spurious spikes below 0mV or extended depolarization blocks are not taken as spikes.
    peak_indx_2 = find_peaks(pts['Vpost'], height=threshold, prominence=60)
    firing_freq_pre_val = len(peak_indx_1[0])/max(pts['t'])
    firing_freq_post_val = len(peak_indx_2[0])/max(pts['t'])
    return firing_freq_pre_val, firing_freq_post_val




#--------------------------AC stimulation ----------------------------
def glu_stim_ac(run):
    extrasyn_glu = [0, 0.2, 0.45]
    ac_amp = np.arange(0.5,9)
    ac_freq = [0.5,1,2,5,10,15,20,25,30,50,60,100,120,140,150]
    glu_acstim_dict = {}
    print('AC stimulation')

    for g in extrasyn_glu:
        print('Glutamate: ', g)
        freq_firing_pre_stim = [] #presynaptic neuron
        freq_firing_post_stim = [] #post_synaptic neuron firing

        for ac in ac_amp:
            print('AC amplitude: ', ac)
            freq_firing_pre = []
            freq_firing_post = []
            for f in ac_freq:
                print('Frequency (Hz)', f)
                _, x_, pts = ffe(Istim1=2, extrasyn_glu=g, forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        glu_acstim_dict[g] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('glutamate_acstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(glu_acstim_dict, f)





def Ko_stim_ac(run):
    Ko_vals = [2, 4, 6, 8, 10]
    ac_amp = np.arange(0.5,9)
    ac_freq = [0.5,1,2,5,10,15,20,25,30,50,60,100,120,140,150]
    Ko_acstim_dict = {}
    print('AC stimulation')

    for Ko in Ko_vals:
        print('Ko: ', Ko)
        freq_firing_pre_stim = [] #presynaptic neuron
        freq_firing_post_stim = [] #post_synaptic neuron firing

        for ac in ac_amp:
            print('AC amplitude: ', ac)
            freq_firing_pre = []
            freq_firing_post = []
            for f in ac_freq:
                print('Frequency (Hz)', f)
                _, x_, pts = ffe(Istim1=2, Ko_rest=Ko, forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        Ko_acstim_dict[Ko] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('Ko_acstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(Ko_acstim_dict, f)




def atp_stim_ac(run):
    atp_vals = [0.01, 0.51, 1.01, 1.51, 2, 5, 10]
    ac_amp = np.arange(0.5,9)
    ac_freq = [0.5,1,2,5,10,15,20,25,30,50,60,100,120,140,150]
    atp_acstim_dict = {}
    print('AC stimulation')

    for atp_v in atp_vals:
        print('atp: ', atp_v)
        freq_firing_pre_stim = [] #presynaptic neuron
        freq_firing_post_stim = [] #post_synaptic neuron firing

        for ac in ac_amp:
            print('AC amplitude: ', ac)
            freq_firing_pre = []
            freq_firing_post = []
            for f in ac_freq:
                print('Frequency (Hz): ', f)
                _, x_, pts = ffe(Istim1=2, atp=atp_v, forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        atp_acstim_dict[atp_v] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('atp_acstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(atp_acstim_dict, f)




def syn_stim_ac(run):
    syn_vals = [0.0, 5, 8, 10, 12, 15, 30]
    ac_amp = np.arange(0.5,9)
    ac_freq = [0.5,1,2,5,10,15,20,25,30,50,60,100,120,140,150]
    syn_acstim_dict = {}
    print('AC stimulation')

    for syn in syn_vals:
        print('Syn: ', syn)
        freq_firing_pre_stim = [] 
        freq_firing_post_stim = [] 

        for ac in ac_amp:
            print('AC amplitude: ', ac)
            freq_firing_pre = []
            freq_firing_post = []
            for f in ac_freq:
                print('Frequency (Hz): ', f)
                _, x_, pts = ffe(Istim1=2, forward_syn_weight=syn, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        syn_acstim_dict[syn] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('syn_acstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(syn_acstim_dict, f)




def mito_stim_ac(run):
    mito_vals = [20, 35, 40, 50, 75, 100]
    ac_amp = np.arange(0.5,9)
    ac_freq = [0.5,1,2,5,10,15,20,25,30,50,60,100,120,140,150]
    mito_acstim_dict = {}
    print('AC stimulation')

    for mito in mito_vals:
        print('Mito: ', mito)
        freq_firing_pre_stim = [] 
        freq_firing_post_stim = [] 

        for ac in ac_amp:
            print('AC amplitude: ', ac)
            freq_firing_pre = []
            freq_firing_post = []
            for f in ac_freq:
                print('Frequency (Hz): ', f)
                _, x_, pts = ffe(Istim1=2, forward_syn_weight=10, neuromod='VE_sin(t)', freq_sin = f, Amp_sin = ac, del_phi_mito=mito)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        mito_acstim_dict[mito] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('mito_acstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(mito_acstim_dict, f)





#--------------------------DBS------------------------
def Ko_stim_dbs(run):
    Ko_vals = [2, 4, 6, 8, 10]
    dbs_amp = np.arange(1.5,10.5)
    dbs_f = [50,60,75,100,120,140,150]
    Ko_dbsstim_dict = {}
    print('DBS stimulation')

    for Ko in Ko_vals:
        print('Ko: ', Ko)
        freq_firing_pre_stim = [] #presynaptic neuron
        freq_firing_post_stim = [] #post_synaptic neuron firing

        for amp in dbs_amp:
            print('DBS amplitude: ', amp)
            freq_firing_pre = []
            freq_firing_post = []
            for f in dbs_f:
                print('Frequency (Hz)', f)
                _, x_, pts = ffe(Istim1=2, Ko_rest=Ko,  forward_syn_weight=10, neuromod='dbs_monophase(t)', dbs_freq = f, Amp_dbs = amp)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        Ko_dbsstim_dict[Ko] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('Ko_dbsstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(Ko_dbsstim_dict, f)   



def glu_stim_dbs(run):
    extrasyn_glu = [0, 0.2, 0.45]
    dbs_amp = np.arange(1.5,10.5)
    dbs_f = [50,60,75,100,120,140,150]
    glu_dbsstim_dict = {}
    print('DBS stimulation')

    for g in extrasyn_glu:
        print('Glutamate: ', g)
        freq_firing_pre_stim = [] #presynaptic neuron
        freq_firing_post_stim = [] #post_synaptic neuron firing

        for amp in dbs_amp:
            print('DBS amplitude: ', amp)
            freq_firing_pre = []
            freq_firing_post = []
            for f in dbs_f:
                print('Frequency (Hz)', f)
                _, x_, pts = ffe(Istim1=2, extrasyn_glu=g, forward_syn_weight=10, neuromod='dbs_monophase(t)', dbs_freq = f, Amp_dbs = amp)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        glu_dbsstim_dict[g] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('glutamate_dbsstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(glu_dbsstim_dict, f)



def atp_stim_dbs(run):
    atp_vals = [0.01, 0.51, 1.01, 1.51, 2, 5, 10]
    dbs_amp = np.arange(1.5,10.5)
    dbs_f = [50,60,75,100,120,140,150]
    atp_dbsstim_dict = {}
    print('DBS stimulation')

    for atp in atp_vals:
        print('ATP: ', atp)
        freq_firing_pre_stim = [] #presynaptic neuron
        freq_firing_post_stim = [] #post_synaptic neuron firing

        for amp in dbs_amp:
            print('DBS amplitude: ', amp)
            freq_firing_pre = []
            freq_firing_post = []
            for f in dbs_f:
                print('Frequency (Hz)', f)
                _, x_, pts = ffe(Istim1=2, atp=atp, forward_syn_weight=10, neuromod='dbs_monophase(t)', dbs_freq = f, Amp_dbs = amp)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        atp_dbsstim_dict[atp] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()


    with open('atp_dbsstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(atp_dbsstim_dict, f)




def syn_stim_dbs(run):
    syn_vals = [0.0, 5, 8, 10, 12, 15, 30]
    dbs_amp = np.arange(1.5,10.5)
    dbs_f = [50,60,75,100,120,140,150]
    syn_dbsstim_dict = {}
    print('dbs stimulation')

    for syn in syn_vals:
        print('Syn: ', syn)
        freq_firing_pre_stim = [] 
        freq_firing_post_stim = [] 

        for amp in dbs_amp:
            print('dbs amplitude: ', amp)
            freq_firing_pre = []
            freq_firing_post = []
            for f in dbs_f:
                print('Frequency (Hz): ', f)
                _, x_, pts = ffe(Istim1=2, forward_syn_weight=syn, neuromod='dbs_monophase(t)', dbs_freq = f, Amp_dbs = amp)
                fr_pre, fr_post = firing_rate_cal_func(pts)
                freq_firing_pre.append(fr_pre)
                freq_firing_post.append(fr_post)
                del _, x_, pts
                gc.collect()
            freq_firing_pre_stim.append(freq_firing_pre)
            freq_firing_post_stim.append(freq_firing_post)
            del freq_firing_pre, freq_firing_post
            gc.collect()

        syn_dbsstim_dict[syn] = (freq_firing_pre_stim, freq_firing_post_stim)
        del freq_firing_pre_stim, freq_firing_post_stim
        gc.collect()

    with open('syn_dbsstim_analysis_{}.pkl'.format(run), 'wb+') as f:
        pkl.dump(syn_dbsstim_dict, f)

