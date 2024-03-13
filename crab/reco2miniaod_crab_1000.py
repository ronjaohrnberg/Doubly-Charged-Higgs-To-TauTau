from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'RECO2MiniAOD_1000_230124_part1_10000'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18MiniAOD-00026_1_1000_part1_cfg.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-HLT2RECO_1000_220124_part1_10000-ce2d8483a217bdee138ad6a78c69df45/USER'
config.Data.inputDBS = 'phys03' #'global'

config.Data.splitting = 'FileBased'  #'LumiBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 2
config.Data.totalUnits = 10000
config.Data.outputDatasetTag = 'RECO2MiniAOD_1000_230124_part1_10000'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
