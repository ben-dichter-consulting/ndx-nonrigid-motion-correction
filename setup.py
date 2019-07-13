# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages
from shutil import copy2

setup_args = {
    'name': 'ndx-nonrigid-motion-correction',
    'version': '0.1.0',
    'description': 'General framework for storing nonrigid motion correction of optical imaging in NWB:N 2.0',
    'author': 'Ben Dichter',
    'author_email': 'ben.dichter@gmail.com',
    'url': '',
    'license': 'BSD 3-Clause',
    'install_requires': [
        'pynwb'
    ],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_nonrigid_motion_correction': [
        'spec/ndx-nonrigid-motion-correction.namespace.yaml',
        'spec/ndx-nonrigid-motion-correction.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-nonrigid-motion-correction.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-nonrigid-motion-correction.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_nonrigid_motion_correction', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
