## Function Documentation for the tinySCPI Object

### `user_input(input_cmd: str) -> str:`
This function processes a given input command, converts it into USB communication protocol format, and sends it to the tinySA.

- **Parameters:**
    - `input_cmd` (`str`): A string representing the input SCPI command.

- **Returns:**
    - `str`: Represents the status or response after sending the command to the device.

### `execute_from_file(filepath: str) -> None:`
This function reads a text file containing a list of SCPI commands and executes these commands one by one using the `user_input` function.

- **Parameters:**
    - `filepath` (`str`): A string representing the file path to the file containing a list of commands.

- **Returns:**
    - `None`

### `capture() -> str:`
This function triggers the SCPI device to capture a screenshot or an image. Alternatively, one may use the `CONF:CAPT` SCPI command to perform the same action.

- **Returns:**
    - `str`: Represents the status or information about the success of capturing the screenshot.

### `scan_raw_points(savedata: bool, start_freq: int, stop_freq: int, num_points: int) -> str:`
This function instructs the SCPI device to conduct a raw data scan within a specified frequency range and a given number of data points. It also provides an option to save the data to a CSV file.

- **Parameters:**
    - `savedata` (`bool`): A boolean indicating whether to save the data to a CSV file.
    - `start_freq` (`int`): An integer representing the starting frequency for the scan.
    - `stop_freq` (`int`): An integer representing the stopping frequency for the scan.
    - `num_points` (`int`): An integer representing the number of data points to be scanned.

- **Returns:**
    - `str`: If `savedata` is `True`, it returns a success message after saving the data to a CSV file. Otherwise, it returns the raw data obtained from the scan.
 
