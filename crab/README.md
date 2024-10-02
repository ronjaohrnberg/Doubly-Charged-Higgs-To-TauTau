The following work on lxplus7 CMSSW_10_6_24, except for digi2hlt step which works in CMSSW_10_2_16_UL.

The steps are in order: lhe2gen, gen2sim, sim2digi, digi2hlt, hlt2reco, reco2miniaod, miniaod2nanoaod.
You can submit the configuration file with the command:
crab submit -c lhe2gen_crab_300.py
and check the status with:
crab status -d <folder>
which should yield the dataset name once ready, which will be then used as an input dataset in later steps.

For lhe2gen you have to have have the Les Houches event files locally (if you have many, you have to add them in parts):
config.JobType.inputFiles = ['mass300/Events/run_03/unweighted_events.lhe','mass300/Events/run_02/unweighted_events.lhe','mass300/Events/run_01/unweighted_events.lhe']
config.Data.inputDBS = 'global'

For other steps, you need to input them from datasets such as below:
config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-LHE2GEN_300_311023-9ecceeec9fd6f907b9d5dfb6f58ed18e/USER'
config.Data.inputDBS = 'phys03'

The file names in EGM-RunIISummer19UL18<step>_1_<mass>_cfg.py should also be checked to match those in the datasets.