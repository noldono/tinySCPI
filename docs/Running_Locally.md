# Running Locally
To run locally you'll need to do the following steps in order.

1. If you haven't already, install virtualenv
```bash
pip install virtualenv
```
2. Create a virtual environment called 'venv'
```bash
virtualenv -p python3 venv
```
3. Depending on your operating system, you'll need to run one of the following commands. Open either a PowerShell window (Windows) or terminal window (Mac/Linux) in the main project directory where the venv folder is located.

**Windows PowerShell**
```bash
\venv\Scripts\Activate.ps1
```
**Linux and Mac**
```bash
source venv/bin/activate
```
4. Ensure you are in the top level directory (where venv, tinyscpi, docs, etc. folders are located) and then execute this command in your terminal or powershell window to run your script you wrote in in run.py
```bash
python3 -m tinyscpi.run
```
