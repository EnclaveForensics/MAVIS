from urllib import request
import json
import pandas as pd
import mongoengine as me
import numpy as np
from time import sleep

class Vulnerability(me.Document):
    cve_id = me.StringField()       #cve['id']
    published = me.StringField()    #cve['published']
    description = me.StringField()  #cve['descriptions'][0]['value']
    references = me.ListField(me.StringField()) #cve['references'] which is a list of objects

base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex="
me.connect('MAVIS', host='yggdrasil.enclaveforensics.com', port=27017)

last = 9999999999
start = 0
short_sleep = 60

while True:
    try:
        start = Vulnerability.objects.count()
        print(f'Starting from {start:,}')
    except:
        print("Database empty.. starting from zero.")
        start = 0

    with request.urlopen(url=f'{base_url}{start}', timeout=5) as content:
        data = json.loads(content.read())
        last = data['totalResults']
        print(f'Processing from {start:,} of {last:,}')
        num_remaining = last - start
        for vulnerability in data['vulnerabilities']:
            this = vulnerability['cve']
            Vulnerability(cve_id = this['id'],
                        published = this['published'],
                        description = this['descriptions'][0]['value'],
                        references = [json.dumps(i) for i in this['references']]).save()
    if num_remaining > 200:
        print(f'There are still {num_remaining:,} entries outstanding. Sleeping {short_sleep} seconds.')
        sleep(short_sleep)
    else:
        print(f'Caught up. Sleeping 3600')
        sleep(3600)