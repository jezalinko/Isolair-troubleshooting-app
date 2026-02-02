## Hydraulic Pump Power Relay Check

**System:** Hydraulic Pump Continues To Run  
**Source:** troubleshooting_guide.pdf (pp. 46–48)

---

## Purpose
Verify that the Hydraulic Pump Power Relay is switching correctly and is not causing continuous Hydraulic Pump operation.

---

## Applicability / Configuration

> **NOTE**
>
> All current tank installations use a **single Hydraulic Pump Power Relay**.  
> Slave Relays are **not fitted** and are no longer supported.
>
> Any legacy references to “slave relays”, “204 tanks”, or “old / new style” relay configurations are **not applicable**.

---

## Preconditions / Notes
- System ON  
- Hydraulic pressure behaviour already assessed  
- Hydraulic Pump running continuously  

> **NOTE**
>
> This check assumes the Pressure Switch has already been evaluated in accordance with  
> **Pressure Switch Check** and has not been identified as the primary fault.

---

## Step 1 — Relay Output Check

**Question:**  
Is the Hydraulic Pump Power Relay remaining energised when it should be de-energised?

### Test Method
- Locate the **Hydraulic Pump Power Relay** inside the Tank Control Box.
- With the system ON and the fault present:
  - Listen for an audible **relay click** when system power is cycled.
  - Observe whether the Hydraulic Pump continues to run with **no demand present**.
- Measure voltage at the **large output terminal** of the relay:
  - Voltage present = relay closed  
  - No voltage = relay open

Refer to **Pic 25** and **Pic 26**.

---

### Result

- **YES — Relay output remains energised**
  - The relay is likely stuck closed or internally faulty.
  - Proceed to **Step 2 — Relay Coil Control Check**.

- **NO — Relay output de-energises correctly**
  - The relay is functioning correctly.
  - The fault lies elsewhere in the system.
  - Proceed to **Jettison Solenoid Check** or **Doors Switch Check**, as applicable.

---

## Step 2 — Relay Coil Control Check

**Question:**  
Is the relay coil being commanded to remain energised when it should not be?

### Test Method
- Identify the **two small control terminals** on the relay.
- Remove **one control wire** from the relay coil  
  (to prevent false readings through the coil).
- With the system ON:
  - Check for **control voltage** at the remaining small terminal.
  - Check for **ground** at the opposite control terminal.

---

### Result

- **YES — Control voltage and ground are both present**
  - The relay is being correctly commanded.
  - The fault is upstream of the relay.
  - Re-check:
    - Pressure Switch behaviour
    - Doors Switch logic
    - Jettison circuit inputs

- **NO — Control signal incorrect or absent**
  - Wiring fault or incorrect control logic.
  - Inspect wiring between:
    - Pressure Switch
    - Doors Switch
    - Jettison circuit
    - Relay control terminals
  - Refer to **Diagrams 6.3, 6.4, and 6.5**.

---

## Relay Replacement

> **CAUTION**
>
> Do **not** replace the relay until control signals have been verified.  
> Replacing relays without confirming control logic may mask the true fault.

- If the relay is confirmed faulty:
  - Replace with approved **24 V, 200 A Hydraulic Pump Power Relay**  
    (**P/N 24214**).
  - Ensure all terminals are secure and free from corrosion.
  - Re-test system operation.

---

## Next Action

- If relay operation is confirmed correct →  
  Proceed to **Jettison Solenoid Check** or **Doors Switch Check**, as applicable.
- If the relay was replaced →  
  Re-test the system before continuing troubleshooting.

