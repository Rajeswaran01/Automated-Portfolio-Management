# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:49:56 2023

@author: nthom
"""

import pandas as pd
from Analyse_Sentiment_Text_Final import Analyse_Sentiment_Text
from Constants_Rapports import ConstantsClass_Rapports

def getOurCompaniesCoefs(Ecoef,Scoef,Gcoef,expectedscore):
    initialTable = pd.read_excel("C:\\Users\\nthom\\OneDrive\\Documents\\ESILV\\P2IP\\AnalyseESG-main\\Analyse du sentiment\\CAC40_valeurs_ESG.xlsx")
    data = {"Company" : initialTable["Company"],
        "Ticker": initialTable["Ticker"],
        "E Score": initialTable["ENVIRONMENT"],
        "S Score": initialTable["SOCIAL"],
        "G Score": initialTable["GOVERNANCE"],
        "Final Score": initialTable["ENVIRONMENT"]*Ecoef+ initialTable["SOCIAL"]*Scoef+initialTable["GOVERNANCE"]*Gcoef}
    companies = pd.DataFrame(data)
    '''
    companies = companies.drop(range(40, 44)).sort_values("Final Score")[::-1]
    for i in range(40):
        if (companies["Final Score"][i]<expectedscore) : companies = companies.drop(i) 
    '''
    return companies

def getOurCompanies(Ecoef,Scoef,Gcoef,expectedScore):
    Ticker_List = pd.read_csv("C:\\Users\\nthom\\OneDrive\\Documents\\ESILV\\P2IP\\Composants_CAC40\\Ticker_List.csv",sep = ';')['Ticker_List']
    companies = pd.DataFrame(columns = ['Ticker','Score Rapports','Score ESG'])
    ESG_Score = getOurCompaniesCoefs(Ecoef,Scoef,Gcoef,0)
    for i in range(0,len(Ticker_List)): #Remplacer par 28 et 35 pour obtenir un resultat /!\ i-28 dans le loc
        #Scoring des rapports uniquement a partir de 2021 pour gagner du temps en test
        companies.loc[i] = [Ticker_List[i] ,1000*Analyse_Sentiment_Text.CompanyScoring(ConstantsClass_Rapports(),Ticker_List[i], '2021')[0],ESG_Score.loc[ESG_Score['Ticker'] == Ticker_List[i]]['Final Score'].values[0]]
    
    for i in range(0,len(companies)):
        if (companies['Score Rapports'][i]+companies['Score ESG'][i])/2 < expectedScore:
            companies = companies.drop(i) 
    
    companies.sort_values('Score Rapports')[::-1]
    
    return companies

companies = getOurCompanies(0.7,0.2,0.1,45)


