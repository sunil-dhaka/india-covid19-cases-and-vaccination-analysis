#!/usr/bin/env python
# coding: utf-8

# #### Import modules

# In[1]:


import json # we will be needing json module
import pandas as pd
import numpy as np


# #### Load given json file

# In[2]:


# how do you open an json file
# opening json file
f=open("neighbor-districts.json")

# json.load() returns json object as dictionary
data_dict=json.load(f)

# list of districts - sample entry: churu/Q1090006
district_id_list=[] # it is an empty list
for i in data_dict:
    district_id_list.append(i)
district_id_list=np.array(district_id_list) # store list into numpy array

# sort districts alphabatically
district_id_list.sort()

# district names - sample entry: churu
district_names_from_json=[] 

# district ids - sample entry: Q1090006
district_ids_from_json=[]

#use split() function and specify the separator '/' . Remember default seperator is whitspace
for i in range(len(district_id_list)):
    district_names_from_json.append(district_id_list[i].split("/")[0])
    district_ids_from_json.append(district_id_list[i].split("/")[1])


# #### Manual name modification of around $25$ districts 

# - [x] Also removing '_' seprater and replace it with ' '(whitespace)
# - [x] Remove '_distrcit' type discrepencies from the end of district names

# In[3]:


# modified list of district names - 
district_names_from_json_modified=[]

for i in range(len(district_names_from_json)):
    # discrepencies are taken from internet manually and sources
    # districts that are being avoided [from json]
    if district_names_from_json[i] == 'jyotiba_phule_nagar':
        district_names_from_json_modified.append('amroha')
    elif district_names_from_json[i] == 'sant_ravidas_nagar':
        district_names_from_json_modified.append('bhadohi')
    elif district_names_from_json[i] == 'bijapur_district':
        district_names_from_json_modified.append('vijayapura')
    elif district_names_from_json[i] == 'hugli':
        district_names_from_json_modified.append('hooghly')
    elif district_names_from_json[i] == 'sri_ganganagar':
        district_names_from_json_modified.append('ganganagar')
    elif district_names_from_json[i] == 'the_dangs':
        district_names_from_json_modified.append('dang')
    elif district_names_from_json[i] == 'kheri':
        district_names_from_json_modified.append('lakhimpur kheri')
    elif district_names_from_json[i] == 'palghat':
        district_names_from_json_modified.append('palakkad')
    elif district_names_from_json[i] == 'faizabad':
        district_names_from_json_modified.append('ayodhya')
    elif district_names_from_json[i] == 'baleshwar':
        district_names_from_json_modified.append('balasore')
    elif district_names_from_json[i] == 'ysr':
        district_names_from_json_modified.append('y.s.r. kadapa')
    elif district_names_from_json[i] == 'purbi_singhbhum':
        district_names_from_json_modified.append('east singhbhum')
    elif district_names_from_json[i] == 'pashchimi_singhbhum':
        district_names_from_json_modified.append('west singhbhum')
    elif district_names_from_json[i] == 'purba_champaran':
        district_names_from_json_modified.append('east champaran')
    elif district_names_from_json[i] == 'pashchim_champaran':
        district_names_from_json_modified.append('west champaran')
    elif district_names_from_json[i] == 'sri_potti_sriramulu_nellore':
        district_names_from_json_modified.append('s.p.s. nellore')
    elif district_names_from_json[i] == 'muktsar':
        district_names_from_json_modified.append('sri muktsar sahib')
    elif district_names_from_json[i] == 'dantewada':
        district_names_from_json_modified.append('dakshin bastar dantewada')
    elif district_names_from_json[i] == 'kochbihar':
        district_names_from_json_modified.append('cooch behar')
    elif district_names_from_json[i] == 'tirunelveli_kattabo':
        district_names_from_json_modified.append('tirunelveli')
    elif district_names_from_json[i] == 'kaimur_(bhabua)':
        district_names_from_json_modified.append('kaimur')
    elif district_names_from_json[i] == 'tirunelveli_kattabo':
        district_names_from_json_modified.append('tirunelveli')
    elif district_names_from_json[i] == 'sahibzada_ajit_singh_nagar':
        district_names_from_json_modified.append('s.a.s. nagar')
    elif district_names_from_json[i] == 'sonapur':
        district_names_from_json_modified.append('subarnapur')
    elif district_names_from_json[i] == 'east_karbi_anglong':
        district_names_from_json_modified.append('karbi anglong')
    elif district_names_from_json[i] == 'the_nilgiris_district':
        district_names_from_json_modified.append('nilgiris')
    elif district_names_from_json[i] == 'bid':
        district_names_from_json_modified.append('beed')
    elif district_names_from_json[i] == 'baudh':
        district_names_from_json_modified.append('boudh')
    else:
        district_names_from_json_modified.append(district_names_from_json[i])
    # to remove '_district' type discrepencies: notice that '_district' is 8 letters long
    if len(district_names_from_json_modified[-1])>9 and district_names_from_json_modified[-1][-9:]=='_district':
        district_names_from_json_modified[-1]=district_names_from_json[i][:-9]
    
    # now to remove '_' with whitspace
    for j in range(len(district_names_from_json_modified[-1])):
        if district_names_from_json_modified[-1][j]=="_":
            district_names_from_json_modified[-1]=district_names_from_json_modified[-1][:j]+" "+district_names_from_json_modified[-1][j+1:]


