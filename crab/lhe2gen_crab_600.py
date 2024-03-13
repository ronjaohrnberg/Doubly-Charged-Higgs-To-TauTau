from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'LHE2GEN_600_210124_part1_10000'

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'EGM-RunIISummer19UL18GEN-00008_1_600_part1_cfg.py'

#200922mass600_ecm6500/Events/
config.JobType.inputFiles = ['200922mass600_ecm6500/Events/run_100/unweighted_events.lhe','200922mass600_ecm6500/Events/run_99/unweighted_events.lhe','200922mass600_ecm6500/Events/run_98/unweighted_events.lhe','200922mass600_ecm6500/Events/run_97/unweighted_events.lhe','200922mass600_ecm6500/Events/run_96/unweighted_events.lhe','200922mass600_ecm6500/Events/run_95/unweighted_events.lhe','200922mass600_ecm6500/Events/run_94/unweighted_events.lhe','200922mass600_ecm6500/Events/run_93/unweighted_events.lhe','200922mass600_ecm6500/Events/run_92/unweighted_events.lhe','200922mass600_ecm6500/Events/run_91/unweighted_events.lhe','200922mass600_ecm6500/Events/run_90/unweighted_events.lhe','200922mass600_ecm6500/Events/run_89/unweighted_events.lhe','200922mass600_ecm6500/Events/run_88/unweighted_events.lhe','200922mass600_ecm6500/Events/run_87/unweighted_events.lhe','200922mass600_ecm6500/Events/run_86/unweighted_events.lhe','200922mass600_ecm6500/Events/run_85/unweighted_events.lhe','200922mass600_ecm6500/Events/run_84/unweighted_events.lhe','200922mass600_ecm6500/Events/run_83/unweighted_events.lhe','200922mass600_ecm6500/Events/run_82/unweighted_events.lhe','200922mass600_ecm6500/Events/run_81/unweighted_events.lhe','200922mass600_ecm6500/Events/run_80/unweighted_events.lhe','200922mass600_ecm6500/Events/run_79/unweighted_events.lhe','200922mass600_ecm6500/Events/run_78/unweighted_events.lhe','200922mass600_ecm6500/Events/run_77/unweighted_events.lhe','200922mass600_ecm6500/Events/run_76/unweighted_events.lhe','200922mass600_ecm6500/Events/run_75/unweighted_events.lhe','200922mass600_ecm6500/Events/run_74/unweighted_events.lhe','200922mass600_ecm6500/Events/run_73/unweighted_events.lhe','200922mass600_ecm6500/Events/run_72/unweighted_events.lhe','200922mass600_ecm6500/Events/run_71/unweighted_events.lhe','200922mass600_ecm6500/Events/run_70/unweighted_events.lhe','200922mass600_ecm6500/Events/run_69/unweighted_events.lhe','200922mass600_ecm6500/Events/run_68/unweighted_events.lhe','200922mass600_ecm6500/Events/run_67/unweighted_events.lhe','200922mass600_ecm6500/Events/run_66/unweighted_events.lhe','200922mass600_ecm6500/Events/run_65/unweighted_events.lhe','200922mass600_ecm6500/Events/run_64/unweighted_events.lhe','200922mass600_ecm6500/Events/run_63/unweighted_events.lhe','200922mass600_ecm6500/Events/run_62/unweighted_events.lhe','200922mass600_ecm6500/Events/run_61/unweighted_events.lhe','200922mass600_ecm6500/Events/run_60/unweighted_events.lhe','200922mass600_ecm6500/Events/run_59/unweighted_events.lhe','200922mass600_ecm6500/Events/run_58/unweighted_events.lhe','200922mass600_ecm6500/Events/run_57/unweighted_events.lhe','200922mass600_ecm6500/Events/run_56/unweighted_events.lhe','200922mass600_ecm6500/Events/run_55/unweighted_events.lhe','200922mass600_ecm6500/Events/run_54/unweighted_events.lhe','200922mass600_ecm6500/Events/run_53/unweighted_events.lhe','200922mass600_ecm6500/Events/run_52/unweighted_events.lhe','200922mass600_ecm6500/Events/run_51/unweighted_events.lhe']
config.Data.inputDBS = 'global' 

config.Data.outputPrimaryDataset = 'CRAB_PrivateMC' 
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100 #2000
NJOBS = 50
config.Data.totalUnits = 10000 #500000 #config.Data.unitsPerJob * NJOBS

config.Data.outputDatasetTag = 'LHE2GEN_600_210124_part1_1000'

config.Data.publication = True

config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX"
