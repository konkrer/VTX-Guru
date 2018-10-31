






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



  def get_input(self):
    
    if self.freq1 != None and self.freq2 != None:
      #group = [self.freq1, self.freq2, self.freq3, self.freq4, self.freq5, self.freq6]
      return self.group

    bands = ['a', 'b', 'c', 'e', 'f', 'r']
    channels = [str(x) for x in range(1,9)]

    print ("""
    


      ----------FPV VTX CHANNEL INTERFERENCE CHECKER-----------
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

  

  def check_freqz(self, freq_lst):
  
    group = [freq for freq in freq_lst if freq != None]
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



  def analyze_interference(self, freq_lst):
  
    bad_freq = self.check_freqz(freq_lst)
    group = [freq for freq in freq_lst if freq != None]
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
      print("\n\n\n\n 			  --ANALYSIS--\n\n 		All clear. Minimal interference.\n\n\n")

    elif bad_match + bad_close + close == 0:
      print("\n\n\n\n 			  --ANALYSIS--\n\n 	   	    Interference not too bad.\n 	  This is an excellent rating for 5 or 6 channels.\n\n\n")

    elif bad_match == 0 and bad_close == 0:
      print("\n\n\n\n 			  --ANALYSIS--\n\n 		Troubling interference possible.\n 		Good rating for 5 and 6 channels.\n\n\n")
    
    elif bad_match == 0 and bad_close > 0:
      print("\n\n\n\n 			  --ANALYSIS--\n\n 		     IMD problems likley!\n 	      IMD within 10MHz of at least one channel.\n\n\n")

    elif bad_match > 0:
      print("\n\n\n\n 			  --ANALYSIS--\n\n 	Bad channel grouping! Debilitating interference!\n\n\n")

  

  def convert_freq_abbreviations(self, freq_lst):
    
    converter = {}
    converted = []

    with open('vtx_channel_guide.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        dirty = sliced_raw[1]
        clean = dirty.strip('\n')
        converter[sliced_raw[0]] = clean
    for chan in freq_lst:
      if chan != None:
        if len(chan) == 2:
          value = converter[chan]
          converted.append(int(value))
        else:
        	converted.append(int(chan))

      else:
      	converted.append(chan)

    return converted



  def score(self, freq_lst):
    
    bad_freq = self.check_freqz(freq_lst)
    group = [freq for freq in freq_lst if freq != None]
    score_total = 0
    #print(bad_freq)
    divide_by = 0
    closest_imd = None

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

    #if divide_by != 0:
     #score = round(100 - ((float(score_total) / divide_by) / 5))
    #else:
      #score = 100

    score_alt_weighted = None
    
    if closest_imd == 0:
    	score_alt = 0
    
    else:
      if divide_by != 0:
        score_alt =  100 - ((((float(score_total) /divide_by) ** .5) * 3) * .952)               
        if len(group) == 6:
      	  score_alt_weighted = round(score_alt * 1.5242, 1)
      	  score_alt = round(score_alt, 1)
        elif len(group) == 5:
      	  score_alt_weighted = round(score_alt * 1.16686, 1) #
      	  score_alt = round(score_alt, 1)
        else:
      	  score_alt = round(score_alt, 1)
      else:
        score_alt = 100

    print("Video Clarity Score: =======> {score}\n".format(score=score_alt))
    if score_alt_weighted != None:
      print("""
Weighted Video Clarity Score
(weighted relevant to {number}
channels): =================> {score}
      	""".format(score=score_alt_weighted, number=len(group)))

    #print("Video Clarity original style Score: {score}".format(score=score)) 
    print("\nTop Possible Score is 100\n\n\n\n")
    print("num of sub 35's - " + str(divide_by))
    return score_alt



  def export(self):

    group = [freq for freq in self.group if freq != None]
    
    if self.output == None:
      
      output_file = input("Name of output_file?")
      with open(output_file, "a") as f:
        for chan in group:
          f.write(str(chan) +" ",)
        f.write("\n")

    



