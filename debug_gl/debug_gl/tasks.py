from __future__ import absolute_import

from celery import shared_task
import graphlab

@shared_task
def simple():
    print('simple task')
    return True

@shared_task
def test_et():
    import xml.etree.ElementTree as ET
    print('test_et')
    fpath = '/vagrant/test_file.xml'
    t = ET.parse(fpath)
    print('--- t', t)
