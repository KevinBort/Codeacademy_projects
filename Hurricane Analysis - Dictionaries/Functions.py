
# Converts the recorded data to float and maintains the not recorded.
# This function iterates over the elements of the input list and if the string is 'Damages not recorded, it will leave it unmodified,
# For the rest of the strings, it will check whether there is an M or B (million, billion) and it will update the conversion factor accordingly M=1000000 ; B=1000000000.
# Removing then, the corresponding letter so the conversion of the string stored in number, to float, can be done.
# Also, handles the exception of the '.' in the string and leaves it unchanged.


def conv(list):
    result=[]
    for string in list:
        number=''
        factor=1
        
        if string=='Damages not recorded':
            result.append(string) 
            continue
                #Handle the M or B conversion factors
        elif 'M' in string:
                factor=1000000 
                string=string.replace('M','') # Remove the M or B
        elif 'B' in string:
                factor=1000000000
                string=string.replace('B','')    
        for j in string:    
                #Get only the numeric part    
            if j.isnumeric() or j=='.' :
                number+=j
        if number: #Checks if it's not empty to avoid ValueError when trying to convert it to float.
            result.append(float(number)*factor) # Append the converted result to the list.
        else:
             result.append(string)
    return result

def dic_generator(names,month,year,max_wind,areas_afected,dmg,deaths):
     pass


def dic_names(names,months,years,max_sustained_winds,areas_affected,damages,deaths):
    dic={}
    for i in range(len(names)):
        dic[names[i]]={'name': names[i], 'month': months[i], 'year': years[i], 'max_sustained_winds': max_sustained_winds[i],'areas affected': areas_affected[i], 'damage': damages[i], 'deaths': deaths[i]}
    return dic

def dic_years(names,months,years,max_sustained_winds,areas_affected,damages,deaths):

# In this function the approach is different since the year  is not unique, meaning for a same year there can be more than 1 entry. 
# so te function checks whether the year is already in dic, and if so, it appends the new entry.
    dic={}
    for i in range(len(years)):
        year = years[i]
        entry = {
            'name': names[i],
            'month': months[i],
            'year': years[i],
            'max_sustained_winds': max_sustained_winds[i],
            'areas affected': areas_affected[i],
            'damage': damages[i],
            'deaths': deaths[i]
        }
        
        # If the year is already in the dictionary, append the new entry to the list
        if year in dic:
            dic[year].append(entry)
        else:
            dic[year] = [entry]  # Start a new list for the year
    
    return dic
    

# This function takes a list of lists and generates one single list with all the elements and then for each it will add it as a key 
# each value will be .count(x) for each iteration. 
def count_areas(areas_affected):

    dict={}
    new=[]
    for i in areas_affected:
        for x in i:
            new.append(x)
        for x in new:
            dict[x]=new.count(x)

    return dict

def most_affected_area(dict):
    max_so_far=0
    key=''
    for i in dict.values():
        if i>max_so_far:
            max_so_far=i
    for k,v in dict.items():
        print(k,v)
        if v==max_so_far:
            key=k


    return f'The most affected area is {key} and it was hit {max_so_far} times'

def deaths_max(names,deaths):
    deaths_by_hurricane={}
    max_so_far=0
    key=''
    for i,j in zip(names,deaths):
        deaths_by_hurricane[i]=j

    for i in deaths_by_hurricane.values():
        if i>max_so_far:
            max_so_far=i
    for k,v in deaths_by_hurricane.items():
        if v==max_so_far:
            key=k
    return(f'the most deaths is from {key} and number is {max_so_far}')

def mortality_rating():
    pass

from collections import defaultdict

def group_by_death (dic):

# First, define a dictionary with the requested structure. Given that the keys are known (since they're the 5 possible categories),
# now, check every entry from dic.values (all the hurricanes) and search within the 'death' key to sort them.
# mortality_scale = {0: 0,
#                    1: 100,
#                    2: 500,
#                    3: 1000,
#                    4: 10000}
    dic_deaths=defaultdict(list)

    for i in dic:
        cat=None
        deaths=i['deaths']
        if deaths>0 and deaths<=100:
            cat=1
        elif  deaths<=500:
            cat=2
        elif  deaths<=1000:
            cat=3
        elif  deaths<=10000:
            cat=4
        else:
            deaths>10000
            cat=5
        
    # Once categorized, append each dict into the list according to the 'cat' key.

        dic_deaths[cat].append(i)
    return dic_deaths

def group_by_death (dic):

# First, define a dictionary with the requested structure. Given that the keys are known (since they're the 5 possible categories),
# now, check every entry from dic.values (all the hurricanes) and search within the 'death' key to sort them.
# mortality_scale = {0: 0,
#                    1: 100,
#                    2: 500,
#                    3: 1000,
#                    4: 10000}
    dic_deaths=defaultdict(list)

    for i in dic:
        cat=None
        deaths=i['deaths']
        if deaths>0 and deaths<=100:
            cat=1
        elif  deaths<=500:
            cat=2
        elif  deaths<=1000:
            cat=3
        elif  deaths<=10000:
            cat=4
        else:
            deaths>10000
            cat=5
        
    # Once categorized, append each dict into the list according to the 'cat' key.

        dic_deaths[cat].append(i)
    return dic_deaths