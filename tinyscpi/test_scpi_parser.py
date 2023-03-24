from scpi_parser import SCPI_Parser

# Create an instance of the SCPI_Parser class
parser = SCPI_Parser()

#########################################
# Test 1: Test the tinySA info command:

# Send the *IDN? command to the parser and get the result
result = parser.parseCommand("*IDN?")

# Verify that the result is the expected instrument ID
if result == "tinySA_v1.3-506-g8291e1e":
    print("Test passed!")
else:
    print("Test failed. Expected 'tinySA_v1.3-506-g8291e1e', but got:", result)

#########################################
# Test 2: Test the tinySA version command:

result2 = parser.parseCommand("SYSTem:VERSion?")
# Verify that the result is the expected instrument ID
if result2 == "tinySA_v1.3-506-g8291e1e":
    print("Test passed!")
else:
    print("Test failed. Expected 'tinySA_v1.3-506-g8291e1e', but got:", result2)

#########################################
# Test 3: Test the tinySA vbat command
result3 = parser.parseCommand("MEASure:VOLTage:DC?")
print("Test 3 Result: ", result3)
