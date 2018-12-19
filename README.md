                                             VTX GURU     
                                      FPV IMD Analysis Tools



VTX Guru is a suite of tools for for FPV pilots, concerning having clear video when multiple pilots fly at once. 
VTX Guru can help pilots easily find a good channel group for multiple pilots; as well as analyze particular 
channel groups, or investigate all possible combinations of a set of channels. Scores are derived from a unique 
algorithm. 



VTX_Guru.py   -  Is the main application where all the individual tools can be accessed.




ET_groups.py  -  Runs analysis on all www.etheli.com/IMD recommended groups.




plots/        -  Graphical information about the distribution of scores, channels, bands, and frequencies 
				 whithin the different channel groups studied.




libr/plot.py  -  The script used to plot (most of) the graphs in the plots folder.







The following are available for viewing within the VTX Guru application, but can also be found here:





libr/studies/ -  Where VTX channel group lists are located. All lists are also viewable using the Charts tool 
				 from within VTX Guru. Group lists are sorted lists of "passing" channel groups organized by 
				 number of pilots and channel set studied. 
				 For example:
				 list3usa.txt = 3 channel groups of USA legal channels only.
				 list3.txt    = 3 channel groups of 40 channel vtx group.
				 list3low.txt = 3 channel groups of 40 channel vtx group plus lowband channels.




libr/Scores.md - Expalins how Video Clarity Scores are calculated. 