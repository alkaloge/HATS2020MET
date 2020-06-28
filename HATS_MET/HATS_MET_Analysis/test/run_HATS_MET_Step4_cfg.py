import FWCore.ParameterSet.Config as cms

process = cms.Process("HATS2020metandpu")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1


#process.TFileService = cms.Service("TFileService", fileName = cms.string("./outputs/metandpu_step4.root") )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring([
            'file:/eos/uscms/store/user/cmsdas/2020/short_exercises/METAndPU/MC/fireworks.root',
            ]
                                      )
    )

process.load("HATS_MET.HATS_MET_Analysis.HATS_MET_AnalysisStep4_cfi")
process.p = cms.Path(process.metandpuanalstep4)

