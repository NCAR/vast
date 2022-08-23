#!/usr/bin/env python
import argparse
from binstar_client.utils import get_server_api
import binstar_client.errors

import os
import sqlite3
import sys

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

packages = ['geocat-comp', 'geocat-f2py', 'geocat-datafiles', 'geocat-viz', 'ncl', 'pynio', 'pyngl', 'uxarray', 'wrf-python']
conda_channels = ['conda-forge', 'ncar']

if args.packages:
    packages = args.packages

for package in packages:
    package_total_dls = 0
    for conda_channel in conda_channels:
        #db_table = "%s_%s" % (package, conda_channel)
        db_table = package.replace('-', '')

        aserver_api = get_server_api(log_level=0)
        try: package_obj = aserver_api.package(conda_channel, package)
        except binstar_client.errors.NotFound: continue
        try:
            c.execute('''CREATE TABLE %s (channel text, version text, build text, platform text, arch text, pyversion text, npversion text, uploaded_date date, downloads int, check_date datetime default CURRENT_TIMESTAMP)''' % db_table)
            conn.commit()
        except sqlite3.OperationalError:
            pass
        for version_str in package_obj['versions']:
            version = aserver_api.release(conda_channel, package, version_str)
            for d in version['distributions']:
                #distribution_os = d['attrs']['operatingsystem']
                distribution_os = d['attrs']['platform']
                #distribution_arch = d['attrs']['arch']
                distribution_arch = d['attrs']['machine']
                distribution_build = d['attrs']['build']
                distribution_downloads = d['ndownloads']
                distribution_upload_time = d['upload_time']

                # detect numpy and python versions
                np_version = None
                py_version = None
                for item in d['dependencies']['depends']:
                    try:
                        if item['name'] == 'numpy':
                            np_version = item['specs'][0][1]
                        if item['name'] == 'python':
                            py_version = item['specs'][0][1]
                    except: pass
                #for key in d.keys():
                #    print "%s: %s" % (key, d[key])
                #sys.exit(0)
                c.execute('''INSERT INTO %s (channel, version, build, platform, arch, pyversion, npversion, uploaded_date, downloads) VALUES (?,?,?,?,?,?,?,?,?)''' % db_table,
                             (conda_channel, version_str, distribution_build, distribution_os, distribution_arch, py_version, np_version, distribution_upload_time, distribution_downloads))
                conn.commit()
conn.close()
