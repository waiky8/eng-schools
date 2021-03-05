# English Schools

I was struggling to find a website where I can compare the ratings and performance of schools in England - ok there is the government one but it is not so friendly to navigate. This is my attempt at bringing the Ofsted ratings and schools performance into one place that is not bloated with a million different pieces of information.<br><br>

Written in **Dash** that predominately uses **datatables** showing data for each of the 3 main phases of education (primary, secondar and post 16).<br><br>

Data is from academic year 2018/19, which can be updated easily (at time of writing this is the latest data available).<br><br>

# Data includes:
  - Primary: reading, writing & maths
  - Secondary: progress 8, attainment 8, eng/maths passes
  - Post16: average A-level grade<br><br>

# Input options:
- Select school name, town and postcode
- Filter by independent and grammar schools<br><br>

Check out https://eng-schools.herokuapp.com/<br><br>

# Description of code and files:
- **app.py** - main code
- **step1_get_postcode_district.py** - extract the postcode district (first part of postcode) that can be selected in the application
- **step2_get_ofsted_rating.py** - extract Ofsted ratings if available
- **step3_get_school_website.py** - extract website of school if available 
- **step4_get_school_type.py** - extract school type from **england_school_information.csv**
- **step5_get_grammar_schools.py** - indicate which are grammar schools by referencing **grammar_schools.csv**
- **step6_delete_unwanted_columns.py** - remove all unused columns to make data more manageable
- **england_gcse_alevel_averages.csv** - average scores for gcse and a-level in England
- **england_ks2final.csv** - contains all relevent data for primary schools (GovUK download)
- **england_ks4final.csv** - contains all relevent data for secondary schools (GovUK download)
- **england_ks5final.csv** - contains all relevent data for post 16 schools (GovUK download)
- **england_school_information.csv** - contains general school data (GovUK download)
- **grammar_schools.csv** - list of all grammar schools in England
- **Grammars-in-England-by-location.xlsx** - list of grammar schools downloaded from the web

# Sample screenshots:
![alt text](https://github.com/waiky8/eng-schools/blob/main/screenshot_1.jpg)
![alt text](https://github.com/waiky8/eng-schools/blob/main/screenshot_2.jpg)
![alt text](https://github.com/waiky8/eng-schools/blob/main/screenshot_3.jpg)