# #### Read Cowin csv file with only necessary columns

# In[4]:


cols=['State_Code', 'State', 'District_Key', 'Cowin Key', 'District']
cowin_data=pd.read_csv('cowin_vaccine_data_districtwise.csv',usecols=cols)
cowin_data=cowin_data.iloc[1:,:]
cowin_data['District']=cowin_data['District'].str.lower()


# In[5]:


cowin_data = cowin_data.sort_values("District", axis = 0, ascending = True, kind='mergesort', inplace = False, na_position ='last')
cowin_data.reset_index(inplace=True)


# #### Read districts
# - [x] **Ignored:** Chengalpattu, Gaurela Pendra Marwahi, Nicobars, North and Middle Andaman, Saraikela-Kharsawan,
#     South Andaman, Tenkasi, Tirupathur, Yanam
# - [x] used district _key **to capture same districts names in different states** such as:
# - [x] Aurangabad, Bilaspur, Balrampur, Hamirpur, Pratapgarh
# 

# In[6]:


State = []
District = []
State_District = []

for i in range(cowin_data.shape[0]):
    dis=cowin_data['District'][i]
    '''Chengalpattu, Gaurela Pendra Marwahi, Nicobars, North and Middle Andaman, Saraikela-Kharsawan,
    South Andaman, Tenkasi, Tirupathur, Yanam
    '''
    if (dis == 'tenkasi' or dis == 'yanam' or dis == 'tirupathur' or dis == 'nicobars' or dis == 'north and middle andaman' 
    or dis == 'saraikela-kharsawan' or dis == 'gaurela pendra marwahi' or dis == 'chengalpattu' or dis == 'south andaman'):
        continue
    # avioding repeat districts names 
    if cowin_data['District_Key'][i] not in State_District:
        State.append(cowin_data['State'][i])
        District.append(cowin_data['District'][i])
        State_District.append(cowin_data['District_Key'][i])


# #### Editdist function for strings

# In[7]:


def editdist(str1, str2): 
    m = len(str1)
    n = len(str2)
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
    #print(dp)
    return dp[m][n] 


# #### Getting list of updated district names with district_keys
# - [x] Also gives new districts that need to be added

# In[8]:


district_names_from_portal_updated=[]
state_district_names_from_portal_updated=[]
state_names_from_portal_updated=[]
new_district_check=np.zeros(len(District))
for i in range(len(district_names_from_json_modified)):
    k=0
    for j in range(len(District)):
        if district_names_from_json_modified[i]==District[j] and new_district_check[j]==0:#don't forget to make lower case
            district_names_from_portal_updated.append(District[j])
            state_names_from_portal_updated.append(State[j])
            state_district_names_from_portal_updated.append(State_District[j])
            new_district_check[j]=1
            k=1
            break
    if k==0:
        district_names_from_portal_updated.append('#')
        state_names_from_portal_updated.append('#')
        state_district_names_from_portal_updated.append('#')
        
for i in range(len(district_names_from_json_modified)):
    if district_names_from_portal_updated[i]=='#':
        for j in range(len(District)):
            if editdist(district_names_from_json_modified[i],District[j])<4 and District[j][0]==district_names_from_json_modified[i][0] and new_district_check[j]==0:
                district_names_from_portal_updated[i]=District[j]
                state_names_from_portal_updated[i]=State[j]
                state_district_names_from_portal_updated[i]=State_District[j]
                new_district_check[j]=1
                break

new_district_names_from_portal=[]
new_state_names_from_portal=[]
new_state_district_names_from_portal=[]
for i in range(len(District)):
    if new_district_check[i]==0:
        new_district_names_from_portal.append(District[i])
        new_state_names_from_portal.append(State[i])
        new_state_district_names_from_portal.append(State_District[i])


# In[9]:


new_district_names_from_portal # new districts to add from cowin dataset


# #### Manual Addition of some districts

