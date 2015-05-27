__author__ = 'yueeong'


#import testing infrastructure
import logging
import os, sys
import time
import yaml
from datetime import datetime
import unittest
from proboscis.asserts import assert_equal
from proboscis.asserts import assert_false
from proboscis.asserts import assert_raises
from proboscis.asserts import assert_true
from proboscis import SkipTest
from proboscis import test
from proboscis import before_class,after_class


#import custom modules
from LabElements import HTTP, HTTP_restapi
from Infrastructure import GenLogCollector


nowstamp = datetime.now()
timeNow = datetime.time(nowstamp)
dateNow = datetime.date(nowstamp)

CONSOLE_LOG_FILE = os.getcwd() + '/logs/' + 'tc_console.' + '{year}{month:02}{day:02}_{hour:02}{minute:02}'.format(year=dateNow.year, month=dateNow.month, day=dateNow.day, hour=timeNow.hour, minute=timeNow.minute) + '.log'

GenLogCollector.setup_file_logger('console_log',CONSOLE_LOG_FILE,True)
loggerCons = logging.getLogger('console_log')


@test(groups=['main.test'],depends_on_groups=['init'])
class Test1():
    @before_class
    def SetUp(self):
        loggerCons.info('Starting Testcase Setup')

        config_file = open('conf/config.yaml')
        config = yaml.safe_load(config_file)

        self.restendpoint1 = HTTP_restapi('target1',config)
        self.restendpoint2 = HTTP_restapi('target2',config)

        assert_equal(self.restendpoint1.getHTTP('/').status_code,200)

    @after_class(always_run=True)
    def TearDown(self):
        loggerCons.info('Test case teardown')
        pass

    @test(groups=['1'])
    def test_returns_what_i_sent(self):
        loggerCons.info('Test 1')
        some_dict_payload = { 'firstvalue': 'Hi there', 'secondvalue': 'bye bye'}
        results = self.restendpoint1.postHTTP('/post', some_dict_payload)
        assert_equal(results.json()['json']['firstvalue'],'Hi there')

    @test(groups=['2'],depends_on_groups=['1'])
    def test_enable_bar_debug(self):
        loggerCons.info('Test 2')
        some_dict_payload = { 'firstvalue': 'Hi there', 'secondvalue': 'bye bye'}
        results = self.restendpoint1.postHTTP('/post', some_dict_payload)
        assert_equal(results.json()['json']['secondvalue'],'bye1 bye')

