#SAV Digital Environments
#Julian Kizanis
#ETA = 1hour
print("Commpany:\tSAV Digital Environments\nDeveloper:\tJulian Kizanis\n\
Powered By:\tAnaconda\n\n")

import pandas as pd
from fuzzywuzzy import fuzz
#import numpy as np
#import math


def Dup(dup, index_1, level):
	if level == 0:
		dup.loc[index_1, 'Duplicate[2]'] = dup.loc[index_1, 'Duplicate[1]']
		dup.loc[index_1, 'Duplicate[1]'] = dup.loc[index_1, 'Duplicate[0]']
		dup.loc[index_1, 'Duplicate[0]'] = model_2
		
		dup.loc[index_1, 'Partial Match Ratio[2]'] = dup.loc[index_1, 'Partial Match Ratio[1]']
		dup.loc[index_1, 'Partial Match Ratio[1]'] = dup.loc[index_1, 'Partial Match Ratio[0]']
		dup.loc[index_1, 'Partial Match Ratio[0]'] = temp_partial_match_ratio
		
		dup.loc[index_1, 'Match Ratio[2]'] = dup.loc[index_1, 'Match Ratio[1]']
		dup.loc[index_1, 'Match Ratio[1]'] = dup.loc[index_1, 'Match Ratio[0]']
		dup.loc[index_1, 'Match Ratio[0]'] = temp_match_ratio
		
		dup.loc[index_1, 'Index[2]'] = dup.loc[index_1, 'Index[1]']
		dup.loc[index_1, 'Index[1]'] = dup.loc[index_1, 'Index[0]']
		dup.loc[index_1, 'Index[0]'] = index_2
		
	elif level == 1:
		dup.loc[index_1, 'Duplicate[2]'] = dup.loc[index_1, 'Duplicate[1]']
		dup.loc[index_1, 'Duplicate[1]'] = model_2
		
		dup.loc[index_1, 'Partial Match Ratio[2]'] = dup.loc[index_1, 'Partial Match Ratio[1]']
		dup.loc[index_1, 'Partial Match Ratio[1]'] = temp_partial_match_ratio
		
		dup.loc[index_1, 'Match Ratio[2]'] = dup.loc[index_1, 'Match Ratio[1]']
		dup.loc[index_1, 'Match Ratio[1]'] = temp_match_ratio
		
		dup.loc[index_1, 'Index[2]'] = dup.loc[index_1, 'Index[1]']
		dup.loc[index_1, 'Index[1]'] = index_2	
		
	elif level == 2:
		dup.loc[index_1, 'Duplicate[2]'] = model_2
		
		dup.loc[index_1, 'Partial Match Ratio[2]'] = temp_partial_match_ratio
		
		dup.loc[index_1, 'Match Ratio[2]'] = temp_match_ratio
		
		dup.loc[index_1, 'Index[2]'] = index_2
		
	return dup

def Dup_ini():
	dup = pd.DataFrame(columns = {'Model Index','Model Number','Keep','Used',\
									 'Best Match Ratio',\
									 'Duplicate[0]', 'Keep[0]','Used[0]', 'Match Ratio[0]',\
									 'Partial Match Ratio[0]','Index[0]',\
									 'Duplicate[1]', 'Keep[1]','Used[1]','Match Ratio[1]',\
									 'Partial Match Ratio[1]','Index[1]',\
									 'Duplicate[2]', 'Keep[2]','Used[2]','Match Ratio[2]',\
									 'Partial Match Ratio[2]','Index[2]'})
	return dup[['Model Index','Model Number','Keep','Used',\
				 'Best Match Ratio',\
				 'Duplicate[0]', 'Keep[0]','Used[0]', 'Match Ratio[0]',\
				 'Partial Match Ratio[0]','Index[0]',\
				 'Duplicate[1]', 'Keep[1]','Used[1]','Match Ratio[1]',\
				 'Partial Match Ratio[1]','Index[1]',\
				 'Duplicate[2]', 'Keep[2]','Used[2]','Match Ratio[2]',\
				 'Partial Match Ratio[2]','Index[2]']]
	
	
	
def Dup_new_row(dup):
	return dup.append({'Model Index':index_1,\
					 'Model Number':model_1, 'Keep':True,'Best Match Ratio':0,\
					 'Duplicate[0]':'', 'Keep[0]':True,'Match Ratio[0]':0,\
					 'Partial Match Ratio[0]':0,'Index[0]':0,\
					 'Duplicate[1]':'', 'Keep[1]':True,'Match Ratio[1]':0,\
					 'Partial Match Ratio[1]':0,'Index[1]':0,\
					 'Duplicate[2]':'', 'Keep[2]':True,'Match Ratio[2]':0,\
					 'Partial Match Ratio[2]':0,'Index[2]':0},\
						ignore_index=True)

