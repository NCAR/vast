import argparse
from binstar_client.utils import get_server_api
import binstar_client.errors

import os
import sqlite3
import sys
import yaml

# detect script dir
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# determine db_file
parser = argparse.ArgumentParser(description='Generate conda metrics.')
parser.add_argument('-d', '--database-file', dest='db_file',
                    help='conda_metrics database file',
                    default=os.path.join(dname, 'conda_metrics.db'))
parser.add_argument('packages', nargs='*', help='Optional package list')
args = parser.parse_args()

# set up sqlite
conn = sqlite3.connect(args.db_file)
c = conn.cursor()

packages_file = 'data/packages.yml'
with open(packages_file) as f:
  packages_dict = yaml.load(f, Loader=yaml.CLoader)
packages = [i['package-name'] for i in packages_dict['packages']]
conda_channels = ['conda-forge', 'ncar']

if args.packages:
    packages = args.packages

download_list = []
for package in packages:
    package_total_dls = 0
    for conda_channel in conda_channels:
        db_table = package.replace('-', '')

        aserver_api = get_server_api(log_level=0)
        try: package_obj = aserver_api.package(conda_channel, package)
        except binstar_client.errors.NotFound: continue
   
        for version_str in package_obj['versions']:
            version = aserver_api.release(conda_channel, package, version_str)
            for d in version['distributions']:
                distribution_downloads = d['ndownloads']\
                
                download_list.append(distribution_downloads)

downloads = sum(download_list)

metrics_file = 'data/metrics.yml'
with open(metrics_file, 'r+') as f:
  metrics_dict = yaml.load(f, Loader=yaml.CLoader)
metrics_dict['counter_item'][0]["number"] = downloads
with open(metrics_file, 'w') as f:
  yaml.dump(metrics_dict, f)
