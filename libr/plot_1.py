from matplotlib import pyplot as plt
from sorter import get_score, get_freq_group, get_chan_group
import pandas as pd
import seaborn as sns




def plot_list_scores(group_list):

	score_list = []

	with open(group_list) as f:

		for line in f:
			score_list.append(get_score(line, 0))

	plt.hist(score_list, bins=50, color='slateblue', histtype='step')
	tit_str = group_list[8:-4]
	plt.title("{} Scores Distribution".format(tit_str))
	plt.xlabel('Scores')
	plt.ylabel('Occurrences')
	#plt.show()




def plot_list_scores_sea(group_list):

	score_list = []

	with open(group_list) as f:

		for line in f:
			score_list.append(get_score(line, 0))

	df = pd.DataFrame({'scores': score_list})

	sns.set_style('whitegrid')
	sns.set_context('notebook')

	sns.kdeplot(df.scores, shade=True)

	tit_str = group_list[8:-4]
	plt.title("{} Scores Distribution".format(tit_str))
	plt.xlabel('Scores')
	plt.ylabel('Occurrences')
	plt.show()





def plot_list_freqs(group_list):

	freqs_list = []

	with open(group_list) as f:

		for line in f:
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

		for line in f:
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

		for line in f:
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

		for line in f:
			group = get_chan_group(line)
			for chan in group:
				chan_list.append(chan)
	
	for freq in chan_list:

		band = freq[0]
		idx = band_to_idx[band]
		band_count_list[idx] += 1

	plt.bar(range(num_bands), band_count_list) 
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

		for line in f:
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

	plt.subplot(4, 3, 1)
	plot_list_scores('Studies/list3.txt')

	plt.subplot(4, 3, 2)
	plot_list_scores('Studies/list3usa.txt')

	plt.subplot(4, 3, 3)
	plot_list_scores('Studies/list3low.txt')

	plt.subplot(4, 3, 4)
	plot_list_scores('Studies/list4.txt')

	plt.subplot(4, 3, 5)
	plot_list_scores('Studies/list4usa.txt')

	plt.subplot(4, 3, 6)
	plot_list_scores('Studies/list4low.txt')

	plt.subplot(4, 3, 7)
	plot_list_scores('Studies/list5.txt')

	plt.subplot(4, 3, 8)
	plot_list_scores('Studies/list5usa.txt')

	plt.subplot(4, 3, 9)
	plot_list_scores('Studies/list5low.txt')

	plt.subplot(4, 3, 10)
	plot_list_scores('Studies/list6.txt')

	plt.subplot(4, 3, 11)
	plot_list_scores('Studies/list6usa.txt')

	plt.subplot(4, 3, 12)
	plot_list_scores('Studies/list6low.txt')

	plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/scores_figure2.png')
	plt.show()


def plot_freq_dist():


	plt.close('all')
	plt.figure(figsize=(13, 11))

	plt.subplot(4, 3, 1)
	plot_list_freqs('Studies/list3.txt')

	plt.subplot(4, 3, 2)
	plot_list_freqs('Studies/list3usa.txt')

	plt.subplot(4, 3, 3)
	plot_list_freqs('Studies/list3low.txt')

	plt.subplot(4, 3, 4)
	plot_list_freqs('Studies/list4.txt')

	plt.subplot(4, 3, 5)
	plot_list_freqs('Studies/list4usa.txt')

	plt.subplot(4, 3, 6)
	plot_list_freqs('Studies/list4low.txt')

	plt.subplot(4, 3, 7)
	plot_list_freqs('Studies/list5.txt')

	plt.subplot(4, 3, 8)
	plot_list_freqs('Studies/list5usa.txt')

	plt.subplot(4, 3, 9)
	plot_list_freqs('Studies/list5low.txt')

	plt.subplot(4, 3, 10)
	plot_list_freqs('Studies/list6.txt')

	plt.subplot(4, 3, 11)
	plot_list_freqs('Studies/list6usa.txt')

	plt.subplot(4, 3, 12)
	plot_list_freqs('Studies/list6low.txt')

	plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/freq_dist_fig.png')
	plt.show()



def plot_chan_occur():


	plt.close('all')
	

	#plt.subplot(4, 3, 1)
	plot_channel_freq('Studies/list3.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list3.png')
	#plt.show()

	#plt.subplot(4, 3, 2)
	plot_channel_freq('Studies/list3usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list3usa.png')
	#plt.show()

	#plt.subplot(4, 3, 3)
	plot_channel_freq('Studies/list3low.txt', 47)
	plt.savefig('Plots/channel_occur/chans_list3low.png')

	#plt.subplot(4, 3, 4)
	plot_channel_freq('Studies/list4.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list4.png')

	#plt.subplot(4, 3, 5)
	plot_channel_freq('Studies/list4usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list4usa.png')

	#plt.subplot(4, 3, 6)
	plot_channel_freq('Studies/list4low.txt', 47)
	plt.savefig('Plots/channel_occur/chans_list4low.png')

	#plt.subplot(4, 3, 7)
	plot_channel_freq('Studies/list5.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list5.png')

	#plt.subplot(4, 3, 8)
	plot_channel_freq('Studies/list5usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list5usa.png')

	#plt.subplot(4, 3, 9)
	plot_channel_freq('Studies/list5low.txt', 47)
	plt.savefig('Plots/channel_occur/chans_list5low.png')

	#plt.subplot(4, 3, 10)
	plot_channel_freq('Studies/list6.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list6.png')

	#plt.subplot(4, 3, 11)
	plot_channel_freq('Studies/list6usa.txt', 39)
	plt.savefig('Plots/channel_occur/chans_list6usa.png')

	#plt.subplot(4, 3, 12)
	plot_channel_freq('Studies/list6low.txt', 47)

	#plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/channel_occur/chans_list6low.png')
	plt.show()




