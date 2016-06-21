BDM/Scholz Expected Uility Model
=================================

A Python implementation of [Scholz, Calbert &amp; Smith (2011)](http://jtp.sagepub.com/content/23/4/510), an attempt to replicate Bruce Bueno de Mesquita's expected utility model for political forecasting.

Original: https://github.com/jmckib/bdm-scholz-expected-utility-model

Changes by David Masad:

- Update to Python 3
- Make terminal output optional
- Enable logging to file

## Command line
usage: python bdm_scholz_model.py [-h] [--verbose] [--log LOG] csv_path num_rounds

positional arguments:
  csv_path    path to csv with input data
  num_rounds  number of rounds of simulation to run

optional arguments:
  -h, --help  show this help message and exit
  --verbose   Output the model dynamics to the terminal.
  --log LOG   Path to log the model run to.

**Example:**

    python bdm_scholz_model.py ExampleActors.csv 10 --verbose --log Example.log

