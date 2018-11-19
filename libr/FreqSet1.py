

"""
A class made to hold a frequency group of 5GHz FPV VTX channels,
then analyze and/or score for IMD interference level.

Investigate method allows for investigating all possible combinations
of channels in study group. Currently, only worldwide(40 chan) and USA only(37 chan)
study groups available to chose. 

"""



class FreqSet:
  
  def __init__(self, lst=[None, None, None, None, None, None]):
    
    self.group = lst
    self.output = None
    self.scores = []




  def get_input(self):
    

    print ("""
    
==========================================================================
==========================================================================

                          ~ VTX Guru ~ 

                FPV VTX CHANNEL INTERFERENCE CHECKER
                          (IMD Analyzer)

    
    Transmitting on two or more video channels can cause problems.
    Enter two to six channels to check for interference.


    Enter Band Channel abbreviation or four digit frequency.
    -Bands: A - B - E - F - R(C)
    -Channels: 1-8
    
    """)
    
    bands = ['a', 'b', 'c', 'e', 'f', 'r']
    channels = [str(x) for x in range(1,9)]


                                        #first channel

    while True:
      
      self.group[0] = input("\nEnter first video channel ==> ").lower()
      
      try:
        
        if (self.group[0][0] in bands and self.group[0][1] in channels)\
        and len(self.group[0]) == 2:
          
          break


        elif (int(self.group[0]) <= 5945 and int(self.group[0]) >= 5645):
          
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")

    
                                         #second channel


    while True:
      
      self.group[1] = input("\nEnter second video channel => ").lower()
      
      try:
        
        if (self.group[1][0] in bands and self.group[1][1] in channels)\
        and len(self.group[1]) == 2:
          
          break


        elif (int(self.group[1]) <= 5945 and int(self.group[1]) >= 5645):
          
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


                                        #third channel


    while True:
      
      self.group[2] = input("\nEnter third video channel\n(Enter D if done) ==========> ").lower()
      
      try:
        
        if (self.group[2][0] in bands and self.group[2][1] in channels)\
        and len(self.group[2]) == 2:
          
          break

        elif self.group[2] == 'd':
          print("\n\n")
          self.group[2] = None
          break

        elif (int(self.group[2]) <= 5945 and int(self.group[2]) >= 5645):
          
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


                                         #fourth channel


    while True:
      
      if self.group[2] == None:
      	break

      self.group[3] = input("\nEnter fourth video channel\n(Enter D if done) ==========> ").lower()
      
      try:
        
        if (self.group[3][0] in bands and self.group[3][1] in channels)\
        and len(self.group[3]) == 2:
          
          break

        elif self.group[3] == 'd':
          self.group[3] = None
          print("\n\n")
          break

        elif (int(self.group[3]) <= 5945 and int(self.group[3]) >= 5645):
          
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


                                        #fifth channel


    while True:

      if self.group[3] == None:
      	break

      self.group[4] = input("\nEnter fifth video channel\n(Enter D if done) ==========> ").lower()
      
      try:
        
        if (self.group[4][0] in bands and self.group[4][1] in channels)\
        and len(self.group[4]) == 2:
          
          break

        elif self.group[4] == 'd':
          self.group[4] = None
          print("\n\n")
          break

        elif (int(self.group[4]) <= 5945 and int(self.group[4]) >= 5645):
          
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")

                                     #sixth channel


    while True:
      
      if self.group[4] == None:
      	break

      self.group[5] = input("\nEnter sixth video channel\n(Enter D if done) ==========> ").lower()
      
      try:
        
        if (self.group[5][0] in bands and self.group[5][1] in channels)\
        and len(self.group[5]) == 2:
          
          break

        elif self.group[5] == 'd':
          self.group[5] = None
          print("\n\n")
          break

        elif (int(self.group[5]) <= 5945 and int(self.group[5]) >= 5645):
          
          break
         
        else:
        	print("\nTry Again.\n")

      except (ValueError, IndexError):
      	print("\nTry Again.\n")


    return self.group

  






  def check_freqz(self, group):
  
    freq_bad = []
  
    for i in range(len(group)):
      
      rest = group[:i] + group[i + 1:]
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
    
    print('\n\n\n')
    print('           --------------------------------------------------')
    print('                 | IMD close to VTX channel instances |') 

    for i in range(len(group)):
      for sublst in bad_freq:
      

        if int(group[i]) not in sublst:
      
          for x in sublst:
            diff = abs(x - int(group[i]))
            if diff <20 and diff >= 10:
              print("\nWarning: IMD on %s is quite close to %s (%s MHz)" % (x, group[i], diff))
              close += 1

            elif diff < 10:
              print("\nWarning: IMD on %s is very close to %s (%s MHz)" % (x, group[i], diff))
              bad_close += 1

            elif  diff < 35:
              print("\nIMD on %s is close to %s (%s MHz)" % (x, group[i], diff))
              near += 1 

        elif int(group[i]) in sublst:
          print("\n**Warning %s will have terrible interference! IMD exact match to VTX channel!**" % (group[i]))
          bad_match += 1
      
    print('\n           --------------------------------------------------')


    if bad_match + bad_close + close + near == 0:
      print("\n\n\n\n\n                   -------ANALYSIS-------\n\n 	    All clear. Minimal IMD interference.")

    
    elif bad_match + bad_close + close == 0:
      
      print("\n\n\n\n\n                  -------ANALYSIS-------\n\n 	   	IMD interference not too bad.\n")
      
      if len(group) >= 5:
        print(" 	This is an excellent IMD rating for 5 or 6 channels.")
    

    elif bad_match == 0 and bad_close == 0:
      print("\n\n\n\n\n                  -------ANALYSIS-------\n\n 	      Troubling interference possible.\n")
      
      if len(group) >= 5:
        print(" 	     Good IMD rating for 5 and 6 channels.")
      

    elif bad_match == 0 and bad_close > 0:
      print("\n\n\n\n\n                   -------ANALYSIS-------\n\n 		     IMD problems likley!\n 	   IMD within 10MHz of at least one channel.")

    
    elif bad_match > 0:
      print("\n\n\n\n\n 			 -------ANALYSIS-------\n\n 	  Bad channel grouping! Debilitating interference!")
    
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

    with open('libr/vtx_channel_guide.txt', 'r') as f:
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

    with open('libr/vtx_channel_guide_abrv.txt', 'r') as f:
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






  def score(self, group, printz=True):
    
    bad_freq = self.check_freqz(group)
    score_total = 0
    divide_by = 0
    IMD_close_to_chan = 0
    broadcast_close_times = 0
    closest_imd = None
    closest_broadcast = None
    broadcast_factor = None
    score_alt = None
    score_alt_weighted = None

    

    sorted_group = sorted(group, reverse=True)
    for i in range(len(sorted_group) - 1):
      seperation = sorted_group[i] - sorted_group[i+1]
      if closest_broadcast:
        if seperation < closest_broadcast:
          closest_broadcast = seperation
      else:
        closest_broadcast = seperation

      if seperation < 40:
        broadcast_close_times += 1
        



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

    if printz:
      print("Number of Problem \nIMD frequencies: ============> " + str(divide_by) + "\n\n")
      print("Times problem IMD freq \nis close to VTX channel: ====> " + str(IMD_close_to_chan) + "\n\n")
      print("Problem IMD close / Channels \nratio is: ===================> " + str(round(ratio, 1)) + "\n\n")
      print("Minimum Problem IMD\nfrequency seperation\nto VTX channel: =============> " + str(closest_imd) + " MHz\n(*within 35Mhz)\n\n")

    
    if closest_imd == 0:
      score_alt = 0
      if printz:
        print("Minimum VTX\nchannel seperation  =========> %sMHz\n\n" % (closest_broadcast))
    
    if closest_broadcast <= 27:
      score_alt = 0
      if printz:
        print("*****VTX channels too close!!! %s MHz apart.*****\n\n" % (closest_broadcast)) 
    
    else:

      if closest_broadcast < 40:
           
        if closest_broadcast < 35:
          if printz:
             print("***VTX channels close! %s MHz apart.***\n\n" % (closest_broadcast))

        else:
          if printz:
            print("Minimum VTX\nChannel seperation  =========> %sMHz\n(Channels getting close!)\n\n" % (closest_broadcast))
            
        broad_score = (40 - closest_broadcast)
        
        if closest_broadcast < 37:
          broadcast_factor = (1 - (broad_score / (26 - broad_score))) * (1/broadcast_close_times)
        
        else:
          broadcast_factor = (1 - (broad_score / (26 - broad_score)))


      if divide_by != 0:

        score_alt =  100 - ((((float(score_total) /divide_by) ** .5) * 3) * .952)               
        score_alt = score_alt * (1 -(IMD_close_to_chan / 30))  # to reduce proportinal to close IMD channels
        
          
        if broadcast_factor:   
          score_alt = score_alt * broadcast_factor  # to reduce proportinal to close broadcast channels         

        else:
          if printz:
            print("Minimum VTX\nchannel seperation  =========> %sMHz\n\n" % (closest_broadcast))
        
        
        if len(group) == 6:
          
          score_alt_weighted = round(score_alt * 2.204, 1)  # old factor 1.966
          
        
        elif len(group) == 5:
          
          compressor =  ((80.0053 - score_alt) / 6.1) + score_alt
          score_alt_weighted = round((compressor + 20), 1) 
          

      else:
        if broadcast_factor == None:
          score_alt = 100.0
          if printz:
            print("Minimum VTX\nchannel seperation  =========> %sMHz\n\n" % (closest_broadcast))
        
        else:
          score_alt = 100.0 * broadcast_factor

        





    if printz:
      print("Video Clarity Score: ========> {:.2f}\n".format(round(score_alt, 2)))
      if score_alt_weighted:
        print("""
Weighted Video Clarity Score
(weighted relevant to {number}
channels): ==================> {score}
        """.format(number=len(group), score=score_alt_weighted))
 
      print("\nTop Possible Score is 100\n\n\n\n\n\n\n")
    
    self.scores = [score_alt, score_alt_weighted, closest_broadcast]









  def export(self):

    group = [freq for freq in self.group if freq != None]
    
    if self.output == None:
      
      output_file = input("Name of output_file?")
      with open(output_file, "a") as f:
        f.write("%s  %s  %s   " % (round(self.scores[0], 2), self.scores[1]), self.scores[2])
        for chan in group:
          f.write(str(chan) +" ")
        f.write("\n")

    else:
      
      with open(self.output, "a") as f:
        f.write("%.2f  %s  %s   " % (round(self.scores[0], 2), self.scores[1], self.scores[2]))
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

    with open('libr/vtx_channel_guide_abrv.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        channels.append(sliced_raw[0])

    if usa_only:
      channels.remove('e4')
      channels.remove('e7')
      channels.remove('e8')

    gen = combo_explor(channels, num_channels)

    coutner = 0

    while True:
      
      out = next(gen)

      if out == None:
        break

      flat = flatten(out)
      self.group = flat
      #print(self.group)

      converted = self.convert_freq_abbreviations()
      self.score(converted, False)

      if num_channels > 4:
        if self.scores[1] != None:
          if self.scores[1] >= score_limit:
            self.export()

      else:
        if self.scores[0] >= score_limit:
          self.export()
      
      coutner+=1

    print("%s combinations checked!" % (coutner))

    
    
    


   

def combo_explor(lst, combo_of):

  first_count = 0

  if combo_of == 1:
    
    while True:

      for i in range(len(lst)):

        if i == 0:
          first_count += 1

        if first_count ==2:
          yield (None)

        yield (lst[i])

  else:

    end_shortened = lst[:-(combo_of-1)]

    while True:

      for i in range(len(end_shortened)):

        if i == 0:
          first_count += 1

        if first_count ==2:
          yield (None)

        option = end_shortened[i]

        rest = combo_explor(lst[i+1:], combo_of-1)

        while True:

          nxt = next(rest)           
          if nxt == None:
            break                           

          yield option, nxt





def flatten(tup):

  if tup == None:
    return None

  flat_list = []

  if not isinstance(tup[1], tuple):
    flat_list = [tup[0], tup[1]]
    return flat_list

  else:

    x = tup[0]
    flat_list.append(x)
    y = tup[1]
    z = flatten(y)

    flat_list += z

    return flat_list





   

'''
l = len(channels)
    
    base_case = factorial(l, num_channels) / factorial(num_channels)


    channel_1_used = []
    combo_count = 0

    while True:
      for i in range(len(channels)):
        
        channel_1 = channels[i]
        channel_1_used.append(channel_1)
        channels_2 = [channel for channel in channels if channel not in channel_1_used] 
        
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
        

        for i in range(len(channels_2_redux)):
          channel_2 = channels_2_redux[i]
          channel_2_used.append(channel_2)
          
          channels_3 = [channel for channel in channels_2 if channel not in channel_2_used]
          
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
                            self.export()

                        combo_count += 1
                        if combo_count == (int(base_case)):
                          return
                  
              
                    else:

                      self.group = [channel_1, channel_2, channel_3, channel_4, channel_5]
                      print(self.group)
                      converted = self.convert_freq_abbreviations()
                      self.score(converted)
                      if self.scores[1] != None:
                        if self.scores[1] >= score_limit: 
                          self.export()

                      combo_count += 1
                      if combo_count == (int(base_case)):
                        return 
         
                else:

                  self.group = [channel_1, channel_2, channel_3, channel_4]
                  print(self.group)
                  converted = self.convert_freq_abbreviations()
                  self.score(converted)
                  if self.scores[0] >= score_limit:
                    self.export()

                  combo_count += 1
                  if combo_count == (int(base_case)):
                    return


            else:

              self.group = [channel_1, channel_2, channel_3]
              print(self.group)
              converted = self.convert_freq_abbreviations()
              self.score(converted)
              if self.scores[0] >= score_limit:
                self.export()  

              combo_count += 1
              if combo_count == (int(base_case)):
                return
              
            
          
def factorial(n, limit=None):

  
  if limit != None:
    if limit == 1:
      return n

  if n == 1:
    return n
  
  else:
    
    if limit != None:
      return n * factorial(n-1, limit-1)
    
    else:
      return n * factorial(n-1)
'''      






'''
    for i in range(len(group)):
      
      bct = 0
      other_chans = [freq for freq in group if freq != group[i]]
      
      for chan in other_chans:

        diff2 = abs(chan - int(group[i]))
        if diff2 < 40:
            bct += 1

        if closest_broadcast == None:
          closest_broadcast = diff2

        else:
          if diff2 < closest_broadcast:
              closest_broadcast = diff2
      
      if btc > 0:
        if broadcast_close_times == 0:
          broadcast_close_times = bct

        else:
          if btc > broadcast_close_times:
            broadcast_close_times = bct

'''    




    