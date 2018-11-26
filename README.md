                                             VTX GURU     
                                      FPV IMD Analysis Tools




	VTX Guru scores FPV VTX channel groups based on the IMD (Inter Modulation Distortion)
	profile of the channel group. Additionally, VTX Guru may progressively reduce
	the output score based upon the VTX channel separation within the group. The resultant 
	score is an attempt to allow comparison of the scores alone to be more meaningful.
	The "Video Clarity Score" term is used to indicate that score may not have been strictly 
	IMD derived; it may have been influenced by the VTX channels separations.


	IMD SCORE
	---------
	The IMD score is calculated based on a unique algorithm, which borrows from a prior IMD
	calculator the idea that when an resultant IMD frequency is within 35MHz of a FPV VTX
	channel we can consider it a problem and the score is reduced from the top score - 100. 
	The previous calculator and corresponding explanation are at http://www.etheli.com/IMD/.

	With VTX Guru, unlike it's predecessor, scores strictly go from 100 (highest) to
	0 (lowest). Not every score of 0 is equally bad, but rather it indicates a fail condition
	has been meet. When scores near perfect (100), a greater discernment between similar 
	performing groups can be observed.

	To begin calculating a score, we look at each resultant IMD frequency in a 5G VTX freq group.
	This is done with the standard IMD formula -  F3 = (F1 x 2) - F2.  If the problem IMD freq is
	an exact match to a VTX channel, a fail condition is met and the score goes to zero.
	Otherwise, if a IMD freq is within 35MHz of a VTX channel, it is considered a "problem IMD 
	frequency". A problem IMD freq. can be within 35MHz of more than one VTX channel. For each
	problem IMD frequency - the least separation (sep.) to a VTX channel (in MHz) is noted; and 
	how many times the separation was less than 35 MHz is noted (IMD_close_to_chan).

	The least separation to a VTX channel is subtracted from 35 resulting in a "reducing score"
	(for each problem IMD freq) that ranges from 1 (34MHz sep.) to 34 (1MHz sep.). Furthermore,
	a "reducing factor" is created based on how many times in total problem IMD frequencies were
	close to VTX channels, for the entire group. 

	reducing factor =  1 - (IMD_close_to_chan / 30)

	Also calculated is the mean deviation of the reducing scores. The worst possible result 
	would be a mean deviation of 35, what all exact IMD matches to VTX channels would produce.
	So this should produce a score zero. The mean deviation of reducing scores is scaled
	so that  35 X (scale factor) =  100, so when subtracted from 100 the score goes to zero 
	(in worst case).
	 
	IMD score =  (100 - scaled mean deviation of reducing scores) X reducing factor


	BROADCAST FACTOR
	----------------
	
	Video Clarity Score = IMD Score X Broadcast Factor

	The IMD score is next multiplied by a broadcast factor, if one has been created, to 
	penalize the score proportional to VTX channel separation. 

	A broadcast factor will be created if any VTX channels are closer than 40 MHz apart.
	If any VTX channels are closer than 27 MHz apart a fail condition is met and the score goes 
	to zero. If VTX channel separations are lower than 40 MHz the closest separation is noted
	and all channel separations under 40 MHz counted (broadcast_close_times). By subtracting 
	closest separation from 40, a reducing score is created from 1 to 40 (broad_score).
	Broadcast factor is calculated as such:

	broadcast_factor = (1 - (broad_score / (26 - broad_score)))


	But if closest VTX separation was below 37MHz - instead:

	broadcast_factor = (1 - (broad_score / (26 - broad_score))) * (1/broadcast_close_times)


	As you can see, if any VTX channels separation is less than 37 MHz an additional 
	factor is multiplied to the broadcast factor. In this case, if broadcast_close_times is 
	greater than one - broadcast factor is greatly reduced. Effectively allowing only one 
	broadcast close time without more than halving the Video Clarity Score.

	

	WEIGHTED SCORE
	--------------
	Additionally, 5 and 6 channel groups cannot score perfect 100 scores. So to make things 
	easier the weighted scoring for 5 and 6 channel groups was created. With weighted scoring 
	the "best in class" group(s) gets a weighted score of 100. The seeming least good of 
	previously recommended groups (IMD5 & IMD6) both get a score of 62.3 weighted. The 
	Video Clarity Score is scaled appropriately to achieve this result.

	With weighted scoring we can call 62.3  (or slightly below at 60, as I have done)
	the fail point. So all scores above 60 are "Pass". It is these groups with Pass scores 
	that compromise	the database searched in Smart Search and shown in Charts. 

	With 3 and 4 channel groups, the same above 60 score = Pass method is used, however the 
	unweighted Video Clarity Score (VCS) is used. In this case to judge from sixty and above 
	is more arbitrary; it's done for consistency of the above 60 pass logic and ensures 
	sufficient entries for Smart Search to search.