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

    for f in ["england_ks2final.csv", "england_ks4final.csv", "england_ks5final.csv"]:
        print("*** ", f)
        df = pd.read_csv(f)

        if {"COLOUR"}.issubset(df.columns):
            df.drop("COLOUR", inplace=True, axis=1)

        colour1 = []
        colour2 = []

        for r in range(0, len(df)):

            ofsted = df["OFSTEDRATING"][r]

            if ofsted == "Outstanding":
                c1 = "green"
            elif ofsted in ["Good", "Satisfactory"]:
                c1 = "blue"
            elif ofsted == "Requires Improvement":
                c1 = "red"
            else:
                c1 = "grey"

            if f == "england_ks2final.csv":
                c2 = "green"
            elif f == "england_ks4final.csv":
                c2 = "blue"
            else:
                c2 = "purple"

            colour1.append(c1)
            colour2.append(c2)

            print(r, ofsted, ">", c1, c2)

        df["COLOUR1"] = colour1
        df["COLOUR2"] = colour2
        df.to_csv(f, index=False, encoding="utf-8")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