#Duplicates_Hybrid.loc[index_1, 'Best Match Ratio'] = hmr_h
def insertion_sort(dup):
        
    for i in range(len(dup.loc[:,'Best Match Ratio'])):
        cursor = dup.loc[i,'Best Match Ratio']
        pos = i
        
        while pos > 0 and dup.loc[pos - 1,'Best Match Ratio'] > cursor:
            # Swap the number down the list
            dup.loc[pos,:] = dup.loc[pos - 1,:]
            pos = pos - 1
        # Break and do the final swap
        dup.loc[pos,:] = dup.loc[i,:]

    return dup
def remove_duplicates(dup):
	remove = []
	i_r = 0
	l = range(len(dup.loc[:,'Model Number']))
	for i_1 in l:
		for i_2 in l[i_1:]:
			if dup.loc[i_1, 'Model Number'] == dup.loc[i_2, 'Duplicate[0]']\
			and dup.loc[i_2, 'Model Number'] == dup.loc[i_1, 'Duplicate[0]']:
				print(f"Redundancy Found at: {i_2}")
				remove.insert(i_r, i_1) 
				i_r += 1
#	for i in l:
#		dup = dup.drop(remove[i])
	return dup.drop(remove)

def find_if_used(dup, use):
	for level in [0,1,2]:
		for i, m_d in enumerate(dup.loc[:,f'Duplicate[{level}]']):
			for m_u in use.loc[:,'Model']:
				if m_d == m_u:
					dup.loc[i,f'Used[{level}]'] = True
					print('Used Models Found:{}'.format(i), end='\r')
					break
				else:
					dup.loc[i,f'Used[{level}]'] = False
					
	for i, m_d in enumerate(dup.loc[:,f'Model Number']):
		for m_u in use.loc[:,'Model']:
			if m_d == m_u:
				dup.loc[i,'Used'] = True
				print('Used Models Found:{}'.format(i), end='\r')
				break
			else:
				dup.loc[i,'Used'] = False		
	return dup			
				
dt_all = pd.read_csv("Models.csv")	#imports the csv file into a dataframe	
used = pd.read_csv("Used.csv")

print("('m':Match, 'p':partial, 'h':hybrid, 'a':all)")
#match_type = input("Enter Match Type: ")
match_type = 'h'

if match_type == 'm' or match_type == 'a':
	Duplicates_Match = Dup_ini()
if match_type == 'p' or match_type == 'a':
	Duplicates_Partial = Dup_ini()
if match_type == 'h' or match_type == 'a':
	Duplicates_Hybrid = Dup_ini()	


#index_1 = 0
for index_1, model_1 in enumerate(dt_all.loc[:,"Model"]):
	if match_type == 'p' or match_type == 'a':
		Duplicates_Partial = Dup_new_row(Duplicates_Partial)
	if match_type == 'm' or match_type == 'a':
		Duplicates_Match = Dup_new_row(Duplicates_Match)
	if match_type == 'h' or match_type == 'a':
		Duplicates_Hybrid = Dup_new_row(Duplicates_Hybrid)
	
	for index_2, model_2 in enumerate(dt_all.loc[:,"Model"]):
		if index_1 != index_2:
			temp_partial_match_ratio = fuzz.partial_ratio(\
			 model_1.lower().strip(' -_()/'), \
			 model_2.lower().strip(' -_()/'))
			
			temp_match_ratio = fuzz.ratio(\
			 model_1.lower().strip(' -_()/'), \
			 model_2.lower().strip(' -_()/'))
			
			if match_type == 'p' or match_type == 'a':
				if temp_partial_match_ratio > Duplicates_Partial.loc[index_1, 'Partial Match Ratio[0]']:
					Duplicates_Partial = Dup(Duplicates_Partial, index_1, 0)
					
				elif temp_partial_match_ratio == Duplicates_Partial.loc[index_1, 'Partial Match Ratio[0]']\
				and temp_match_ratio > Duplicates_Partial.loc[index_1, 'Match Ratio[0]']:
					Duplicates_Partial = Dup(Duplicates_Partial, index_1, 0)
					
				elif temp_partial_match_ratio > Duplicates_Partial.loc[index_1, 'Partial Match Ratio[1]']:
					Duplicates_Partial = Dup(Duplicates_Partial, index_1, 1)
					
				elif temp_partial_match_ratio == Duplicates_Partial.loc[index_1, 'Partial Match Ratio[1]']\
				and temp_match_ratio > Duplicates_Partial.loc[index_1, 'Match Ratio[1]']:
					Duplicates_Partial = Dup(Duplicates_Partial, index_1, 1)						
					
				elif temp_partial_match_ratio > Duplicates_Partial.loc[index_1, 'Partial Match Ratio[2]']:
					Duplicates_Partial = Dup(Duplicates_Partial, index_1, 2)
				
			if match_type == 'm' or match_type == 'a':				
				if temp_match_ratio > Duplicates_Match.loc[index_1, 'Match Ratio[0]']:
					Duplicates_Match = Dup(Duplicates_Match, index_1, 0)			
					
				elif temp_match_ratio > Duplicates_Match.loc[index_1, 'Match Ratio[1]']:
					Duplicates_Match = Dup(Duplicates_Match, index_1, 1)
					
				elif temp_match_ratio > Duplicates_Match.loc[index_1, 'Match Ratio[2]']:
					Duplicates_Match = Dup(Duplicates_Match, index_1, 2)
	
			if match_type == 'h' or match_type == 'a':	
				if temp_match_ratio * temp_partial_match_ratio > \
				Duplicates_Hybrid.loc[index_1, 'Match Ratio[0]'] * Duplicates_Hybrid.loc[index_1, 'Partial Match Ratio[0]']:
					Duplicates_Hybrid = Dup(Duplicates_Hybrid, index_1, 0)			
					
				elif temp_match_ratio * temp_partial_match_ratio > \
				Duplicates_Hybrid.loc[index_1, 'Match Ratio[1]'] * Duplicates_Hybrid.loc[index_1, 'Partial Match Ratio[1]']:
					Duplicates_Hybrid = Dup(Duplicates_Hybrid, index_1, 1)
					
				elif temp_match_ratio * temp_partial_match_ratio > \
				Duplicates_Hybrid.loc[index_1, 'Match Ratio[2]'] * Duplicates_Hybrid.loc[index_1, 'Partial Match Ratio[2]']:
					Duplicates_Hybrid = Dup(Duplicates_Hybrid, index_1, 2)
