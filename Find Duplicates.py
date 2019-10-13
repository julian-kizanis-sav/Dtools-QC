#SAV Digital Environments
#Julian Kizanis
print("Commpany:\tSAV Digital Environments\nDeveloper:\tJulian Kizanis\n\
Powered By:\tAnaconda\n\n")

import pandas as pd
from fuzzywuzzy import fuzz
#import numpy as np

dt_all = pd.read_csv("Models.csv")	#imports the csv file into a dataframe

def Dup(dup, dup_index, level):
	if level == 0:
		dup.loc[dup_index, 'Duplicate[2]'] = dup.loc[dup_index, 'Duplicate[1]']
		dup.loc[dup_index, 'Duplicate[1]'] = dup.loc[dup_index, 'Duplicate[0]']
		dup.loc[dup_index, 'Duplicate[0]'] = model_2
		
		dup.loc[dup_index, 'Partial Match Ratio[2]'] = dup.loc[dup_index, 'Partial Match Ratio[1]']
		dup.loc[dup_index, 'Partial Match Ratio[1]'] = dup.loc[dup_index, 'Partial Match Ratio[0]']
		dup.loc[dup_index, 'Partial Match Ratio[0]'] = temp_partial_match_ratio
		
		dup.loc[dup_index, 'Match Ratio[2]'] = dup.loc[dup_index, 'Match Ratio[1]']
		dup.loc[dup_index, 'Match Ratio[1]'] = dup.loc[dup_index, 'Match Ratio[0]']
		dup.loc[dup_index, 'Match Ratio[0]'] = temp_match_ratio
		
		dup.loc[dup_index, 'Index[2]'] = dup.loc[dup_index, 'Index[1]']
		dup.loc[dup_index, 'Index[1]'] = dup.loc[dup_index, 'Index[0]']
		dup.loc[dup_index, 'Index[0]'] = index_2
		
	elif level == 1:
		dup.loc[dup_index, 'Duplicate[2]'] = dup.loc[dup_index, 'Duplicate[1]']
		dup.loc[dup_index, 'Duplicate[1]'] = model_2
		
		dup.loc[dup_index, 'Partial Match Ratio[2]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[1]']
		dup.loc[dup_index, 'Partial Match Ratio[1]'] = temp_partial_match_ratio
		
		dup.loc[dup_index, 'Match Ratio[2]'] = dup.loc[dup_index, 'Match Ratio[1]']
		dup.loc[dup_index, 'Match Ratio[1]'] = temp_match_ratio
		
		dup.loc[dup_index, 'Index[2]'] = dup.loc[dup_index, 'Index[1]']
		dup.loc[dup_index, 'Index[1]'] = index_2	
		
	elif level == 2:
		dup.loc[dup_index, 'Duplicate[2]'] = model_2
		
		dup.loc[dup_index, 'Partial Match Ratio[2]'] = temp_partial_match_ratio
		
		dup.loc[dup_index, 'Match Ratio[2]'] = temp_match_ratio
		
		dup.loc[dup_index, 'Index[2]'] = index_2
		
	return dup


Duplicates = pd.DataFrame(columns = {'Model Index',	'Model Number',\
									 'Best Match Ratio',\
									 'Duplicate[0]', 'Match Ratio[0]',\
									 'Partial Match Ratio[0]','Index[0]',\
									 'Duplicate[1]','Match Ratio[1]',\
									 'Partial Match Ratio[1]','Index[1]',\
									 'Duplicate[2]','Match Ratio[2]',\
									 'Partial Match Ratio[2]','Index[2]'})
	

