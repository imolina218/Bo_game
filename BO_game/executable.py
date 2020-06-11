import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="BO_game",
      version="0.1",
      description="Riddle game",
      options={"build_exe": build_exe_options},
      executables=[Executable("Bo_game.py", base=base)])






