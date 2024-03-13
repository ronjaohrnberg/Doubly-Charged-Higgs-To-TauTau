from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'LHE2GEN_500_090124_part1_10000'

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'EGM-RunIISummer19UL18GEN-00008_1_500_part1_cfg.py'

config.JobType.inputFiles = ['mass500_ecm6500_130922_events/run_100/unweighted_events.lhe','mass500_ecm6500_130922_events/run_99/unweighted_events.lhe','mass500_ecm6500_130922_events/run_98/unweighted_events.lhe','mass500_ecm6500_130922_events/run_97/unweighted_events.lhe','mass500_ecm6500_130922_events/run_96/unweighted_events.lhe','mass500_ecm6500_130922_events/run_95/unweighted_events.lhe','mass500_ecm6500_130922_events/run_94/unweighted_events.lhe','mass500_ecm6500_130922_events/run_93/unweighted_events.lhe','mass500_ecm6500_130922_events/run_92/unweighted_events.lhe','mass500_ecm6500_130922_events/run_91/unweighted_events.lhe','mass500_ecm6500_130922_events/run_90/unweighted_events.lhe','mass500_ecm6500_130922_events/run_89/unweighted_events.lhe','mass500_ecm6500_130922_events/run_88/unweighted_events.lhe','mass500_ecm6500_130922_events/run_87/unweighted_events.lhe','mass500_ecm6500_130922_events/run_86/unweighted_events.lhe','mass500_ecm6500_130922_events/run_85/unweighted_events.lhe','mass500_ecm6500_130922_events/run_84/unweighted_events.lhe','mass500_ecm6500_130922_events/run_83/unweighted_events.lhe','mass500_ecm6500_130922_events/run_82/unweighted_events.lhe','mass500_ecm6500_130922_events/run_81/unweighted_events.lhe','mass500_ecm6500_130922_events/run_80/unweighted_events.lhe','mass500_ecm6500_130922_events/run_79/unweighted_events.lhe','mass500_ecm6500_130922_events/run_78/unweighted_events.lhe','mass500_ecm6500_130922_events/run_77/unweighted_events.lhe','mass500_ecm6500_130922_events/run_76/unweighted_events.lhe','mass500_ecm6500_130922_events/run_75/unweighted_events.lhe','mass500_ecm6500_130922_events/run_74/unweighted_events.lhe','mass500_ecm6500_130922_events/run_73/unweighted_events.lhe','mass500_ecm6500_130922_events/run_72/unweighted_events.lhe','mass500_ecm6500_130922_events/run_71/unweighted_events.lhe','mass500_ecm6500_130922_events/run_70/unweighted_events.lhe','mass500_ecm6500_130922_events/run_69/unweighted_events.lhe','mass500_ecm6500_130922_events/run_68/unweighted_events.lhe','mass500_ecm6500_130922_events/run_67/unweighted_events.lhe','mass500_ecm6500_130922_events/run_66/unweighted_events.lhe','mass500_ecm6500_130922_events/run_65/unweighted_events.lhe','mass500_ecm6500_130922_events/run_64/unweighted_events.lhe','mass500_ecm6500_130922_events/run_63/unweighted_events.lhe','mass500_ecm6500_130922_events/run_62/unweighted_events.lhe','mass500_ecm6500_130922_events/run_61/unweighted_events.lhe','mass500_ecm6500_130922_events/run_60/unweighted_events.lhe','mass500_ecm6500_130922_events/run_59/unweighted_events.lhe','mass500_ecm6500_130922_events/run_58/unweighted_events.lhe','mass500_ecm6500_130922_events/run_57/unweighted_events.lhe','mass500_ecm6500_130922_events/run_56/unweighted_events.lhe','mass500_ecm6500_130922_events/run_55/unweighted_events.lhe','mass500_ecm6500_130922_events/run_54/unweighted_events.lhe','mass500_ecm6500_130922_events/run_53/unweighted_events.lhe','mass500_ecm6500_130922_events/run_52/unweighted_events.lhe','mass500_ecm6500_130922_events/run_51/unweighted_events.lhe']
config.Data.inputDBS = 'global' 

config.Data.outputPrimaryDataset = 'CRAB_PrivateMC' 
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100 #2000
NJOBS = 50
config.Data.totalUnits = 10000 #500000 #config.Data.unitsPerJob * NJOBS

config.Data.outputDatasetTag = 'LHE2GEN_500_090124_part1_1000'

config.Data.publication = True

config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"  #"T3_CH_CERNBOX"
