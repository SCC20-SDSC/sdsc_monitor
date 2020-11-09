$ErrorActionPreference = "Stop"

function choco-install-python() {
    if ((Get-Command "choco.exe" -ErrorAction SilentlyContinue) -ne $null){
        Write-Host "Python can be installed via chocolatey with the command: 'choco install python'"
    }
}

function fail-if-missing-python() {
    if ((Get-Command "python.exe" -ErrorAction SilentlyContinue) -eq $null){
        Write-Host "ERROR: Missing a Python installation, please install Python 3.7+ before proceeding."
        choco-install-python
        exit 1
    }
}

fail-if-missing-python
python $PSScriptRoot/install.py $args
