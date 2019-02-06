#include "step1.cc" //you have to change this to match whatever the name of your .cc file is
//#include "MARY_1FEB2019_step1.cc"

void testStep1(){
  
  //TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/2016/LJMet_1lepTT_070516/nominal/SingleMuon_PRB2/SingleMuon_PRB2_60.root";
  //TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/2018/LJMet94X_1lepTT_091518/nominal/TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8/TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_1.root";
//  TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/2018/LJMet102X_1lep_111618/nominal/Data18_SingleMuon_17Sep18/Data18_SingleMuon_17Sep18_993.root";
  //TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/2018/LJMet94X_1lepTT_091518/nominal/SingleMuon_Mar2018/SingleMuon_Mar2018_993.root";
// TString inputFile="/uscms_data/d3/mhadley/LJMET_for_4Tops_firstTest/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/4T_17_MC_Signal_List_1.root"; //put my test file here
 TString inputFile ="TT_17_MC_Bkg_List_1.root"; //TT semilep bkg
  
  TString outputFile="Mary_test_TTSemiLep_17_MC_Bkg_6_Feb_2019.root";
  
  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");
  
  step1 t(inputFile,outputFile);
  t.Loop();
}


