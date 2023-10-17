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
### Read before continuing:
- Commands can be interpreted in "tree" format. So the first command in the list is FREQuency:START
- Only the uppercase letters in the command are needed. So ```FREQ:START``` would work. ```FREQuencyyyyy:START``` would also work too as the parser removes any lowercase letters
```
FREQuency:
	START [0M-350M]
		arguments: A frequency between 0 and 350MHz [0M-350M]
		Sets starting frequency

	STOP [0M-350M]
		arguments: A frequency between 0 and 350MHz [0M-350M]
		Sets stopping frequency 

	CENTer [0M-350M]
		arguments: A frequency between 0 and 350MHz [0M-350M]
		Sets the center frequency 

	SPAN [0-290]
		arguments: Integer value between 0 and 290
		Description still pending

	SPAN:ZERO
		arguments: none
		Sets the span to zero

	RBW [3 | 10 | 30 | 100  | 300 | 600]
		arguments: One of the following values: [3 | 10 | 30 | 100  | 300 | 600]
		Sets the resolution bandwidth to 3k, 10k, 30k, etc.

	RBW:AUTO
		arguments: none
		Sets the resolution bandwidth to "auto" mode
	DUMP
		arguments: none
		Dumps a list of the frequencies being analyzed on the tinySA.
	IF:AUTO
		if [0 | 433M - 435M]
		Expert Feature: sets the intermediate frequency to a dynamic value (0) or a specific value

	SCAN:FREQ
		arguments: [start frequency] [stop frequency]
		Outputs all frequencies being sampled over 290 points between the start and stop frequency

	SCAN:MEASure
		arguments: [start frequency] [stop frequency]
		Outputs 290 signal strength values between the start and stop frequency

	SCAN:STORed
		arguments: [start frequency] [stop frequency]
		Outputs 290 signal strength values along with some stored values.
```

## System Subtree
```
SYSTem:
	DAC
		arguments: none
		Dumps the current value of the dac (0-4095). Could be used to listen to signals on the tinySA.

	ID
		arguments: none
		Returns the id of the current device

	VERSion
		arguments: none
		Returns the firmware version

	VBAT
		arguments: none
		Returns the tinySA’s battery voltage

	MODE:LOW
		arguments: [input | output]
		Sets tinySA to low input or low output mode

	MODE:HIGH
		arguments: [input | output]
		Sets tinySA to high input or low output mode

	OFFSet
		arguments: [0-4095]
		Returns or sets the offset of the tinySA battery voltage

	SAVE
		arguments: [0-4]
		Saves the current settings to a preset

	SaveCONFig
		arguments: none
		Saves the current configuration of the tinySA

	TouchCAL
		arguments: none
		Starts the touch calibration process

	TouchTEST
		arguments: none
		Starts the touch test

	THREads
		arguments: none
		Lists information about the system’s threads

	SelfTEST
		arguments: none
		Performs a complete selftest of the system
```

## Level Subtree
```
LeVeL:
	ATTenuate [0dB - 30dB]
		arguments: [value between 0 and 30dB]
		In dB. Controls internal attenuation.

	ATTenuate:AUTO
		arguments: none
		Automatically controls internal attenuation. On by default. 

	REFerence [Float Value]
		arguments: Any float value between the minimum and maximum float value.
		Sets the reference value for display with respect to current unit
	
		Example: Current units are in dBm, then `LEVEL:REF -5` will set the reference level to -5 dBM and shift the display lower and upper boundaries seem to accommodate up to like 1x10^9, but wouldn’t be that  	 
                meaningful when it comes to levels since accepting a signal that will reach those boundaries will  break the tinySA first.
	 	
	REFerence:AUTO
		arguments: none
		Automatically sets the reference value (top of screen). On by default.

	SCALe [1 | 2 | 5 | 10 | 20]
		arguments: one of the above numbers
		In decibels, still scales by decibels even when units are different. Basically the # of units between each square.

	SCALe:AUTO
		arguments: none
		Automatically sets the scale

	UNITs {dBm|dBmV|dBuV|V|W}
		arguments: one of the above units
		Sets the tinySA trace units display. Note that raw mode is not available.
		`trace RAW` is served to display raw data, normally not accessible 

	(LVL:XGAIN) eXternal_GAIN [-100 … 100] 
		arguments: [value between -100 and 100]
		Sets a digital external gain offset to display. Does not control internal attenuation and is used for
		display / calculation purposes only.
```

## Trigger Subtree
```
TRIGger:
	TYPE:AUTO
		arguments: none
		Normal spectrum analyzer scanning mode, triggering is not active.

	TYPE:NORMal
		arguments: none
		Displays a new scan as soon as a signal in the scan causes a trigger event.

	TYPE:SiNGLe
		arguments: none
		Waits for a signal to cause a trigger event and display the scan. 
		Restart the waiting for an event by activating SINGLE again.

	LeVeL [signal strength]
		arguments: [signal strength value in the device's current unit]
		Enters the trigger level. Trigger level is shown as a blue line. In current units 
		I.e. current LVL:UNIT is dBm, then entering -90 as src will set trigger level at -90 dBm

```

## Trace Subtree
```
TRACe:
	FREeZe:
		ON [1-3]
			arguments: [value between 1 and 3]
			Freezes the trace of [1-3]. Note that this does not stop the sweep.

		OFF [1-3]
			arguments: [value between 1 and 3]
			Unfreezes the trace of [1-3]. Note that this does not resume the sweep. 

	VIEW:ON [1-3]
		arguments: [value between 1 and 3]
		Turns a trace on

	VIEW:OFF [1-3]
		arguments: [value between 1 and 3]
		Turns a trace off
	
	COPY [src:1-3] [dst:1-3]
		arguments: [value between 1 and 3] [value between 1 and 3]
		Copies the trace data of [src] to [dst]

	SUBtract:[src:1-3] [dst:1-3]
		arguments: [value between 1 and 3] [value between 1 and 3]
		Subtracts [src] by the [dst] amount. If [src] == [dst] then nothing happens.

	SUBtract:OFF
		arguments: [value between 1 and 3] [value between 1 and 3]
		Turns the subtraction off, reverts to previous readings.
```
