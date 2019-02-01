# ACCrypto Data Demo

ACC develops data-tools for quantitative and fundamental financial institutions working in Cryptocurrency market investment and risk management. With wide technological knowledge and hands-on experience in the Cryptocurrency space, we tackle the market’s biggest challenges using alternative and traditional data-sets, deep blockchain-layer research and advanced artificial intelligence algorithms.

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
