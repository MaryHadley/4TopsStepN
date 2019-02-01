import ROOT
import math
import sys

#initialize counters
nEvents = 0
nMuEvents = 0
nElEvents = 0
mu7jets = 0
mu8jets = 0
mu9jets = 0
mu10jets = 0
mu11jets = 0
mu12jets = 0
mu13jets = 0

el8jets = 0
el9jets = 0
el10jets = 0
el11jets = 0
el12jets = 0

#Define histograms
h_mu_nJets_vs_AK4HT = ROOT.TH2F("NJets_vs_AK4HT_mu", "AK4 Jet HT vs. nJets in the Event for TTSemiLep  Mu Events; nJets; AK4HT (GeV)", 8, 6, 13, 50, 400, 800) #maybe tweak this

h_el_nJets_vs_AK4HT = ROOT.TH2F("NJets_vs_AK4HT_el", "AK4 Jet HT vs. NJets in the Event for TTSemiLep  El Events; nJets; AK4HT (GeV)", 8, 6, 13, 50, 400, 800)

h_mu_avg_AK4HT_vs_nJets = ROOT.TProfile("mu_prof_nJets_vs_avg_AK4HT", "Average AK4HT by Jet Multiplicity for TTSemiLep  Mu Events (GeV); nJets; Avg. AK4HT (GeV)", 8, 6, 13)

h_el_avg_AK4HT_vs_nJets = ROOT.TProfile("el_prof_nJets_vs_avg_AK4HT", "Average AK4HT by Jet Multiplicity for TTSemiLep  El Events (GeV); nJets; Avg. AK4HT (GeV)", 8, 6, 13)

f = ROOT.TFile("Mary_test_TTSemiLep_17_MC_Bkg_29_Jan_2019.root")
print "I got the file!"

t = f.Get("ljmet")
print "I got the tree!"

t.Print()

for event in t:
    nEvents +=1
    if event.isMuon == 1:
        #print "I am a muon event!"
        nMuEvents += 1
        
        if event.NJets_JetSubCalc < 7:
            continue
        h_mu_nJets_vs_AK4HT.Fill(event.NJets_JetSubCalc, event.AK4HT)
        h_mu_avg_AK4HT_vs_nJets.Fill(event.NJets_JetSubCalc, event.AK4HT)
        if event.NJets_JetSubCalc == 7:
            print "I am a mu event with 7 jets!"
            mu7jets += 1
        if event.NJets_JetSubCalc == 8:
            print "I am a mu event with 8 jets!"
            mu8jets += 1
        if event.NJets_JetSubCalc == 9:
            print "I am a mu event with 9 jets!"
            mu9jets += 1
        if event.NJets_JetSubCalc == 10:
            print "I am a mu event with 10 jets!"
            mu10jets += 1
        if event.NJets_JetSubCalc == 11:
            print "I am a mu event with 11 jets!"
            mu11jets +=1
        if event.NJets_JetSubCalc == 12:
            print "I am a mu event with 12 jets!"
            mu12jets +=1
        if event.NJets_JetSubCalc == 13:
            print "I am a mu event with 13 jets!"
            mu13jets +=1
     
    if event.isElectron ==1:
        #print "I am an electron event!"
        nElEvents += 1
        if event.NJets_JetSubCalc < 8:
           continue
        h_el_nJets_vs_AK4HT.Fill(event.NJets_JetSubCalc, event.AK4HT)
        h_el_avg_AK4HT_vs_nJets.Fill(event.NJets_JetSubCalc, event.AK4HT)
        if event.NJets_JetSubCalc == 8:
           print "I am an el event with 8 jets!"
           el8jets += 1
        if event.NJets_JetSubCalc == 9:
           print "I am an el event with 9 jets!"
           el9jets +=1
        if event.NJets_JetSubCalc == 10:
           print "I am an el event with 10 jets!"
           el10jets +=1
        if event.NJets_JetSubCalc == 11:
           print "I am an el event with 11 jets!"
           el11jets +=1
        if event.NJets_JetSubCalc == 12:
           print "I am an el event with 12 jets!"
           el12jets +=1

