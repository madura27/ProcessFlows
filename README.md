
# Assumptions
Program assumes that the logs in the input_flow_logs.txt are in default log format, not custom and the only version that is supported is 2.

Port/Protocol count assumes DestinationPort/Protocol and not SourcePort/Protocol combination

Protocol names in the lookup tables are assumed to be valid.

# Code Layout
All the python code is under src/ directory

Unit Tests are under test/ directory

Input files are under input_files/directory

Generated Output files are under output_files/directory

# Instructions to Run
cd src

make run

# Tests
UTs are written with pytest.
To run the UTs:

cd src

make test

# Clean output_files directory

make clean : Deletes the output files in the output_files directory

Happy reviewing!




