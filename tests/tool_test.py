# -*- coding: UTF-8 -*-

# Import from standard library
import mlproject
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    lon1, lat1, lon2, lat2 = (48.865070, 2.380009, 48.235070, 2.393409)
    distance = haversine(lon1, lat1, lon2, lat2)
    assert(round(distance)) == 70
