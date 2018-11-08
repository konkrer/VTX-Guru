from FreqSet1 import FreqSet

def sort_list(inputfile):
	
	scored_groups_list = []

	with open(inputfile, 'r') as f:
		for line in f:
			#info = f.readline()
			scored_groups_list.append(line)


	perfects = list(filter(lambda x: x[0]=='1', scored_groups_list)) # [group for group in scored_groups_list if group[0] == '1']
	
	rest = list(filter(lambda x: x[0]!='1', scored_groups_list))  #rest = [group for group in scored_groups_list if group[0] != '1']

	rest.sort(reverse=True)

	rest_100 = [line for line in rest if line[6:9] == '100']
	
	rest_rest = [line for line in rest if line[6:9] != '100']

	rest_100.sort()

	updated_rest = rest_100 + rest_rest


	sorted_output = perfects + updated_rest



	f2 = open(inputfile, 'w')

	f2.writelines(sorted_output)

	f2.close()

	print('winning!')


x = FreqSet()
x.investigate()
sort_list(x.output)