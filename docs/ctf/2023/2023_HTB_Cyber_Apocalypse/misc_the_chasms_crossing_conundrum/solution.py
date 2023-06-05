people_time  = '''Person 1 will take 54 minutes to cross the bridge.
Person 2 will take 53 minutes to cross the bridge.
Person 3 will take 9 minutes to cross the bridge.
Person 4 will take 17 minutes to cross the bridge.
Person 5 will take 81 minutes to cross the bridge.
Person 6 will take 8 minutes to cross the bridge.
Person 7 will take 71 minutes to cross the bridge.
Person 8 will take 55 minutes to cross the bridge.'''
max_time = '''The flashlight has charge for 276 minutes. 🔦'''

'''
RULES:
☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ 
☠                                                                             ☠
☠  [*] The path ahead is treacherous.                                         ☠
☠  [*] You have to find a viable strategy to get everyone across safely.      ☠
☠  [*] The bridge can hold a maximum of two persons.                          ☠
☠  [*] The chasm lurks on either side of the bridge waiting for those         ☠
☠      who think they can get across in total darkness.                       ☠
☠  [*] If two persons get across, one must come back with the flashlight.     ☠
☠  [*] The flashlight has energy only for a limited amount of time.           ☠
☠  [*] The time required for two persons to cross, is dictated by the slower. ☠
☠  [*] The answer must be given in crossing and returning pairs. For example, ☠
☠      [1,2],[2],... . This means that persons 1 and 2 cross and 2 gets back  ☠
☠       with the flashlight so others can cross.                              ☠
☠                                                                             ☠
☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ 
'''

# SETUP - DO NOT CHANGE
pl = [x.split(" ")[4] for x in people_time.split("\n")]
p1,p2,p3,p4,p5,p6,p7,p8 = people_time[0],people_time[1],people_time[2],people_time[3],people_time[4],people_time[5],people_time[6],people_time[7]

tl = [x.split(" ")[5] for x in max_time.split("\n")]
max_time = tl[0]

p = [p1,p2,p3,p4,p5,p6,p7,p8]
# ---- SETUP END ---- #

p_dict = dict()
for x,time in enumerate(p):
    p_dict[x+1] = time
    
sorted_p_dict = {k: v for k, v in sorted(p_dict.items(), key=lambda item: item[1])}

print(sorted_p_dict)

crossed = list()
not_crossed = list(sorted_p_dict.keys())

total_time = 0
max_persons = len(not_crossed)

if True:
    # Cross with fastest and next-fastest
    a = 1

first,second = not_crossed[0],not_crossed[1]

crossing_order = []
while len(crossed) != max_persons:
    if len(not_crossed) == 1:
        crosser = not_crossed.pop(0)
        crossed.append(crosser)
        total_time += p_dict[crosser]
        break
    elif len(not_crossed) == 0:
        break
        
    escort = not_crossed.pop(0)
    escort_time = p_dict[escort]
    crosser = not_crossed.pop(0)
    crosser_time = p_dict[crosser]
    
    crossing_order.append([escort,crosser])
    
    crossed = [first,second] + crossed

    total_time += max([escort_time,crosser_time])
    print("Current time: {}\nNot Crossed: {}\nCrossed: {}\n".format(total_time,not_crossed,crossed))
    
    if total_time >= max_time:
        print("Time fail.  {}".format(total_time))
        #quit()
        
    if len(not_crossed) == 1:
        crosser = not_crossed.pop(0)
        crossed.append(crosser)
        total_time += p_dict[crosser]
        break
    elif len(not_crossed) == 0:
        break
        
    # Fastest crosses back
    escort = crossed.pop(0)
    not_crossed = [escort] + not_crossed
    total_time += escort_time
    
    crossing_order.append([escort])
    
    print("Current time: {}\nNot Crossed: {}\nCrossed: {}\n".format(total_time,not_crossed,crossed))
    
    if total_time >= max_time:
        print("Time fail.  {}".format(total_time))
        #quit()
        
    if len(not_crossed) == 1:
        crosser = not_crossed.pop(0)
        crossed.append(crosser)
        total_time += p_dict[crosser]
        break
    elif len(not_crossed) == 0:
        break
        
    escort = not_crossed.pop()
    escort_time = p_dict[escort]
    crosser = not_crossed.pop()
    crosser_time = p_dict[crosser]
    
    crossing_order.append([escort,crosser])
    
    crossed.append(escort)
    crossed.append(crosser)
    
    total_time += max([escort_time,crosser_time])
    print("Current time: {}\nNot Crossed: {}\nCrossed: {}\n".format(total_time,not_crossed,crossed))
    
    if total_time >= max_time:
        print("Time fail.  {}".format(total_time))
        #quit()
        
    if len(not_crossed) == 1:
        crosser = not_crossed.pop(0)
        crossed.append(crosser)
        total_time += p_dict[crosser]
        break
    elif len(not_crossed) == 0:
        break
        
    # Second-fastest crosses back
    escort = crossed.pop(0)
    
    not_crossed = [first,second] + not_crossed[1:]
    total_time += escort_time
    
    crossing_order.append([escort])
    
    print("Current time: {}\nNot Crossed: {}\nCrossed: {}\n".format(total_time,not_crossed,crossed))
    
    if total_time >= max_time:
        print("Time fail.  {}".format(total_time))
        #quit()

    if len(not_crossed) == 1:
        crosser = not_crossed.pop(0)
        crossed.append(crosser)
        total_time += p_dict[crosser]
        break
    elif len(not_crossed) == 0:
        break

if total_time > max_time:
    print("Fail.  Time: {}\nOrder: {}".format(total_time,crossing_order))
else:
    print("Success!  Time: {}\nOrder: {}".format(total_time,crossing_order))