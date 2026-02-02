# Hydraulic Pump Continues To Run
**Source:** `docs/source_pdfs/troubleshooting_guide.pdf`  
**Pages:** 44–58

---

--- PAGE 44 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16
3. HYDRAULIC PUMP CONTINUES TO RUN
Possible Causes:
• Faulty Pressure Switch
• Faulty Relay
• Faulty Jettison Solenoid
• Faulty Jettison Switch
• Faulty Doors Switch
3.1 - QUICK CHECK
The most common problem is the Pressure Switch failing. Continue with ‘Hydraulic Pressure
Check’ below. (para. 3.2.1)
DO NOT throw Pressure Switch’s away as they may only need re-adjustment. See para. 3.9
- Pressure Switch Adjustment to adjust Pressure Switch setting.
3.2 – HYDRAULIC PRESSURE CHECK
3.2.1 - Q – What is the hydraulic pressure when the Hydraulic Pump is running?
With the system turned ON, check the Pressure Gauge on the hydraulic system to check the
hydraulic pressure. (see pic 24)
HIGH – If the pressure is sitting above 1200psi, then the problem is likely to be - either the
Pressure Switch, a Hydraulic Pump Relay, or the Doors Switch. Continue with ‘Pressure
Switch Check’ below. (para. 3.3.1)
MEDIUM – If the pressure is sitting between 850psi - 1200psi, then the problem is possibly
the Hydraulic Pump output pressure being too low. Re-set the output pressure and re-try
(see ‘Hydraulic Pump Output Pressure Adjustment’ – para. 3.8.1 ) With the Hydraulic Pump
output pressure set correctly and the Pressure Switch re-connected, the pressure should be
sitting in the normal operating range (850-1150psi) and the Hydraulic Pump should stop
running. If not, continue with ‘Pressure Switch Check’ below. (para. 3.3.1)
LOW – If there is very little pressure built up in the system, then it is likely to be the Jettison
Solenoid/Valve or Jettison Switch. Continue with ‘Jettison Solenoid Check’ (para. 3.5.1)

--- PAGE 45 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

Pic 24


3.3 - PRESSURE SWITCH CHECK
3.3.1 - Q – Does the Hydraulic Pump continue to run if you remove the wire from the ‘low
pressure’ contact off the Pressure Switch, and with the system turned ON? (see pic 22 and
Diagram 6.9)
Stauff Pressure Switch - Terminal 2
Isolair Pressure Switch - Green Wire
Removing this wire will break the control circuit (power) to the Hydraulic Pump Power Relay
(new style 214 tanks).
Yes – Pressure Switch may be fine, and the problem may be with either Hydraulic Pump Power Relay.



New style 214 tank and 204 tank – continue with ‘Hydraulic Pump Power Relay Check’ (para 3.4.2)
No – Likely to be a faulty Pressure Switch. Change the Pressure Switch and re-check system.
The faulty Pressure Switch may just need re-setting. DO NOT throw pressure switch away.
To adjust Pressure Switch setting, see ‘Pressure Switch Adjustment’ (para 3.9.1) Ensure that
the new Pressure Switch is sealed well from water ingress - use DC4 silicone grease.

Pressure Gauge

--- PAGE 46 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16


Power Relay check
3.4.2 - Q – Is there continuity between the two large power terminals of the Hydraulic Pump
Power Relay when the system is turned OFF? (see pic’s 25 and 26)
There should only be continuity between these two large terminals when there is a ground
and power to the respective small control terminals. When the system is off, there will not
be a power present at the control terminals, therefor the Hydraulic Pump Power Relay
should not be energised and therefore not have continuity across the two large terminals.
Yes – The relay is faulty, replace relay and re-check system. (ensure to use a 200amp relay
P/N - 24214)
No – Power relay is fine - continue with ‘Jettison Solenoid Check’ (para 3.5.1)
Pic 25





Power Relay
Large Power
output/input
terminals
Small Control terminals

--- PAGE 47 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

Pic 26



