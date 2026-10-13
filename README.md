# FishGenes: Rhodopsin and Adaptation to Depth

A collaborative bioinformatics study comparing rhodopsin (RH1) nucleotide and amino acid sequences in deep-water and shallow-water fish. The project asks whether unrelated deep-water fish show recurring sequence changes that could be explored in relation to adaptation to low-light environments.

**Project team:** Elena Polyakova and Anna Namyatova. Elena Dalboni da Rocha contributed under her previous name, Elena Polyakova.

**Academic context:** Spring 2019 research project at the Bioinformatics Institute. Supervised by Nadezhda Potapova, Faculty of Bioengineering and Bioinformatics, Moscow State University.

[Institute project presentation (PDF)](https://bioinformaticsinstitute.ru/sites/default/files/polyakova_namyatova_-_adaptation_of_the_fish_to_depth.pdf) · [Graduate profile and project record](https://bioinf.me/graduates2018-19#!/tab/259037411-2)

[View the original project presentation](https://github.com/enterlina/FishGenes/blob/master/Polyakova%2C%20Namyatova%20-%20Adaptation%20of%20the%20fish%20to%20depth.pdf)

## Analysis workflow

- Compare sequence changes and amino acid replacements between fish groups.
- Count nucleotide and amino acid frequencies.
- Summarize patterns in tables and histograms for exploratory interpretation.

## Repository guide

| Resource | Purpose |
| --- | --- |
| [FishGenes.ipynb](FishGenes.ipynb) | Amino acid replacement analysis |
| [FishGenes_amino_frequency_histogram.ipynb](FishGenes_amino_frequency_histogram.ipynb) | Amino acid frequency visualization |
| [FishGenes_nucleotide_frequency.ipynb](FishGenes_nucleotide_frequency.ipynb) | Nucleotide frequency analysis |
| [FishGenes_get_frequency.py](FishGenes_get_frequency.py) | Counting replacement frequencies from a sequence-comparison table |
| [data](data/) | Source data included with the project |
| [result](result/) | Saved analysis outputs |
| [img](img/) | Figures |

![Amino acid frequency histogram from the FishGenes project](img/FishGenes_amino_histogram.png?raw=true)

## Tools and scope

Python, pandas, and Jupyter notebooks. This educational research project contains exploratory comparisons; sequence-frequency patterns alone do not establish a causal mechanism of adaptation. Refer to the original presentation for the project's interpretation.

Some scripts reference local input and output paths. Update those paths to your working copy and review the supplied data before rerunning. The original computational environment is not pinned.

## Author

Elena Dalboni da Rocha · [Portfolio and current work](https://buildnxt.app) · [GitHub](https://github.com/enterlina)
