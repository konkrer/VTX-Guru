from matplotlib import pyplot as plt
from sorter import get_score, get_freq_group, get_chan_group
import pandas as pd
import seaborn as sns


studies = [
'studies/list3.txt', 'studies/list3usa.txt', 'studies/list3low.txt',
'studies/list4.txt',  'studies/list4usa.txt', 'studies/list4low.txt',
'studies/list5.txt', 'studies/list5usa.txt', 'studies/list5low.txt',
'studies/list6.txt', 'studies/list6usa.txt', 'studies/list6low.txt'
]


def plot_list_scores(group_list):

	score_list = []

	with open(group_list) as f:
		all_lines = f.readlines()

	for line in all_lines[3:]:
		score_list.append(get_score(line, 0))

	plt.hist(score_list, bins=50, color='slateblue')
	tit_str = group_list[8:-4]
	plt.title("{} Scores Distribution".format(tit_str))
	plt.xlabel('Scores')
	plt.ylabel('Occurrences')
	#plt.show()



def plot_list_freqs(group_list):

	freqs_list = []

	with open(group_list) as f:
		all_lines = f.readlines()

	for line in all_lines[3:]:
		group = get_freq_group(line)
		for chan in group:
			freqs_list.append(int(chan))


	plt.hist(freqs_list, bins=50) 
	tit_str = group_list[8:-4]
	plt.title("{} Frequency Distribution".format(tit_str))
	plt.xlabel('Frequency')
	plt.ylabel('Occurrences')
	#plt.show()



def plot_channel_freq(group_list, num_channels):

	channel_count_list = [0 for i in range(num_channels)]
	freqs_list = []
	freq_to_chan = {}
	freq_to_indx = {}
	

	# load data
	with open(group_list) as f:
		all_lines = f.readlines()

	for line in all_lines[3:]:
		group = get_freq_group(line)
		for chan in group:
			freqs_list.append(int(chan))


	#populate dictionary
	with open('vtx_channel_guide_abrv.txt') as f:  

		for i in range(num_channels):
			line = f.readline()
			pair = line.strip('\n').split(', ')
			freq_to_chan[int(pair[1])] = pair[0]

	#create list from .keys()
	possible_freqs = [x for x in freq_to_chan.keys()]
	possible_freqs.sort()
	
	#create dictionary to know which count in channel_count_list to increment
	idx_count = 0
	for freq in possible_freqs:
		freq_to_indx[freq] = idx_count
		idx_count += 1

	# increment appropriate count in channel_count_list
	for freq in freqs_list:
		idx = freq_to_indx[freq]
		channel_count_list[idx] += 1

	# convert frequency to channel for labels
	channel_labels = [freq_to_chan[freq].upper() for freq in possible_freqs]
		
	#plot
	sns.set(palette='deep')
	plt.figure(figsize=(13, 5))
	ax = plt.subplot()
	plt.bar(range(num_channels), channel_count_list) #, color='green'
	tit_str = group_list[8:-4]
	plt.title("{} Channel Occurrences".format(tit_str))
	plt.xlabel('Channel')
	plt.ylabel('Occurrences')
	ax.set_xticks(range(num_channels))
	ax.set_xticklabels(channel_labels)

	#plt.show()



def plot_channel_occur_sea(group_list, num_channels):

	channel_count_list = [0 for i in range(num_channels)]
	freqs_list = []
	freq_to_chan = {}
	freq_to_indx = {}
	

	# load data
	with open(group_list) as f:
		all_lines = f.readlines()

	for line in all_lines[3:]:
		group = get_freq_group(line)
		for chan in group:
			freqs_list.append(int(chan))


	#populate dictionary
	with open('vtx_channel_guide_abrv.txt') as f:  

		for i in range(num_channels):
			line = f.readline()
			pair = line.strip('\n').split(', ')
			freq_to_chan[int(pair[1])] = pair[0]

	#create list from .keys()
	possible_freqs = [x for x in freq_to_chan.keys()]
	possible_freqs.sort()
	
	#create dictionary to know which count in channel_count_list to increment
	idx_count = 0
	for freq in possible_freqs:
		freq_to_indx[freq] = idx_count
		idx_count += 1

	# increment appropriate count in channel_count_list
	for freq in freqs_list:
		idx = freq_to_indx[freq]
		channel_count_list[idx] += 1

	# convert frequency to channel for labels
	channel_labels = [freq_to_chan[freq].upper() for freq in possible_freqs]
		
	# create DataFrame
	df = pd.DataFrame({
		'Channel': channel_labels,
		'Occurrences': channel_count_list
})

	#plot

	plt.figure(figsize=(14,6))
	sns.set_style('darkgrid')
	sns.set_context('notebook')
	tit_str = group_list[8:-4]
	plt.title("{} Channel Occurrences".format(tit_str))
	sns.barplot(
		data=df,
		x='Channel',
		y='Occurrences',
		palette='dark'
)
	#plt.show()


def plot_band_frequency(group_list, num_bands, ax_obj):

	band_count_list = [0 for i in range(num_bands)]
	chan_list = []
	band_to_idx = {'a': 0, 'b': 1, 'e': 2, 'f': 3, 'r':4, 'l': 5}
	labels = ['A', 'B', 'E', 'F', 'R', 'L']

	with open(group_list) as f:

		with open(group_list) as f:
			all_lines = f.readlines()

	for line in all_lines[3:]:
		group = get_chan_group(line)
		for chan in group:
			chan_list.append(chan)
	
	for freq in chan_list:

		band = freq[0]
		idx = band_to_idx[band]
		band_count_list[idx] += 1

	plt.bar(range(num_bands), band_count_list, color='slateblue') 
	tit_str = group_list[8:-4]
	plt.title("{} Band Occurrences".format(tit_str))
	plt.xlabel('Band')
	plt.ylabel('Occurrences')
	ax_obj.set_xticks(range(num_bands))
	ax_obj.set_xticklabels(labels[:num_bands])

	#plt.show()



