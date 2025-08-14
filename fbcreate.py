import requests
import random
import time,sys
from faker import Faker

def get_fake_desktop_ua():
    """
    Menghasilkan fake desktop User-Agent, perkiraan width, dan info header terkait.
    Return:
        tuple (ua_string, width_px, browser_name, browser_version, full_version_list)
    """
    desktop_uas = [
        # Windows Edge
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
            "width": 1920,
            "browser": "Microsoft Edge",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"'
        },

        # Windows Firefox
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) "
                  "Gecko/20100101 Firefox/119.0",
            "width": 1920,
            "browser": "Firefox",
            "version": "119",
            "full_version_list": '"Firefox";v="119.0"'
        },

        # Windows Chrome
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36",
            "width": 1920,
            "browser": "Chromium",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184"'
        }
    ]
    return random.choice(desktop_uas)

def delai(j=3):
    for s in range(j, 0, -1):  # hitung mundur dari j ke 1
        print(f'[INFO] [+] TIDUR SELAMA {s} detik', end='\r')
        sys.stdout.flush()
        time.sleep(1)
    print(' ' * 50, end='\r')  # bersihkan baris setelah selesai

def parse_set_cookie(headers):
    """
    Parse 'Set-Cookie' dari response.headers jadi dictionary dan string siap pakai.
    """
    raw_cookie = headers.get('Set-Cookie')
    cookies = {}

    if not raw_cookie:
        return cookies, ""

    # Pisahkan cookie dengan aman (hindari pecah di tanggal)
    parts = raw_cookie.split(',')
    temp = []
    for part in parts:
        if '=' in part.split(';')[0]:
            temp.append(part.strip())
        else:
            temp[-1] += ',' + part.strip()

    # Ambil hanya key=value
    for ck in temp:
        kv = ck.split(';', 1)[0]
        if '=' in kv:
            k, v = kv.split('=', 1)
            cookies[k.strip()] = v.strip()

    # Buat string siap dipakai
    cookie_str = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    return cookies, cookie_str

