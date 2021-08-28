# This module help you filter system logs

## Usage

```bash
git clone git@github.com:francisizme/python-logs-filter.git
cd python-logs-filter
```
Make it executable

```bash
chmod +x ./find_errors.py

./find_errors.py $LOG_FILE$ [OUTUT_PATH OUTPUT_NAME]
```

## Example

Find error contain `cake pie` in the log file `sys.log`
```bash
./find_errors.py ~/var/logs/sys.log
>>> What is the error?
cake pie
```
As the output path and output name are not provided. The output file will be named `errors_found.log` as default and placed in the current directory