def plot_band_frequency_pie(group_list, num_bands, Axes):

	band_count_list = [0 for i in range(num_bands)]
	chan_list = []
	band_to_idx = {'a': 0, 'b': 1, 'e': 2, 'f': 3, 'r':4, 'l': 5}
	labels = ['A', 'B', 'E', 'F', 'R', 'L']
	
	with open(group_list) as f:
		all_lines = f.readlines()

	for line in all_lines[3:]:
		group = get_chan_group(line)
		for chan in group:
			chan_list.append(chan)
	
	for freq in chan_list:

		band = freq[0]
		idx = band_to_idx[band]
		band_count_list[idx] += 1

	#Axes = plt.subplot()
	sns.set()
	plt.pie(band_count_list, labels=labels[:num_bands], 
		autopct='%.0f%%', shadow=True, pctdistance=.7,
		startangle=90) 
	Axes.set_aspect(.9)
	tit_str = group_list[8:-4]
	plt.title("{} Band Occurrences".format(tit_str))
	
	#plt.show()




def plot_scores_groups():

	plt.close('all')
	plt.figure(figsize=(10, 11))

	for i in range(len(studies)):

		plt.subplot(4, 3, i+1)
		plot_list_scores(studies[i])

	plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/Scores_Dist_Barchart.png')
	plt.show()


def plot_freq_dist():


	plt.close('all')
	plt.figure(figsize=(13, 11))

	for i in range(len(studies)):
		plt.subplot(4, 3, i+1)
		plot_list_freqs(studies[i])

	plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/Frequency_dist.png')
	plt.show()



def plot_chan_occur():


	plt.close('all')
	

	#plt.subplot(4, 3, 1)
	plot_channel_freq('studies/list3.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list3.png')
	#plt.show()

	#plt.subplot(4, 3, 2)
	plot_channel_freq('studies/list3usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list3usa.png')
	#plt.show()

	#plt.subplot(4, 3, 3)
	plot_channel_freq('studies/list3low.txt', 47)
	plt.savefig('Plots/channel_occur/chans_list3low.png')

	#plt.subplot(4, 3, 4)
	plot_channel_freq('studies/list4.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list4.png')

	#plt.subplot(4, 3, 5)
	plot_channel_freq('studies/list4usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list4usa.png')

	#plt.subplot(4, 3, 6)
	plot_channel_freq('studies/list4low.txt', 47)
	plt.savefig('Plots/channel_occur/chans_list4low.png')

	#plt.subplot(4, 3, 7)
	plot_channel_freq('studies/list5.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list5.png')

	#plt.subplot(4, 3, 8)
	plot_channel_freq('studies/list5usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list5usa.png')

	#plt.subplot(4, 3, 9)
	plot_channel_freq('studies/list5low.txt', 47)
	plt.savefig('Plots/channel_occur/chans_list5low.png')

	#plt.subplot(4, 3, 10)
	plot_channel_freq('studies/list6.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list6.png')

	#plt.subplot(4, 3, 11)
	plot_channel_freq('studies/list6usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list6usa.png')

	#plt.subplot(4, 3, 12)
	plot_channel_freq('studies/list6low.txt', 47)

	plt.subplots_adjust(hspace=.75, wspace=.6)
	#plt.savefig('Plots/channel_occur/chans_list6low.png')
	plt.show()




def plots_chan_occur_sea():


	plt.close('all')
	

	plot_channel_occur_sea('studies/list3.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list3.png')
	#plt.show()

	
	plot_channel_occur_sea('studies/list3usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list3usa.png')
	#plt.show()

	
	plot_channel_occur_sea('studies/list3low.txt', 47)
	plt.savefig('Plots/channel_occur2/chans_list3low.png')

	
	plot_channel_occur_sea('studies/list4.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list4.png')

	
	plot_channel_occur_sea('studies/list4usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list4usa.png')

	
	plot_channel_occur_sea('studies/list4low.txt', 47)
	plt.savefig('Plots/channel_occur2/chans_list4low.png')

	
	plot_channel_occur_sea('studies/list5.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list5.png')

	
	plot_channel_occur_sea('studies/list5usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list5usa.png')

	
	plot_channel_occur_sea('studies/list5low.txt', 47)
	plt.savefig('Plots/channel_occur2/chans_list5low.png')

	
	plot_channel_occur_sea('studies/list6.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list6.png')

	
	plot_channel_occur_sea('studies/list6usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list6usa.png')

	
	plot_channel_occur_sea('studies/list6low.txt', 47)

	plt.savefig('Plots/channel_occur2/chans_list6low.png')
	plt.show()







def plot_band_occur():


	plt.close('all')
	plt.figure(figsize=(13, 11))
	bands_pattern = [5, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 6]

	for i in range(len(studies)):
		x = plt.subplot(4, 3, i+1)
		plot_band_frequency(studies[i], bands_pattern[i], x)

	plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/Band_Dist_Barchart.png')
	plt.show()



def plots_band_occur_pie():


	plt.close('all')
	plt.figure(figsize=(13, 11))
	bands_pattern = [5, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 6]

	for i in range(len(studies)):
		x = plt.subplot(4, 3, i+1)
		plot_band_frequency_pie(studies[i], bands_pattern[i], x)

	#plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/Band_Dist_Piechart.png')
	plt.show()




if __name__ == '__main__':
	plots_band_occur_pie()