#	hmr = math.sqrt(Duplicates_Partial.loc[index_1, 'Match Ratio[0]'] * Duplicates_Partial.loc[index_1, 'Partial Match Ratio[0]'])					
#	print(f"{model_1}:\tHybrid Match % = {hmr}%")			
	
	
						
	if match_type == 'h' or match_type == 'a':	
		hmr_h = (Duplicates_Hybrid.loc[index_1, 'Match Ratio[0]'] * Duplicates_Hybrid.loc[index_1, 'Partial Match Ratio[0]'])/100	
		Duplicates_Hybrid.loc[index_1, 'Best Match Ratio'] = hmr_h
		print(f"{model_1}\t\t{Duplicates_Hybrid.loc[index_1, 'Duplicate[0]']}\t{hmr_h}")	
			
	if match_type == 'm' or match_type == 'a':	
		hmr_m = (Duplicates_Match.loc[index_1, 'Match Ratio[0]'] * Duplicates_Match.loc[index_1, 'Partial Match Ratio[0]'])/100
		Duplicates_Match.loc[index_1, 'Best Match Ratio'] = hmr_m
		print(f"{model_1}\t\t{Duplicates_Match.loc[index_1, 'Duplicate[0]']}\t{hmr_m}")	
		
	if match_type == 'p' or match_type == 'a':
		hmr_p = (Duplicates_Partial.loc[index_1, 'Match Ratio[0]'] * Duplicates_Partial.loc[index_1, 'Partial Match Ratio[0]'])/100
		Duplicates_Partial.loc[index_1, 'Best Match Ratio'] = hmr_p
		print(f"{model_1}\t\t{Duplicates_Partial.loc[index_1, 'Duplicate[0]']}\t{hmr_p}")

			
if match_type == 'h' or match_type == 'a':	
	Duplicates_Hybrid = remove_duplicates(Duplicates_Hybrid)
	find_if_used(Duplicates_Hybrid, used)
	Duplicates_Hybrid = Duplicates_Hybrid.sort_values('Best Match Ratio',ascending=False)	
	export_csv = Duplicates_Hybrid.to_csv ('Duplicates_Hybrid.csv', header=True)
		
if match_type == 'm' or match_type == 'a':	
	Duplicates_Match = remove_duplicates(Duplicates_Match)			
	find_if_used(Duplicates_Match, used)
	Duplicates_Match = Duplicates_Match.sort_values('Best Match Ratio',ascending=False)	
	export_csv = Duplicates_Match.to_csv ('Duplicates_Match.csv', header=True)
	
if match_type == 'p' or match_type == 'a':
	Duplicates_Partial = remove_duplicates(Duplicates_Partial)
	find_if_used(Duplicates_Partial, used)
	Duplicates_Partial = Duplicates_Partial.sort_values('Best Match Ratio',ascending=False)				
	export_csv = Duplicates_Partial.to_csv ('Duplicates_Partial.csv', header=True)					
			
				
				
				
				
				
				
				