import pandas as pd
import bs4 as bs
import urllib.request
import datetime
import time

'''
================================
ADD LATITUDE & LONGITUDE COLUMNS
================================
'''


def main():
    start_time = time.time()

    for f in ["england_ks2final.csv", "england_ks4final.csv", "england_ks5final.csv"]:
        df = pd.read_csv(f)

        latitude = []
        longitude = []

        for r in range(0, len(df)):
            urn = df["URN"][r]
            pcode = df["PCODE"][r]

            print(r, urn, pcode)
            lat, long = get_coord(pcode)

            latitude.append(lat)
            longitude.append(long)

            print(r, pcode, lat, long)

        df["LATITUDE"] = latitude
        df["LONGITUDE"] = longitude

        df.to_csv(f, index=False, encoding="utf-8")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


def get_coord(pcode):
    lat = long = ""

    if pd.isna(pcode):
        return lat, long

    url = ("https://www.doogal.co.uk/ShowMap.php?postcode=" + pcode).replace(" ", "%20")

    try:
        source = urllib.request.urlopen(url)
        soup = bs.BeautifulSoup(source, 'lxml')
        tables = soup.find_all("table")

        for tb in tables:
            table_rows = tb.find_all("tr")

            for tr in table_rows:
                thd = tr.find_all(["th", "td"])
                row = [i.text for i in thd]

                if not row:
                    pass
                else:
                    if row[1] == "Latitude":
                        lat = row[2]
                    elif row[1] == "Longitude":
                        long = row[2]
                        break

    except urllib.request.HTTPError as err:
        print("HTTP Error: (postcode ", pcode, ")", err.code)

    return lat, long


if __name__ == "__main__":
    main()
