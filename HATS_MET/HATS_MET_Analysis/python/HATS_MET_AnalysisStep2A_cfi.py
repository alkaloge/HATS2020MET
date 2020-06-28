import FWCore.ParameterSet.Config as cms

metandpuanalstep2a = cms.EDAnalyzer('HATS_MET_AnalysisStep2A',
                                    doprints = cms.bool(True),      
                                    mets     = cms.InputTag("slimmedMETs")
                                    )
