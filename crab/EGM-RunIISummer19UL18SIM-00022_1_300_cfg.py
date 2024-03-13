# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename EGM-RunIISummer19UL18SIM-00022_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:EGM-RunIISummer19UL18SIM-00022n5.root --conditions 106X_upgrade2018_realistic_v11_L1v1 --beamspot Realistic25ns13TeVEarly2018Collision --step SIM --geometry DB:Extended --filein file:../../CMSSW_10_6_12/src/EGM-RunIISummer19UL18GEN-00008n5.root --era Run2_2018 --runUnscheduled --no_exec --mc -n 5
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('SIM',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000000)
)

# Input source
process.source = cms.Source("PoolSource", #"EmptySource" "PoolSource",
                            fileNames = cms.untracked.vstring('file:EGM-RunIISummer19UL18GEN-00008_300_part2_1.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_2.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_3.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_4.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_5.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_6.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_7.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_8.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_9.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_10.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_11.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_12.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_13.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_14.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_15.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_16.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_17.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_18.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_19.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_20.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_21.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_22.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_23.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_24.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_25.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_26.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_27.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_28.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_29.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_30.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_31.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_32.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_33.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_34.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_35.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_36.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_37.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_38.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_39.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_40.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_41.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_42.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_43.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_44.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_45.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_46.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_47.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_48.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_49.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_50.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_51.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_52.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_53.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_54.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_55.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_56.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_57.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_58.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_59.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_60.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_61.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_62.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_63.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_64.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_65.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_66.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_67.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_68.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_69.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_70.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_71.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_72.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_73.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_74.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_75.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_76.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_77.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_78.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_79.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_80.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_81.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_82.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_83.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_84.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_85.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_86.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_87.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_88.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_89.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_90.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_91.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_92.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_93.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_94.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_95.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_96.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_97.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_98.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_99.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_100.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_101.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_102.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_103.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_104.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_105.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_106.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_107.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_108.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_109.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_110.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_111.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_112.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_113.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_114.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_115.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_116.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_117.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_118.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_119.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_120.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_121.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_122.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_123.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_124.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_125.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_126.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_127.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_128.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_129.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_130.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_131.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_132.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_133.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_134.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_135.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_136.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_137.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_138.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_139.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_140.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_141.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_142.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_143.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_144.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_145.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_146.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_147.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_148.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_149.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_150.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_151.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_152.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_153.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_154.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_155.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_156.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_157.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_158.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_159.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_160.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_161.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_162.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_163.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_164.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_165.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_166.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_167.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_168.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_169.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_170.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_171.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_172.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_173.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_174.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_175.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_176.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_177.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_178.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_179.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_180.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_181.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_182.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_183.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_184.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_185.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_186.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_187.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_188.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_189.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_190.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_191.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_192.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_193.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_194.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_195.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_196.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_197.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_198.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_199.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_200.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_201.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_202.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_203.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_204.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_205.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_206.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_207.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_208.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_209.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_210.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_211.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_212.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_213.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_214.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_215.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_216.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_217.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_218.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_219.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_220.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_221.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_222.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_223.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_224.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_225.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_226.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_227.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_228.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_229.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_230.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_231.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_232.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_233.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_234.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_235.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_236.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_237.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_238.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_239.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_240.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_241.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_242.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_243.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_244.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_245.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_246.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_247.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_248.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_249.root', 'file:EGM-RunIISummer19UL18GEN-00008_300_part2_250.root'),
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
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:EGM-RunIISummer19UL18SIM-00022_300_part2.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')

# Path and EndPath definitions
process.simulation_step = cms.Path(process.psim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
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


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
