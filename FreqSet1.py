






class FreqSet:
  
  def __init__(self, freq1 = None, freq2 = None, freq3 = None, freq4 = None, freq5 = None, freq6 = None):
    self.freq1 = freq1
    self.freq2 = freq2
    self.freq3 = freq3
    self.freq4 = freq4
    self.freq5 = freq5
    self.freq6 = freq6
    self.group = [self.freq1, self.freq2, self.freq3, self.freq4, self.freq5, self.freq6]
    self.output = None
    self.scores = []








  def get_input(self):
    
    if self.freq1 != None and self.freq2 != None:
      #group = [self.freq1, self.freq2, self.freq3, self.freq4, self.freq5, self.freq6]
      return self.group

    bands = ['a', 'b', 'c', 'e', 'f', 'r']
    channels = [str(x) for x in range(1,9)]

    print ("""
    


----------------FPV VTX CHANNEL INTERFERENCE CHECKER----------------------
                          (IMD Analyzer)

    
    Transmitting on two or more video channels can cause problems.
    Enter two to six channels to check for interference.


    Enter Band Channel abbreviation.(i.e. F1, R7) OR four digit frequency. 
    Bands: A - B - E - F - R(C)
    Channels: 1-8
    

    """)
    

                                        #first channel

    while True:
      
      self.freq1 = input("Enter first video channel => ").lower()
      
      try:
        
        if (self.freq1[0] in bands and self.freq1[1] in channels)\
        and len(self.freq1) == 2:
          print ("ok\n")
          break

        #elif self.freq1 == 'd':
         # break

        elif (int(self.freq1) <= 5945 and int(self.freq1) >= 5645):
          print ("ok\n")
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")

    
                                         #second channel


    while True:
      
      self.freq2 = input("Enter second video channel => ").lower()
      
      try:
        
        if (self.freq2[0] in bands and self.freq2[1] in channels)\
        and len(self.freq2) == 2:
          print ("ok\n")
          break

        #elif self.freq2 == 'd':
          #break

        elif (int(self.freq2) <= 5945 and int(self.freq2) >= 5645):
          print ("ok\n")
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


                                        #third channel


    while True:
      
      self.freq3 = input("Enter third video channel\nEnter D if done entering channels => ").lower()
      
      try:
        
        if (self.freq3[0] in bands and self.freq3[1] in channels)\
        and len(self.freq3) == 2:
          print ("ok\n")
          break

        elif self.freq3 == 'd':
          print("\n\n")
          self.freq3 = None
          break

        elif (int(self.freq3) <= 5945 and int(self.freq3) >= 5645):
          print ("ok\n")
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


                                         #fourth channel


    while True:
      
      if self.freq3 == None:
      	break

      self.freq4 = input("Enter fourth video channel.\nEnter D if done entering channels => ").lower()
      
      try:
        
        if (self.freq4[0] in bands and self.freq4[1] in channels)\
        and len(self.freq4) == 2:
          print ("ok\n")
          break

        elif self.freq4 == 'd':
          self.freq4 = None
          print("\n\n")
          break

        elif (int(self.freq4) <= 5945 and int(self.freq4) >= 5645):
          print ("ok\n")
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


                                        #fifth channel


    while True:

      if self.freq4 == None:
      	break

      self.freq5 = input("Enter fifth video channel.\nEnter D if done entering channels => ").lower()
      
      try:
        
        if (self.freq5[0] in bands and self.freq5[1] in channels)\
        and len(self.freq5) == 2:
          print ("ok\n")
          break

        elif self.freq5 == 'd':
          self.freq5 = None
          print("\n\n")
          break

        elif (int(self.freq5) <= 5945 and int(self.freq5) >= 5645):
          print ("ok\n")
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")

                                     #sixth channel


    while True:
      
      if self.freq5 == None:
      	break

      self.freq6 = input("Enter sixth video channel.\nEnter D if done entering channels => ").lower()
      
      try:
        
        if (self.freq6[0] in bands and self.freq6[1] in channels)\
        and len(self.freq6) == 2:
          print ("ok\n")
          break

        elif self.freq6 == 'd':
          self.freq6 = None
          print("\n\n")
          break

        elif (int(self.freq6) <= 5945 and int(self.freq6) >= 5645):
          print ("ok\n")
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


    self.group = [self.freq1, self.freq2, self.freq3, self.freq4, self.freq5, self.freq6]
    return self.group

  






  def check_freqz(self, group):
  
    freq_bad = []
  
    for i in range(len(group)):
      temp = (i + 1)
      rest = group[:i] + group[temp:]
      lst_bad = []
      for n in range(len(rest)):
        bad_one = (int(group[i]) * 2) - int(rest[n])
        lst_bad.append(bad_one)
      freq_bad.append(lst_bad)


    return freq_bad









  def analyze_interference(self, group):
  
    bad_freq = self.check_freqz(group)
    bad_match = 0
    bad_close = 0
    close = 0
    near = 0
    #print()
    #print(bad_freq)
    #print(group)

    for i in range(len(group)):
      for sublst in bad_freq:
      

        if int(group[i]) not in sublst:
      
          for x in sublst:
            diff = abs(x - int(group[i]))
            if diff <20 and diff >= 10:
              print("\nWarning: IMD on %s is quite close to %s.(%sMHz)" % (x, group[i], diff))
              close += 1

            elif diff < 10:
              print("\nWarning: IMD on %s is very close to %s.(%sMHz)" % (x, group[i], diff))
              bad_close += 1

            elif  diff < 35:
              near += 1 

        elif int(group[i]) in sublst:
          print("\nWarning %s will have terrible interference!" % (group[i]))
          bad_match += 1
      
      
    if bad_match + bad_close + close + near == 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 	    All clear. Minimal IMD interference.")

    
    elif bad_match + bad_close + close == 0:
      
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 	   	IMD interference not too bad.\n")
      
      if len(group) >= 5:
        print(" 	This is an excellent IMD rating for 5 or 6 channels.")
    

    elif bad_match == 0 and bad_close == 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 	      Troubling interference possible.\n")
      
      if len(group) >= 5:
        print(" 	     Good IMD rating for 5 and 6 channels.")
      

    elif bad_match == 0 and bad_close > 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 		     IMD problems likley!\n 	   IMD within 10MHz of at least one channel.")

    
    elif bad_match > 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n 			 -------ANALYSIS-------\n\n 	  Bad channel grouping! Debilitating interference!")
    
    printable = self.convert_to_abbreviations()

    print("\n")
    print("                 ", end='')
    for chan in printable:
      print (chan.upper(), end='   ')
    
    converted = self.convert_freq_abbreviations()

    print("\n")
    print("           ", end='')
    for chan in converted:
      print (chan, end='   ')

    print("\n\n\n\n\n")




  def convert_freq_abbreviations(self):
    
    converter = {}
    converted = []

    with open('vtx_channel_guide.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        dirty = sliced_raw[1]
        clean = dirty.strip('\n')
        converter[sliced_raw[0]] = clean
    
    for chan in self.group:
      
      if chan != None:
        
        if len(chan) == 2:
          value = converter[chan]
          converted.append(int(value))
        
        else:
        	converted.append(int(chan))

    return converted





  def convert_to_abbreviations(self):
    
    converter = {}
    converted = []

    with open('vtx_channel_guide_abrv.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        dirty = sliced_raw[1]
        clean = dirty.strip('\n')
        converter[clean] = sliced_raw[0]
    
    for chan in self.group:
      
      if chan != None:
        
        if len(chan) == 4:
          if chan in converter.keys():
            value = converter[chan]
            converted.append(value)

          else:
            converted.append(chan)
        
        else:
          converted.append(chan)


    return converted






  def score(self, group):
    
    bad_freq = self.check_freqz(group)
    score_total = 0
    divide_by = 0
    IMD_close_to_chan = 0
    closest_imd = None
    closest_broadcast = None
    score_alt = None
    score_alt_weighted = None
    broadcast_factor = None

    #print(bad_freq)

    for i in range(len(group)):
      
      other_chans = [freq for freq in group if freq != group[i]]
      
      for chan in other_chans:

        diff2 = abs(chan - int(group[i]))
        
        if closest_broadcast == None:
          closest_broadcast = diff2
          
        else:
          if diff2 < closest_broadcast:
              closest_broadcast = diff2


    
    for sublst in bad_freq:
      for x in sublst:
        worst = None
        for chan in group:
          diff3 = abs(x - chan)
          if diff3 < 35:
            IMD_close_to_chan += 1
            if worst == None:
              worst = diff3
            else:
              if diff3 < worst:
                worst = diff3
        
        if worst != None:
          if closest_imd == None:
            closest_imd = worst
          else:
            if worst < closest_imd:
              closest_imd = worst

          to_add = (35 - worst) ** 2
          score_total += to_add
          divide_by += 1 

           

    ratio = (IMD_close_to_chan / len(group))


    print("Number of Problem \nIMD frequencies: ============> " + str(divide_by) + "\n\n")
    print("Times problem IMD freq \nis close to VTX channel: ====> " + str(IMD_close_to_chan) + "\n\n")
    print("Problem IMD freqs / Channels \nratio is: ===================> " + str(round(ratio, 1)) + "\n\n")
    print("Minimum Problem IMD\nfrequency seperation\nto VTX channel: =============> " + str(closest_imd) + " MHz\n(*within 35Mhz)\n\n")

    
    if closest_imd == 0:
      score_alt = 0
      print("Minimum VTX\nchannel seperation  =========> %sMHz\n\n" % (closest_broadcast))
    
    
    else:

      if closest_broadcast < 40:
          
        if closest_broadcast <= 19:
            #score_alt = 0
          print("*****VTX channels too close!!! %s MHz apart.*****\n\n" % (closest_broadcast))      

        elif closest_broadcast < 35:
          print("***VTX channels close! %s MHz apart.***\n\n" % (closest_broadcast))

        else:
          print("Minimum VTX\nChannel seperation  =========> %sMHz\n(Channels getting close!)\n\n" % (closest_broadcast))
          
        broadcast_factor = (1 - ((40 - closest_broadcast) / 25))

      if divide_by != 0:
 
        score_alt =  100 - ((((float(score_total) /divide_by) ** .5) * 3) * .952)               
        score_alt = score_alt * (1 -(IMD_close_to_chan / 30))  # to reduce proportinal to close IMD channels
        
        
        
          
        if broadcast_factor != None:   
          score_alt = score_alt * broadcast_factor  # to reduce proportinal to close broadcast channels

          #else:
           # score_alt = 100 * broadcast_factor

        else:
          print("Minimum VTX\nchannel seperation  =========> %sMHz\n\n" % (closest_broadcast))
        
        

        if len(group) == 6:
          
          score_alt_weighted = round(score_alt * 2.204, 1)  # old factor 1.966
          score_alt = round(score_alt, 1)
        
        elif len(group) == 5:
          
          compressor =  ((80.0053 - score_alt) / 6.1) + score_alt
          score_alt_weighted = round((compressor + 20), 1) 
          score_alt = round(score_alt, 1)
        
        else: 
          score_alt = round(score_alt, 1)

      else:
        if broadcast_factor == None:
          score_alt = 100
          print("Minimum VTX\nchannel seperation  =========> %sMHz\n\n" % (closest_broadcast))
        
        else:
          score_alt = 100 * broadcast_factor

        





    print("Video Clarity Score: ========> {score}\n".format(score=score_alt))
    if score_alt_weighted != None:
      print("""
Weighted Video Clarity Score
(weighted relevant to {number}
channels): ==================> {score}
        """.format(number=len(group), score=score_alt_weighted))
 
    print("\nTop Possible Score is 100\n\n\n\n\n\n\n\n")
    
    self.scores = [score_alt, score_alt_weighted]









  def export(self):

    group = [freq for freq in self.group if freq != None]
    
    if self.output == None:
      
      output_file = input("Name of output_file?")
      with open(output_file, "a") as f:
        f.write("%s  %s   " % (self.scores[0], self.scores[1]))
        for chan in group:
          f.write(str(chan) +" ",)
        f.write("\n")

    else:
      with open(self.output, "a") as f:
        f.write("%s  %s   " % (self.scores[0], self.scores[1]))
        for chan in group:
          f.write(str(chan) +" ",)
        f.write("\n")
 






  def investigate(self, score_limit=60):
    
    num_channels =  int(input("How many in channel group to investigate? (3-6): "))
    
    if num_channels > 6 or num_channels < 3:
      return
    
    usa_only = input("USA only? (Enter Y or N): ").lower()
    
    if usa_only == 'y':
      print('\n\n*USA VTX CHANNELS ONLY CONFIRMED*\n\n')
      usa_only = True
    else:
      print('\n\nWORLDWIDE VTX CHANNELS CONFIRMED\n\n')
      usa_only = False

    self.output = input("Filename to output data?")

    channels = []

    with open('vtx_channel_guide_abrv.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        channels.append(sliced_raw[0])

    if usa_only:
      channels.remove('e4')
      channels.remove('e7')
      channels.remove('e8')

    #good_groups = []
    channel_1_used = []
    base_case = None
    combo_count = 0
    
    l = len(channels)
    if num_channels == 6:
      base_case = (l*(l-1)*(l-2)*(l-3)*(l-4)*(l-5)) / (6*5*4*3*2)
    elif num_channels == 5:
      base_case = (l*(l-1)*(l-2)*(l-3)*(l-4)) / (5*4*3*2)
    elif num_channels == 4:
      base_case = (l*(l-1)*(l-2)*(l-3)) / (4*3*2)
    elif num_channels == 3:
      base_case = (l*(l-1)*(l-2)) / (3*2)


    #loop = True

    while True:
      for i in range(len(channels)):
        #print(float(combo_count), base_case)
        channel_1 = channels[i]
        channel_1_used.append(channel_1)
        channels_2 = [channel for channel in channels if channel not in channel_1_used] 
        #print('channels_2')   
        #print(channels_2)
        channel_2_used = []
        channels_2_redux = [channel for channel in channels_2]
        if num_channels == 3:
          channels_2_redux.pop()
        elif num_channels == 4:
          channels_2_redux.pop()
          channels_2_redux.pop()
        elif num_channels == 5:
          channels_2_redux.pop()
          channels_2_redux.pop()
          channels_2_redux.pop()
        elif num_channels == 6:
          channels_2_redux.pop()
          channels_2_redux.pop()
          channels_2_redux.pop()
          channels_2_redux.pop()
        #print('channels_2_redux')
        #print(channels_2_redux)
        #print('channels_2')   
        #print(channels_2)

        for i in range(len(channels_2_redux)):
          channel_2 = channels_2_redux[i]
          channel_2_used.append(channel_2)
          #print('channel_2_used')
          #print(channel_2_used)
          channels_3 = [channel for channel in channels_2 if channel not in channel_2_used]
          #print("channels_3")
          #print(channels_3)
          channel_3_used = []
          channels_3_redux = [channel for channel in channels_3]
          if num_channels == 4:
            channels_3_redux.pop()
          elif num_channels == 5:
            channels_3_redux.pop()
            channels_3_redux.pop()
          elif num_channels == 6:
            channels_3_redux.pop()
            channels_3_redux.pop()
            channels_3_redux.pop()
          #print("channels_3_redux")
          #print(channels_3_redux)    

          for i in range(len(channels_3_redux)):
            channel_3 = channels_3_redux[i]
          
            if num_channels >= 4:
              channel_3_used.append(channel_3)
              channels_4 = [channel for channel in channels_3 if channel not in channel_3_used]
              channel_4_used = []
              channels_4_redux = [channel for channel in channels_4]
              if num_channels == 5:
                channels_4_redux.pop()
              elif num_channels == 6:
                channels_4_redux.pop()
                channels_4_redux.pop()

              for i in range(len(channels_4_redux)):
                channel_4 = channels_4_redux[i]
              
                if num_channels >= 5:
                  channel_4_used.append(channel_4)
                  channels_5 = [channel for channel in channels_4 if channel not in channel_4_used]
                  channel_5_used = []
                  channels_5_redux = [channel for channel in channels_5]
                  if num_channels == 6:
                    channels_5_redux.pop()

                  for i in range(len(channels_5_redux)):
                    channel_5 = channels_5_redux[i]

                    if num_channels == 6:
                      channel_5_used.append(channel_5)
                      channels_6 = [channel for channel in channels_5 if channel not in channel_5_used]
                    
                      for i in range(len(channels_6)):
                        channel_6 = channels_6[i]

                        self.group = [channel_1, channel_2, channel_3, channel_4, channel_5, channel_6]
                        converted = self.convert_freq_abbreviations()
                        print(self.group)
                        self.score(converted)
                        if self.scores[1] != None:
                          if self.scores[1] >= score_limit:
                            #sorted_group = sorted(self.group)
                            #if sorted_group not in good_groups:
                              #good_groups.append(sorted_group)
                            self.export()
                        combo_count += 1
                        if combo_count >= (int(base_case)):
                          #loop = False
                          return
                  
              
                    else:
                      self.group = [channel_1, channel_2, channel_3, channel_4, channel_5]
                      print(self.group)
                      converted = self.convert_freq_abbreviations()
                      self.score(converted)
                      if self.scores[1] != None:
                        if self.scores[1] >= score_limit:
                          #sorted_group = sorted(self.group)
                          #if sorted_group not in good_groups:
                            #good_groups.append(sorted_group)
                          self.export()
                      combo_count += 1
                      if combo_count >= (int(base_case)):
                        #loop = False
                        return 
         
                else:
                  self.group = [channel_1, channel_2, channel_3, channel_4]
                  print(self.group)
                  converted = self.convert_freq_abbreviations()
                  self.score(converted)
                  if self.scores[0] >= score_limit:
                    #sorted_group = sorted(self.group)
                    #if sorted_group not in good_groups:
                      #good_groups.append(sorted_group)
                    self.export()
                  combo_count += 1
                  if combo_count >= (int(base_case)):
                    #loop = False
                    return


            else:
              self.group = [channel_1, channel_2, channel_3]
              print(self.group)
              converted = self.convert_freq_abbreviations()
              self.score(converted)
              if self.scores[0] >= score_limit:
                self.export()  
              combo_count += 1
              if combo_count >= (int(base_case)):
                #loop = False
                return
              #print(combo_count, int(base_case))
              #print(loop)
            
          




   














    