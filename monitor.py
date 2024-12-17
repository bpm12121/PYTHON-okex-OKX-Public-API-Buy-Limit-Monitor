import okx.PublicData as PublicData
import time
from colorama import Fore, Style

flag = "0"  # Production trading: 0, Demo trading: 1
publicDataAPI = PublicData.PublicAPI(flag=flag)
buy_limit_start = None
start_time = time.time()

while True:
    result = publicDataAPI.get_price_limit(instId="BTC-USD-SWAP")
    print(result)
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 10:
        buy_limit_end = float(result.get("data", [{}])[0].get("buyLmt", 0))        
        if buy_limit_start is not None and buy_limit_start != buy_limit_end:
            buy_limit_change_rate = ((buy_limit_end - buy_limit_start) / buy_limit_start) * 10000
            color = Fore.GREEN if buy_limit_change_rate > 0 else Fore.RED
            print(f"{color}buyLmt变动率: {buy_limit_change_rate:.10f}{Style.RESET_ALL}")
        elif buy_limit_start is not None:
            print(f"{Fore.GREEN}buyLmt变动率: 0.0000000000{Style.RESET_ALL}")    
        buy_limit_start = buy_limit_end
        start_time = current_time
    time.sleep(3)
