from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HLT2RECO_700_220124_part1_10000'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18RECO-00025_1_700_part1_cfg.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-DIGI2HLT_700_220124_part1_10000-b403a189a2d057e62e59ed092120c7f4/USER'
config.Data.inputDBS = 'phys03' #'global'

config.Data.splitting = 'FileBased' #'LumiBased'  #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 10000 

config.Data.outputDatasetTag = 'HLT2RECO_700_220124_part1_10000'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
