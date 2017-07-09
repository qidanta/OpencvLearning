from cx_Freeze import setup, Executable

setup(name = "reandurllib" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("train_annotate_folder.py")])