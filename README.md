## Computational modeling and analysis of acute electrical brain stimulation paradigms during Secondary Brain Injury (SBI).

The project uses PyDSTool library (https://pydstool.github.io/PyDSTool/FrontPage.html) to work with the ODEs presented in the paper. To properly work with PyDSTool:
  1. python version <= 3.9.13
  2. setuptools <= 65.0.0
The conda environment that provides these is provided in conda_environment_PyDSTool.yml. To set up this envornment, go to the base environment and execute the following command:
                          conda env create -f conda_environment_PyDSTool.yml

To run the SBI parameter analysis for Motif 1 or Motif 2, execute the codes in the folder Motif1_SBI_analysis and Motif2_SBI_analysis. Here, run the files run_motif1_SBIanalysis.py anf run_motif2_SBIanalysis.py for Motif 1 and Motif 2 respectively in the command line as follows:
  1. python run_motif1_SBIanalysis.py 2 1
  2. python run_motif2_SBIanalysis.py 4 1
The first input option, given here as 2 in 1. and 4 in 2. represents the choice of SBI parameter analysis function. The second input represents experiment/run number to keep track of runs.

Similarly run the stimulation analysis for both Motif 1 and motif 2:
  1. python run_motif1_stim_analysis.py 2 1
  2. python run_motif2_stim_analysis.py 3 2

The firing rate data is stoked in a list for both the neurons in the motifs and ultimately stored as pickle files. The pickle files are too large to upload on the github and hence do let me know if you want to have access to them, I could provide you with a drive link.

The data visualuzation and plottfing codes are provided in the Data_visualization folder which plots the results given in the paper.
