import pandas as pd
import os

f = pd.read_csv("england_ks2final.csv")
keep_col = ["RECTYPE", "URN", "SCHNAME", "PCODE", "PCODE2", "TOWN", "READPROG", "READPROG_DESCR", "WRITPROG",
            "WRITPROG_DESCR", "MATPROG", "MATPROG_DESCR", "OFSTEDRATING", "INSPECTIONDT", "WEB", "SCHTYPE", "GENDER",
            "RELIGION"]
new_f = f[keep_col]
new_f.to_csv("england_ks2final_new.csv", index=False)

f = pd.read_csv("england_ks4final.csv")
keep_col = ["RECTYPE", "URN", "SCHNAME", "PCODE", "PCODE2", "TOWN", "P8MEA", "P8_BANDING", "ATT8SCR",
            "PTL2BASICS_95", "PTEBACC_E_PTQ_EE", "EBACCAPS", "OFSTEDRATING", "INSPECTIONDT", "WEB", "SCHTYPE",
            "GRAMMAR", "GENDER", "RELIGION"]
new_f = f[keep_col]
new_f.to_csv("england_ks4final_new.csv", index=False)

f = pd.read_csv("england_ks5final.csv")
keep_col = ["RECTYPE", "URN", "SCHNAME", "PCODE", "PCODE2", "TOWN", "VA_INS_ALEV", "PROGRESS_BAND_ALEV",
            "TALLPPE_ALEV_1618", "TALLPPEGRD_ALEV_1618", "OFSTEDRATING", "INSPECTIONDT", "WEB", "SCHTYPE", "GRAMMAR",
            "GENDER", "RELIGION"]
new_f = f[keep_col]
new_f.to_csv("england_ks5final_new.csv", index=False)

os.rename("england_ks2final.csv", "england_ks2final_orig.csv")
os.rename("england_ks4final.csv", "england_ks4final_orig.csv")
os.rename("england_ks5final.csv", "england_ks5final_orig.csv")
os.rename("england_ks2final_new.csv", "england_ks2final.csv")
os.rename("england_ks4final_new.csv", "england_ks4final.csv")
os.rename("england_ks5final_new.csv", "england_ks5final.csv")
