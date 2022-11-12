# silkexercise
Silk Security exercise problem


This exercise contains a main script called runner.py. 
Usage:
./runner.py -j -> Creates 100 JIRA tickets randomly over a period of 1 hour.
./runner.py -s -> Stores 'High' and 'Highest' jira tickets into a db.
./runner.py -p -> Plots a bar graph counting open jira tickets.

There are interfaces for managing:
    2.1. database: A helper to interact with a db. SQLITE is used in this example.
    2.2. ticketing: A helper to interact with a ticketing system. JIRA is used in this example.
    2.3. visualizer: A helper to interact with a plotting library. matplotlib is used in this example and writes to an output file.


Future enhancements possible:
1. Unit test addition.
2. Create a factory class for each interface and use the implementation to be specific to that abstract class.
3. Support for different types of ticketing, db and visualizer functionalities.
