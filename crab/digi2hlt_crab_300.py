from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DIGI2HLT_300_040124_test50events_t2hip'

config.JobType.pluginName = 'Analysis' #'PrivateMC' 
config.JobType.psetName = 'EGM-RunIISummer19UL18HLT-00026_1_300_cfg.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/CRAB_PrivateMC/rohrnber-SIM2DIGI_300_s23_test50events_t2hip-b20238ea3fc5080b0f98a6952cc4fe0b/USER' #'/CRAB_PrivateMC/rohrnber-SIM2DIGI_300_s23_test50events_t2hip_v3-b20238ea3fc5080b0f98a6952cc4fe0b/USER' #'/CRAB_PrivateMC/rohrnber-SIM2DIGI_300_s23_test50events_t2hip_v2-b20238ea3fc5080b0f98a6952cc4fe0b/USER'
config.Data.inputDBS = 'phys03' #'global'

#config.Data.outputPrimaryDataset = 'GEN2SIM_300_s23_test500events_t2hip' #'CRAB_PrivateMC' 
config.Data.splitting = 'LumiBased'  #'FileBased' #'Automatic' #'EventBased'
config.Data.unitsPerJob = 50
NJOBS = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outputDatasetTag = 'DIGI2HLT_300_040124_test50events_t2hip'
config.Data.publication = True
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX" 
