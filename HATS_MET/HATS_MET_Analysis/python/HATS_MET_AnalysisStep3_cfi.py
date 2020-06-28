import FWCore.ParameterSet.Config as cms

metandpuanalstep3 = cms.EDAnalyzer('HATS_MET_AnalysisStep3',
                                   vertices  = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                   mets       = cms.InputTag("slimmedMETs"),
                                   metspuppi  = cms.InputTag("slimmedMETsPuppi"),
                                   muons     = cms.InputTag("slimmedMuons"),
                                   )
