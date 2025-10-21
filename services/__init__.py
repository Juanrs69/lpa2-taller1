import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC_SERVICES = os.path.join(ROOT, 'src', 'services')

if os.path.isdir(SRC_SERVICES):
    __path__ = [SRC_SERVICES]
else:
    __path__ = [os.path.dirname(__file__)]