# - [x] Ranipet, Mumbai, Lakshadweep
# - [x] As **delhi** is given in seperate parts in both cowin dataset and districts json. Did not merge them.

# In[10]:


# Manual Changes to be done 
##### ranipet: vellore, thiruvallur, kanchipuram, tiruvannamalai | part of kanchipuram_district
##### mumbai: thane | combine mumbai city and mumbai suburban

## need to remove kheri and parbhani as asked in question
for i in range(len(district_names_from_portal_updated)):
    if district_names_from_portal_updated[i]=='parbhani' or district_names_from_portal_updated[i] == 'lakhimpur kheri':
        district_names_from_portal_updated[i]='#'

district_proxy={}

for i in range(len(district_id_list)):
    if district_names_from_portal_updated[i]=='#':
        district_proxy[district_id_list[i]]=district_names_from_portal_updated[i]
    else:
        district_proxy[district_id_list[i]]=district_names_from_portal_updated[i]+'/'+district_id_list[i].split('/')[1]


data_modified = {}
for i in range(len(district_id_list)):
    if district_proxy[district_id_list[i]]!='#':
        data_modified[district_proxy[district_id_list[i]]]=[]
        for j in range(len(data_dict[district_id_list[i]])):
            if district_proxy[data_dict[district_id_list[i]][j]]!='#':
                data_modified[district_proxy[district_id_list[i]]].append(district_proxy[data_dict[district_id_list[i]][j]])
                

districts_to_complete_ids = {}
for i in range(len(district_names_from_portal_updated)):
    districts_to_complete_ids[district_names_from_portal_updated[i]] = district_names_from_portal_updated[i] + '/' + district_id_list[i].split('/')[1]

for i in range(len(new_district_names_from_portal)):
    districts_to_complete_ids[new_district_names_from_portal[i].split('/')[0]] = new_district_names_from_portal[i]

for dis in new_district_names_from_portal:
    data_modified[dis] = []
    
# Manual work

for key in data_modified:
    if key.split('/')[0]== 'ranipet':
        data_modified[key].append(districts_to_complete_ids['vellore'])
        data_modified[key].append(districts_to_complete_ids['thiruvallur'])
        data_modified[key].append(districts_to_complete_ids['kancheepuram'])
        data_modified[key].append(districts_to_complete_ids['tiruvannamalai'])
        data_modified[districts_to_complete_ids['vellore']].append(key)
        data_modified[districts_to_complete_ids['thiruvallur']].append(key)
        data_modified[districts_to_complete_ids['kancheepuram']].append(key)
        data_modified[districts_to_complete_ids['tiruvannamalai']].append(key)
    elif key.split('/')[0] == 'mumbai':
        data_modified[key].append(districts_to_complete_ids['thane'])
        data_modified[districts_to_complete_ids['thane']].append(key)
    data_modified[key].sort()


# In[11]:


district_list_modified = []
for i in data_modified:
    district_list_modified.append(i)
district_list_modified = np.array(district_list_modified)
district_list_modified.sort() # sorting districts alphabetically


# #### Adding modified district names to dictionary keys

# In[12]:


modified_json={}
for i in range(len(district_list_modified)):
    for j in range(len(State_District)):
        if district_list_modified[i].split('/')[0]==State_District[j].split('_')[1].lower():
            modified_json[district_list_modified[i].split('/')[0] + '/' + State_District[j]] = data_modified[district_list_modified[i]].copy()


# #### manual modification of repeat name districts
# - [x] Aurangabad, Bilaspur, Balrampur, Hamirpur, Pratapgarh

# In[13]:


modified_json['aurangabad/BR_Aurangabad']=data_modified['aurangabad/Q43086']
modified_json['bilaspur/CT_Bilaspur']=data_modified['bilaspur/Q100157']
modified_json['balrampur/CT_Balrampur']=data_modified['balrampur/Q16056268']
modified_json['hamirpur/UP_Hamirpur']=data_modified['hamirpur/Q2019757']
modified_json['pratapgarh/UP_Pratapgarh']=data_modified['pratapgarh/Q1473962']


# #### Adding modified district values to dictionary keys

# In[14]:


for key in modified_json:
    for i in range(len(modified_json[key])):
        for j in range(len(State_District)):
            if modified_json[key][i].split('/')[0]==State_District[j].split('_')[1].lower():
                
                modified_json[key][i]=modified_json[key][i].split('/')[0] + '/' + State_District[j]
                break


# #### Dumping modified district json

# In[15]:


with open("neighbor-districts-modified.json", "w") as outfile:  
    json.dump(modified_json, outfile, indent = 4) 

