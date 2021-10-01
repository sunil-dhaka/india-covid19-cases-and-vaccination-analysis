-----------------Please read README.md to see other details----------------------------------


Plugins-
Software: python3 jupyter notebook (.sh files run python3 jupyter notebooks)

Environments: conda 4.10.3, python 3.8.5


Dependencies-
Python Libraries: pandas 1.1.3, numpy 1.19.2, json 2.0.9, scipy 1.5.2, datetime


Programs-

.sh files:

assign1.sh 
top level script that runs the entire assignment

How to use:
In order to run all programs sequentially, run the following command from the terminal-
bash assign1.sh 

Things to note:
It takes about 8 mins to run on my machine.
scipy is used only in question 4.

--------------------------------------------------------------------------------------------
neighbor-districts-modifier.sh
runs Q1_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q1_Asgn1.ipynb

edge-generator.sh
runs Q2_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q2_Asgn1.ipynb

case-generator.sh
runs Q3_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q3_Asgn1.ipynb

peaks-generator.sh
runs Q4_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q4_Asgn1.ipynb

vaccinated-count-generator.sh
runs Q5_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q5_Asgn1.ipynb

vaccination-population-ratio-generator.sh
runs Q6_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q6_Asgn1.ipynb

vaccine-type-ratio-generator.sh
runs Q7_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q7_Asgn1.ipynb

vaccinated-ratio-generator.sh
runs Q8_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q8_Asgn1.ipynb

complete-vaccination-generator.sh
runs Q9_Asgn1.ipynb as
jupyter nbconvert --to notebook --execute Q9_Asgn1.ipynb
------------------------------------------------------------------------------------------------

Jupyter Notebook files:

Q1_Asgn1.ipynb
Input: neighbor-districts.json, cowin_vaccine_data_districtwise.csv

Output: nieghbor-districts-modified.json

Q2_Asgn1.ipynb
Input: neighbor-districts-modified.json

Output: edge-graph.csv

Q3_Asgn1.ipynb
Input: neighbor-districts-modified.json, districts.csv

Output: cases-week.csv, cases-month.csv, cases-overall.csv

Q4_Asgn1.ipynb -- uses scipy
Input: neighbor-districts-modified.json, districts.csv

Output: district-peaks.csv, state-peaks.csv, overall-peaks.csv

Q5_Asgn1.ipynb
Input: neighbor-districts-modified.json, cowin_vaccine_data_districtwise.csv

Output: district-vaccinated-count-week.csv, district-vaccinated-count-month.csv, district-vaccinated-count-overall.csv,state-vaccinated-count-week.csv, state-vaccinated-count-month.csv, state-vaccinated-count-overall.csv

Q6_Asgn1.ipynb
Input: neighbor-districts-modified.json, cowin_vaccine_data_districtwise.csv, DDW_PCA0000_2011_Indiastatedist.xlsx

Output: district-vaccination-population-ratio.csv,state-vaccination-population-ratio.csv,overall-vaccination-population-ratio.csv

Q7_Asgn1.ipynb
Input: neighbor-districts-modified.json, cowin_vaccine_data_districtwise.csv

Output: district-vaccine-type-ratio.csv,state-vaccine-type-ratio.csv,overall-vaccine-type-ratio.csv

Q8_Asgn1.ipynb
Input: neighbor-districts-modified.json, cowin_vaccine_data_districtwise.csv, DDW_PCA0000_2011_Indiastatedist.xlsx

Output: district-vaccinated-dose-ratio.csv,state-vaccinated-dose-ratio.csv,overall-vaccinated-dose-ratio.csv

Q9_Asgn1.ipynb
Input: neighbor-districts-modified.json, cowin_vaccine_data_districtwise.csv, DDW_PCA0000_2011_Indiastatedist.xlsx

Output: complete-vaccination.csv
