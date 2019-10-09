#SAV Digital Environments
#Julian Kizanis
print("Commpany:\tSAV Digital Environments\nDeveloper:\tJulian Kizanis\n\
Powered By:\tAnaconda\n\n")

import pandas as pd

dt_all = pd.read_csv("Models.csv")	#imports the csv file into a dataframe
#dt_use = pd.read_csv("Used.csv")
#print(dt_all.head())

Is_Used = []
error = pd.DataFrame(columns = dt_all.columns)
error_used = pd.DataFrame(columns = dt_all.columns)
error_not_used = pd.DataFrame(columns = dt_all.columns)
error_index = 0

for index, model in enumerate(dt_all.loc[:, "Model"]):
	Is_Used.insert(index, False)
#	for model_use in dt_use[:, "Model"]:
#		if model_use == model:
#			Is_Used[index] = True
#			break
	
	if "-CHOOSE COLOR" in model or "-*" in model \
	or ", Specify Color" in model or "-CHOOSE COLOR" in model\
	or "?CHOOSE COLOR" in model or "(CHOOSE COLOR)" in model\
	or " SELECT COLOR" in model or "(CHOOSE FINISH)" in model\
	or "  ***SPECIFY COLOR" in model or "CHOOSE COLOR'" in model\
	or "CHOOSE COLOR" in model or "choose color" in model\
	or "CHOOSE FINISH" in model:
		error = error.append(dt_all.loc[index,:], ignore_index = True)
		error = error.append(dt_all.loc[index,:], ignore_index = True)
		#print(error.head())
		error.loc[error_index, "Approved"] = False
		
		error.loc[error_index + 1, "Model"] = error.loc[error_index + 1, "Model"]\
		.replace("-CHOOSE COLOR", "-XX").replace("-*", "-XX")\
		.replace(", Specify Color", "").replace("?CHOOSE COLOR", "")\
		.replace("(CHOOSE COLOR)", "").replace("  ***SPECIFY COLOR", "")\
		.replace("CHOOSE COLOR'", "").replace("(CHOOSE FINISH)", "-METALXX")\
		.replace("-XX (CHOOSE FINISH)", "-METALXX")
				
		error_index += 2
			
export_csv = error.to_csv ('No Choose Color.csv', header=True) #Don't forget to add '.csv' at the end of the path

print("Done!")