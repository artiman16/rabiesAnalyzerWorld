# -*- coding: utf-8 -*-

#Import packages
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font


import sys
import os
import time
import shutil

import pandas as pd
import numpy as np

from Bio import AlignIO

import warnings
warnings.filterwarnings("ignore")
    
#Function for browse files
def browseFiles():
    label_progress.config(text = "")
    global filename 
    filename = filedialog.askopenfilename(initialdir = "./home",
                                          title = "Choose file",
                                          filetypes = (("Fasta files",
                                                        "*.fasta*"), ("Fa files", "*.fa"),
                                                       ("all files",
                                                        "*.*"))) 
    global file1
    
#Push analysis
def push():
    file1 = filename
    label_progress.config(text = "Wait...")
    while not os.path.exists("Probe.csv"): 
        
        ref_file = str(os.path.abspath('rabies_ref.fasta'))
        in_file = str(os.path.abspath(file1))
        
        print('Alignment...')
        cmd = f'mafft --quiet --reorder --6merpair --keeplength --addfragments {in_file} {ref_file}  > alignment.fa'
        output = os.system(cmd)
        print('Alignment is completed!')
        
        print('Search nucleotide mutations...')
        alignment = AlignIO.read("alignment.fa", "fasta")
        num = len([1 for line in open("alignment.fa") if line.startswith(">")])
        rows = []
        for j in range(1, num):
            rows_list = []
            for i in range(0, len(alignment[0])):
                if alignment[j][i] != alignment[0][i]: 
                    dict1 = {'REF': alignment[0][i], 'POS': i, 'ALT': alignment[j][i]} 
                    rows_list.append(dict1)
            df0 = pd.DataFrame(rows_list) 
            df0.ALT = df0.ALT.replace('-', 'del')
            df0.REF = df0.REF.replace('-', 'ins')
            k = 0
            ins = 0
            #Search INDEL's and change numeration, if they are found
            for ii in range(0, df0.ALT.count()): 
                if df0.ALT.iloc[ii] == "del": k+=1
                if df0.REF.iloc[ii] == "ins": 
                    df0.POS.iloc[ii] = df0.POS.iloc[ii] - k+2
                    ins+=1
                if (df0.ALT.iloc[ii] != "del"): df0.POS.iloc[ii] = df0.POS.iloc[ii] - ins+1
                
            arr = []
            
            #Write mutations in list
            if (df0.empty): reps = ''
            else:
                df0 = df0[df0.POS.values >= 70]
                df0 = df0[df0.POS.values <= 1422]
                df0.POS = df0.POS - 70
                x = df0.to_string(header=False, index=False, index_names=False).split('\n')
                reps = [''.join(ele.split()) for ele in x]
                arr.append(reps)        
                    
            sp = str(arr)
            chars = ["[","]","'"]
            for c in chars: sp = sp.replace(c, "")
            
            #Write mutations in table for comparing with references
            dict0 = {'Sample name': [1], 'Mutations': [2], 'Group': [3], 'Description': [4]}
            dd1 = pd.DataFrame(columns = dict0.keys())
                
            result = pd.concat([dd1])
            flname, ext = os.path.splitext(os.path.basename(filename))
            name = flname.split('.')[0]
            
            result['Sample name'] = [name]
            result['Mutations'] = [sp]
            result['Group'] = [np.NaN]
            result['Description'] = [np.NaN]
            
            rows.append(result)
            table = pd.concat(rows)            
        
        print('Searching of mutations is completed!')
        table.to_csv("Probe.csv", sep=';', index=False)
        print('Group definition...') 
        
    if os.path.isfile("Probe.csv"): 
        resultat()
        label_progress.config(text = "Analysis is completed!")
        
        flname, ext = os.path.splitext(os.path.basename(filename))
        suffix = flname.split('.')[0]
        
        shutil.move('Probe.csv', f'Results/Probe-{suffix}-result.csv')
        shutil.move('alignment.fa', f'Results/Probe-{suffix}-alignment.fa')

#Clear group labels
def refreshLabels():
    cluster.config(foreground = "white", font = font.Font(size=16), text="")
    label_explanation.config(foreground = "blue", font = font.Font(size=10),text="")

#Define a group for strain
def analysis():
    ref_table = pd.read_csv("Clusters.csv", sep = ';')
    mutsRef = []
    for i in range(0, len(ref_table)): 
        lst = list(str(ref_table['Mutations'][i]).split(", "))
        mutsRef.append(lst)
    
    df = pd.read_csv("Probe.csv", sep = ';')
    
    mutsProbe = list(map(str, df['Mutations'][0].split(", ")))
    
    ref_table['Count'] = np.NaN
    for i in range (0, len(mutsRef)):
        ref_table['Count'][i] = len(set(mutsProbe).intersection(mutsRef[i]))   
    
    ref_table.sort_values("Count", ascending = False, inplace=True)
    ref_table.to_csv('Sorted.csv', sep = ";")
    table = pd.read_csv("Sorted.csv", sep=";")
    itog = str(table.Group[0]) 
    
    shutil.move('Sorted.csv', 'tmp/Sorted.csv')
    return itog

#Show in program, what the group we found and its description
def clust(res, region):
    subs = 'Probably this isolate is from: ' + '\n'
    cluster.config(text = "Group " + res, foreground = "red", font = font.Font(size=24))
    description = subs + region
    label_explanation.config(text = description)
    
    df = pd.read_csv("Probe.csv", sep=';')
    df.Group[0] = res
    df.Mutations = df.Mutations.str.upper()
    df.Description[0] = region   
    df.to_csv("Probe.csv", sep = ';', index=False)    

def desc(res):
    desc_table = pd.read_csv("Description.csv", sep=";")
    it = desc_table.loc[desc_table['Group'] == res]
    it = it.reset_index()
    return str(it['Description'][0])    
      
#Show final result
def resultat():
    refreshLabels()
    res = str(analysis())
    clust(res, desc(res))  
    print('The group is found!')
    
#Make graphical interface
window = Tk()
window.title('RabiesAnalyzer')

#Make main window
frame = ttk.Frame(window, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
  
#Make size of window  
window.resizable(0, 0)

#Set the icon of the app
img = PhotoImage(file='icon.png')
window.wm_iconphoto(True, img)

#Make all necessary widgets    
button_explore = ttk.Button(frame,
                        text = "Open .fasta file",
                        command = browseFiles) 
button_push = ttk.Button(frame, 
                         text='Analysis', 
                         command = push)
    
label_progress = ttk.Label(frame)

cluster = ttk.Label(frame, font = font.Font(size=16))
label_explanation = ttk.Label(frame, font = font.Font(size=10))

#Set widgets
def initGroups():
        
    button_explore.grid(column=1, row=1)
    button_push.grid(column=1, row=2)
    
    label_progress.grid(column=1, row=3) 
    cluster.grid(column=1, row=4)
    label_explanation.grid(column=1, row=5)

#Draw widgets into window
initGroups()

#Set margins to widgets
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

#Push interface
window.mainloop()
