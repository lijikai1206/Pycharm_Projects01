#!c:\users\lijik\pycharmprojects\pythonfile\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pqi==2.0.6','console_scripts','pqi'
__requires__ = 'pqi==2.0.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pqi==2.0.6', 'console_scripts', 'pqi')()
    )
