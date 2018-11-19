from random import randrange
import sys





def sort_list2(inputfile):

	scored_groups_list = []

	with open(inputfile, 'r') as f:
		scored_groups_list = f.readlines()
	
	sys.setrecursionlimit(5000)
	quicksort(scored_groups_list, 0, (len(scored_groups_list)-1))
	
	with open(inputfile, 'w') as f:
		f.writelines(scored_groups_list)




def quicksort(lst, start, end):

	if start >= end:
		return 
	pivot = randrange(start, end+1)
	pivot_value = lst[pivot]
	lst[pivot], lst[end] = lst[end], lst[pivot]
	marker = start
	for i in range(start,end):
		if int(get_score(lst[i])) > int(get_score(pivot_value)):
			lst[marker], lst[i] = lst[i], lst[marker]
			marker += 1
		elif int(get_score(lst[i])) == int(get_score(pivot_value)):
			if get_vtx_sep(lst[i]) > get_vtx_sep(pivot_value):
				lst[marker], lst[i] = lst[i], lst[marker]
				marker += 1
			elif get_vtx_sep(lst[i]) == get_vtx_sep(pivot_value):
				if lst[i] < pivot_value:
					lst[marker], lst[i] = lst[i], lst[marker]
					marker += 1

	lst[marker], lst[end] = lst[end], lst[marker]

	quicksort(lst, start, marker-1)
	quicksort(lst, marker+1, end)




def get_score(string):

	halves = string.split('   ')
	scores = halves[0].split('  ')
	score = scores[0]
	split = score.split('.')
	whole = split[0] + split[1]
	
	return whole



def get_vtx_sep(string):

	halves = string.split('   ')
	scores = halves[0].split('  ')
	vtx_sep = int(scores[2])
	return vtx_sep



'''
def get_wgtscore(string):

	halves = string.split('   ')
	scores = halves[0].split('  ')
	wgtscore = scores[1]
	split = score.split('.')
	whole = split[0] + split[1]
	
	return whole

'''








# old method using innate python sort method




# sort_list - for sorting score resutls of IMD investigation, best to worst score

def sort_list(inputfile):

	

    # add every line of .txt file (from investigation) a into list

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


    #checks to see if perfects VTX channel seperation is < 100. if so seperate into new list. 
	#combine perfects lists so order is correct

	rest_perfects = [line for line in perfects if line[11:14] not in abv100_sep_checklist]
	new_perfects = above_100_seperation + rest_perfects


    #seperate the non-perfect scores and sort higher numbers first.

	rest = list(filter(lambda x: x[0]!='1', scored_groups_list))  
	rest.sort(reverse=True)

    #combine final list in correct order

	sorted_output = new_perfects + rest

    #output sorted data

	f2 = open(inputfile, 'w')
	f2.writelines(sorted_output)
	f2.close()

	print('winning!')




'''
def radix_sort(lst):

	shmist = lst.copy()
	max_ = None

	for line in shmist:
		x = get_score(line)
		if max_:
			if len(x) > max_:
				max_ = len(x)
		else:
			max_ = len(x)

	for i in range(max_):
		position = i + 1
		index = - position
		buckets = [[] for i in range(10)]

		for line in shmist:
			y = get_score(line)
		
			try:
				digit = int(y[index])

			except IndexError:
				digit = 0

			buckets[9 - digit].append(line)

		shmist = []
		for bucket in buckets:
			shmist.extend(bucket)

	return shmist
'''