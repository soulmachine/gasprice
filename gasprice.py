import json
import os
import time
from datetime import datetime, timezone

import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


def get_gas_price():
    try:
        response = requests.get('https://etherchain.org/api/gasnow',
                                headers=headers)
        obj = response.json()
        if obj['code'] == 200:
            with open(
                    os.path.join(
                        'data',
                        datetime.now(timezone.utc).strftime("%Y-%m") + ".json"),
                    "a") as f:
                f.write(json.dumps(obj['data']) + '\n')
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    start_time = time.time()
    while True:
        get_gas_price()
        # Run for 30 minutes - 5 seconds
        if (int(time.time()) + 5) // 60 % 30 == 0:
            break
        time.sleep(5)  # sleep for 5 seconds
