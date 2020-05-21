# pyplant: Plant Village Survey Export Simple CLI

This is an application to programmatically export Survey results from [Plant Village surveys](https://plantvillage.psu.edu/). The tool will be extended to include multiple surveys and data sources but for now it exports only the Locust survey datasets. This tools access will depend on your access with plantvillage.

## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
    * [pyplant auth](#pyplant-auth)
    * [pyplant locust](#pyplant-locust)

## Installation
This assumes that you have native python3 & pip installed in your system, you can test this by going to the terminal (or windows command prompt) and trying

```python``` and then ```pip list```


To install **Plant Village Simple CLI for Survey Access** you can install using two methods.

```pip install pyplant```

or you can also try

```
git clone https://github.com/samapriya/pyplant.git
cd pyplant
python setup.py install
```
For Linux use sudo or try ```pip install pyplant --user```.

I recommend installation within a virtual environment.


## Getting started

As usual, to print help:

```
pyplant -h
usage: pyplant [-h] {auth,locust} ...

Plant Village Survey Export: Simple CLI

positional arguments:
  {auth,locust}
    auth         Saves your username and password
    locust       Extract locust survey data

optional arguments:
  -h, --help     show this help message and exit
```

To obtain help for specific functionality, simply call it with _help_ switch, e.g.: `pyplant auth -h`.

### pyplant auth
For now this stores the username and password as a JSON file which eliminates the need for users to input authentication details again and again. It has some inherent features, it looks for your country in existing country list and will let you know if returned CSV is empty.

```
pyplant auth -h
usage: pyplant auth [-h]

optional arguments:
  -h, --help  show this help message and exit
```

![pyplant_auth](https://user-images.githubusercontent.com/6677629/82528773-86640680-9b07-11ea-9d0a-e554b1f05b43.gif)
****

### pyplant locust
This allows you to export the locust reports based on country, start and end date into a CSV file. Usage is simply

```
pyplant locust -h
usage: pyplant locust [-h] --start START --end END --country COUNTRY --report
                      REPORT

optional arguments:
  -h, --help         show this help message and exit

Required named arguments.:
  --start START      Start Date YYYY-MM-DD
  --end END          End date YYYY-MM-DD
  --country COUNTRY  Select country to get data
  --report REPORT    full path to CSV report file
```

![pyplant_locust](https://user-images.githubusercontent.com/6677629/82528784-89f78d80-9b07-11ea-8ef7-f1fb2ba38148.gif)
