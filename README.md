# tinySCPI
A Python library that enables the use of SCPI commands on the tinySA.

See the [Commands](https://github.com/noldono/tinySCPI/blob/main/docs/Commands.md) documentation for each command and a description.

# Table of Contents

1. [**Getting Started**](#getting-started)
2. [**Dependencies**](#dependencies)
3. [**Unit Testing**](#unit-test)
4. [**Coverage**](#coverage)
5. [**Contact Us**](#contact)
6. [**Safety**](#safety)
7. [**Output**](#output) 

## Getting Started <a name="getting-started"></a>
1. Create a new Python file.
2. In your terminal/command line, install the tinySCPI library by typing `pip install tinyscpi`
3. Copy and paste the below code into your Python file.
```python
from tinyscpi import tinySCPI

print(tinySCPI.user_input("*IDN?"))
```
4. Connect the tinySA device to your computer via USB. Your device should have come with said cable.
5. Run the file using the line below. Ensure your command-line/terminal is in the same path as your Python file!
```
python3 <name_of_your_file>.py
```
This should return something similar to this, it will usually be specific to your device but in a similar format:
```
Running info 
tinySA v0.3
2019-2022 Copyright @Erik Kaashoek
2016-2020 Copyright @edy555
SW licensed under GPL. See: https://github.com/erikkaashoek/tinySA
Version: tinySA_v1.3-506-g8291e1e
Build Time: Nov 28 2022 - 14:01:16
Kernel: 4.0.0
Compiler: GCC 7.2.1 20170904 (release) [ARM/embedded-7-branch revision 255204]
Architecture: ARMv6-M Core Variant: Cortex-M0
Port Info: Preemption through NMI
Platform: STM32F072xB Entry Level Medium Density devices
ESD protected
```
6. Now you're ready to execute any of the commands located in the [Command Tree](https://github.com/noldono/tinySCPI/blob/main/docs/Commands.md)!

- If you're looking for a taste of what you're capable of with tinySCPI, see this [Example Script](https://github.com/noldono/tinySCPI/blob/main/examples/example_script.txt)
- To see what other functions are a part of our library see the [Class Documentation](https://github.com/noldono/tinySCPI/blob/main/docs/Class_Documentation.md)

## Dependency: <a name="dependencies"></a>
tinySCPI requires python >= 3.6, pyserial, pytest, and pytest-cov

```pip install pyserial```
```pip install pytest```
```pip install pytest-cov```

## Unit Test: <a name="unit-test"></a>
```pytest``` is required to execute unit tests.

You can install pytest library by typing `pip install pytest` in your terminal/command line

You can execute unit tests by typing `pytest` in your terminal/command line root directoryscpi`

## Coverage: <a name="coverage"></a>
`pytest` and `pytest-cov` are required to execute code coverage analysis. 

You can install pytest andn pytest-ocv library by typing `pip install pytest pytest-cov` in your temrinal/command line.

You can execute unit tests by typing `pytest --cov-config=.coveragerc --cov=tinyscpi tinyscpi/tests/ --cov-report html`

After the execution you will be able to find the coverage report at `./htmlcov/index.html`

## Contact Us: <a name="contact"></a>
Email: tinyscpi@vt.edu

## Safety: <a name="safety"></a>
Like with all RF devices, there involves some risk in operation. For more information, please refer to [Safety](https://github.com/noldono/tinySCPI/blob/main/SAFETY.md).

## Output: <a name="output"></a>
On older firmware, output mode control over serial may not be stable and can return the "FATAL ERROR" message on screen. [Updating to a newer firmware](https://github.com/noldono/tinySCPI/blob/main/docs/tinySA_Firmware_Update_Manual.pdf) seems to resolve this issue.
