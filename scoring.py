# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:00:26 2022

@author: a-raj
"""


# Liste_positive=[" investissement "," profit ", " bénéfices ", " croissance "]
# Liste_negative=[" pertes "," instabilités "]

# def Scoring_PDF_Liste("nom_du_PDF"):
#     score_total=0
#     reader = PdfReader("nom_du_PDF.pdf")
#     number_of_pages = len(reader.pages)
#     for i in range(number_of_pages):
#         score_page=0
#         page = reader.pages[i]
#         text = page.extract_text()
#         for mot in Liste_positive:
#             x=text.count(mot)
#             score_page=score_page + x
#         for mot in Liste_negative:
#             x=text.count(mot)
#             score_page=score_page - x
#         score_total=score_total + score_page
#     return score_total


# dico={" investissement ":1," profit ":2, " bénéfices ":3, " croissance ":1.5," pertes ": -3," instabilités ":-2," un ":1}

# def Scoring_PDF_Dico("nom_du_PDF"):
#      score_total=0
#      reader = PdfReader("nom_du_PDF")
#      number_of_pages = len(reader.pages)
#      for i in range(number_of_pages):
#          score_page=0
#          page = reader.pages[i]
#          text = page.extract_text()
#          for mot in dico:
#              x=text.count(mot)
#              score_page=score_page + dico[mot]*x
#          score_total=score_total=score_page
#      return score_total

  
dico={"un":1,"deux":2,"trois":3}
def Score(path_PDF):
    score_total=0
    file=open(path_PDF,"rb")
    reader=PyPDF2.PdfFileReader(file)
    totalpages=reader.numPages
    for i in range(totalpages):
        page=reader.getPage(i)
        text=page.extractText()
        score_page=0
        for mot in dico: 
            occurence=text.count(mot)
            score_page=score_page+dico[mot]*occurence
        score_total=score_total+score_page    
    return score_total/totalpages
    

# C:\Users\username\Documents\mypdf.pdf

import os
import PyPDF2

folder_path = "chemin/vers/dossier"

Liste_Company_folder=[folder for folder in os.listdir(folder_path)]

Liste_Company_folder_path=[os.path.join(folder_path,folder) for folder in Liste_Company_folder]
 
L=[]

for company_path in Liste_Company_folder_path:
    Liste_score_d_une_entreprise=[]
    pdf_files = [f for f in os.listdir(company_path) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        path_pdf = os.path.join(folder_path, pdf_file)
        score=Score(path_pdf)
        Liste_score_d_une_entreprise.append(score)
        L.append(Liste_score_d_une_entreprise)
        
        
        
        # with open(path, 'rb') as file:
        #     reader = PyPDF2.PdfFileReader(file)
        #     print("Nombre de pages dans le fichier {} : {}".format(pdf_file, reader.numPages))
    
    


    

    