import pandas as pd
import requests
import csv

df = pd.read_csv('lala.csv')

new_df = df.iloc[:, 1:11].copy()
new_df.columns = ['no', 'site', 'content_url_title', 'content_local_title', 'url', 'wp', 'status', 'date', 'issue_found','issue_desc']
urls = new_df['url']
urls = 'https://www.samsung.com' + urls.astype(str)

redirected_urls_columns = ['url', 'if_redirects', 'redirect_url']
redirected_urls = pd.DataFrame(columns = redirected_urls_columns)

url = []
if_redirects = []
redirect_url = []

def parser():
    for x in urls:
        redirect_check = requests.get(x)
        redirect_check_status = requests.get(x, allow_redirects = False).status_code
        url.append(x)
        if redirect_check_status == 301:
            if_redirects.append('Yes')
            redirect_url.append(redirect_check.url)
        else:
            if_redirects.append('No')
            redirect_url.append('No Redirect')
    
def create_dataframe():
    redirected_urls.iloc[:, 0] = url
    redirected_urls.iloc[:, 1] = if_redirects
    redirected_urls.iloc[:, 2] = redirect_url

parser()
create_dataframe()
redirected_urls.to_csv(r'PATH_TO_CSV', index = False) #saves result in csv file
