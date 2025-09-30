
def distancetimecalculator():
    choice = ''
    while choice not in ('MPH', 'KMH'):
        choice = input('Do you want to input Miles per Hour (Type MPH) or KM per hour (KMH): ').upper()
        if choice not in ('MPH', 'KMH'):
            print("Please type 'MPH' or 'KMH'. Try again.")
    
    if choice == 'MPH':
        distance = float(input('Input the Distance (Miles): '))
        time = float(input('Input the Time (Hours): '))
        distanceovertime = (distance*1609.34)/(time*3600)
        print('You travelled at ' +str(distanceovertime) ,'Meters Per Second')
        tenkm = ((10000/distanceovertime))/60
        print('If you were to run a 10km Race, it would take you ' +str(tenkm) , 'minutes to run')
        fivekm = ((5000/distanceovertime))/60
        print('If you were to run a 5km Race, it would take you ' +str(fivekm) , 'minutes to run')
        
    elif choice == 'KMH':
        distance = float(input('Input the Distance (KM): '))
        time = float(input('Input the Time (Hours): '))
        distanceovertime = (distance*1000)/(time*3600)
        print('You travelled at ' +str(distanceovertime) ,'Meters Per Second')
        tenkm = ((10000/distanceovertime))/60
        print('If you were to run a 10km Race, it would take you ' +str(tenkm) , 'minutes to run')
        fivekm = ((5000/distanceovertime))/60
        print('If you were to run a 5km Race, it would take you ' +str(fivekm) , 'minutes to run')

    else:
        print('Error')

distancetimecalculator()
