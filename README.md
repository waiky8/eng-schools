# English Schools

This application was written to show Ofsted ratings and school performance in one place. It covers all education levels - Primary (KS2), Secondary (KS4 GCSE) and Post 16 (KS5 A-Level).<br><br>

Written in **Dash** that utilises **datatables** to show data grouped by the 3 aforementioned educational phases.<br><br>

**Mapbox** is used to show school locations that include additional information by way of hover textbox.

Data is for academic year 2018/19, which can be updated easily in future (at time of writing this is the latest data available).<br><br>

The application is uploaded to **Heroku**. Check out https://eng-schools.herokuapp.com/<br><br>

# Features:
- Interactive dashboard
- Primary: reading, writing & maths performance
- Secondary: progress 8, attainment 8, eng/maths pass rate
- Post16: average A-level grade
- Comparison of performance against the national average for secondary and post 16<br><br>

# Description of code and files:
- **app.py** - main code
- **step0_delete_unwanted_columns.py** - remove all unused columns to make data more manageable
- **step1_get_postcode_district.py** - extract the postcode district (first part of postcode) that can then be selected in the application
- **step2_get_ofsted_rating.py** - extract Ofsted ratings if available
- **step3_get_school_website.py** - extract website of school from Gov UK if available (google to find any missing ones)
- **step4_get_school_type.py** - extract school type from **england_school_information.csv**
- **step5_get_grammar_schools.py** - indicate which are grammar schools by referencing **grammar_schools.csv**
- **step6_get_lat_long.py** - get school latitude & longitude (from https://www.doogal.co.uk/) for map markers
- **step7_get_colour.py** - set ofsted ratings colour code for map markers<br><br>
- **england_ks2final.csv** - contains all relevent data for primary schools (GovUK download)
- **england_ks4final.csv** - contains all relevent data for secondary schools (GovUK download)
- **england_ks5final.csv** - contains all relevent data for post 16 schools (GovUK download)
- **england_school_information.csv** - contains general school data (GovUK download)
- **england_gcse_alevel_averages.csv** - average scores for gcse and a-level in England (obtained by querying performance of any suitable school)
- **Grammars-in-England-by-location.xlsx** - list of grammar schools downloaded from the web
- **grammar_schools.csv** - list of all grammar schools in England extracted from **Grammars-in-England-by-location.xlsx**


# Sample screenshots:
![alt text](https://github.com/waiky8/eng-schools/blob/main/screenshot1.png)
![alt text](https://github.com/waiky8/eng-schools/blob/main/screenshot2.png)
![alt text](https://github.com/waiky8/eng-schools/blob/main/screenshot3.png)
