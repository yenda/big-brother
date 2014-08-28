__author__ = 'yenda'

import os

class API(object):
    def connect(self):
        pass

    def disconnect(self):
        pass

    def set_project(self):
        pass

    def get_activities(self):
        pass

    def get_resources(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources.xml')
        with open(path, "r") as f:
            resources = f.read()
            return resources