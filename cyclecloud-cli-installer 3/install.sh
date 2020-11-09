#!/bin/bash

set -eou pipefail

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Determine the python executable to use, if there is a python3 alias
# use that since it's what we require otherwise default to python
if command -v python3 > /dev/null ; then
    python_bin="python3"
elif command -v python > /dev/null; then
    python_bin="python"
else
    echo "ERROR: Missing a Python installation, please install Python 3.7+ before proceeding"
    exit 1
fi

$python_bin "${CURRENT_DIR}/install.py" "$@"
