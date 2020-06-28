import FWCore.ParameterSet.Config as cms

process = cms.Process("das2019metandpu")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.TFileService = cms.Service("TFileService",
    fileName = cms.string("metandpu_step3.root"),
    closeFileFast = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring([
            '/store/user/cmsdas/2019/short_exercises/METAndPU/data/handson1_dylljets_amcatnlo.root',
            ]
                                      )
    )

process.load("MetAndPu.MetAndPuAnal.MetAndPuAnalStep3_cfi")
process.p = cms.Path(process.metandpuanalstep3)
