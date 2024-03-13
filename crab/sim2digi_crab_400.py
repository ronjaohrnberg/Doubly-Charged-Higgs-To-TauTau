from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SIM2DIGI_400_090124_part1_10000'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18DIGI-00015_1_400_part1_cfg.py'
config.JobType.maxMemoryMB = 2400
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-GEN2SIM_300_090124_part1_10000-397dc7239876db084790767ceffd6993/USER'
config.Data.inputDBS = 'phys03' # global

config.Data.splitting = 'FileBased' #'LumiBased'  #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 1
NJOBS = 1
config.Data.totalUnits = 10000
config.Data.outputDatasetTag = 'SIM2DIGI_400_090124_part1_10000'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
