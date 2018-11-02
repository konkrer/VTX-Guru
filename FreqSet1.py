






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

  

  def check_freqz(self, freq_set):
  
    group = [freq for freq in freq_set if freq != None]
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



  def analyze_interference(self, freq_set):
  
    bad_freq = self.check_freqz(freq_set)
    group = [freq for freq in freq_set if freq != None]
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
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 		All clear. Minimal interference.\n\n\n\n\n\n")

    elif bad_match + bad_close + close == 0:
      
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 	   	  Interference not too bad.\n")
      
      if len(group) >= 5:
        print(" 	  This is an excellent rating for 5 or 6 channels.\n\n\n\n\n\n")
      
      else:
        print("\n\n\n\n\n\n")
    
    elif bad_match == 0 and bad_close == 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 		Troubling interference possible.\n")
      
      if len(group) >= 5:
        print(" 		Good rating for 5 and 6 channels.\n\n\n\n\n\n")
      
      else:
        print("\n\n\n\n\n\n")

    elif bad_match == 0 and bad_close > 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n                   -------ANALYSIS-------\n\n 		     IMD problems likley!\n 	     IMD within 10MHz of at least one channel.\n\n\n\n\n\n")

    elif bad_match > 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n 			 -------ANALYSIS-------\n\n 	  Bad channel grouping! Debilitating interference!\n\n\n\n\n\n")

  

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

      else:
      	converted.append(chan)

    return converted



  def score(self, freq_set):
    
    bad_freq = self.check_freqz(freq_set)
    group = [freq for freq in freq_set if freq != None]
    score_total = 0
    #print(bad_freq)
    divide_by = 0
    closest_imd = None
    score_alt_weighted = None

    for i in range(len(group)):
      for sublst in bad_freq:
        for x in sublst:
          diff = abs(x - int(group[i]))
          if diff < 35:
            if closest_imd == None:
              closest_imd = diff
            else:
              if diff < closest_imd:
              	closest_imd = diff

            to_add = (35 - diff) ** 2
            score_total += to_add
            divide_by += 1
            #print(x)

    #if divide_by != 0:
     #score = round(100 - ((float(score_total) / divide_by) / 5))
    #else:
      #score = 100

    ratio = divide_by / len(group)
    print("Number of Problem \nIMD frequencies: ============> " + str(divide_by) + "\n\n")
    print("Problem IMD freqs / Channels \nratio is: ===================> " + str(round(ratio, 1)) + "\n\n")
    
    if closest_imd == 0:
      score_alt = 0
    
    else:

      if divide_by != 0:
        score_alt =  100 - ((((float(score_total) /divide_by) ** .5) * 3) * .952)               
        score_alt = score_alt * (1 -(divide_by / 50))
        
        if len(group) == 6:
          
          score_alt_weighted = round(score_alt * 1.904762, 1)
          score_alt = round(score_alt, 1)
        
        elif len(group) == 5:
          
          compressor =  ((82.3 - score_alt) / 2.63) + score_alt
          score_alt_weighted = round((compressor + 17.7), 1) 
          score_alt = round(score_alt, 1)
        
        else: 
          score_alt = round(score_alt, 1)

      else:
        score_alt = 100

    print("Video Clarity Score: ========> {score}\n".format(score=score_alt))
    if score_alt_weighted != None:
      print("""
Weighted Video Clarity Score
(weighted relevant to {number}
channels): ==================> {score}
        """.format(score=score_alt_weighted, number=len(group)))

    #print("Video Clarity original style Score: {score}".format(score=score)) 
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

   
  def investigate(self, score_limit=70, usa_only=False):
    
    num_channels =  int(input("How many in channel group to investigate?"))
    if num_channels > 6 or num_channels < 3:
      return
    self.output = input("Filename to output data?")

    channels = []

    with open('vtx_channel_guide_abrv.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        channels.append(sliced_raw[0])

    good_groups = []   

    for i in range(len(channels)):
      channel_1 = channels[i]
      channels_2 = [channel for channel in channels if channel != channel_1] 
      #channels_2.remove(channel_1)
      

      for i in range(len(channels_2)):
        channel_2 = channels_2[i]
        channels_3 = [channel for channel in channels_2 if channel != channel_2]
        #channels_3 = channels_2
        #channels_3.remove(channel_2)
        print(channels_2)
        print(channels_3)

        for i in range(len(channels_3)):
          channel_3 = channels_3[i]
          
          if num_channels == 4:
            channels_4 = [channel for channel in channels_3 if channel != channel_3]
            
            for i in range(len(channels_4)):
              channel_4 = channels_4[i]
              
              if num_channels == 5:
                channels_5 = [channel for channel in channels_4 if channel != channel_4]
            
                for i in range(len(channels_5)):
                  channel_5 = channels_5[i]

                  if num_channels == 6:
                    channels_6 = [channel for channel in channels_5 if channel != channel_5]

                    for i in range(len(channels_6)):
                      channel_6 = channels_6[i]

                      self.group = [channel_1, channel_2, channel_3, channel_4, channel_5, channel_6]
                      converted = self.convert_freq_abbreviations()
                      print(self.group)
                      self.score(converted)
                      if self.scores[1] > score_limit:
                        sorted_group = sorted(self.group)
                        if sorted_group not in good_groups:
                          good_groups.append(sorted_group)
                          self.export()
                  
              
                  else:
                    self.group = [channel_1, channel_2, channel_3, channel_4, channel_5]
                    print(self.group)
                    converted = self.convert_freq_abbreviations()
                    self.score(converted)
                    if self.scores[1] > score_limit:
                      sorted_group = sorted(self.group)
                      if sorted_group not in good_groups:
                        good_groups.append(sorted_group)
                        self.export() 
         
              else:
                self.group = [channel_1, channel_2, channel_3, channel_4]
                print(self.group)
                converted = self.convert_freq_abbreviations()
                self.score(converted)
                if self.scores[0] > score_limit:
                  sorted_group = sorted(self.group)
                  if sorted_group not in good_groups:
                    good_groups.append(sorted_group)
                    self.export()


          else:
            self.group = [channel_1, channel_2, channel_3]
            print(self.group)
            converted = self.convert_freq_abbreviations()
            self.score(converted)
            if self.scores[0] > score_limit:
              sorted_group = sorted(self.group)
              if sorted_group not in good_groups:
                good_groups.append(sorted_group)
                self.export()
          




   

            















    