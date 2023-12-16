def add_time(start, duration):
    pm = False
    am = False
    morning = start.split()[-1]
    if morning == 'AM':
        am = True
    else:
        pm = True
    
    minutes =  int(duration.split(':')[-1])
    hours = int(duration.split(':')[0])
    
    start2 = start.replace(' ' , ':')
    minutes_start = int(start2.split(':')[1])
    hours_start = int(start2.split(':')[0])
    
    #sommo i minuti e aggiungo 1 ora se oltre 59' oppure restituisco la str della somma
    if minutes_start + minutes > 59:
        hours_start +=1
        minutes_start = '00'
    else:
        minutes_start = str(minutes_start + minutes)
    
    #sommo le ore
    days = hours / 12
    hour_extra = hours % 12
    
    total_hours = hours_start + hour_extra
    if total_hours == 12:
        
    
    
    
    new_time = []

    return new_time
    
#print(add_time("11:06 PM", "2:02"))