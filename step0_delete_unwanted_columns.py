import pandas as pd
import os

'''
=========================================
DELETE UNUSED COLUMNS TO REDUCE FILE SIZE
=========================================
'''

df = pd.read_csv('england_ks2final.csv')
df1 = df[df['RECTYPE'].isin(['1', '2'])]  # mainstream & special schools
keep_col = ['RECTYPE', 'URN', 'SCHNAME', 'PCODE', 'TOWN', 'READPROG', 'READPROG_DESCR', 'WRITPROG',
            'WRITPROG_DESCR', 'MATPROG', 'MATPROG_DESCR']
new_f = df1[keep_col]
new_f.to_csv('england_ks2final_new.csv', index=False)

df = pd.read_csv('england_ks4final.csv')
df1 = df[df['RECTYPE'].isin(['1', '2'])]  # mainstream & special schools
keep_col = ['RECTYPE', 'URN', 'SCHNAME', 'PCODE', 'TOWN', 'P8MEA', 'P8_BANDING', 'ATT8SCR',
            'PTL2BASICS_95', 'PTEBACC_E_PTQ_EE', 'EBACCAPS']
new_f = df1[keep_col]
new_f.to_csv('england_ks4final_new.csv', index=False)

df = pd.read_csv('england_ks5final.csv')
df1 = df[df['RECTYPE'].isin(['1', '2'])]  # mainstream & special schools
keep_col = ['RECTYPE', 'URN', 'SCHNAME', 'PCODE', 'TOWN', 'VA_INS_ALEV', 'PROGRESS_BAND_ALEV',
            'TALLPPE_ALEV_1618', 'TALLPPEGRD_ALEV_1618']
new_f = df1[keep_col]
new_f.to_csv('england_ks5final_new.csv', index=False)

os.rename('england_ks2final.csv', 'england_ks2final_orig.csv')
os.rename('england_ks4final.csv', 'england_ks4final_orig.csv')
os.rename('england_ks5final.csv', 'england_ks5final_orig.csv')
os.rename('england_ks2final_new.csv', 'england_ks2final.csv')
os.rename('england_ks4final_new.csv', 'england_ks4final.csv')
os.rename('england_ks5final_new.csv', 'england_ks5final.csv')
