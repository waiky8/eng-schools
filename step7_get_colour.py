import pandas as pd
import datetime
import time

'''
====================================
ADD COLOUR COLUMN FOR MAPBOX MARKERS
====================================
'''


def main():
    start_time = time.time()

    for f in ['england_ks2final.csv', 'england_ks4final.csv', 'england_ks5final.csv']:
        print('*** ', f)
        df = pd.read_csv(f)

        if {'COLOUR'}.issubset(df.columns):
            df.drop('COLOUR', inplace=True, axis=1)

        tot_rows = df.shape[0]
        colour1 = []
        colour2 = []

        for n, r in enumerate(range(0, len(df)), start=1):

            ofsted = df['OFSTEDRATING'][r]

            if ofsted == 'Outstanding':
                c1 = 'limegreen'
            elif ofsted in ['Good', 'Satisfactory']:
                c1 = 'dodgerblue'
            elif ofsted == 'Requires Improvement':
                c1 = 'orangered'
            elif ofsted == 'Inadequate':
                c1 = 'red'
            else:
                c1 = 'gold'

            if f == 'england_ks2final.csv':
                c2 = 'limegreen'
            elif f == 'england_ks4final.csv':
                c2 = 'dodgerblue'
            else:
                c2 = 'blueviolet'

            colour1.append(c1)
            colour2.append(c2)

            elapsed_time = time.time() - start_time
            print(datetime.timedelta(seconds=elapsed_time), ":", f, '[', n, '/', tot_rows, ']', ofsted, '>', c1, c2)

        df['COLOUR1'] = colour1
        df['COLOUR2'] = colour2
        df.to_csv(f, index=False, encoding='utf-8')


if __name__ == '__main__':
    main()
