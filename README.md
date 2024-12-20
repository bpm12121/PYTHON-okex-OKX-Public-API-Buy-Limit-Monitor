# OKX Public API Buy Limit Monitor

This project is a Python script that monitors the `buyLmt` data for the `BTC-USD-SWAP` instrument from the OKX Public API. It tracks the change rate of the `buyLmt` over time and prints the change rate to the console.

## Features
- Fetches `buyLmt` data every 3 seconds from the OKX Public API.
- Tracks the change rate of `buyLmt` over time.
- Prints the change rate in green for positive changes and red for negative changes.
- Runs continuously, updating every 10 seconds.

## About BTC-USD-SWAP
By default, the script monitors the `BTC-USD-SWAP` trading pair, which is a **Bitcoin Futures contract** on OKX. This pair is used for trading Bitcoin with USDT in the futures market.

## Change Trading Pair
You can easily modify the script to monitor a different trading pair. 

## Finding Available Trading Pairs
To find the list of available trading pairs, refer to OKX's official [API documentation](https://www.okx.com/docs-v5/zh/#order-book-trading-market-data-get-tickers). There, you'll find the correct `instId` values for the pairs you want to track.
