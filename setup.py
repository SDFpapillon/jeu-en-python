import sys, os

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "includes": ["pygame", "pygame.base"]
                     }


# build_exe_options = {'packages': ['os', 'tkinter', 'matplotlib.backends.backend_svg', 'subprocess'],
#                      'namespace_packages': ['mpl_toolkits'],
#                      'include_files':['input3.json', 'SF.xlsx', 'SF logo.ico', 'Operative Temperature.pkl',
#                                       'Rect_icon.png', 'Soltissim logo.png', 'SF full logo.jpg', 'IES logo.jpg']}
#
#


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

if sys.platform == "win32":
    base = "Win32GUI"

#if sys.platform == "win64":
 #   base = "Win64GUI"



setup(  name = "jeu",
        version = "0.1",
        description = "Mon super jeu!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)]
        )