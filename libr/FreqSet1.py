

"""
A class made to hold a frequency group of 5GHz FPV VTX channels,
then analyze and/or score for IMD interference level. 

Investigate method allows for scoring all possible combinations
of 40 VTX channels in study group.  Only passing scores are output
to file.  U.S. legal channels only option available; and selective removal of
channels allow for almost all possible subsets of the 40 channel set to 
be explored. (min 8 channel subset, i.e.one FPV VTX band)

"""



class FreqSet:
  
  def __init__(self, lst=[]):
    
    self.group = lst
    self.output = None
    self.scores = []





  def get_input(self, printz=True, channels=6, quit_on=2):
    
    self.group = []
    if printz:
      print ("""
    


=============================================================================
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/>IMD ACE<\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
=============================================================================


                               ~ VTX Guru ~
                               IMD Analyzer 

                   FPV VTX CHANNEL INTERFERENCE CHECKER


    
    Transmitting on two or more video channels can cause problems.
    Enter two to six channels to check for interference.
""")
    print("""    
    Enter Band Channel abbreviation or four digit frequency.
    -Bands: A - B - E - F - R(C)
    -Channels: 1-8
    
""")   

    
    for i in range(0, int(channels)):
      continue_on = self.ask_question(i, quit_on)
      if continue_on == False:
        print('\n\n')
        return
    print('\n\n')




  def ask_question(self, ques_num, quit_on):

    questions =[
      "\n-- Enter first VTX channel -OR-\n-- enter G to input entire group at once ==> ",
      "\n-- Enter second video channel => ",
      "\n-- Enter third video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter fourth video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter fifth video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter sixth video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter seventh video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter eighth video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter ninth video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter tenth video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 11th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 12th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 13th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 14th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 15th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 16th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 17th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 18th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 19th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter 20th video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter next video channel\n-- (Enter D if done) ==========> ",
      "\n-- Enter second video channel\n-- (Enter D if done) ==========> ",
      ] 

    bands = ['a', 'b', 'c', 'e', 'f', 'r']
    channels = [str(x) for x in range(1,9)]


    while True:

      if (ques_num == 1) and (quit_on == 1):
        answer = input(questions[-1]).lower().strip(' ')

      elif (ques_num > 19):
        answer = input(questions[-2]).lower().strip(' ')
      else:
        answer = input(questions[ques_num]).lower().strip(' ')
      
      if ques_num == 0:
        if answer == 'g':
          while True:
            string_group = input('\n-- Enter channel group ======> ').lower()
            input_group_init = string_group.split(' ')
            input_group = [x for x in input_group_init if x != '']

            if len(input_group) < 2 or len(input_group) > 32:
              print('\n-----Try again.-----')
              continue

            ok = True
            for chan in input_group:
              if not self.check_channel_input(chan, bands, channels):
                ok = False
                break
            if not ok:
              continue

            self.group = input_group
            return False


      if ques_num >= int(quit_on):
        if answer == 'd':        
          return False

      if self.check_channel_input(answer, bands, channels):
        self.group.append(answer)
        return True






  def check_channel_input(self, chan_input, bands, channels):
    

    try:
        
      if (chan_input[0] in bands and chan_input[1] in channels)\
      and len(chan_input) == 2:
          
        return True


      elif (int(chan_input) <= 5945 and int(chan_input) >= 5645):
          
        return True
         
      else:
        print("\n-----Try Again.-----\n")
        return False


    except (ValueError, IndexError):
      print("\n-----Try Again.-----\n")
      return False






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
    
    print('          --------------------------------------------------')
    print('                | IMD close to VTX channel instances |') 

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
    if (close == 0) and (bad_close ==  0) and (near == 0) and (bad_match) == 0:
     print('                            --- NONE ---')  
    print('          --------------------------------------------------\n\n\n')


    if bad_match + bad_close + close + near == 0:
      print("                   -------ANALYSIS-------\n\n 	    All clear. Minimal IMD interference.")

    
    elif bad_match + bad_close + close == 0:
      
      print("                  -------ANALYSIS-------\n\n 	   	IMD interference not too bad.\n")
      
      if len(group) >= 5:
        print(" 	This is an excellent IMD rating for 5 or 6 channels.")
    

    elif bad_match == 0 and bad_close == 0:
      print("                  -------ANALYSIS-------\n\n 	      Troubling interference possible.\n")
      
      if len(group) >= 5:
        print(" 	     Good IMD rating for 5 and 6 channels.")
      

    elif bad_match == 0 and bad_close > 0:
      print("                   -------ANALYSIS-------\n\n 		     IMD problems likely!\n 	   IMD within 10MHz of at least one channel.")

    
    elif bad_match > 0:
      print(" 			 -------ANALYSIS-------\n\n 	  Bad channel grouping! Debilitating interference!")
    
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
        
      if len(str(chan)) == 2:
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
          
      if len(str(chan)) == 4:
        if str(chan) in converter.keys():
          value = converter[str(chan)]
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
      
      if closest_broadcast == None:
        closest_broadcast = seperation

      else:
        if seperation < closest_broadcast:
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
      print(" Number of Problem \n IMD frequencies: ============> " + str(divide_by) + "\n\n")
      print(" Times problem IMD freq \n is close to VTX channel: ====> " + str(IMD_close_to_chan) + "\n\n")
      print(" Problem IMD close / Channels \n ratio is: ===================> " + str(round(ratio, 1)) + "\n\n")
      print(" Minimum Problem IMD\n frequency seperation\n to VTX channel: =============> " + str(closest_imd) + " MHz\n (*within 35Mhz)\n\n")

    
    if closest_imd == 0:
      score_alt = 0
      if printz:
        if closest_broadcast <= 27:
          print(" *****VTX channels too close!!! %s MHz apart.*****\n\n" % (closest_broadcast))
        else:
          print(" Minimum VTX\n channel separation  =========> %sMHz\n\n" % (closest_broadcast))
    
    elif closest_broadcast <= 27:
      score_alt = 0
      if printz:
        print(" *****VTX channels too close!!! %s MHz apart.*****\n\n" % (closest_broadcast)) 
    
    else:

      if closest_broadcast < 40:
           
        if closest_broadcast < 35:
          if printz:
             print(" ***VTX channels close! %s MHz apart.***\n\n" % (closest_broadcast))

        else:
          if printz:
            print(" Minimum VTX\n channel separation  =========> %sMHz\n(Channels getting close!)\n\n" % (closest_broadcast))
            
        broad_score = (40 - closest_broadcast)
        
        if closest_broadcast < 37:
          broadcast_factor = (1 - (broad_score / (26 - broad_score))) * (1/broadcast_close_times)
        
        else:
          broadcast_factor = (1 - (broad_score / (26 - broad_score)))


      if divide_by != 0:

        score_alt =  100 - ((((float(score_total) /divide_by) ** .5) * 3) * .952)               
        score_alt = score_alt * (1 - (IMD_close_to_chan / 30))  # to reduce proportional to close IMD channels
        
          
        if broadcast_factor:   
          score_alt = score_alt * broadcast_factor  # to reduce proportional to close broadcast channels         
          
        else:
          if printz:
            print(" Minimum VTX\n channel separation  =========> %sMHz\n\n" % (closest_broadcast))
        
        
        if len(group) == 6:
          
          score_alt_weighted = round(score_alt * 2.204, 1)  # old factor 1.966
          
        
        elif len(group) == 5:
          
          compressor =  ((80.0053 - score_alt) / 6.1) + score_alt
          score_alt_weighted = round((compressor + 20), 1) 
          

      else:
        if broadcast_factor == None:
          score_alt = 100.0
          if printz:
            print(" Minimum VTX\n channel separation  =========> %sMHz\n\n" % (closest_broadcast))
        
        else:
          score_alt = 100.0 * broadcast_factor



    if printz:
      print(" Video Clarity Score: ========> {:.2f}\n".format(round(score_alt, 2)))
      if score_alt_weighted:
        print("""
 Weighted Video Clarity Score
 (weighted relevant to {number}
 channels): ==================> {score}
        """.format(number=len(group), score=score_alt_weighted))
 
      print("\n Top Possible Score is 100\n\n\n\n\n\n\n")
    
    self.scores = [score_alt, score_alt_weighted, closest_broadcast]






  def export(self, converted):
    
    if self.output == None:
      
      abbreviations = self.convert_to_abbreviations()
      output_file = input("-- Name of output_file?")

      with open(output_file, "a") as f:
        f.write("%s  %s  %s   " % (round(self.scores[0], 2), self.scores[1], self.scores[2]))
        for chan in abbreviations:
          f.write(str(chan) +" ")
        f.write('-- ')
        for freq in converted:
          f.write(str(freq) + " ",)
        f.write('-- ')
        converted.sort()
        for freq in converted:
          f.write(str(freq) + " ",) 
        f.write("\n")

    else:

      with open(self.output, "a") as f:
        f.write("%.2f  %s  %s   " % (round(self.scores[0], 2), self.scores[1], self.scores[2]))
        for chan in self.group:
          f.write(str(chan) + " ",)
        f.write('-- ')
        for freq in converted:
          f.write(str(freq) + " ",)
        f.write('-- ')
        converted.sort()
        for freq in converted:
          f.write(str(freq) + " ",)
        f.write("\n")
 






  def investigate(self, score_limit=60):

    extra_remove = False
    print("""



===========================================================================      
??????????????????????????????????i????????????????????????????????????????      
===========================================================================

                             iNVESTIGATE





** NOTE: Channels R7 and F8 are both the same frequency - 5880 MHz.
         The output only shows 'R7' when referring to 5880 MHz.


         """)
    while True:
      num_channels_raw =  input("\n\n-- How many in channel group\n-- to investigate? (3-6) =======> ")
      num_channels = num_channels_raw.strip(' ')
      
      if (num_channels == '3') or (num_channels == '4')\
         or (num_channels == '5') or (num_channels == '6')\
         or (num_channels == '7'):
        
        if (num_channels == '7'):
          print("\n\n\n**** YOU SELCETED 7 ......SNEAKY!!! GET READY TO WAIT FOR COMPLETION!\n**** CTRL C to force quit program.")  
          print("**** SCORE LIMIT FOR CHANNEL GROUPS LOWERED TO 8.")
          score_limit = 8
          break
          
        else:
          break
      else:
        print("\n\n---- Try Again ----\n\n")
    
    while True:
      usa_only_raw = input("\n\n--USA only? (Enter Y or N) =====> ").lower()
      usa_only = usa_only_raw.strip(' ')
      if usa_only == 'y':
        print('\n\n** USA VTX CHANNELS ONLY CONFIRMED **\n\n')
        usa_only = True
        break
      if usa_only == 'n':
        print('\n\n---- 40 VTX CHANNELS CONFIRMED ----\n\n')
        usa_only = False
        break
      else:
        print("\n\n---- Try Again ----\n\n")
      

    if not usa_only:
      while True:
        extra_remove_raw = input("""
-- Would you like to remove any frequencies from the 40 VTX channel set? --

-- Enter Y for Yes or N for No =======> """).lower()
        extra_remove = extra_remove_raw.strip(' ')
        if (extra_remove == 'y'):
          extra_remove = True
          break
        if (extra_remove == 'n'):
          extra_remove = False
          break
        else:
          print("\n\n---- Try Again ----\n\n")
    
    if extra_remove:
      to_remove = FreqSet()
      to_remove.get_input(False, 32, 1)
      new_list =[]
      
      
      if 'f8' in to_remove.group:
        f8_idx = to_remove.group.index('f8')
        to_remove.group[f8_idx] = 'r7'

      for chan in to_remove.group:
        if (chan not in new_list):
          new_list.append(chan)
      to_remove.group = new_list
      

    self.output = input("-- Filename to output data?\n\n-- (E.g. something.txt): ")

    
    channels = []

    with open('libr/vtx_channel_guide_abrv.txt', 'r') as f:
      for line in f:

        sliced_raw = line.split(', ')
        channels.append(sliced_raw[0])

    if usa_only:
      channels.remove('e4')
      channels.remove('e7')
      channels.remove('e8') 

    else:
      if extra_remove:
        for chan in to_remove.group:
          try:
            channels.remove(chan)
          except ValueError:
            pass
        print("\n\n\n** Channels that were removed\n   from study set ============> ", end=' ')
        for chan in to_remove.group:
          print(chan, end=' ')
        print("\n")

    print("\n")
    gen = combo_explor(channels, int(num_channels))

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

      if int(num_channels) in [5,6]:
        if self.scores[1] != None:
          if self.scores[1] >= score_limit:
            self.export(converted)

      else:
        if self.scores[0] >= score_limit:
          self.export(converted)
      
      coutner+=1

    print("\n\n-- %s Combinations checked!" % (coutner))

    
    
    


   

def combo_explor(lst, combo_of, first_loop=True):

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
        if first_loop:
          print("-- WORKING.....")
        if i == 0:
          first_count += 1

        if first_count ==2:
          yield (None)

        option = end_shortened[i]

        rest = combo_explor(lst[i+1:], combo_of-1, False)

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



