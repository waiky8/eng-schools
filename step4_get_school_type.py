import pandas as pd
import datetime
import time

df_info = pd.read_csv("england_school_information.csv")

def main():
    start_time = time.time()

    for f in ["england_ks2final.csv", "england_ks4final.csv", "england_ks5final.csv"]:
        df = pd.read_csv(f)

        sch_type = []
        sch_gender = []
        sch_religion = []

        for r in range(0, len(df)):
            urn = str(df["URN"][r]).split(".")[0]
            stype, gender, religion = get_info(urn)

            sch_type.append(stype)
            sch_gender.append(gender)
            sch_religion.append(religion)

            print(r, urn, stype, gender, religion)

        # df["SCHTYPE"] = sch_type
        # df["GENDER"] = sch_gender
        df["RELIGION"] = sch_religion

        df.to_csv(f, index=False, encoding="utf-8")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


def get_info(urn):
    df1 = df_info[df_info["URN"].isin([urn])]

    if df1.empty:
        stype = gender = religion = ""

    else:
        stype = [str(d) for d in df1["MINORGROUP"]][0]
        gender = [str(d) for d in df1["GENDER"]][0]
        religion = [str(d) for d in df1["RELCHAR"]][0]

    return stype, gender, religion


if __name__ == "__main__":
    main()