3.5 - JETTISON SOLENOID CHECK
3.5.1 - Q - Is there both a ground and power (24v-28v) at respective terminals of the Jettison
Solenoid when the system is turned on?
Remove either the cap from the back of the Jettison Solenoid coil, or the two wires that
connect directly to the Solenoid Coil terminals, and check for both a ground and power at
each respective wire or terminal inside the cap. (see pic 27)
Yes- Wiring is fine. Replace the cap or wires, and check system again. If pump continues to
run and the hydraulic pressure is high, continue with the ‘Doors Switch Check’ (3.6.1) If the
pump continues to run and the hydraulic pressure is low, continue with ‘Jettison Solenoid
Check’ in Part 4 – “Uncommanded Door Opening” (para. 4.2.2)
No-
No
power-
Continue
with
‘Jettison
Switch
Check’.
(para.
3.7.1)
No ground – check ground wiring to Jettison Solenoid.



New style 214 tank
Hydraulic pump
power relay


--- PAGE 48 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

Pic 27





3.6 - DOORS SWITCH CHECK
3.6.1 - Q- Is there continuity between pins 9 and 4 on the Cyclic Controller plug (small DB9
connector) when the Jettison Switch is in the normal position (up) and the Doors Switch is
relaxed (NOT triggered)? (see pic 28)
With the Jettison Switch in the normal position, there should not be continuity between
these pins until the Door Switch is triggered.
Yes- The Door Switch in the Cyclic Controller is faulty. Replace Cyclic Controller, and replace
faulty Door Switch as soon as possible.
No- Door Switch is fine. Continue with ‘Jettison Switch Check’ (para 3.7.1)
Pic 28



Jettison Solenoid –

New Style 214 tank
Cyclic Controller
Small ‘DB9’ connector

--- PAGE 49 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

3.7 – JETTISON SWITCH CHECK
3.7.1 – Q – Is there continuity between pins 9 and 5 on the Cyclic Controller plug (small DB9
connector) when the Jettison Switch is in the normal position (up)? (see pic 28)
Power is supplied to the Jettison Switch through pin 9 on the DB9 connector, then to the
Jettison Solenoid via pin 5. There must be continuity between these pins when the Jettison
Switch is in the normal position (up).
Yes – If the connection is broken when the Jettison Switch is pulled down into the
Emergency position (off) then the Jettison Switch is fine. Continue with question below
(para. 3.7.2)
No – Jettison Switch is faulty. Replace Cyclic Controller and re-check system. Replace faulty
Jettison Switch as soon as possible.

3.7.2 – Q – Is there power (24v-28v) at pin ‘G’ on the Milspec 24 pin Data Plug RECEPTACLE
with the system turned on?
Power to the Jettison Valve Solenoid is supplied via pin ‘G’ on the Milspec 24 pin Data Plug
RECEPTACLE located under the pilot door. (see pic 23)
Yes – Power supply for the Jettison Valve up to pin ‘G’ is fine. Continue below. (para 3.7.3)
No – Either a faulty Isolair Display Box or a faulty wire from pin ‘19’ in the large DB25
connector (connected to Isolair Display Box) to pin ‘G’ in the Milspec 24 pin data plug
RECEPTACLE. Change the Display Box and re-try system. If this does not work, check for
continuity between pin ’19’ of the large DB25 connector to slot ‘G’ of the Milspec 24 pin
Data PLUG. (see Diagram 6.2 - Isolair Display Box)






--- PAGE 50 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

3.7.3 - Q - Is there continuity between pin ‘G’ on the 24 pin Milspec data PLUG and the
power supply terminal of the Jettison Valve Solenoid?
Check continuity from pin ‘G’ on the Milspec 24 pin Data PLUG to the power terminal on the
Jettison Valve Solenoid by removing BOTH wires off the Jettison Solenoid Coil.
 Yes – Power supply to the Jettison should be fine, but if there is still no power present at
the Jettison Solenoid, there is a likely problem with the data plug and receptacle connection
- check this connection. Also ensure that the Jettison Valve Solenoid has a good ground. If all
wiring checks out fine and the problem still exists, investigate Jettison Solenoid and Jettison
Valve further, continue with ‘Jettison Solenoid Check’ in Section 4 – “Uncommanded Door
Opening” para. 4.2.2)
No – There is a problem with the wiring from pin ‘G’ on the 24 pin Milspec plug, and the
Jettison Valve Solenoid. Check this wire/connection. (see Diagrams 6.3, 6.4 or 6.5)

