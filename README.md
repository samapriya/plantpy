# plantpy: Plant Village Survey Export Simple CLI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3842118.svg)](https://doi.org/10.5281/zenodo.3842118)
[![PyPI version](https://badge.fury.io/py/plantpy.svg)](https://badge.fury.io/py/plantpy)
![Build Status](https://img.shields.io/badge/dynamic/json.svg?label=downloads&url=https%3A%2F%2Fpypistats.org%2Fapi%2Fpackages%2Fplantpy%2Frecent%3Fperiod%3Dmonth&query=%24.data.last_month&colorB=blue&suffix=%2fmonth)
[![Build status](https://ci.appveyor.com/api/projects/status/1wbpu6fa8xvqglw6?svg=true)](https://ci.appveyor.com/project/samapriya/plantpy)


This is an application to programmatically export Survey results from [Plant Village surveys](https://plantvillage.psu.edu/). The tool will be extended to include multiple surveys and data sources but for now it exports only the Locust survey datasets. This tools access will depend on your access with plantvillage.

Simple citation:

```
Samapriya Roy. (2020, May 24). samapriya/plantpy: plantpy: Plant Village Survey Simple Export CLI (Version 0.0.3). Zenodo.
http://doi.org/10.5281/zenodo.3842118
```


## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
    * [plantpy auth](#plantpy-auth)
    * [plantpy locust](#plantpy-locust)
    * [plantpy extract](#plantpy-extract)

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

As usual, to print help:

```
plantpy -h
usage: plantpy [-h] {auth,locust,extract} ...

Plant Village Survey Export: Simple CLI

positional arguments:
  {auth,locust,extract}
    auth                Saves your username and password
    locust              Export locust survey data
    extract             Export and filter locust survey to geometry

optional arguments:
  -h, --help            show this help message and exit
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
This allows you to export the locust reports based on country, start and end date into a CSV file. Use country as "all" to get report on all countries in current survey list. It has some inherent features, it looks for your country in existing country list and will let you know if returned CSV is empty. Usage is simply

```
plantpy locust -h
usage: plantpy locust [-h] --start START --end END --country COUNTRY --report
                      REPORT

optional arguments:
  -h, --help         show this help message and exit

Required named arguments.:
  --start START      Start Date YYYY-MM-DD
  --end END          End date YYYY-MM-DD
  --country COUNTRY  Select country to get data or use 'all'
  --report REPORT    full path to CSV report file
```

![plantpy_locust](https://user-images.githubusercontent.com/6677629/82530828-29b71a80-9b0c-11ea-914c-7dca93f127c1.gif)
****

### plantpy extract
This tool will allow you to work with the extracted CSV file and generate a point GeoJSON file containing the location and properties of the survey report. The tool also allows you to pass a geometry GeoJSON file to filter by geometry.

```
plantpy extract -h
usage: plantpy extract [-h] --input INPUT --output OUTPUT
                       [--geometry GEOMETRY]

optional arguments:
  -h, --help           show this help message and exit

Required named arguments.:
  --input INPUT        Path to input CSV survey data file
  --output OUTPUT      Path to output GeoJSON file

Optional named arguments:
  --geometry GEOMETRY  Path to filter geometry as a GeoJSON file
```

![pyplant_extract](https://user-images.githubusercontent.com/6677629/82766045-b2bea200-9de9-11ea-9847-4335d71e8555.gif)

****

### Changelog

**v0.0.3**
* Used pandas for efficient reporting.
* Extract and export CSV report to geometry file and filter by geometry.

**v0.0.2**
* Added version check for automatic release notification.
* Now export locust report for all countries.
* General improvements to handle country lists and exports.
