__copyright__ = """

    Copyright 2020 Samapriya Roy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"

from bs4 import BeautifulSoup as bs
from requests import Session
from rapidfuzz import fuzz
from datetime import datetime
from os.path import expanduser
import argparse
import subprocess
import os
import platform
import time
import pandas as pd
import csv
import pkg_resources
import sys
import json
import requests
if str(platform.system().lower()) == "windows":
    # Get python runtime version
    version =sys.version_info[0]
    try:
        import pipwin
        if pipwin.__version__=='0.5.0':
            pass
        else:
            a=subprocess.call('{} -m pip install pipwin==0.5.0'.format(sys.executable), shell=True,stdout=subprocess.PIPE)
            subprocess.call('pipwin refresh', shell=True)
        '''Check if the pipwin cache is old: useful if you are upgrading porder on windows
        [This section looks if the pipwin cache is older than two weeks]
        '''
        home_dir = expanduser("~")
        fullpath=os.path.join(home_dir, ".pipwin")
        file_mod_time = os.stat(fullpath).st_mtime
        if int((time.time() - file_mod_time) / 60) > 43200:
            print('Refreshing your pipwin cache')
            subprocess.call('pipwin refresh', shell=True)
    except ImportError:
        a=subprocess.call('{} -m pip install pipwin==0.5.0'.format(sys.executable), shell=True,stdout=subprocess.PIPE)
        subprocess.call('pipwin refresh', shell=True)
    except Exception as e:
        print(e)
    try:
        import gdal
    except ImportError:
        subprocess.call('pipwin install gdal', shell=True)
    except Exception as e:
        print(e)
    try:
        import pyproj
    except ImportError:
        subprocess.call('pipwin install pyproj', shell=True)
    except Exception as e:
        print(e)
    try:
        import shapely
    except ImportError:
        subprocess.call('pipwin install shapely', shell=True)
    except Exception as e:
        print(e)
    try:
        import fiona
    except ImportError:
        subprocess.call('pipwin install fiona', shell=True)
    except Exception as e:
        print(e)
    try:
        import geopandas
    except ImportError:
        subprocess.call('pipwin install geopandas', shell=True)
    except Exception as e:
        print(e)
# Setup an agent for login
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}


# Current country list
country_list = [
    "Algeria",
    "Bahrain",
    "Burkina Faso",
    "Cameroon",
    "Chad",
    "Djibouti",
    "Egypt",
    "Eritrea",
    "Ethiopia",
    "India",
    "Iraq",
    "Iran",
    "Jordan",
    "Kenya",
    "Kuwait",
    "Libya",
    "Mali",
    "Mauritania",
    "Morocoo",
    "Niger",
    "Nigeria",
    "Oman",
    "Pakistan",
    "Qatar",
    "Saudi",
    "Senegal",
    "Somalia",
    "South Sudan",
    "Sudan",
    "Tanzania",
    "UAE",
    "Uganda",
    "Yemen",
]

all_locations = 'Algeria&search[locations][]=Bahrain&search[locations][]=Burkina Faso&search[locations][]=Cameroon&search[locations][]=Chad&search[locations][]=Djibouti&search[locations][]=Egypt&search[locations][]=Eritrea&search[locations][]=Ethiopia&search[locations][]=India&search[locations][]=Iraq&search[locations][]=Iran&search[locations][]=Jordan&search[locations][]=Kenya&search[locations][]=Kuwait&search[locations][]=Libya&search[locations][]=Mali&search[locations][]=Mauritania&search[locations][]=Morocoo&search[locations][]=Niger&search[locations][]=Nigeria&search[locations][]=Oman&search[locations][]=Pakistan&search[locations][]=Qatar&search[locations][]=Saudi&search[locations][]=Senegal&search[locations][]=Somalia&search[locations][]=South Sudan&search[locations][]=Sudan&search[locations][]=Tanzania&search[locations][]=UAE&search[locations][]=Uganda&search[locations][]=Yemen'


# Get package version
def plantpy_version():
    url = "https://pypi.org/project/plantpy/"
    source = requests.get(url)
    html_content = source.text
    soup = bs(html_content, "html.parser")
    company = soup.find("h1")
    if (
        not pkg_resources.get_distribution("plantpy").version
        == company.string.strip().split(" ")[-1]
    ):
        print(
            "\n"
            + "========================================================================="
        )
        print(
            "Current version of plantpy is {} upgrade to lastest version: {}".format(
                pkg_resources.get_distribution("plantpy").version,
                company.string.strip().split(" ")[-1],
            )
        )
        print(
            "========================================================================="
        )


plantpy_version()

# set credentials
def auth():
    home = expanduser("~/village.json")
    usr = input("Enter username: ")
    pwd = input("Enter password: ")
    data = {"username": usr, "password": pwd}
    with open(home, "w") as outfile:
        json.dump(data, outfile)


# auth()
def auth_from_parser(args):
    auth()


# Locust data export
country_matches = []


def locust(report, start, end, country):
    """[Locust Survey Export tool]

    [This tool allows you to interact with the locust tabular data and export it as CSV file locally]

    Arguments:
        report {[type]} -- [Full path to CSV file]
        start {[type]} -- [Start date YYYY-MM-DD]
        end {[type]} -- [End date YYYY-MM-DD]
        country {[type]} -- [Country of export]
    """
    try:
        home = expanduser("~/village.json")
        with open(home) as json_file:
            data = json.load(json_file)
            if not data.get("username"):
                username = input("Enter username: ")
            else:
                username = data.get("username")
            if not data.get("password"):
                password = input("Enter password: ")
            else:
                password = data.get("password")
    except Exception as e:
        print(e)
    start_time = datetime.strptime(start, "%Y-%m-%d")
    start_format = start_time.strftime("%m-%d-%Y")
    end_time = datetime.strptime(end, "%Y-%m-%d")
    end_format = end_time.strftime("%m-%d-%Y")
    for countries in country_list:
        rat = fuzz.ratio(countries, country)
        if rat > 70:
            country_matches.append(countries)
    if not len(country_matches) == 0:
        country = country_matches[0]
    elif len(country_matches) == 0 and country == "all":
        country=all_locations
    else:
        print("Country not found in list: Choose from or choose 'all'")
        print(country_list)
        sys.exit()
    with Session() as s:
        site = s.get("https://plantvillage.psu.edu/users/sign_in")
        soup = bs(site.content, "html.parser")
        data = {
            "authenticity_token": soup.find(
                "input", attrs={"name": "authenticity_token"}
            )["value"],
            "user[email]": username,
            "user[password]": password,
        }
        r = s.post("https://plantvillage.psu.edu/users/sign_in", data=data)
        b = s.get(
            "https://plantvillage.psu.edu/admin/locust_surveys/export_csv.csv?utf8=%E2%9C%93&start_date={}&end_date={}&search[locations][]={}&commit=Export".format(
                start_format, end_format, country
            )
        )
        url_content = b.content
        print("\n" + "Writing report to : {}".format(report))
        csv_file = open(report, "wb")
        csv_file.write(url_content)
        csv_file.close()

    df = pd.read_csv(report, encoding="utf8")
    value= len(df.index)
    country_count= len(df['Country'].unique())
    if value > 1:
        if len(country.split('=')) ==1:
            print("Total rows in dataset {} for {}".format(value - 1, country))
        elif len(country.split('='))>1:
            print("Total rows in dataset {} for {} countries".format(value - 1, country_count))
    elif value == 1:
        print("No data found for {}".format(country))


# village(report=r'C:\planet_demo\report.csv',start='2020-05-01',end='2020-05-20',country='ethiopia')
def locust_from_parser(args):
    locust(start=args.start, end=args.end, country=args.country, report=args.report)

li = []


def extract(input, output, geometry):
    import geopandas as gpd
    from collections import OrderedDict
    from shapely.geometry import shape, Point
    if geometry is None:
        with open(input, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                d = OrderedDict()
                d["type"] = "Feature"
                d["geometry"] = {
                    "type": "Point",
                    "coordinates": [float(row["longitude"]), float(row["Latitude"])],
                }
                d["properties"] = {
                    "Country": row["Country"],
                    "Date": row["Date"],
                    "Location": row["Location"],
                    "Altitude": float(row["Altitude"]),
                    "Accuracy": float(row["Accuracy"]),
                    "Locust Type": row["Locust Type"],
                    "Area (ha)": float(row["Area (ha)"]),
                    "Flavour": row["Flavour"],
                    "Platform": row["Platform"],
                    "Language": row["Language"],
                    "Hopper Instar": row["Hopper Instar"],
                }
                li.append(d)

        d = OrderedDict()
        d["type"] = "FeatureCollection"
        d["features"] = li
        if output.endswith('.geojson'):
            with open(output, "w") as f:
                json.dump(d, f, indent=2)
            print(
                "Extracted a total of {} features: File written to {}".format(
                    len(li), output
                )
            )
        elif output.endswith('.shp'):
            with open(output.replace('.shp','.geojson'), "w") as f:
                json.dump(d, f, indent=2)
            myshpfile = gpd.read_file(output.replace('.shp','.geojson'))
            myshpfile.to_file(output)
            os.remove(output.replace('.shp','.geojson'))
            print(
                "Extracted a total of {} features: File written to {}".format(
                    len(li), output
                )
            )

    elif geometry is not None:
        with open(geometry) as f:
            js = json.load(f)
        with open(input, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                point = Point(float(row["longitude"]), float(row["Latitude"]))
                for feature in js["features"]:
                    polygon = shape(feature["geometry"])
                    if polygon.contains(point):
                        d = OrderedDict()
                        d["type"] = "Feature"
                        d["geometry"] = {
                            "type": "Point",
                            "coordinates": [
                                float(row["longitude"]),
                                float(row["Latitude"]),
                            ],
                        }
                        d["properties"] = {
                            "Country": row["Country"],
                            "Date": row["Date"],
                            "Location": row["Location"],
                            "Altitude": float(row["Altitude"]),
                            "Accuracy": float(row["Accuracy"]),
                            "Locust Type": row["Locust Type"],
                            "Area (ha)": float(row["Area (ha)"]),
                            "Flavour": row["Flavour"],
                            "Platform": row["Platform"],
                            "Language": row["Language"],
                            "Hopper Instar": row["Hopper Instar"],
                        }
                        li.append(d)
        d = OrderedDict()
        d["type"] = "FeatureCollection"
        d["features"] = li

        if output.endswith('.geojson'):
            with open(output, "w") as f:
                json.dump(d, f, indent=2)
            print(
                "Extracted a total of {} features: File written to {}".format(
                    len(li), output
                )
            )
        elif output.endswith('.shp'):
            with open(output.replace('.shp','.geojson'), "w") as f:
                json.dump(d, f, indent=2)
            myshpfile = gpd.read_file(output.replace('.shp','.geojson'))
            myshpfile.to_file(output)
            os.remove(output.replace('.shp','.geojson'))
            print(
                "Extracted a total of {} features: File written to {}".format(
                    len(li), output
                )
            )

def extract_from_parser(args):
    extract(input=args.input, output=args.output, geometry=args.geometry)


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Plant Village Survey Export: Simple CLI"
    )
    subparsers = parser.add_subparsers()

    parser_auth = subparsers.add_parser("auth", help="Saves your username and password")
    parser_auth.set_defaults(func=auth_from_parser)

    parser_locust = subparsers.add_parser("locust", help="Export locust survey data")
    required_named = parser_locust.add_argument_group("Required named arguments.")
    required_named.add_argument("--start", help="Start Date YYYY-MM-DD", required=True)
    required_named.add_argument("--end", help="End date YYYY-MM-DD", required=True)
    required_named.add_argument(
        "--country", help="Select country to get data or use 'all'", required=True
    )
    required_named.add_argument(
        "--report", help="full path to CSV report file", required=True
    )
    parser_locust.set_defaults(func=locust_from_parser)

    parser_extract = subparsers.add_parser("extract", help="Export and filter locust survey to geometry")
    required_named = parser_extract.add_argument_group("Required named arguments.")
    required_named.add_argument("--input", help="Path to input CSV survey data file", required=True)
    required_named.add_argument("--output", help="Path to output GeoJSON file or Shapefile", required=True)
    optional_named = parser_extract.add_argument_group('Optional named arguments')
    optional_named.add_argument('--geometry', help="Path to filter geometry as a GeoJSON", default=None)
    parser_extract.set_defaults(func=extract_from_parser)

    args = parser.parse_args()

    try:
        func = args.func
    except AttributeError:
        parser.error("too few arguments")
    func(args)


if __name__ == "__main__":
    main()
