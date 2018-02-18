from cx_Freeze import setup, Executable
import sys, os

includes = []
include_files = [r"C:\Users\Equipo\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"C:\Users\Equipo\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"]
#base = 'Win32GUI' if sys.platform == 'win32' else None
base='Console'
os.environ['TCL_LIBRARY'] = r'C:\Users\Equipo\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Equipo\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(name="Calculo Por Prioridad",
	  version="1.0",
	  description="Programa para calcular",
	  options={"build_exe": {"includes": includes, "include_files": include_files}},
	  executables=[Executable("nuevo.py", base=base, icon="ico.ico")]
	)
