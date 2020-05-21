# plantpy: Plant Village Survey Simple Export CLI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3837103.svg)](https://doi.org/10.5281/zenodo.3837103)
[![PyPI version](https://badge.fury.io/py/plantpy.svg)](https://badge.fury.io/py/plantpy)


This is an application to programmatically export Survey results from [Plant Village surveys](https://plantvillage.psu.edu/). The tool will be extended to include multiple surveys and data sources but for now it exports only the Locust survey datasets. This tools access will depend on your access with plantvillage.

## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
    * [plantpy auth](#plantpy-auth)
    * [plantpy locust](#plantpy-locust)

## Installation
This assumes that you have native python3 & pip installed in your system, you can test this by going to the terminal (or windows command prompt) and trying

```python``` and then ```pip list```


To install **Plant Village Simple CLI for Survey Access** you can install using two methods.

```pip install plantpy```

or you can also try

```
git clone https://github.com/samapriya/plantpy.git
cd plantpy
python setup.py install
```
For Linux use sudo or try ```pip install plantpy --user```.

I recommend installation within a virtual environment.


## Getting started

Easy citation

```
Samapriya Roy. (2020, May 21). samapriya/plantpy: plantpy: Plant Village Survey Simple Export CLI (Version 0.0.1). Zenodo.
http://doi.org/10.5281/zenodo.3837103
```

As usual, to print help:

```
plantpy -h
usage: plantpy [-h] {auth,locust} ...

Plant Village Survey Export: Simple CLI

positional arguments:
  {auth,locust}
    auth         Saves your username and password
    locust       Extract locust survey data

optional arguments:
  -h, --help     show this help message and exit
```

To obtain help for specific functionality, simply call it with _help_ switch, e.g.: `plantpy auth -h`.

### plantpy auth
For now this stores the username and password as a JSON file which eliminates the need for users to input authentication details again and again. 

```
plantpy auth -h
usage: plantpy auth [-h]

optional arguments:
  -h, --help  show this help message and exit
```

![plantpy_auth](https://user-images.githubusercontent.com/6677629/82530833-2b80de00-9b0c-11ea-82db-b1c73436b869.gif)
****

### plantpy locust
This allows you to export the locust reports based on country, start and end date into a CSV file. It has some inherent features, it looks for your country in existing country list and will let you know if returned CSV is empty. Usage is simply

```
plantpy locust -h
usage: plantpy locust [-h] --start START --end END --country COUNTRY --report
                      REPORT

optional arguments:
  -h, --help         show this help message and exit

Required named arguments.:
  --start START      Start Date YYYY-MM-DD
  --end END          End date YYYY-MM-DD
  --country COUNTRY  Select country to get data
  --report REPORT    full path to CSV report file
```

![plantpy_locust](https://user-images.githubusercontent.com/6677629/82530828-29b71a80-9b0c-11ea-914c-7dca93f127c1.gif)
