import pandas as pd
import bs4 as bs
import urllib.request
import datetime
import time


def get_school_url(url):
    global soup

    url_exist = True

    try:
        source = urllib.request.urlopen(url).read()
    except urllib.request.HTTPError as err:
        url_exist = False
        print("HTTP Error:", err.code)
        return url_exist

    soup = bs.BeautifulSoup(source, "lxml")

    return url_exist


def get_rating():
    global soup

    inspect_date = ""
    rating = ""

    school_details = soup.find(class_="timeline")

    for s in school_details.find_all(["time", "strong"]):
        if s.name == "time":
            inspect_date = str(datetime.datetime.strptime(s.text, "%d %B %Y"))[:10].replace("-", "")
        elif s.name == "strong":
            rating = s.text
            break

    if rating == "":
        inspect_date = ""

    return inspect_date, rating


def main():
    start_time = time.time()

    for f in ["england_ks2final.csv", "england_ks4final.csv", "england_ks5final.csv"]:
        df = pd.read_csv(f, engine="python")

        ofsted_rating = []
        inspect_date = []

        n = 0
        for r in range(0, len(df)):
            n += 1
            print(f, ": ", n, ">>>>>>")

            urn = df["URN"][r]
            sch = df["SCHNAME"][r]

            ofsted_url = "http://www.ofsted.gov.uk/oxedu_providers/full/(urn)/" + str(urn).split(".")[0]
            print(sch, ofsted_url)

            url_found = get_school_url(ofsted_url)
            if not url_found:
                ofsted_rating.append("")
                inspect_date.append("")
                print("*** Not Found ***")
            else:
                insp_date, rating = get_rating()
                ofsted_rating.append(rating)
                inspect_date.append(insp_date)
                print(urn, insp_date, rating)

        df["OFSTEDRATING"] = ofsted_rating
        df["INSPECTIONDT"] = inspect_date
        df.to_csv(f, index=False, encoding="utf-8")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