#dup_index = 0
for index_1, model_1 in enumerate(dt_all.loc[:,"Model"]):
	dup_index = index_1
	Duplicates = Duplicates.append({'Model Index':index_1,\
					 'Model Number':model_1,'Best Match Ratio':0,\
					 'Duplicate[0]':'', 'Match Ratio[0]':0,\
					 'Partial Match Ratio[0]':0,'Index[0]':0,\
					 'Duplicate[1]':'','Match Ratio[1]':0,\
					 'Partial Match Ratio[1]':0,'Index[1]':0,\
					 'Duplicate[2]':'','Match Ratio[2]':0,\
					 'Partial Match Ratio[2]':0,'Index[2]':0},\
						ignore_index=True)
	
	
	for index_2, model_2 in enumerate(dt_all.loc[:,"Model"]):
		if index_1 != index_2:
			temp_partial_match_ratio = fuzz.partial_ratio(model_1.lower(), model_2.lower())
			temp_match_ratio = fuzz.ratio(model_1.lower(), model_2.lower())

			if temp_partial_match_ratio > Duplicates.loc[dup_index, 'Partial Match Ratio[0]']:
				Duplicates.loc[dup_index, 'Duplicate[2]'] = Duplicates.loc[dup_index, 'Duplicate[1]']
				Duplicates.loc[dup_index, 'Duplicate[1]'] = Duplicates.loc[dup_index, 'Duplicate[0]']
				Duplicates.loc[dup_index, 'Duplicate[0]'] = model_2
				
				Duplicates.loc[dup_index, 'Partial Match Ratio[2]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[1]']
				Duplicates.loc[dup_index, 'Partial Match Ratio[1]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[0]']
				Duplicates.loc[dup_index, 'Partial Match Ratio[0]'] = temp_partial_match_ratio
				
				Duplicates.loc[dup_index, 'Match Ratio[2]'] = Duplicates.loc[dup_index, 'Match Ratio[1]']
				Duplicates.loc[dup_index, 'Match Ratio[1]'] = Duplicates.loc[dup_index, 'Match Ratio[0]']
				Duplicates.loc[dup_index, 'Match Ratio[0]'] = temp_match_ratio
				
				Duplicates.loc[dup_index, 'Index[2]'] = Duplicates.loc[dup_index, 'Index[1]']
				Duplicates.loc[dup_index, 'Index[1]'] = Duplicates.loc[dup_index, 'Index[0]']
				Duplicates.loc[dup_index, 'Index[0]'] = index_2
				
			elif temp_partial_match_ratio == Duplicates.loc[dup_index, 'Partial Match Ratio[0]']\
			and temp_match_ratio > Duplicates.loc[dup_index, 'Match Ratio[0]']:
				Duplicates.loc[dup_index, 'Duplicate[2]'] = Duplicates.loc[dup_index, 'Duplicate[1]']
				Duplicates.loc[dup_index, 'Duplicate[1]'] = Duplicates.loc[dup_index, 'Duplicate[0]']
				Duplicates.loc[dup_index, 'Duplicate[0]'] = model_2
				
				Duplicates.loc[dup_index, 'Partial Match Ratio[2]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[1]']
				Duplicates.loc[dup_index, 'Partial Match Ratio[1]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[0]']
				Duplicates.loc[dup_index, 'Partial Match Ratio[0]'] = temp_partial_match_ratio
				
				Duplicates.loc[dup_index, 'Match Ratio[2]'] = Duplicates.loc[dup_index, 'Match Ratio[1]']
				Duplicates.loc[dup_index, 'Match Ratio[1]'] = Duplicates.loc[dup_index, 'Match Ratio[0]']
				Duplicates.loc[dup_index, 'Match Ratio[0]'] = temp_match_ratio
				
				Duplicates.loc[dup_index, 'Index[2]'] = Duplicates.loc[dup_index, 'Index[1]']
				Duplicates.loc[dup_index, 'Index[1]'] = Duplicates.loc[dup_index, 'Index[0]']
				Duplicates.loc[dup_index, 'Index[0]'] = index_2
				
			elif temp_partial_match_ratio > Duplicates.loc[dup_index, 'Partial Match Ratio[1]']:
				Duplicates.loc[dup_index, 'Duplicate[2]'] = Duplicates.loc[dup_index, 'Duplicate[1]']
				Duplicates.loc[dup_index, 'Duplicate[1]'] = model_2
				
				Duplicates.loc[dup_index, 'Partial Match Ratio[2]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[1]']
				Duplicates.loc[dup_index, 'Partial Match Ratio[1]'] = temp_partial_match_ratio
				
				Duplicates.loc[dup_index, 'Match Ratio[2]'] = Duplicates.loc[dup_index, 'Match Ratio[1]']
				Duplicates.loc[dup_index, 'Match Ratio[1]'] = temp_match_ratio
				
				Duplicates.loc[dup_index, 'Index[2]'] = Duplicates.loc[dup_index, 'Index[1]']
				Duplicates.loc[dup_index, 'Index[1]'] = index_2			
				
			elif temp_partial_match_ratio == Duplicates.loc[dup_index, 'Partial Match Ratio[1]']\
			and temp_match_ratio > Duplicates.loc[dup_index, 'Match Ratio[1]']:
				Duplicates.loc[dup_index, 'Duplicate[2]'] = Duplicates.loc[dup_index, 'Duplicate[1]']
				Duplicates.loc[dup_index, 'Duplicate[1]'] = model_2
				
				Duplicates.loc[dup_index, 'Partial Match Ratio[2]'] = Duplicates.loc[dup_index, 'Partial Match Ratio[1]']
				Duplicates.loc[dup_index, 'Partial Match Ratio[1]'] = temp_partial_match_ratio
				
				Duplicates.loc[dup_index, 'Match Ratio[2]'] = Duplicates.loc[dup_index, 'Match Ratio[1]']
				Duplicates.loc[dup_index, 'Match Ratio[1]'] = temp_match_ratio
				
				Duplicates.loc[dup_index, 'Index[2]'] = Duplicates.loc[dup_index, 'Index[1]']
				Duplicates.loc[dup_index, 'Index[1]'] = index_2							
				
			elif temp_partial_match_ratio > Duplicates.loc[dup_index, 'Partial Match Ratio[1]']:
				Duplicates.loc[dup_index, 'Duplicate[2]'] = model_2
				
				Duplicates.loc[dup_index, 'Partial Match Ratio[2]'] = temp_partial_match_ratio
				
				Duplicates.loc[dup_index, 'Match Ratio[2]'] = temp_match_ratio
				
				Duplicates.loc[dup_index, 'Index[2]'] = index_2
							
	print(f"{model_1}:\t{Duplicates.loc[dup_index, 'Duplicate[0]']}\
   \tParMatch% = {Duplicates.loc[dup_index, 'Partial Match Ratio[0]']}%\
   Match% = {Duplicates.loc[dup_index, 'Match Ratio[0]']}%")			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				