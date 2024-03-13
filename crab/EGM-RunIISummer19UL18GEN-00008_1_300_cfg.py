# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Example_cff.py --python_filename EGM-RunIISummer19UL18GEN-00008_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --fileout file:EGM-RunIISummer19UL18GEN-00008n5.root --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN --geometry DB:Extended --era Run2_2018 --no_exec --mc -n 5
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('GEN',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("LHESource",
                            fileNames = cms.untracked.vstring(['file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe','file:unweighted_events.lhe']) #(['260822mass300/Events/run_99/unweighted_events.lhe','260822mass300/Events/run_98/unweighted_events.lhe','260822mass300/Events/run_97/unweighted_events.lhe','260822mass300/Events/run_96/unweighted_events.lhe','260822mass300/Events/run_95/unweighted_events.lhe','260822mass300/Events/run_94/unweighted_events.lhe','260822mass300/Events/run_93/unweighted_events.lhe','260822mass300/Events/run_92/unweighted_events.lhe','260822mass300/Events/run_91/unweighted_events.lhe','260822mass300/Events/run_90/unweighted_events.lhe','260822mass300/Events/run_89/unweighted_events.lhe','260822mass300/Events/run_88/unweighted_events.lhe','260822mass300/Events/run_87/unweighted_events.lhe','260822mass300/Events/run_86/unweighted_events.lhe','260822mass300/Events/run_85/unweighted_events.lhe','260822mass300/Events/run_84/unweighted_events.lhe','260822mass300/Events/run_83/unweighted_events.lhe','260822mass300/Events/run_82/unweighted_events.lhe','260822mass300/Events/run_81/unweighted_events.lhe','260822mass300/Events/run_80/unweighted_events.lhe','260822mass300/Events/run_79/unweighted_events.lhe','260822mass300/Events/run_78/unweighted_events.lhe','260822mass300/Events/run_77/unweighted_events.lhe','260822mass300/Events/run_76/unweighted_events.lhe','260822mass300/Events/run_75/unweighted_events.lhe','260822mass300/Events/run_74/unweighted_events.lhe','260822mass300/Events/run_73/unweighted_events.lhe','260822mass300/Events/run_72/unweighted_events.lhe','260822mass300/Events/run_71/unweighted_events.lhe','260822mass300/Events/run_70/unweighted_events.lhe','260822mass300/Events/run_69/unweighted_events.lhe','260822mass300/Events/run_68/unweighted_events.lhe','260822mass300/Events/run_67/unweighted_events.lhe','260822mass300/Events/run_66/unweighted_events.lhe','260822mass300/Events/run_65/unweighted_events.lhe','260822mass300/Events/run_64/unweighted_events.lhe','260822mass300/Events/run_63/unweighted_events.lhe','260822mass300/Events/run_62/unweighted_events.lhe','260822mass300/Events/run_61/unweighted_events.lhe','260822mass300/Events/run_60/unweighted_events.lhe','260822mass300/Events/run_59/unweighted_events.lhe','260822mass300/Events/run_58/unweighted_events.lhe','260822mass300/Events/run_57/unweighted_events.lhe','260822mass300/Events/run_56/unweighted_events.lhe','260822mass300/Events/run_55/unweighted_events.lhe','260822mass300/Events/run_54/unweighted_events.lhe','260822mass300/Events/run_53/unweighted_events.lhe','260822mass300/Events/run_52/unweighted_events.lhe','260822mass300/Events/run_51/unweighted_events.lhe']) #'gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_50/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_49/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_48/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_47/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_46/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_45/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_44/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_43/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_42/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_41/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_40/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_39/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_38/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_37/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_36/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_35/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_34/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_33/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_32/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_31/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_30/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_29/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_28/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_27/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_26/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_25/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_24/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_23/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_22/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_21/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_20/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_19/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_18/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_17/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_16/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_15/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_14/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_13/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_12/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_11/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_10/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_09/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_08/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_07/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_06/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_05/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_04/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_03/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_02/unweighted_events.lhe','gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/CMSSW_10_6_24/src/260822mass300/Events/run_01/unweighted_events.lhe'])#'gsiftp://eosuserftp.cern.ch/eos/user/r/rohrnber/LHEfiles/mass500/run_01/unweighted_events.lhe']) #(['/store/user/rohrnber/CRAB_PrivateMC/LHEfiles/mass500/run_01/unweighted_events.lhe'])#('file:gsiftp://madhatter.csc.fi/pnfs/csc.fi/data/cms/store/user/rohrnber/CRAB_PrivateMC/LHEfiles/mass500/run_01/unweighted_events.lhe') #cms.untracked.vstring('file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_99/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_98/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_97/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_96/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_95/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_94/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_93/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_92/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_91/unweighted_events.lhe','file:gsiftp://eosuserftp.cern.ch/eos/home-r/rohrnber/LHEfiles/mass500_ecm6500_130922_events/run_90/unweighted_events.lhe')#('file:mass500_ecm6500_runs100_merge.lhe') #290422_300events.lhe') #mass500_ecm6500_runs100_merge.lhe') #290422_300events.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Example_cff.py nevts:5'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:EGM-RunIISummer19UL18GEN-00008_300_part2.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v4', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        JetMatchingParameters = cms.vstring('JetMatching:setMad = off'),
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'JetMatchingParameters'
        ),
        pythia8CUEP8M1Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(14000.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

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
