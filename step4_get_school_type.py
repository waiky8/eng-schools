import pandas as pd
import datetime
import time

'''
======================
ADD SCHOOL TYPE COLUMN
======================
'''

df_info = pd.read_csv('england_school_information.csv')


def main():
    start_time = time.time()

    for f in ['england_ks2final.csv', 'england_ks4final.csv', 'england_ks5final.csv']:
        df = pd.read_csv(f)

        tot_rows = df.shape[0]
        sch_type = []
        sch_gender = []
        sch_religion = []
        sch_phase = []

        if f == 'england_ks2final.csv':
            phase = 'Primary'
        elif f == 'england_ks4final.csv':
            phase = 'Secondary'
        else:
            phase = 'Post16'

        for n, r in enumerate(range(0, len(df)), start=1):
            urn = str(df['URN'][r]).split('.')[0]
            stype, gender, religion = get_info(urn)

            sch_type.append(stype)
            sch_gender.append(gender)
            sch_religion.append(religion)
            sch_phase.append(phase)

            elapsed_time = time.time() - start_time
            print(datetime.timedelta(seconds=elapsed_time), ":", f, '[', n, '/', tot_rows, ']', urn, stype, gender,
                  religion, phase)

        df['SCHTYPE'] = sch_type
        df['GENDER'] = sch_gender
        df['RELIGION'] = sch_religion
        df['PHASE'] = sch_phase

        df.to_csv(f, index=False, encoding='utf-8')


def get_info(urn):
    df1 = df_info[df_info['URN'].isin([urn])]

    if df1.empty:
        stype = gender = religion = ''

    else:
        stype = [str(d) for d in df1['MINORGROUP']][0]
        gender = [str(d) for d in df1['GENDER']][0]
        religion = [str(d) for d in df1['RELCHAR']][0]

    return stype, gender, religion


if __name__ == '__main__':
    main()
