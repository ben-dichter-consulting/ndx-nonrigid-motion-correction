import os
from pynwb import load_namespaces, get_class
from os import path

name = 'ndx-nonrigid-motion-correction'

here = path.abspath(path.dirname(__file__))
ns_path = os.path.join(here, 'spec', name + '.namespace.yaml')

load_namespaces(ns_path)

NonrigidMotionCorrection = get_class('NonrigidMotionCorrection', name)


def local_interpolation(transform, image, npixels=1):
    """

    Parameters
    ----------
    transform
    image
    npixels: int

    Returns
    -------

    """
    pass


def nonrigid_motion_correction_apply(self, ts):
    """Apply transformation to TimeSeries

    Parameters
    ----------
    ts: pynwb.TimeSeries

    Returns
    -------

    """
    pass




NonrigidMotionCorrection.apply = nonrigid_motion_correction_apply