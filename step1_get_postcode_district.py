import pandas as pd
import datetime
import time

'''
============================
ADD POSTCODE DISTRICT COLUMN
============================
'''


def main():
    start_time = time.time()

    for f in ['england_ks2final.csv', 'england_ks4final.csv', 'england_ks5final.csv']:
        df = pd.read_csv(f)

        tot_rows = df.shape[0]
        district = []

        for n, r in enumerate(range(0, len(df)), start=1):
            postcode = df['PCODE'][r]

            try:
                d = df['PCODE'][r].split(' ')[0]
                district.append(d)

            except Exception as e:
                d = ''
                district.append(d)
                print(e)

            elapsed_time = time.time() - start_time
            print(datetime.timedelta(seconds=elapsed_time), ":", f, "[", n, "/", tot_rows, "]", postcode, d)

        df['PCODE2'] = district
        df.to_csv(f, index=False, encoding='utf-8')


if __name__ == '__main__':
    main()
