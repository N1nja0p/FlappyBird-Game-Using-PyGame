import cx_Freeze
import sys
import os 
base = None
if sys.platform == 'win32':
    base = "Win32GUI"
executables = [cx_Freeze.Executable("flappybird.py", base=base,icon="icon.png")]
cx_Freeze.setup(
    name = "FlappyBird Game By N1nja0p",
    options = {"build_exe": {"packages":["pygame","sys","random"], "include_files":['gallery','icon.png']}},
    version = "0.01",
    description = "FlappyBird Game By N1nja0p",
    executables = executables
    )
