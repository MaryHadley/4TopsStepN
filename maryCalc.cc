#include <iostream>
#include <limits>   // std::numeric_limits

#include "LJMet/Com/interface/BaseCalc.h"
#include "LJMet/Com/interface/LjmetFactory.h"
#include "LJMet/Com/interface/LjmetEventContent.h"
#include "TLorentzVector.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObject.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"
#include "LJMet/Com/interface/MVAElectronSelector.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "DataFormats/BTauReco/interface/CATopJetTagInfo.h"
#include "LJMet/Com/interface/MiniIsolation.h"

#include "LHAPDF/LHAPDF.h"
#include "LHAPDF/GridPDF.h"
#include "LHAPDF/Info.h"
#include "LHAPDF/Config.h"
#include "LHAPDF/PDFInfo.h"
#include "LHAPDF/PDFSet.h"
#include "LHAPDF/Factories.h"

using std::cout;
using std::endl;

class LjmetFactory;

class maryCalc : public BaseCalc {
public:
    maryCalc();
    virtual ~maryCalc();
    virtual int BeginJob();
    virtual int AnalyzeEvent(edm::EventBase const & event, BaseEventSelector * selector);
    virtual int EndJob(){return 0;};

private: 
    bool isMC;
    std::string dataType;

};

static int reg = LjmetFactory::GetInstance()->Register(new maryCalc(), "maryCalc");

using namespace LHAPDF;


maryCalc::maryCalc()
{
}
maryCalc::~maryCalc()
{
}

int maryCalc::BeginJob(){

    if (mPset.exists("dataType"))     dataType = mPset.getParameter<std::string>("dataType");
    else                              dataType = "None";
    if (mPset.exists("isMC"))         isMC = mPset.getParameter<bool>("isMC");
    else                              isMC = false;

    return 0;
}

int maryCalc::AnalyzeEvent(edm::EventBase const & event, BaseEventSelector * selector) {

// Get Objects (also, selected)

   std::vector<edm::Ptr<pat::Jet>>             const & vSelJets = selector->GetSelectedJets();
   std::vector<edm::Ptr<pat::Muon>>            const & vSelMuons = selector->GetSelectedMuons();
   std::vector<edm::Ptr<pat::Electron>>        const & vSelElectrons = selector->GetSelectedElectrons();
//Get pointers (not selected)
   edm::Handle<std::vector<pat::Jet>>          vJets;
   edm::Handle<std::vector<pat::Muon>>         vMuons;
   edm::Handle<std::vector<pat::Electron>>     vElectrons; 
   
   //This getByLable stuff is important because otherwise your code will try to access a blank memory block and it will seg fault and your life will be sad
   event.getByLabel(edm::InputTag("slimmedJets"), vJets);
   event.getByLabel(edm::InputTag("slimmedMuons"), vMuons);
   event.getByLabel(edm::InputTag("slimmedElectrons"), vElectrons);
  
  //Get number of muons (not selected)
  int nMuons_all = vMuons->size();
  //Make the branch in your tree
  SetValue("nMuons_all", nMuons_all);
  
 //Get number of electrons (not selected)
 int nElectrons_all = vElectrons->size();
 //Make the branch in your tree
 SetValue("nElectrons_all", nElectrons_all);

 //Get number of muons (selected)
 int nMuons_sel = vSelMuons.size();
// Make the branch in your tree
 SetValue("nMuons_sel", nMuons_sel);

//Get number of electrons (selected)
int nElectrons_sel = vSelElectrons.size();
//Make the branch in your tree
SetValue("nElectrons_sel", nElectrons_sel);
                  

//Get number of jets (not selected)
int nJets_all = vJets->size();
SetValue("nJets_all", nJets_all);

//Get number of jets (selected)
int nJets_sel = vSelJets.size();
SetValue("nJets_sel", nJets_sel);

return 0;
}
