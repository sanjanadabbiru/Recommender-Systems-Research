import pandas as pd

# reading dataset values

diet = pd.read_csv('diet.csv')

#taking input from questionnaire

print("Q1. Does the patient have a family history of diabetes(mother,father,sibling) (Yes/No)")
fam_his = input()

print("Q2. OGTT Test. Enter PPBS test value.")# Q: but where are we using it?
og_pp = int(input())

print("Q3. OGTT Test. Enter FBS test value.")
og_fb = int(input())

print("Q4. HB1AC Test. Enter HB1AC test value.")
hb = int(input())

print("Q5. Enter preferred food type: South or North?")
pref_sn = input()

print("Q6. Veg or Non-veg?")
pref_vnv = input()

print("Q7. Are you allergic to dairy products (Yes/No)?")
aller_d = input()

print("Q8. Are you allergic to nuts (Yes/No)?")
aller_n = input()

print("Q9. Are you allergic to fish/eggs (Yes/No)?")
aller_fe = input()

#end of questionnaire

fin_res1 =[]#recommended food list got from rules will be here first


#start: applying rules

#if hb value is >= 7 then only low gi food
if hb>=7:

	#1. if veg south with no allergies
	if pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='No':

		df1 =diet.drop(['north','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])
		

	#1.1 if veg south with dairy allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.2 if veg south with nuts allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.3 if veg south with fish/eggs allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry'],axis=1)#aLready excluding poultry which has fish and eggs
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.4 if veg south with dairy and nuts allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.5 if veg south with dairy and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.6 if veg south with nuts and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#1.7 if veg south with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])



	#2. if veg north with no allergies
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.1 if veg north with dairy allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.2 if veg north with nuts allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.3 if veg north with fish/eggs allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.4 if veg north with dairy and nuts allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.5 if veg north with dairy and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.6 if veg north with nuts and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.7 if veg north with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])




	#3. non veg case

	#1. if nonveg south with no allergies
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

		

	#1.1 if nonveg south with dairy allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.2 if nonveg south with nuts allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.3 if nonveg south with fish/eggs allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry'],axis=1)#excluded full poultry for now
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.4 if nonveg south with dairy and nuts allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.5 if nonveg south with dairy and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','dairy','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.6 if nonveg south with nuts and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#1.7 if nonveg south with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])



	#2. if nonveg north with no allergies
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.1 if nonveg north with dairy allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.2 if nonveg north with nuts allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.3 if nonveg north with fish/eggs allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.4 if nonveg north with dairy and nuts allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.5 if nonveg north with dairy and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','dairy','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.6 if nonveg north with nuts and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.7 if nonveg north with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','dairy','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		diet_low_list = df2.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


elif hb>=6.5 and hb<=6.8:

	#low+medium gi only


	#1. if veg south with no allergies
	if pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='No':

		df1 = diet.drop(['north','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])
		

	#1.1 if veg south with dairy allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.2 if veg south with nuts allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.3 if veg south with fish/eggs allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry'],axis=1)#aLready excluding poultry which has fish and eggs
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.4 if veg south with dairy and nuts allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.5 if veg south with dairy and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.6 if veg south with nuts and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#1.7 if veg south with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])



	#2. if veg north with no allergies
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.1 if veg north with dairy allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.2 if veg north with nuts allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.3 if veg north with fish/eggs allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.4 if veg north with dairy and nuts allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.5 if veg north with dairy and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.6 if veg north with nuts and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.7 if veg north with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])




	#3. non veg case

	#1. if nonveg south with no allergies
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

		

	#1.1 if nonveg south with dairy allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.2 if nonveg south with nuts allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.3 if nonveg south with fish/eggs allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry'],axis=1)#excluded full poultry for now
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.4 if nonveg south with dairy and nuts allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.5 if nonveg south with dairy and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','dairy','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.6 if nonveg south with nuts and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#1.7 if nonveg south with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])



	#2. if nonveg north with no allergies
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.1 if nonveg north with dairy allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','dairy'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.2 if nonveg north with nuts allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.3 if nonveg north with fish/eggs allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.4 if nonveg north with dairy and nuts allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','dairy','nuts'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.5 if nonveg north with dairy and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','dairy','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.6 if nonveg north with nuts and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.7 if nonveg north with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','dairy','nuts','poultry'],axis=1)
		df2 = df1[df1.gi=='low']
		df3 = df1[df1.gi=='medium']
		diet_low_list = df2.values.tolist() + df3.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_fr[i][j]!='medium' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])




elif hb<6.5:
	#low+medium+high gi all foods can be consumed

	#1. if veg south with no allergies
	if pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='No':

		df1 =diet.drop(['north','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])
		

	#1.1 if veg south with dairy allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','dairy'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.2 if veg south with nuts allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.3 if veg south with fish/eggs allergy
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry'],axis=1)#aLready excluding poultry which has fish and eggs
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.4 if veg south with dairy and nuts allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','poultry','dairy','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.5 if veg south with dairy and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','dairy'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.6 if veg south with nuts and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#1.7 if veg south with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry','dairy','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])



	#2. if veg north with no allergies
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.1 if veg north with dairy allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','dairy'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.2 if veg north with nuts allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.3 if veg north with fish/eggs allergy
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.4 if veg north with dairy and nuts allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','poultry','dairy','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.5 if veg north with dairy and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','dairy'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.6 if veg north with nuts and fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.7 if veg north with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry','dairy','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])




	#3. non veg case

	#1. if nonveg south with no allergies
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

		

	#1.1 if nonveg south with dairy allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['north','dairy'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.2 if nonveg south with nuts allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.3 if nonveg south with fish/eggs allergy
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','poultry'],axis=1)#excluded full poultry for now
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.4 if nonveg south with dairy and nuts allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['north','dairy','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.5 if nonveg south with dairy and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['north','dairy','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#1.6 if nonveg south with nuts and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','nuts','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#1.7 if nonveg south with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='South' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['north','nuts','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])



	#2. if nonveg north with no allergies
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.1 if nonveg north with dairy allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='No':
		df1 =diet.drop(['south','dairy'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.2 if nonveg north with nuts allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.3 if nonveg north with fish/eggs allergy
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.4 if nonveg north with dairy and nuts allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='No':
		df1 =diet.drop(['south','dairy','nuts'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.5 if nonveg north with dairy and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='No' and aller_fe=='Yes':
		df1 =diet.drop(['south','dairy','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])

	#2.6 if nonveg north with nuts and fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='No' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','nuts','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


	#2.7 if nonveg north with dairy, nuts, fish/eggs allergic
	elif pref_vnv=='Non-veg' and pref_sn=='North' and aller_d=='Yes' and aller_n=='Yes' and aller_fe=='Yes':
		df1 =diet.drop(['south','dairy','nuts','poultry'],axis=1)
		diet_low_list = df1.values.tolist()

		for i in range(len(diet_low_list)):
		    for j in range(len(diet_low_list[0])):
		        if diet_low_list[i][j]!='low' and diet_low_list[i][j]!='medium' and diet_low_list[i][j]!='high' and str(diet_low_list[i][j])!= 'nan':
		            fin_res1.append(diet_low_list[i][j])


else:
	print("End")


print("here are the recommended list of foods which you can eat - ")

for i in fin_res1:
    print(i)	


