
# coding: utf-8

# In[ ]:


from Bio import SeqIO


class FishGenes(object):
    def __init__(self, fish_id=None, fish_type=None, sequence=None, fishes={'fishname':[],'number':[],'replace':[]}):
        self.fish_id = fish_id
        self.fish_type = fish_type
        self.sequence = sequence
        self.fishes={'fishname':[],'number':[],'replace':[]}


def parse_fasta(reffilename, fish_type):
    Fish_List = []
    for rec in SeqIO.parse(reffilename, "fasta"):
        name, sequence = rec.id, str(rec.seq)
        Fish_List.append(FishGenes(fish_id=name, fish_type=fish_type, sequence=sequence, fishes={}))
    return Fish_List


reffilename = '/Users/alena_paliakova/Google Drive/!Bioinf_drive/00_FishPr/genes_fasta/deep_water_al_test.fasta'

reffilename2 = '/Users/alena_paliakova/Google Drive/!Bioinf_drive/00_FishPr/genes_fasta/shallowwater_al_test.fasta'

Fish_DeepWater = []
Fish_ShalloWater = []

Fish_DeepWater = parse_fasta(reffilename, fish_type='deepwater')
Fish_ShalloWater = parse_fasta(reffilename2, fish_type='shallowater')



for i in range((len(Fish_DeepWater))):
    for j in range(len(Fish_ShalloWater)):
        Fish_DeepWater[i].fishes['fishname'].append(Fish_ShalloWater[j].fish_id)
        for k in range(len(Fish_ShalloWater[j].sequence)):
            if (Fish_DeepWater[i].sequence[k]!='-') and (Fish_ShalloWater[j].sequence[k]!='-')and (Fish_DeepWater[i].sequence[k]!=Fish_ShalloWater[j].sequence[k]):
                Fish_DeepWater[i].fishes['number'].append([k])
                Fish_DeepWater[i].fishes['replace'].append([Fish_DeepWater[i].sequence[k]+Fish_ShalloWater[j].sequence[k]])
    
# for i in range(len(Fish_DeepWater)):
#     print(Fish_DeepWater[i].fish_id, Fish_DeepWater[i].fish_type, Fish_DeepWater[i].sequence)
    
# for i in range(len(Fish_ShalloWater)):
#     print(Fish_ShalloWater[i].fish_id, Fish_ShalloWater[i].fish_type, Fish_ShalloWater[i].sequence)  
   
    
for i in range(len(Fish_DeepWater)):
    print(Fish_DeepWater[i].fish_id, Fish_DeepWater[i].fish_type, Fish_DeepWater[i].fishes)
    
    
    

