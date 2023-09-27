## System Commands
```
*IDN?
  Displays the information of the tinySA, including version

*RST
  Resets the tinySA. Will require a serial connection again.

*CLR
  Clears configuration data.

*TST
  Runs the tinySA diagnostics test.

*HLP
  Returns a list of all available tinySA USB serial commands
```

## Frequency Subtree
- Commands can be interpreted in "tree" format. So the first command in the list is FREQuency:START
- Only the uppercase letters in the command are needed. So ```FREQ:START``` would work. ```FREQuencyyyyy:START``` would also work too as the parser removes any lowercase letters
```
FREQuency:
	START
		arguments: A frequency between 0 and 350MHz [0M-350M]
		Sets starting frequency

	STOP
		arguments: A frequency between 0 and 350MHz [0M-350M]
		Sets stopping frequency 

	CENTer
		arguments: A frequency between 0 and 350MHz [0M-350M]
		Sets the center frequency 

	SPAN
		arguments: Integer value between 0 and 290
		Description still pending

	SPAN:ZERO
		arguments: none
    Sets the span to zero

	RBW
		rbw [3 | 10 | 30 | 100  | 300 | 600]
		Sets the resolution bandwidth to 3k, 10k , 30k
	RBW:AUTO
		rbw auto
	DUMP
		frequencies
```
