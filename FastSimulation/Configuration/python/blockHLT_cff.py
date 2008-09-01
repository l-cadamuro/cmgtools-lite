# /dev/CMSSW_2_1_5/HLT/V2 (CMSSW_2_1_5_HLT1)

import FWCore.ParameterSet.Config as cms

block_hltL1NonIsoLargeWindowElectronPixelSeeds = cms.PSet(
  SCEtCut = cms.double( 5.0 ),
  maxHOverE = cms.double( 0.2 ),
  hOverEConeSize = cms.double( 0.1 ),
  hbheInstance = cms.string( "" ),
  hbheModule = cms.string( "hbhereco" ),
  pPhiMax1 = cms.double( 0.045 ),
  pPhiMin1 = cms.double( -0.03 ),
  ePhiMax1 = cms.double( 0.03 ),
  ePhiMin1 = cms.double( -0.045 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  DeltaPhi1High = cms.double( 0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  SizeWindowENeg = cms.double( 0.675 ),
  HighPtThreshold = cms.double( 35.0 ),
  LowPtThreshold = cms.double( 5.0 ),
  searchInTIDTEC = cms.bool( True ),
  dynamicPhiRoad = cms.bool( False ),
  rMaxI = cms.double( 0.2 ),
  rMinI = cms.double( -0.2 ),
  r2MaxF = cms.double( 0.3 ),
  r2MinF = cms.double( -0.3 ),
  z2MaxB = cms.double( 0.2 ),
  z2MinB = cms.double( -0.2 ),
  PhiMax2 = cms.double( 0.01 ),
  PhiMin2 = cms.double( -0.01 ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  fromTrackerSeeds = cms.bool( False ),
  preFilteredSeeds = cms.bool( False ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" )
)
block_hltL1IsoLargeWindowElectronPixelSeeds = cms.PSet(
  SCEtCut = cms.double( 5.0 ),
  maxHOverE = cms.double( 0.2 ),
  hOverEConeSize = cms.double( 0.1 ),
  hbheInstance = cms.string( "" ),
  hbheModule = cms.string( "hbhereco" ),
  pPhiMax1 = cms.double( 0.045 ),
  pPhiMin1 = cms.double( -0.03 ),
  ePhiMax1 = cms.double( 0.03 ),
  ePhiMin1 = cms.double( -0.045 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  DeltaPhi1High = cms.double( 0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  SizeWindowENeg = cms.double( 0.675 ),
  HighPtThreshold = cms.double( 35.0 ),
  LowPtThreshold = cms.double( 5.0 ),
  searchInTIDTEC = cms.bool( True ),
  dynamicPhiRoad = cms.bool( False ),
  rMaxI = cms.double( 0.2 ),
  rMinI = cms.double( -0.2 ),
  r2MaxF = cms.double( 0.3 ),
  r2MinF = cms.double( -0.3 ),
  z2MaxB = cms.double( 0.2 ),
  z2MinB = cms.double( -0.2 ),
  PhiMax2 = cms.double( 0.01 ),
  PhiMin2 = cms.double( -0.01 ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  fromTrackerSeeds = cms.bool( False ),
  preFilteredSeeds = cms.bool( False ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" )
)
block_hltL1NonIsoStartUpElectronPixelSeeds = cms.PSet(
  SCEtCut = cms.double( 5.0 ),
  maxHOverE = cms.double( 0.2 ),
  hOverEConeSize = cms.double( 0.1 ),
  hbheInstance = cms.string( "" ),
  hbheModule = cms.string( "hbhereco" ),
  pPhiMax1 = cms.double( 0.025 ),
  pPhiMin1 = cms.double( -0.015 ),
  ePhiMax1 = cms.double( 0.015 ),
  ePhiMin1 = cms.double( -0.025 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  DeltaPhi1High = cms.double( 0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  SizeWindowENeg = cms.double( 0.675 ),
  HighPtThreshold = cms.double( 35.0 ),
  LowPtThreshold = cms.double( 5.0 ),
  searchInTIDTEC = cms.bool( True ),
  dynamicPhiRoad = cms.bool( False ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  r2MaxF = cms.double( 0.096 ),
  r2MinF = cms.double( -0.096 ),
  z2MaxB = cms.double( 0.06 ),
  z2MinB = cms.double( -0.06 ),
  PhiMax2 = cms.double( 0.0050 ),
  PhiMin2 = cms.double( -0.0050 ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  fromTrackerSeeds = cms.bool( False ),
  preFilteredSeeds = cms.bool( False ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" )
)
block_hltL1NonIsoElectronPixelSeeds = cms.PSet(
  SCEtCut = cms.double( 5.0 ),
  maxHOverE = cms.double( 0.2 ),
  hOverEConeSize = cms.double( 0.1 ),
  hbheInstance = cms.string( "" ),
  hbheModule = cms.string( "hbhereco" ),
  pPhiMax1 = cms.double( 0.025 ),
  pPhiMin1 = cms.double( -0.015 ),
  ePhiMax1 = cms.double( 0.015 ),
  ePhiMin1 = cms.double( -0.025 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  DeltaPhi1High = cms.double( 0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  SizeWindowENeg = cms.double( 0.675 ),
  HighPtThreshold = cms.double( 35.0 ),
  LowPtThreshold = cms.double( 5.0 ),
  searchInTIDTEC = cms.bool( True ),
  dynamicPhiRoad = cms.bool( False ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  r2MaxF = cms.double( 0.08 ),
  r2MinF = cms.double( -0.08 ),
  z2MaxB = cms.double( 0.05 ),
  z2MinB = cms.double( -0.05 ),
  PhiMax2 = cms.double( 0.0010 ),
  PhiMin2 = cms.double( -0.0010 ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  fromTrackerSeeds = cms.bool( False ),
  preFilteredSeeds = cms.bool( False ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" )
)
block_hltL1IsoStartUpElectronPixelSeeds = cms.PSet(
  SCEtCut = cms.double( 5.0 ),
  maxHOverE = cms.double( 0.2 ),
  hOverEConeSize = cms.double( 0.1 ),
  hbheInstance = cms.string( "" ),
  hbheModule = cms.string( "hbhereco" ),
  pPhiMax1 = cms.double( 0.025 ),
  pPhiMin1 = cms.double( -0.015 ),
  ePhiMax1 = cms.double( 0.015 ),
  ePhiMin1 = cms.double( -0.025 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  DeltaPhi1High = cms.double( 0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  SizeWindowENeg = cms.double( 0.675 ),
  HighPtThreshold = cms.double( 35.0 ),
  LowPtThreshold = cms.double( 5.0 ),
  searchInTIDTEC = cms.bool( True ),
  dynamicPhiRoad = cms.bool( False ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  r2MaxF = cms.double( 0.096 ),
  r2MinF = cms.double( -0.096 ),
  z2MaxB = cms.double( 0.06 ),
  z2MinB = cms.double( -0.06 ),
  PhiMax2 = cms.double( 0.0050 ),
  PhiMin2 = cms.double( -0.0050 ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  fromTrackerSeeds = cms.bool( False ),
  preFilteredSeeds = cms.bool( False ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" )
)
block_hltL1IsoElectronPixelSeeds = cms.PSet(
  SCEtCut = cms.double( 5.0 ),
  maxHOverE = cms.double( 0.2 ),
  hOverEConeSize = cms.double( 0.1 ),
  hbheInstance = cms.string( "" ),
  hbheModule = cms.string( "hbhereco" ),
  pPhiMax1 = cms.double( 0.025 ),
  pPhiMin1 = cms.double( -0.015 ),
  ePhiMax1 = cms.double( 0.015 ),
  ePhiMin1 = cms.double( -0.025 ),
  DeltaPhi2 = cms.double( 0.0040 ),
  DeltaPhi1High = cms.double( 0.08 ),
  DeltaPhi1Low = cms.double( 0.23 ),
  SizeWindowENeg = cms.double( 0.675 ),
  HighPtThreshold = cms.double( 35.0 ),
  LowPtThreshold = cms.double( 5.0 ),
  searchInTIDTEC = cms.bool( True ),
  dynamicPhiRoad = cms.bool( False ),
  rMaxI = cms.double( 0.11 ),
  rMinI = cms.double( -0.11 ),
  r2MaxF = cms.double( 0.08 ),
  r2MinF = cms.double( -0.08 ),
  z2MaxB = cms.double( 0.05 ),
  z2MinB = cms.double( -0.05 ),
  PhiMax2 = cms.double( 0.0010 ),
  PhiMin2 = cms.double( -0.0010 ),
  hcalRecHits = cms.InputTag( "hltHbhereco" ),
  fromTrackerSeeds = cms.bool( False ),
  preFilteredSeeds = cms.bool( False ),
  initialSeeds = cms.InputTag( "globalMixedSeeds" )
)
block_hltL3TrajectorySeed = cms.PSet(
  beamSpot = cms.InputTag( "offlineBeamSpot" ),
  UseVertex = cms.bool( False ),
  Rescale_eta = cms.double( 3.0 ),
  Rescale_phi = cms.double( 3.0 ),
  Rescale_Dz = cms.double( 3.0 ),
  DeltaZ_Region = cms.double( 15.9 ),
  DeltaR = cms.double( 0.2 ),
  EscapePt = cms.double( 1.5 ),
  Phi_min = cms.double( 0.1 ),
  Eta_min = cms.double( 0.1 ),
  UseFixedRegion = cms.bool( False ),
  EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
  EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
  PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
  PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
  vertexCollection = cms.InputTag( "pixelVertices" ),
  Eta_fixed = cms.double( 0.2 ),
  Phi_fixed = cms.double( 0.2 ),
  OnDemand = cms.double( -1.0 )
)
