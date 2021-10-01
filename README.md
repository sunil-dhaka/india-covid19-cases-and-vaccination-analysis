## Course Assignment-1 for CS685A: Data Mining

All plugin details etc are given in **README.txt** file.

- Render *.md* file for better readability.

> In order to run the entire script, run the coomand *"bash assign1.sh"* command from terminal.

**Time taken** to run all files using assign1.sh script: **7m18.726s** 
- [x] It takes around **7-8 minutes** to run on my *machine*.
- [x]  Individual time taken by questions is given below with their file names.

**Request:**
I have considered only that population of the state which is included in the districts in our Analysis rather than consider the Population of a State as the whole population of the State. Though it won't make much difference in most states except Delhi, AP and J&K. And I also believe by considering only population of the districts in our Analysis, we will get better result, other wise ratios will either be undermined or overmined. If it would have been cleared before last day(on course forum it was asked on 21 September @4PM) I would have implement as requested. Please consider my situation.

**Points:**
1. Particular details about questions are given in markdown section of individual .ipynb files. All codes are moderately commented, some section where explanation  seems necessary, codes are heavely commented with markdown explanations also.
2. All output files are Laxographically sorted, except some ratio csv files which are sorted by the ratio asked in particular questions.
3. In Que-4 I have used number of active cases on last day of week(overlapping that smooths data)/month(15th to 14th). For more details please see *Q4_Asgn1.ipynb*.
4. $active=confirmed-deceased-reccovered$ formula is used in Que-4.
5. $Vaccination Rate($%$)=\frac{100*Doses In Last Week}{Total Population}$ formula is used in Que-9.
6. Some(~25) manual changes are done in district names in Que-1. Please look into *Q1_Asgn1.ipynb* for list and their modification.
7. I have taken common disstricts if cowin and json file in Que-1, to get more district updates, and also more data.
---
Jupyter Notebook files:

### Q1_Asgn1.ipynb
Input: neighbor-districts.json, cowin_vaccine_data_districtwise.csv

Output: nieghbor-districts-modified.json

Time taken to run on my machine: **0m4.744s**

### Q2_Asgn1.ipynb
Input: neighbor-districts-modified.json

Output: edge-graph.csv

Time taken to run on my machine: **0m2.162s**

### Q3_Asgn1.ipynb
Input: neighbor-districts-modified.json, districts.csv

Output: cases-week.csv, cases-month.csv, cases-overall.csv

Time taken to run on my machine: **1m27.668s**

### Q4_Asgn1.ipynb
Input: nieghbor-districts-modified.json, districts.csv

Output: district-peaks.csv, state-peaks.csv, overall-peaks.csv

Time taken to run on my machine: **1m17.783s**

### Q5_Asgn1.ipynb
Input: nieghbor-districts-modified.json, cowin_vaccine_data_districtwise.csv

Output: district-vaccinated-count-week.csv, district-vaccinated-count-month.csv, district-vaccinated-count-overall.csv,state-vaccinated-count-week.csv, state-vaccinated-count-month.csv, state-vaccinated-count-overall.csv

Time taken to run on my machine: **3m41.532s**

### Q6_Asgn1.ipynb
Input: nieghbor-districts-modified.json, cowin_vaccine_data_districtwise.csv, DDW_PCA0000_2011_Indiastatedist.xlsx

Output: district-vaccination-population-ratio.csv,state-vaccination-population-ratio.csv,overall-vaccination-population-ratio.csv

Time taken to run on my machine: **0m19.123s**

### Q7_Asgn1.ipynb
Input: nieghbor-districts-modified.json, cowin_vaccine_data_districtwise.csv

Output: district-vaccine-type-ratio.csv,state-vaccine-type-ratio.csv,overall-vaccine-type-ratio.csv

Time taken to run on my machine: **0m7.860s**

### Q8_Asgn1.ipynb
Input: nieghbor-districts-modified.json, cowin_vaccine_data_districtwise.csv, DDW_PCA0000_2011_Indiastatedist.xlsx

Output: district-vaccinated-dose-ratio.csv,state-vaccinated-dose-ratio.csv,overall-vaccinated-dose-ratio.csv

Time taken to run on my machine: **0m18.938s**

### Q9_Asgn1.ipynb
Input: nieghbor-districts-modified.json, cowin_vaccine_data_districtwise.csv, DDW_PCA0000_2011_Indiastatedist.xlsx

Output: complete-vaccination.csv

Time taken to run on my machine: **0m18.938s**