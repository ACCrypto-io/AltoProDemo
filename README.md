# ACCrypto Data Demo

ACC develops data-tools for quantitative and fundamental financial institutions working in Cryptocurrency market investment and risk management. With wide technological knowledge and hands-on experience in the Cryptocurrency space, we tackle the market’s biggest challenges using alternative and traditional data-sets, deep blockchain-layer research and advanced artificial intelligence algorithms.
The goal of the demo is to grant a basic understanding on the structure of Alto's PRO data-sets and a glimpse to the endless information and use-cases hidden in them.

### Whats inside the Data folder?
* The file btc-price-change-7days.csv: This file contain the maximum/minimum price change in 7 days (168 hours) for every hour. Example: for created_utc 1455145200 (February 10, 2016 11:00:00 PM) the maximum price change for BTC in the next 7 days is 10.179% while the minimum price change is -1.2609%.
* The file BTC-Samples.csv.gz: This file is the ACC data sample for Bitcoin and should be download from https://ACCrypto.io.

### Program steps
* Loading ACC data
* Smooth the data for sliding window (window size is 24, can be changed from Utilities/Consts.py).
* Creating random variables for comparison, normalize and calculating Pearson correlation.
* Normalize ACC data and calculating the Pearson correlation.
* Print the random variables correlation results.
* Print ACC data variables correlation results.

### Installation
The project is using Numpy. Please visit https://www.scipy.org/scipylib/download.html to install Numpy if you do not have it already (Ubuntu users can just follow the following commands).

Install python3.6 and pip if not already installed (Ubuntu commands).

```sh
$ sudo add-apt-repository ppa:deadsnakes/ppa;
$ sudo apt-get update;
$ sudo apt-get install python3.6;
$ curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6;
$ sudo apt-get install build-essential libssl-dev libffi-dev python3.6-dev;
```

Install and create python3.6 virtual environment

```sh
$ sudo apt install python3.6-venv;
$ python3.6 -m venv env-acc-data-demo;
$ source env-acc-data-demo;
$ python3.6 -m pip install -r requirements.txt;
```

Download the data from https://ACCrypto.io and move it into the Data folder.
Finally run the following command to show Pearson correlation between ACC data to BTC price change (the project also create random variables for comparison).
```sh
$ python3.6 StartAnalyze
```
