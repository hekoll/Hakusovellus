# -*- mode: python -*-
# -*- coding: utf-8 -*-

"""
This is a PyInstaller spec file.
"""

import os
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import is_module_satisfies
from PyInstaller.archive.pyz_crypto import PyiBlockCipher

# Constants
DEBUG = os.environ.get("CEFPYTHON_PYINSTALLER_DEBUG", False)
CIPHER_OBJ = None

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def get_pandas_path():
    import pandas
    pandas_path = pandas.__path__[0]
    return pandas_path


a = Analysis(
    ["HakuSovellus.py", "haku.py"],
    datas=[("index.html", "."),("isodata.sas7bdat","."), ("biologisetnaytteet.sas7bdat","."), ("biotiedot_kaikki_pitka.sas7bdat","."), ("lomaketiedot.sas7bdat",".")],
    hookspath=["."],  # To find "hook-cefpython3.py"
    cipher=CIPHER_OBJ,
    win_private_assemblies=True,
    win_no_prefer_redirects=True,
)


dict_tree = Tree(get_pandas_path(), prefix='pandas', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'pandas' not in x[0], a.binaries)


if not os.environ.get("PYINSTALLER_CEFPYTHON3_HOOK_SUCCEEDED", None):
    raise SystemExit("Error: Pyinstaller hook-cefpython3.py script was "
                     "not executed or it failed")

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=CIPHER_OBJ)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name="HKA Datatietoja",
          debug=DEBUG,
          strip=False,
          upx=False,
          console=DEBUG,
          icon="kettu_ja_kukka_pikkuinen_aGA_icon.ico")

COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=False,
        name="HKA Datatietoja")
