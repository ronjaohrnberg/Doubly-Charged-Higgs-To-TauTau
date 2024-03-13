from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DIGI2HLT_600_220124_part1_10000'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18HLT-00026_1_600_part1_cfg.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-SIM2DIGI_600_220124_part1_10000-b20238ea3fc5080b0f98a6952cc4fe0b/USER'
config.Data.inputDBS = 'phys03' #'global'

config.Data.splitting = 'FileBased' #'LumiBased'  #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 1
NJOBS = 1
config.Data.totalUnits = 10000 #config.Data.unitsPerJob * NJOBS
config.Data.outputDatasetTag = 'DIGI2HLT_600_220124_part1_10000'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
