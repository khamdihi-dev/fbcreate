import requests
import re
import time
import os
import sys

# File input, akan ada jika kamu sudah melakukan pembuatan akun
akun_file = 'akun_id'

# Cek apakah file ada
if not os.path.exists(akun_file):
    print(f"[!] File '{akun_file}' tidak ditemukan. Pastikan file berisi daftar akun tersedia.")
    sys.exit(1)

# Cookie untuk akses Facebook
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

# Header untuk request
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
}

ok = 0

# Membaca file akun_id
with open(akun_file, 'r') as file:
    for line in file:
        match = re.search(r'c_user=(\d+)', line)
        if not match:
            continue

        user_id = match.group(1)
        url = f'https://www.facebook.com/{user_id}?_rdc=1&_rdr'

        try:
            response = requests.get(url, cookies=cookies, headers=headers, timeout=10)
            if response.headers.get('Link'):
                ok += 1
                link_info = response.headers.get('Link')
                print(f"{ok}. {user_id} {link_info}")

                with open('fbok.txt', 'a') as out_file:
                    out_file.write(f'{user_id}\n')

                time.sleep(5)

        except requests.RequestException as e:
            print(f"[!] Gagal memeriksa {user_id}: {e}")
