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


def get_website():
    global soup

    school_url = ""

    school_details = soup.find(class_="module info-block info-block--details")

    if school_details is None:
        return school_url

    num = 0
    for school in school_details.find_all(["span"]):

        if school.text == "Type":
            num = 1
            continue
        elif school.text == "Religious character":
            num = 2
            continue
        elif school.text == "Local authority":
            num = 3
            continue
        elif school.text == "Region":
            num = 4
            continue
        elif school.text == "Website":
            num = 5
            continue

        if num in range(1, 4):
            pass
        elif num == 5:
            school_url = school.text
            break

    return school_url


def main():
    start_time = time.time()

    for f in ["england_ks2final.csv", "england_ks4final.csv", "england_ks5final.csv"]:
        df = pd.read_csv(f, engine="python")

        website = []

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
                website.append("")
                print("*** Not Found ***")
            else:
                web = get_website()
                website.append(web)
                print(urn, web)

        df["WEB"] = website
        df.to_csv(f, index=False, encoding="utf-8")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
