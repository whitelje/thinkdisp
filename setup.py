#!/user/bin/env python
from distutils.core import setup

setup(name='Thinkdisp',
      version='1.3.1',
      description='Display Manager for Thinkpads with Optimus',
      author='Sagar Karandikar',
      author_email='apps@sagark.org',
      url='http://sagark.org/thinkdisp/',
      packages=['thinkdisputil'],
      scripts=['thinkdisp'],
      data_files=[('/etc/thinkdisp', ['config/config.ini']),
                  ('/etc/xdg/autostart', ['thinkdisp.desktop']),
                  ('/usr/bin', ['scripts/killdisp']),
                  ('/usr/bin', ['scripts/thinkdisp-fix-permissions'])
                 ]
     )
