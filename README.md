# Related-Collections


## Pyinstaller

1. Navigate to the directory that contains your Python script
    - `cd /path/to/your/script`
2. Install pyinstaller
    - `pip install pyinstaller`
3. Create a standalone executable file using pyinstaller
    -  `pyinstaller --onefile --name name_0_0_1 your_script_name.py`
4. The executable file will be created in a dist directory in the same location as your script
5. Distribute the executable file to users who don't have Python installed



## Input Format

1. The Excel sheet should have a column named `Title` in the first column and a column named `URL` in the second column. 
2. The sheet can have additional columns, but they will be ignored. 
3. If the sheet is named template, it will be given precedence over Sheet 1.