
# coding: utf-8

# In[97]:


from Bio import SeqIO
import sklearn.metrics as skmetrics
from matplotlib import pyplot
from sklearn.metrics import roc_auc_score
from sklearn import metrics
import pandas as pd
import numpy as np
import numpy as np


class FishGenes(object):
    def __init__(self, fish_id=None, fish_type=None, sequence=None,
                 fishes={'fishname': [], 'number': [], 'replace': []}):
        self.fish_id = fish_id
        self.fish_type = fish_type
        self.sequence = sequence
        self.fishes = {'fishname': [], 'number': [], 'replace': []}


def parse_fasta(reffilename, fish_type):
    Fish_List = []
    for rec in SeqIO.parse(reffilename, "fasta"):
        name, sequence = rec.id, str(rec.seq)
        Fish_List.append(FishGenes(fish_id=name, fish_type=fish_type, sequence=sequence, fishes={}))
    return Fish_List


def convert_files(reffilename, reffilename2):
    Fish_DeepWater = []
    Fish_ShalloWater = []

    Fish_DeepWater = parse_fasta(reffilename, fish_type='deepwater')
    Fish_ShalloWater = parse_fasta(reffilename2, fish_type='shallowater')
    return Fish_DeepWater, Fish_ShalloWater


def get_numbers(sequence, replace_sequence):
    repeated_elements = []
    repeated_idx = []
    repeated_sequence = []

    for idx, val in enumerate(sequence):
        if sequence.count(val) > 1:
            repeated_elements.append(val)
            repeated_idx.append(idx)
            repeated_sequence.append(replace_sequence[idx])
    return repeated_elements, repeated_sequence


def sequence_dictionary(repeat_sequence, replace_sequence):
    sequence_dictionary = dict()
    for i in range(len(repeat_sequence)):
        key = repeat_sequence[i]
        if key not in sequence_dictionary:
            sequence_dictionary[key] = []
        sequence_dictionary[repeat_sequence[i]].append(replace_sequence[i])
    return sequence_dictionary


def convert_panda(data):
    for i in range(len(data)):
        key = list(data)[i]

        while len(data[key]) < 4:
            data[key].append('-')
    df = pd.DataFrame.from_dict(data)
    return df

reffilename = '/Users/alena_paliakova/Google Drive/!Bioinf_drive/00_FishPr/genes_fasta/deep_water_al_test2.fasta'
reffilename2 = '/Users/alena_paliakova/Google Drive/!Bioinf_drive/00_FishPr/genes_fasta/shallowwater_al_test2.fasta'

Fish_DeepWater, Fish_ShalloWater = convert_files(reffilename, reffilename2)

for i in range((len(Fish_DeepWater))):
    for j in range(len(Fish_ShalloWater)):
        Fish_DeepWater[i].fishes['fishname'].append(Fish_ShalloWater[j].fish_id)
        for k in range(len(Fish_ShalloWater[j].sequence)):
            if (Fish_DeepWater[i].sequence[k] != '-') and (Fish_ShalloWater[j].sequence[k] != '-') and (
                    Fish_DeepWater[i].sequence[k] != Fish_ShalloWater[j].sequence[k]):
                Fish_DeepWater[i].fishes['number'].append(k)
                Fish_DeepWater[i].fishes['replace'].append(
                    Fish_DeepWater[i].sequence[k] + Fish_ShalloWater[j].sequence[k])

for i in range(len(Fish_DeepWater)):
    sequence = Fish_DeepWater[i].fishes['number']
    replace_sequence = Fish_DeepWater[i].fishes['replace']
    sequence_data = sequence_dictionary(sequence, replace_sequence)
    print('\n \n{0} {1} \n'.format(Fish_DeepWater[i].fish_id, Fish_DeepWater[i].fish_type))
    df=convert_panda(sequence_data)
    df.insert(0, " compare with shallowater", ['MH796519.1','MH796519.1','-','-']) 
    print(df)

