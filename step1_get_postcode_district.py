import pandas as pd
import datetime
import time


def main():
    start_time = time.time()

    for f in ["england_ks2final.csv", "england_ks4final.csv", "england_ks5final.csv"]:
        df = pd.read_csv(f)

        district = []

        for r in range(0, len(df)):
            postcode = df["PCODE"][r]

            try:
                d = df["PCODE"][r].split(" ")[0]
                district.append(d)

            except Exception as e:
                d = ""
                district.append(d)
                print(e)

            print(r, postcode, d)

        df["PCODE2"] = district
        df.to_csv(f, index=False, encoding="utf-8")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()