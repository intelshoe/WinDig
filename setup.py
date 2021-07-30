from cx_Freeze import setup, Executable
  
setup(name = "WinDig" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("sysinfo.py")])