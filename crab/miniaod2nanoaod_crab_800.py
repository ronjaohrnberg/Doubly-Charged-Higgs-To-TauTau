from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MiniAOD2NanoAOD_800_230124_part1_10000'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18NanoAOD-00028_1_800_part1_cfg.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-RECO2MiniAOD_800_230124_part1_10000-db45fee337e0994af9218e5fc86c79a3/USER'
config.Data.inputDBS = 'phys03' #'global'

config.Data.splitting = 'FileBased' #'LumiBased'  #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits = 10000 

config.Data.outputDatasetTag = 'MiniAOD2NanoAOD_800_230124_part1_10000'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