while True:
    fake = Faker('en_US')
    ua_data = get_fake_desktop_ua()
    first_name = fake.first_name_female()
    last_name = fake.last_name()

    email_akun = f'{first_name.lower()}{last_name.lower()}@gmail.com'
    password = 'zaradev3303#'
    

    cookies = {'wd': '738x688','locale': 'en_GB'}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'dpr': '1',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': f'"Not)A;Brand";v="8", "{ua_data["browser"]}";v="{ua_data["version"]}"',
        'sec-ch-ua-full-version-list': ua_data["full_version_list"],
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua_data["ua"],
        'viewport-width': str(ua_data["width"])
    }

    response = requests.get(
        'https://www.facebook.com/?_rdc=1&_rdr',
        cookies=cookies,
        headers=headers
    )
    cookies.update(dict(response.cookies.get_dict()))
    headers.update({'referer': 'https://www.facebook.com/?_rdc=1&_rdr',})
    signup = requests.get('https://www.facebook.com/r.php?entry_point=login',cookies=cookies,headers=headers).text.replace('\\','')
    lsd_token = 'AVo86L310qI'
    # re.search('name="lsd" value="(.*?)"',signup).group(1)
    haste_session = re.search('"haste_session":"(.*?)"',signup).group(1)
    ccg = re.search('"connectionClass":"(.*?)"',signup).group(1)
    rev = re.search(r'"consistency":{"rev":(\d+)',signup).group(1)
    hsi = re.search(r'"hsi":"(\d+)"',signup).group(1)
    spint = re.search(r'"__spin_t":(\d+)',signup).group(1)
    vip = re.search('"vip":"(.*?)"',signup).group(1)
    headers.update({
        'x-asbd-id': '359341',
        'x-fb-lsd': lsd_token
    })
    print(f'[INFO] [+] IP ADRESS {vip}')
    response = requests.get(
       f'https://web.facebook.com/ajax/registration/validation/contactpoint_invalid/?contactpoint={email_akun}&fb_dtsg_ag&__user=0&__a=1&__req=4&__hs={haste_session}&dpr=1&__ccg={ccg}&__rev={rev}&__s=an0im4%3Afuzmdi%3Ahsr1au&__hsi={hsi}&__dyn=7xe6EsK36Q5E5ObwKBWg5S1Dxu13wqovzEdEc8uw9-3K0lW4o3Bw5VCwjE3awdu0FE2awpUO0n24o5-0me1Fw5uwbO0KU3mwaS0zE5W09yyE1582ZwrU1Xo1UU3jwea&__hsdp=hIfEA5EIox0IkE99fxTFBAwNy2wJBCx90NhE4a1nxe0ky0mK0MEMw7W1kwk87Feoqh0&__hblp=0PU2Owjo620kq0k63a0tG1ew9W2a0cZAw3q80zS0-o04XK0Go1pU0OG1uKLDBFoDh80rQw&__spin_r={rev}&__spin_b=trunk&__spin_t={spint}',
       cookies=cookies,
       headers=headers,
    )
    
    print(f'[INFO] [+] EMAIL {email_akun}')
    headers.update({
        'origin':'https://www.facebook.com',  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
          'accept': '*/*',
    'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://www.facebook.com/r.php?entry_point=login',
        'cookie':'datr=gKGYaMFDH3Zw5Gg2sggX9tbi; sb=gKGYaLge53jtbcJoymqEnZXl; ps_l=1; ps_n=1; locale=en_GB; wd=738x688; fr=1HLHrBbAGkoJv5O1l.AWeSwdELticByfVx58z4uY-kWUf_iGff96qe3DzSwDRT0GEF8Jo.BomL39..AAA.0.0.BomL4I.AWddslGP88dg7QDodcwbRuVHL_k'

 
   })
    data = {
        'jazoest': re.search(r'name="jazoest" value="(\d+)"',signup).group(1),
        'lsd': lsd_token,
        'firstname': first_name,
        'lastname': last_name,
        'birthday_day': '10',
        'birthday_month': '8',
        'birthday_year': '2005',
        'birthday_age': '',
        'did_use_age': 'false',
        'sex': '1',
        'preferred_pronoun': '',
        'custom_gender': '',
        'reg_email__': email_akun,
        'reg_email_confirmation__': '',
        'reg_passwd__': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
        'referrer': '',
        'asked_to_login': '0',
        'use_custom_gender': '',
        'terms': 'on',
        'ns': '0',
        'ri': re.search('name="ri" value="(.*?)"',signup).group(1),
        'action_dialog_shown': '',
        'invid': '',
        'a': '',
        'oi': '',
        'locale': 'en_GB',
        'app_bundle': '',
        'app_data': '',
        'reg_data': '',
        'app_id': '',
        'fbpage_id': '',
        'reg_oid': '',
        'reg_instance': re.search('name="reg_instance" value="(.*?)"',signup).group(1),
        'openid_token': '',
        'uo_ip': '',
        'guid': '',
        'key': '',
        're': '',
        'mid': '',
        'fid': '',
        'reg_dropoff_id': '',
        'reg_dropoff_code': '',
        'ignore': 'captcha|reg_email_confirmation__',
        'captcha_persist_data': re.search('name="captcha_persist_data" value="(.*?)"',signup).group(1),
        'captcha_response': '',
        '__user': '0',
        '__a': '1',
        '__req': '5',
        '__hs': haste_session,
        'dpr': '1',
        '__ccg': ccg,
        '__rev': rev,
        '__s': 'an0im4:fuzmdi:hsr1su',
        '__hsi': hsi,
        '__dyn': '7xe6EsK36Q5E5ObwKBWg5S1Dxu13wqovzEdEc8uw9-3K0lW4o3Bw5VCwjE3awdu0FE2awpUO0n24o5-0me1Fw5uwbO0KU3mwaS0zE5W09yyE1582ZwrU1Xo1UU3jwea',
        '__hsdp': 'hIfEA5EIox0IkE99fxTFBAwNy2wJBCx90NhE4a1nxe0ky0mK0MEMw7W1kwk87Feoqh0',
        '__hblp': '0PU2Owjo620kq0k63a0tG1ew9W2a0cZAw3q80zS0-o04XK0Go1pU0OG1uKLDBFoDh80rQw',
        '__spin_r': rev,
        '__spin_b': 'trunk',
        '__spin_t': spint
    }

    c = response = requests.post('https://web.facebook.com/ajax/register.php', headers=headers, data=data)
    if '"registration_succeeded":true' in c.text:
        cookie_dict, cookie_str = parse_set_cookie(c.headers)
        print(f'[INFO] [+] Name => {first_name} {last_name}\n[INFO] [+] Cookie => {cookie_str}\n')
        open('akun_id','a').write(f'{cookie_str}|{password}\n')
        delai(120)