import requests, re, time

cookies = {
    'datr': 'gKGYaMFDH3Zw5Gg2sggX9tbi',
    'sb': 'gKGYaLge53jtbcJoymqEnZXl',
    'ps_l': '1',
    'ps_n': '1',
    'locale': 'en_GB',
    'dpr': '1.25',
    'ar_debug': '1',
    'fr': '13476ORWljTBktUe7.AWfWH5JcFYtadbA7YjUYOtYIUZ1zGZCN9Xx6ZwllHLA5hm9wGhg.BomgCw..AAA.0.0.BomhOB.AWek9CPWXh3aupV8PoZniXRWWHg',
    'wd': '596x642',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'dpr': '1.25',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'viewport-width': '596',
    # 'cookie': 'datr=gKGYaMFDH3Zw5Gg2sggX9tbi; sb=gKGYaLge53jtbcJoymqEnZXl; ps_l=1; ps_n=1; locale=en_GB; dpr=1.25; ar_debug=1; fr=13476ORWljTBktUe7.AWfWH5JcFYtadbA7YjUYOtYIUZ1zGZCN9Xx6ZwllHLA5hm9wGhg.BomgCw..AAA.0.0.BomhOB.AWek9CPWXh3aupV8PoZniXRWWHg; wd=596x642',
}
ok=0
for x in open('akun_id','r').read().splitlines():
    id = re.search(r'c_user=(\d+)',x).group(1)
    response = requests.get(f'https://www.facebook.com/{id}?_rdc=1&_rdr', cookies=cookies, headers=headers)
    if(response.headers.get('Link')):
        ok+=1
        print(f"{ok}. {id} {response.headers.get('Link')}")
        open('fbok.txt','a').write(f'{id}\n')
        time.sleep(5)