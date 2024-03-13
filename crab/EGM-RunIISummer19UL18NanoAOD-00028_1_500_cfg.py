# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename EGM-RunIISummer19UL18NanoAOD-00028_1_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:EGM-RunIISummer19UL18NanoAOD-00028n5.root --conditions 106X_upgrade2018_realistic_v11_L1v1 --step NANO --filein file:../../CMSSW_10_6_4_patch1/src/EGM-RunIISummer19UL18MiniAOD-00026n5.root --era Run2_2018 --no_exec --mc -n 5
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('NANO',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_1.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_2.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_3.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_4.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_5.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_6.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_7.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_8.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_9.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_10.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_11.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_12.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_13.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_14.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_15.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_16.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_17.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_18.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_19.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_20.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_21.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_22.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_23.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_24.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_25.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_26.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_27.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_28.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_29.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_30.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_31.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_32.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_33.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_34.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_35.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_36.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_37.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_38.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_39.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_40.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_41.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_42.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_43.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_44.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_45.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_46.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_47.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_48.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_49.root', 'file:EGM-RunIISummer19UL18MiniAOD-00026_500_part1_10000_50.root'),
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

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:EGM-RunIISummer19UL18NanoAOD-00028_500_part1_10000.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
