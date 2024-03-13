# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename EGM-RunIISummer19UL18MiniAOD-00026_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:EGM-RunIISummer19UL18MiniAOD-00026n5.root --conditions 106X_upgrade2018_realistic_v11_L1v1 --step PAT --geometry DB:Extended --filein file:EGM-RunIISummer19UL18RECO-00025n5.root --era Run2_2018 --runUnscheduled --no_exec --mc -n 5
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('PAT',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_1.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_2.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_3.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_4.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_5.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_6.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_7.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_8.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_9.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_10.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_11.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_12.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_13.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_14.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_15.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_16.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_17.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_18.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_19.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_20.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_21.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_22.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_23.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_24.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_25.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_26.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_27.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_28.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_29.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_30.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_31.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_32.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_33.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_34.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_35.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_36.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_37.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_38.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_39.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_40.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_41.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_42.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_43.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_44.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_45.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_46.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_47.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_48.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_49.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_50.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_51.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_52.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_53.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_54.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_55.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_56.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_57.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_58.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_59.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_60.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_61.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_62.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_63.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_64.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_65.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_66.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_67.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_68.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_69.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_70.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_71.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_72.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_73.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_74.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_75.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_76.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_77.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_78.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_79.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_80.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_81.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_82.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_83.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_84.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_85.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_86.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_87.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_88.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_89.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_90.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_91.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_92.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_93.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_94.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_95.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_96.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_97.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_98.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_99.root', 'file:EGM-RunIISummer19UL18RECO-00025_500_part1_10000_100.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:5'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
