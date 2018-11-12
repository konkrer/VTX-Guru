from FreqSet1 import FreqSet

"""
--------------------------------------------
Run this script to perform an investigation.
--------------------------------------------

"""




#sort_list - for sorting resutls of  IMD investigation into a list ordered best to worst


def sort_list(inputfile):

	

# add every line of .txt file from investigation a into list for resorting


	scored_groups_list = []

	with open(inputfile, 'r') as f:
		for line in f:			
			scored_groups_list.append(line)



# seperate the perfect scores and sort, so perfects are now odreded by VTX channel seperation 


	perfects = list(filter(lambda x: x[0]=='1', scored_groups_list)) 
	perfects.sort(reverse=True)



#checks to see if perfects VTX channel seperation is > 100. if so seperate into new list	

	
	abv100_sep_checklist = [str(x) for x in range(100, 200)]
	above_100_seperation = [line for line in perfects if line[11:14] in abv100_sep_checklist]



#checks to see if perfects VTX channel seperation is < 100. if so seperate into new list. combine perfects lists so order is correct

	
	rest_perfects = [line for line in perfects if line[11:14] not in abv100_sep_checklist]
	new_perfects = above_100_seperation + rest_perfects



#seperate the non-perfect scores and sort higher numbers first. combine final list in correct order


	rest = list(filter(lambda x: x[0]!='1', scored_groups_list))  
	rest.sort(reverse=True)

	sorted_output = new_perfects + rest



#output file


	f2 = open(inputfile, 'w')

	f2.writelines(sorted_output)

	f2.close()

	print('winning!')





#perform investigation and sort output


x = FreqSet()
x.investigate()
sort_list(x.output)