cd %1
pip install --upgrade --user pip
pip install --user -r requirements.txt
pyinstaller --onefile -w --icon=prehrajto_logo.ico --name=PTDL ptdl.pyw