print "nEvents is:", nEvents 
print "nMuEvents is:", nMuEvents
print "nElEvents is:", nElEvents
print "Sum of nMuEvents and nElEvents is:", nMuEvents + nElEvents

if (nMuEvents + nElEvents) == nEvents:
    print "Sum of nMuEvents and nElEvents equals nEvents, as it should. Poodles! Success!"

print "mu7jets is:", mu7jets
print "mu8jets is:", mu8jets
print "mu9jets is:", mu9jets
print "mu10 jets is:", mu10jets
print "mu11 jets is:", mu11jets
print "mu12 jets is:", mu12jets
print "mu13 jets is:", mu13jets

print "el8jets is:", el8jets
print "el9jets is:", el9jets
print "el10jets is:", el10jets
print "el11jets is:", el11jets
print "el12jets is:", el12jets

#Draw histograms
c1 = ROOT.TCanvas()
ROOT.gStyle.SetStatX(.7)
h_mu_nJets_vs_AK4HT.Scale(121) #lumi recorded in 2017 is 45 inv  fb, cross section for TTSemiLep  tops is 888000 fb, nEventsGenerated before any cuts is 328994 for the file files I ran over
h_mu_nJets_vs_AK4HT.Draw("COLZ")
c1.SaveAs("TTSemiLep_Bkg_mu_nJets_vs_AK4HT.pdf")

c2 = ROOT.TCanvas()
ROOT.gStyle.SetStatX(.7)
h_el_nJets_vs_AK4HT.Scale(121) #lumi recorded in 2017 is 45 inv fb, cross section for TTSemiLep  is 888000 fb, nEventsGenerated before any cuts is 328994 for the file files I ran over
h_el_nJets_vs_AK4HT.Draw("COLZ")
c2.SaveAs("TTSemiLep_Bkg_el_nJets_vs_AK4HT.pdf")

c3 = ROOT.TCanvas()
ROOT.gStyle.SetStatY(.4)
h_mu_avg_AK4HT_vs_nJets.Scale(1) #I think this is ok because it is an average already
h_mu_avg_AK4HT_vs_nJets.Draw() 
c3.SaveAs("TTSemiLep_Bkg_mu_prof_nJets_vs_avg_AK4HT.pdf")

c4 = ROOT.TCanvas()
ROOT.gStyle.SetStatY(.4)
h_el_avg_AK4HT_vs_nJets.Scale(1) #I think this is ok because it is an average already
h_el_avg_AK4HT_vs_nJets.Draw()
c4.SaveAs("TTSemiLep_Bkg_el_prof_nJets_vs_avg_AK4HT.pdf")

c5 = ROOT.TCanvas()
ROOT.gStyle.SetStatY(.4)
h_mu_avg_AK4HT_vs_nJets.Scale(1) #I think this is ok because it is an average already 
h_el_avg_AK4HT_vs_nJets.Scale(1) #same as above
h_mu_avg_AK4HT_vs_nJets.SetLineColor(2)
h_el_avg_AK4HT_vs_nJets.SetLineColor(3)
h_mu_avg_AK4HT_vs_nJets.Draw()
h_el_avg_AK4HT_vs_nJets.Draw("SAME")
c5.SaveAs("TTSemiLep_Bkg_el_and_muon_together_prof_vs_avg_AK4HT.pdf")

#debug
bin1 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(1)
bin2 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(2)
bin3 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(3)
bin4 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(4)
bin5 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(5)
bin6 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(6)
bin7 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(7)
bin8 = h_mu_avg_AK4HT_vs_nJets.GetBinContent(8)

print "bin1 is:", bin1
print "bin2 is:", bin2
print "bin3 is:", bin3
print "bin4 is:", bin4
print "bin5 is:", bin5
print "bin6 is:", bin6
print "bin7 is:", bin7
print "bin8 is:", bin8
