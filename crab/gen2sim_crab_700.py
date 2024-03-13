from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'GEN2SIM_700_210124_part1_10000'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18SIM-00022_1_700_part1_cfg.py' #'EGM-RunIISummer19UL18SIM-00022_1_300_part1_cfg.py'
config.JobType.maxMemoryMB = 1900
#config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-LHE2GEN_700_210124_part1_1000-9ecceeec9fd6f907b9d5dfb6f58ed18e/USER'
config.Data.inputDBS = 'phys03' #'global'


config.Data.splitting = 'FileBased' #'EventAwareLumiBased' #'LumiBased' #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 10000 

config.Data.outputDatasetTag = 'GEN2SIM_700_210124_part1_10000'

config.Data.publication = True

config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
