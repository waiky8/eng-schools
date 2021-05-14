import pandas as pd
import numpy as np
import bs4 as bs
import urllib.request
import datetime
import time

'''
=========================
ADD SCHOOL WEBSITE COLUMN
=========================
'''


def get_school_url(url):
    global soup

    url_exist = True

    try:
        source = urllib.request.urlopen(url).read()
    except urllib.request.HTTPError as err:
        url_exist = False
        print('HTTP Error:', err.code)
        return url_exist

    soup = bs.BeautifulSoup(source, 'lxml')

    return url_exist


def get_website():
    global soup

    school_url = ''

    school_details = soup.find(class_='govuk-summary-list')

    # print(school_details)

    if school_details is None:
        return school_url

    for school in school_details.find_all(['dd']):

        if 'http' in school.text:
            school_url = school.text.replace('(opens in new tab)', '').strip()
            break

    return school_url


def main():
    start_time = time.time()

    for f in ['england_ks2final.csv', 'england_ks4final.csv', 'england_ks5final.csv']:
        df = pd.read_csv(f, engine='python')

        if 'WEB' in df.columns:
            web_col = True
        else:
            web_col = False
 
        website = []

        for n, r in enumerate(range(0, len(df)), start=1):
            print(f, ': ', n, '>>>>>>')

            urn = df['URN'][r]
            sch = df['SCHNAME'][r]

            ofsted_url = 'https://get-information-schools.service.gov.uk/Establishments/Establishment/Details/' + \
                         str(urn).split('.')[0]

            if web_col:
                u = str(df['WEB'][r])
                if u == 'nan':
                    print(sch, ofsted_url)

                    url_found = get_school_url(ofsted_url)
                    if not url_found:
                        website.append('')
                        print('*** Not Found ***')
                    else:
                        web = get_website()
                        website.append(web)
                        print(urn, web)

                    time.sleep(2)

                else:

                    website.append(u)
                    print(urn, u)

            else:

                print(sch, ofsted_url)

                url_found = get_school_url(ofsted_url)
                if not url_found:
                    website.append('')
                    print('*** Not Found ***')
                else:
                    web = get_website()
                    website.append(web)
                    print(urn, web)

        df['WEB'] = website
        df.to_csv(f, index=False, encoding='utf-8')

    elapsed_time = time.time() - start_time
    print('\n', datetime.timedelta(seconds=elapsed_time))


if __name__ == '__main__':
    main()
