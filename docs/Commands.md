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

## Display Subtree
```
DISPlay
	PAUSE
		arguments: none
		Pauses the sweeping in either input or output mode indefinitely.

	RESUME
		arguments: none
		resumes the display/sweep

	COLOR?
		arguments: none
		Dumps the colors used.

	COLOR [0 - 30] [0x000000 - 0xFFFFFF]
		arguments: [value between 0-30] [RGB hex value between 0x000000 and 0xFFFFFF]
		Changes the color of various parts of the display, each number 0-30 represents a different part of the tinySA display. Some of which are not immediately visible.
	
	SWEEPTIME [0 - 10]
		arguments: [value between 0 and 10]
		Sets the target time to complete 1 sweep time in seconds.

	TOUCH:PUSH [0 - 320] [0 - 140]
		arguments: [value between 0 - 320] [value between 0 - 140]
		Emulates the action of touching and holding on the tinySA screen. Top left is 0,0. Screen is 320x240 pixels.

	TOUCH:RELEase
		arguments: none
		Emulates a release of a touch on the tinySA screen

	SPUR {on|off}
		arguments: [on or off]
		Enables / disables spur removal
```

## Marker Subtree
```
MARKer:
	FREQuency [src:1-4] [dst:frequency_range]
		arguments: [src:1-4] [dst:frequency_range]
		Places marker `src` on `freq` Hz in the trace. Note that dst has to be in raw numbers in Hz or in 
		units of k, M, G and in valid frequency range.. 

	DELTa [src:1-4] [dst: 1-4] 
		arguments: [src:1-4] [dst:1-4]
		Subtracts frequency and power level in units from `dst` to `src` and displays on the tinySA as a
  		‘delta' mode. Does not return values. For that, see DIFFerence.

	DELTa:OFF [src:1-4]: 
		arguments: [src:1-4]
		Turns off the delta mode on the selected marker `src`, if on. 

	NOISe:SET [src:1-4]
		arguments: [src:1-4]
		Sets `src` marker as the noise marker

	NOISe:OFF [src:1-4]
		arguments: [src:1-4]
		Unsets the `src` marker as the noise marker

	TRAcK:SET [src:1-4] 
		arguments: [src:1-4]
		Sets the marker of `src` to tracking mode- i.e. tracking the largest signal in the sweep

	TRAcK:OFF [src:1-4] 
		arguments: [src:1-4]
		Unsets the marker from track mode and fixes it to the frequency it was at.

	TRACe [src:1-4] [dst:1-3] 
		arguments: [src:1-4] [dst: 1-3]
		Assigns marker `src` to the trace `dst`

	AVERage:SET [src:1-4] 
		arguments: [src:1-4]
		Sets the marker to display the current trace’s average 

	AVERage:OFF [src:1-4] 
		arguments: [src:1-4]
		Unsets the marker to display the current trace’s average

	SeaRCH:
		PEAK [src: 1-4]
			arguments: [src:1-4]
			Sets `src` marker to global maximum. Note this returns a serial output.

		FREQuency [src: 1-4] [freq: in frequency range]
			arguments: [src: 1-4]
			Sets marker `src` to a specific frequency. Keep in mind that `freq` has to be a valid frequency, more than 10kHz otherwise anything entered 0-290 will be treated as an index instead (needs input 
                        checking).

	DELete [src: 1-4]
		arguments: [src: 1-4]
		Removes marker `src` from display.

	ReSeT 
		arguments: none
		Removes all markers from display

	DIFFerence [src:1-4] [dst:1-4]
		arguments: [src:1-4] [dst:1-4]
		This, unlike DELT, returns the difference data to the user.
```

## Measure Subtree
```
MEASure: 
	OFF
		arguments: none
		switches off any measurement related setting and behavior and returns the tinySA to regular operation

	HARMonic [frequency of fundamental]
		arguments: [frequency]
		switches to a marker configuration for measuring the level of harmonics of a signal frequency of fundamental is the lowest frequency of a periodic waveform

	OIP3 (output third order intermodulation) [frequency of left signal] [frequency of right signal]
		arguments: [frequency of left signal] [frequency of right signal]
		switches to a marker configuration for measuring the Output IP3 level of a signal configures itself with a span of five times the difference in frequency and the center at the average of the two frequencies

	PHase NOIse (PHNOI) [frequency of signal] [frequency offset]
		arguments: [frequency of signal] [frequency offset]
		switches to a marker configuration for measuring phase noise of a signal. Shows the noise spectrum that is seen spreading out on either side of a signal

	SNR [frequency of signal] [bandwidth]
		arguments: [frequency of signal] [bandwidth]
		switches to a marker configuration for SNR measurement ratio between the desired information or the power of a signal and the undesired signal or the power of the background noise. in unit calculator to find 
                the desired SNR through logarithms

	3DB
		arguments: none
		switches to a marker configuration for -3dB width measurement.

	AM [frequency of signal] [modulation frequency: 3-10k Hz]
		arguments: [frequency of signal] [modulation frequency: 3-10k Hz]
		sets various settings to optimize observations of an AM modulated signal

	FM [frequency of signal] [modulation frequency: 1-2.5k Hz]
		arguments: [frequency of signal] [modulation frequency: 1-2.5k Hz]
		sets various settings to optimize observations of an FM modulated signal

	THD (Total Harmonic Distortion)
		arguments: none
		enables the measurement of the THD defined as the percentage of energy in the harmonics versus the energy in the fundamental. Looks at the output spectrum and observes values of the second, third, fourth, 
                etc., harmonics with respect to the amplitude of the fundamental signal

	CHannel POWer (CHPOW) [channel frequency] [channel width]
		arguments: [channel frequency] [channel width]
		Enables ACP (adjacent channel power) and channel power measurement. Measures the power leakage from carrier channels into the neighboring frequency channels

	LINEar
		arguments: none
		steps the internal attenuator through all attenuation levels and draws a green line showing the measured maximum level for each attenuation setting.

	DUMP [id:0-2]
		arguments: [id:0-2]
		Dumps all information related to trace data, id 0 for temporary data, 1 for stored trace, 2 for measurement.

```