3.8 – HYDRAULIC PUMP OUTPUT PRESSURE ADJUSTMENT
3.8.1 – The Hydraulic Pump output pressure is the maximum pressure that the Hydraulic
Pump will produce if it was to continuously run. This is NOT the operating pressure of the
hydraulic system (the operating pressure is set by the Pressure Switch). The output pressure
should be set between 1400-1500psi. This pressure setting is important, as if the pressure is
too low, the Fire Tank may not operate properly, or if it’s too high, it could cause internal
damage to the tank if a Pressure Switch was to fail.
The output pressure is set during the yearly inspection, but it may gradually decrease over
time and should be monitored after extended periods of use - eg. 100hours.
If the output is found to be too low or high, an adjustment should be made to ensure the
system is operating at the correct pressure. If you think there could be a problem with the
hydraulic pressure, begin with ‘Checking the Hydraulic Pump output pressure’. (para 3.8.2)

3.8.2 - Checking the Hydraulic Pump output pressure.



--- PAGE 51 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

Pic 29



• With someone at the Isolair Display Box, turn the system ON. Then press the "Orange" test button on the right-hand side of the Isolair Junction box. Pressure Gauge will indicate the
current output pressure of the pump. If the pressure is higher than the outer limits
of the gauge, turn the system off immediately, and continue to ‘Adjusting the
Hydraulic Pump Output Pressure’ (para 3.8.3). (It’s important to keep someone at
the Isolair Display Box to turn the system off immediately IF the pressure is set too
high, to stop any damage occurring.)
If the pressure is sitting around 1400-1500psi, then that is the preferred setting and
no adjustment is required. 
If the pressure is sitting between 1200-1400psi, this should not normally cause any
problems, but the output pressure could be adjusted. Continue with ‘Setting the
Hydraulic Pump output pressure’ (para 3.8.3). (see pic 30)
If the pressure is sitting below 1200psi, then the pressure is too low and it is possible
that there may be issues with the operation of the tank. Continue with ‘Setting the
Hydraulic Pump output pressure’ (para 3.8.3). (see pic 30)


Stauff Pressure Switch
Isolair Pressure Switch
Terminals

--- PAGE 52 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

Pic 30







3.8.3 - Setting the Hydraulic Pump output pressure.
• Remove the Locking Cap from on top of the Pressure Adjusting Screw located on the
pump section of the Hydraulic Power Pack. (see pic 31).
Pic 31



Pressure
Adjusting
Screw
Locking
Cap
Normal pump
output pressure
range

--- PAGE 53 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

Pic 32





• With someone controlling the power
at the Isolair Display Box, turn the system power ON, and press the "Orange"test button on the right-hand side of the junction box, and use a large flat blade
screwdriver to turn the Pressure Adjusting Screw to increase or decrease the output
pressure with the Hydraulic Pump running.

Turn the Pressure Adjusting Screw clockwise (IN) to increase the output pressure.
Turn the Pressure Adjusting Screw anti-clockwise (OUT) to decrease the output
pressure. (see pic 33)
Pic 33


• Once the pressure is sitting at between 1400-1500psi, then turn the system off and
replace the locking nut and the Locking Cap.


Locking nut
Pressure Adjusting Screw

--- PAGE 54 ---



 Hydraulic Pump Continues To Run
Doc No: McDav-FFTTG
Revision: 03
Date: 12/07/16

3.9 – PRESSURE SWITCH ADJUSTMENT
3.9.1 - The Pressure Switch is used to set the normal operating range pressure of the
hydraulic system. To ensure that the system operates properly and that the doors seal
correctly, the hydraulic pressure must not drop below 850psi, nor should the Hydraulic
Pump continue to run.
The normal operating range is 850 - 1150pi, and the Pressure Gauge should normally
indicate approximately 1000 -1100psi. It is sometimes common for the hydraulic pressure to
slowly bleed off. If this occurs, the hydraulic pressure will slowly drop and the Pressure
Switch should be set so it will ‘cut in’ at 850psi. When Pressure Switch ‘cuts in’, it will
momentarily run the Hydraulic Pump and therefore raising the pressure back up to around
1000 - 1100psi. This occurs in a fraction of a second, and unless you are either watching the
Pressure Gauge when it occurs, or you are ground testing the tank system, you may not
even realise that this has occurred.
If at any stage it is found that the hydraulic pressure is sitting below 850psi, the Pressure
Switch is set too low and must be re-set. Continue with ‘Setting The Pressure Switch’. (para.
3.9.3)
If the hydraulic pump continues to run, it is possible that the Pressure Switch is set too high
and must be re-set. Continue below. (para 3.9.2)
If you are experiencing any problems that you believe may be due to an incorrect Pressure
Switch setting, continue with ‘Determining Pressure Switch Setting’ below. (para 3.9.2)

