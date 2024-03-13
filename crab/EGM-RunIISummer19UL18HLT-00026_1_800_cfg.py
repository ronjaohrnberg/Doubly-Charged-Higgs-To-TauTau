# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename EGM-RunIISummer19UL18HLT-00026_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:EGM-RunIISummer19UL18HLT-00026n5.root --conditions 102X_upgrade2018_realistic_v15 --customise_commands process.source.bypassVersionCheck = cms.untracked.bool(True) --step HLT:2018v32 --geometry DB:Extended --filein file:../../CMSSW_10_6_4_patch1/src/EGM-RunIISummer19UL18DIGI-00015n5.root --era Run2_2018 --no_exec --mc -n 5
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_2018v32_cff') #process.load('HLTrigger.Configuration.HLT_2018v32_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_1.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_2.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_3.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_4.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_5.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_6.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_7.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_8.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_9.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_10.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_11.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_12.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_13.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_14.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_15.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_16.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_17.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_18.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_19.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_20.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_21.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_22.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_23.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_24.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_25.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_26.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_27.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_28.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_29.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_30.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_31.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_32.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_33.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_34.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_35.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_36.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_37.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_38.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_39.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_40.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_41.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_42.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_43.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_44.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_45.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_46.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_47.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_48.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_49.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_50.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_51.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_52.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_53.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_54.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_55.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_56.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_57.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_58.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_59.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_60.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_61.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_62.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_63.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_64.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_65.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_66.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_67.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_68.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_69.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_70.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_71.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_72.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_73.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_74.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_75.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_76.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_77.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_78.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_79.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_80.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_81.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_82.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_83.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_84.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_85.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_86.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_87.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_88.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_89.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_90.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_91.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_92.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_93.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_94.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_95.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_96.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_97.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_98.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_99.root','file:EGM-RunIISummer19UL18DIGI-00015_800_part1_10000_100.root'),
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

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:EGM-RunIISummer19UL18HLT-00026_800_part1_10000.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

process.source.bypassVersionCheck = cms.untracked.bool(True)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
