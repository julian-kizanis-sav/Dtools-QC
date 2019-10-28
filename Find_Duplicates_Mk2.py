#SAV Digital Environments
#Julian Kizanis
#ETA = 7 hours
print("Commpany:\tSAV Digital Environments\nDeveloper:\tJulian Kizanis\n\
Powered By:\tAnaconda\n\n")
import pandas as pd
from fuzzywuzzy import fuzz
import time
#import numpy as np
#import math

def Dup_ini():
	dup = pd.DataFrame(columns = {'Index[0]','Manufacturer[0]','Model[0]',\
							   'Part[0]','Keep[0]','Used[0]', \
							   'Match Ratio','Index[1]','Manufacturer[1]',\
							   'Model[1]','Part[1]','Keep[1]','Used[1]'})
	
	return dup[['Index[0]','Manufacturer[0]','Model[0]',\
			   'Part[0]','Keep[0]','Used[0]', \
			   'Match Ratio','Index[1]','Manufacturer[1]',\
			   'Model[1]','Part[1]','Keep[1]','Used[1]']]
	
def Dup_new_row(dup, mod, i):
	return dup.append({'Index[0]':i,'Manufacturer[0]':mod.loc[i,"Manufacturer"],'Model[0]':mod.loc[i,"Model"],\
			   'Part[0]':mod.loc[i,"Part Number"],'Keep[0]':True,'Used[0]':False, \
			   'Match Ratio':0,'Index[1]':0,'Manufacturer[1]':"",\
			   'Model[1]':"",'Part[1]':"",'Keep[1]':True,'Used[1]':False},\
						ignore_index=True)
	
def New_best_match(dup, d, mod, mr, i):
	dup.loc[d,"Index[1]"] = i
	dup.loc[d,"Manufacturer[0]"] = mod.loc[i,"Manufacturer"]
	dup.loc[d,"Model[1]"] = mod.loc[i,"Model"]
	dup.loc[d,"Part[1]"] = mod.loc[i,"Part Number"]
	dup.loc[d,"Match Ratio"] = mr
	
def find_if_used(dup, use):

	for i, m_d in enumerate(dup.loc[:,f'Model[0]']):
		for m_u in use.loc[:,'Model']:
			if m_d == m_u:
				dup.loc[i,f'Used[0]'] = True
				if i%100 == 1:
					print(f'Used Models Found:{i}')
				
	for i, m_d in enumerate(dup.loc[:,f'Model[1]']):
		for m_u in use.loc[:,'Model']:
			if m_d == m_u:
				dup.loc[i,f'Used[1]'] = True
				if i%100 == 1:
					print(f'Used Models Found:{i}')				
	
	return dup			
	
dt_all = pd.read_csv("Models.csv")	#imports the csv file into a dataframe	
used = pd.read_csv("Used.csv")

print("This program will run for about 7 hours")

Duplicates = Dup_ini()
index_d = 0
part_0 = "test"
part_1 = "test"
start = time.time()
for index_0, model_0 in enumerate(dt_all.loc[:,"Model"]):
	Duplicates = Dup_new_row(Duplicates, dt_all, index_0)
#	print (Duplicates.loc[index_d,"Match Ratio"])
	for index_1, model_1 in enumerate(dt_all.loc[:,"Model"]):
		if index_0 != index_1:

			part_0 = f"dt_all.loc[index_0, 'Part Number']"
			part_1 = f"{dt_all.loc[index_1, 'Part Number']}"
			
			temp_match_ratio = fuzz.partial_ratio(\
			 model_0.lower().strip(' -_()/'), \
			 model_1.lower().strip(' -_()/')) * \
			 fuzz.ratio(\
			 model_0.lower().strip(' -_()/'), \
			 model_1.lower().strip(' -_()/')) / 100
#			print(Duplicates.loc[index_d,"Match Ratio"])
			if temp_match_ratio > Duplicates.loc[index_d,"Match Ratio"]:
					New_best_match(Duplicates, index_d, dt_all, temp_match_ratio, index_1)
			
			if part_0:
				temp_match_ratio = fuzz.partial_ratio(\
				 model_0.lower().strip(' -_()/'), \
				 part_1.lower().strip(' -_()/')) * \
				 fuzz.ratio(\
				 model_0.lower().strip(' -_()/'), \
				 part_1.lower().strip(' -_()/')) / 100
			
				if temp_match_ratio > Duplicates.loc[index_d,"Match Ratio"]:
					New_best_match(Duplicates, index_d, dt_all, temp_match_ratio, index_1)
				
			if part_1:	
				temp_match_ratio = fuzz.partial_ratio(\
				 part_0.lower().strip(' -_()/'), \
				 model_1.lower().strip(' -_()/')) * \
				 fuzz.ratio(\
				 part_0.lower().strip(' -_()/'), \
				 model_1.lower().strip(' -_()/')) / 100
				
				if temp_match_ratio > Duplicates.loc[index_d,"Match Ratio"]:
					New_best_match(Duplicates, index_d, dt_all, temp_match_ratio, index_1)
				
			if part_0 and part_1:	
				temp_match_ratio = fuzz.partial_ratio(\
				 part_0.lower().strip(' -_()/'), \
				 part_1.lower().strip(' -_()/')) * \
				 fuzz.ratio(\
				 part_0.lower().strip(' -_()/'), \
				 part_1.lower().strip(' -_()/')) / 100
			
				if temp_match_ratio > Duplicates.loc[index_d,"Match Ratio"]:
					New_best_match(Duplicates, index_d, dt_all, temp_match_ratio, index_1)
	e_time = time.time() - start
	avg_time = e_time / (index_0 + 1)
	print(f"{model_0}:\tMatch%: {Duplicates.loc[index_d,'Match Ratio']} \tElapsed Time(s): {round(e_time)}\tAvg time: {avg_time}")
	index_d += 1	
				
#Duplicates = Remove_duplicates(Duplicates)
Duplicates = Duplicates.sort_values('Match Ratio',ascending=False)	
export_csv = Duplicates.to_csv ('Duplicates Mk2.csv', header=True)	

find_if_used(Duplicates, used)
Duplicates = Duplicates.sort_values('Match Ratio',ascending=False)	
export_csv = Duplicates.to_csv ('Duplicates Mk2.csv', header=True)				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				