3.9.2 – Determining Pressure Switch Setting
• Take a CLEAN container, bucket or jug to catch any hydraulic fluid, and place it under
one of the hydraulic hose connections close by Pressure Switch.

• With the system turned ON, slowly ‘crack’ the hydraulic connection above the
container and loosen until the hydraulic fluid slowly flows from the fitting, catching
the fluid in the container. (See pic 34)



Pic 34




• As the pressure continues to bleed off, you will notice that the Hydraulic Pump will
consistently continue to run in shorts bursts to boost the pressure.

• Tighten or loosen the hydraulic hose connection to make the Hydraulic Pump run
every 3-4 seconds. This will allow the pressure to bleed off slowly enough to get an
accurate pressure reading as the Pressure Switch ‘cuts in’.

• As the pressure bleeds off, take note of where the pressure drops to before the
pump ‘kicks’ back in to boost the pressure.

• The pressure that this occurs should be NO LESS than 850psi and no greater than
approximately 900psi. (See pic 35.)
Pic 35








• If the pump ‘cuts in’ outside this pressure range, then the Pressure Switch must be
re-set. Continue with ‘Setting The Pressure Switch’ below. (para 3.9.3)
Normal operating range
‘Cut in’ pressure. 850psi


3.9.3 – Setting The Pressure Switch


• Remove the locking screw with a 2.5mm allen key from the end of the Pressure Switch.
(see pic 37)
Pic 37 – NOTE; Pressure Switches have been removed from hydraulic system in the
pictures for instructional purposes. Pressure Switches MUST remain installed on the
hydraulic system for setting.


Stauff Pressure Switch


• Take a CLEAN container, bucket or jug to catch any hydraulic fluid, and place it under
one of the hydraulic hose connections close to the pressure switch.

• With the system turned ON, slowly ‘crack’ the hydraulic connection above the
container and loosen until the hydraulic fluid slowly flows from the fitting, catching
the fluid in the container. (See pic 38)
Pic 38






• As the pressure continues to bleed off, you will notice that the hydraulic pump will
consistently continue to run in shorts bursts to boost up the pressure.

• Tighten or loosen the hydraulic connection to make the pump run every 3-4 seconds.
This will allow the pressure to bleed off slowly enough to get an accurate pressure
reading as the Pressure Switch ‘cuts in’.

• Watch the Pressure Gauge as the pressure bleeds off. The pressure at which the
hydraulic pump momentarily runs to boost the pressure, is the current setting, or
‘cut in’ pressure. This ‘cut in’ pressure, must be set at 850psi. (see pic 39).
Pic 39





‘Cut in’ pressure
– 850psi


• To adjust the pressure, insert either a large flat blade screwdriver or Dzus fastner screwdriver if avaialable (preferred tool) into the end of the Pressure Switch and
turn the Pressure Adjusting Screw either clockwise (IN) to increase the pressure, or
anti-clockwise (OUT) to decrease the pressure. With the system turned on and the
hydraulic pressure bleeding off, monitor the pressure gauge and slowly turn the
pressure adjust screw until the hydraulic pump consistently ‘cuts in’ at 850psi. (see
pic 40)

Pic 40



• Once the pressure has been set to ‘cut in’ at 850psi, turn the system off, replace the
locking screw back into the end of the Pressure Switch, and tighten the hydraulic fitting that was used to bleed off the
hydraulic pressure.

• Once everything has been put back together, turn the system on and check that the
hydraulics are operating within the correct pressure range.

Stauff Pressure
Switch
Pressure Adjust
Screw
Isolair Pressure
Switch
Pressure Adjust
Screw - inside
