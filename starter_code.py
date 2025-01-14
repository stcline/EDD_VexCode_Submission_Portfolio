#region VEXcode Generated Robot Configuration

# Brain should be defined by default
brain=Brain()

# Robot configuration code


# wait for rotation sensor to fully initialize
wait(30, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# Library imports
from vex import *

# Begin project code
