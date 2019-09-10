# registration
Contains a script to alert the user when a course at Brown University has available seats.

## Dependencies
- [Selenium](https://www.seleniumhq.org/) to automate the web browsing.
    - Recommended to install via [pip](https://pypi.org/project/pip/) with command `pip3 install --user selenium`.
- [Chromedriver](https://chromedriver.chromium.org/) for checking CAB.
- [Sox](http://sox.sourceforge.net/) for output audio.
    - Pre-installed on Linux

## Configuration
You must first change the `COURSE` constant in `registration.py` to reflect the course you want to check. Next you must change the `CHROMEDRIVER_PATH` path to point to the Chromedriver executable.

## Execution
```
usage: registration.py [-h] [--no_headless]

optional arguments:
  -h, --help     show this help message and exit
  --no_headless  Disable headless browsing for debugging.
```
The `no_headless` flag will display Chrome as the script runs. Recommended to use initially to ensure the automation is working properly.
