import pandas as pd
import datetime
import time

'''
=========================
ADD GRAMMAR SCHOOL COLUMN
=========================
'''

df_grammar = pd.read_csv('grammar_schools.csv')


def main():
    start_time = time.time()

    for f in ['england_ks4final.csv', 'england_ks5final.csv']:

        df = pd.read_csv(f)

        tot_rows = df.shape[0]
        grammar = []

        for n, r in enumerate(range(0, len(df)), start=1):
            urn = str(df['URN'][r]).split('.')[0]
            g = get_grammar(urn)
            grammar.append(g)

            elapsed_time = time.time() - start_time
            print(datetime.timedelta(seconds=elapsed_time), ":", f, '[', n, '/', tot_rows, ']', urn, g)

        df['GRAMMAR'] = grammar
        df.to_csv(f, index=False, encoding='utf-8')


def get_grammar(urn):
    df1 = df_grammar[df_grammar['URN'].isin([urn])]

    if df1.empty:
        g = 'No'
    else:
        g = 'Yes'

    return g


if __name__ == '__main__':
    main()
