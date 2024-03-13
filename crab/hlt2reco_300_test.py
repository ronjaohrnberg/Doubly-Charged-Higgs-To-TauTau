from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HLT2RECO_300_s23_test50events_t2hip_2'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18RECO-00025_1_300_cfg.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-DIGI2HLT_300_s23_test50events_t2hip-b6b9e899d12545712721992b50e8a22e/USER'
config.Data.inputDBS = 'phys03' #'global'

config.Data.splitting = 'LumiBased'  #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 50
NJOBS = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outputDatasetTag = 'HLT2RECO_300_s23_test50events_t2hip_2'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
