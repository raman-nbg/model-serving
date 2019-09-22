# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
from . import configuration
import argparse

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'model-serving'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound


def _parse_args():
    parser = argparse.ArgumentParser(description='Model server for graduate admissions')
    parser.add_argument('-c',
                        '--configuration',
                        type=str,
                        help='Path to the application configuration file',
                        default=None)
    return parser.parse_args()


args = _parse_args()
config = configuration.Configuration(args.configuration)
