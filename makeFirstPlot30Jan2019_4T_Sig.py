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

el8jets = 0
el9jets = 0
el10jets = 0
el11jets = 0
el12jets = 0

#Define histograms
h_mu_nJets_vs_AK4HT = ROOT.TH2F("NJets_vs_AK4HT_mu", "AK4 Jet HT vs. nJets in the Event for 4 Tops Mu Events; nJets; AK4HT (GeV)", 7, 5.5, 12.5, 50, 400, 1200) #maybe tweak this

h_el_nJets_vs_AK4HT = ROOT.TH2F("NJets_vs_AK4HT_el", "AK4 Jet HT vs. NJets in the Event for 4 Tops El Events; nJets; AK4HT (GeV)", 7, 5.5, 12.5 , 50, 400, 1200)

h_mu_avg_AK4HT_vs_nJets = ROOT.TProfile("mu_prof_nJets_vs_avg_AK4HT", "Average AK4HT by Jet Multiplicity for 4 Tops Events; nJets; Avg. AK4HT (GeV)", 7, 5.5, 12.5)

h_el_avg_AK4HT_vs_nJets = ROOT.TProfile("el_prof_nJets_vs_avg_AK4HT", "Average AK4HT by Jet Multiplicity for 4 Tops Events; nJets; Avg. AK4HT (GeV)", 7, 5.5, 12.5)

f = ROOT.TFile("Mary_test_4T_17_MC_Sig_29_Jan_2019.root")
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

print "el8jets is:", el8jets
print "el9jets is:", el9jets
print "el10jets is:", el10jets
print "el11jets is:", el11jets
print "el12jets is:", el12jets

#Draw histograms
c1 = ROOT.TCanvas()
#ROOT.gStyle.SetStatX(.3)
ROOT.gStyle.SetOptStat(0)
h_mu_nJets_vs_AK4HT.Scale(.002) #lumi recorded in 2017 is 45 inv fb, cross section for 4 tops is 12 fb, nEventsGenerated before any cuts is 221727 for the file files I ran over
h_mu_nJets_vs_AK4HT.Draw("COLZ")
c1.SaveAs("4T_Sig_mu_nJets_vs_AK4HT.pdf")

c2 = ROOT.TCanvas()
#ROOT.gStyle.SetStatX(.3)
ROOT.gStyle.SetOptStat(0)
h_el_nJets_vs_AK4HT.Scale(.002) #lumi recorded in 2017 is 45 inv fb, cross section for 4 tops is 12 fb, nEventsGenerated before any cuts is 221727 for the file files I ran over
h_el_nJets_vs_AK4HT.Draw("COLZ")
c2.SaveAs("4T_Sig_el_nJets_vs_AK4HT.pdf")

c3 = ROOT.TCanvas()
#ROOT.gStyle.SetStatY(.4)
ROOT.gStyle.SetOptStat(0)
h_mu_avg_AK4HT_vs_nJets.Scale(1) #I think this is ok because it is an average already
h_mu_avg_AK4HT_vs_nJets.SetLineColor(2)
#h_mu_avg_AK4HT_vs_nJets.SetBarOffset(-0.5) #this did not do what root forum from 2013 claimed it would do, sad. It in fact appears to do nothing at all.
h_mu_avg_AK4HT_vs_nJets.Draw() 
l3 = ROOT.TLegend(.2, .2, .4, .4)
l3.AddEntry(h_mu_avg_AK4HT_vs_nJets, 'Mu Events', 'l')
l3.Draw()
c3.SaveAs("4T_Sig_mu_prof_nJets_vs_avg_AK4HT.pdf")

c4 = ROOT.TCanvas()
#ROOT.gStyle.SetStatY(.4)
ROOT.gStyle.SetOptStat(0)
h_el_avg_AK4HT_vs_nJets.Scale(1) #I think this is ok because it is an average already
h_el_avg_AK4HT_vs_nJets.SetLineColor(3)
h_el_avg_AK4HT_vs_nJets.Draw()
l4 = ROOT.TLegend(.2,.2, .4, .4)
l4.AddEntry(h_el_avg_AK4HT_vs_nJets, 'El Events', 'l')
l4.Draw()
c4.SaveAs("4T_Sig_el_prof_nJets_vs_avg_AK4HT.pdf")

c5 = ROOT.TCanvas()
#ROOT.gStyle.SetStatY(.4)
ROOT.gStyle.SetOptStat(0)
h_mu_avg_AK4HT_vs_nJets.Scale(1) #I think this is ok because it is an average already 
h_el_avg_AK4HT_vs_nJets.Scale(1) #same as above
h_mu_avg_AK4HT_vs_nJets.SetLineColor(2)
h_el_avg_AK4HT_vs_nJets.SetLineColor(3)
h_mu_avg_AK4HT_vs_nJets.Draw()
h_el_avg_AK4HT_vs_nJets.Draw("SAME")
l5 = ROOT.TLegend(.2, .2, .4, .4)
l5.AddEntry(h_mu_avg_AK4HT_vs_nJets, 'Mu Events', 'l')
l5.AddEntry(h_el_avg_AK4HT_vs_nJets, 'El Events', 'l')
l5.Draw()
c5.SaveAs("4T_Sig_el_and_muon_together_prof_vs_avg_AK4HT.pdf")