def plots_chan_occur_sea():


	plt.close('all')
	

	plot_channel_occur_sea('Studies/list3.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list3.png')
	#plt.show()

	
	plot_channel_occur_sea('Studies/list3usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list3usa.png')
	#plt.show()

	
	plot_channel_occur_sea('Studies/list3low.txt', 47)
	plt.savefig('Plots/channel_occur2/chans_list3low.png')

	
	plot_channel_occur_sea('Studies/list4.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list4.png')

	
	plot_channel_occur_sea('Studies/list4usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list4usa.png')

	
	plot_channel_occur_sea('Studies/list4low.txt', 47)
	plt.savefig('Plots/channel_occur2/chans_list4low.png')

	
	plot_channel_occur_sea('Studies/list5.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list5.png')

	
	plot_channel_occur_sea('Studies/list5usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list5usa.png')

	
	plot_channel_occur_sea('Studies/list5low.txt', 47)
	plt.savefig('Plots/channel_occur2/chans_list5low.png')

	
	plot_channel_occur_sea('Studies/list6.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list6.png')

	
	plot_channel_occur_sea('Studies/list6usa.txt', 39)
	plt.savefig('Plots/channel_occur2/chans_list6usa.png')

	
	plot_channel_occur_sea('Studies/list6low.txt', 47)

	plt.savefig('Plots/channel_occur2/chans_list6low.png')
	plt.show()







def plot_band_occur():


	plt.close('all')
	plt.figure(figsize=(13, 11))

	x = plt.subplot(4, 3, 1)
	plot_band_frequency('Studies/list3.txt', 5, x)

	x = plt.subplot(4, 3, 2)
	plot_band_frequency('Studies/list3usa.txt', 5, x)

	x = plt.subplot(4, 3, 3)
	plot_band_frequency('Studies/list3low.txt', 6, x)

	x = plt.subplot(4, 3, 4)
	plot_band_frequency('Studies/list4.txt', 5, x)

	x = plt.subplot(4, 3, 5)
	plot_band_frequency('Studies/list4usa.txt', 5, x)

	x = plt.subplot(4, 3, 6)
	plot_band_frequency('Studies/list4low.txt', 6, x)

	x = plt.subplot(4, 3, 7)
	plot_band_frequency('Studies/list5.txt', 5, x)

	x = plt.subplot(4, 3, 8)
	plot_band_frequency('Studies/list5usa.txt', 5, x)

	x = plt.subplot(4, 3, 9)
	plot_band_frequency('Studies/list5low.txt', 6, x)

	x = plt.subplot(4, 3, 10)
	plot_band_frequency('Studies/list6.txt', 5, x)

	x = plt.subplot(4, 3, 11)
	plot_band_frequency('Studies/list6usa.txt', 5, x)

	x = plt.subplot(4, 3, 12)
	plot_band_frequency('Studies/list6low.txt', 6, x)

	plt.subplots_adjust(hspace=.75, wspace=.6)
	#plt.savefig('Plots/band_occur.png')
	plt.show()



def plots_band_occur_pie():


	plt.close('all')
	plt.figure(figsize=(13, 11))

	x = plt.subplot(4, 3, 1)
	plot_band_frequency_pie('Studies/list3.txt', 5, x)

	x = plt.subplot(4, 3, 2)
	plot_band_frequency_pie('Studies/list3usa.txt', 5, x)

	x = plt.subplot(4, 3, 3)
	plot_band_frequency_pie('Studies/list3low.txt', 6, x)

	x = plt.subplot(4, 3, 4)
	plot_band_frequency_pie('Studies/list4.txt', 5, x)

	x = plt.subplot(4, 3, 5)
	plot_band_frequency_pie('Studies/list4usa.txt', 5, x)

	x = plt.subplot(4, 3, 6)
	plot_band_frequency_pie('Studies/list4low.txt', 6, x)

	x = plt.subplot(4, 3, 7)
	plot_band_frequency_pie('Studies/list5.txt', 5, x)

	x = plt.subplot(4, 3, 8)
	plot_band_frequency_pie('Studies/list5usa.txt', 5, x)

	x = plt.subplot(4, 3, 9)
	plot_band_frequency_pie('Studies/list5low.txt', 6, x)

	x = plt.subplot(4, 3, 10)
	plot_band_frequency_pie('Studies/list6.txt', 5, x)

	x = plt.subplot(4, 3, 11)
	plot_band_frequency_pie('Studies/list6usa.txt', 5, x)

	x = plt.subplot(4, 3, 12)
	plot_band_frequency_pie('Studies/list6low.txt', 6, x)

	#plt.subplots_adjust(hspace=.75, wspace=.6)
	plt.savefig('Plots/band_occur_pie.png')
	plt.show()




if __name__ == '__main__':
	plots_band_occur_pie()
