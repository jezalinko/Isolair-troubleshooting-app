## Jettison Solenoid Check

**System:** Hydraulic Pump Continues To Run  
**Source:** troubleshooting_guide.pdf (pp. 47–50)

---

## Purpose
Verify that the Jettison Solenoid is not causing continuous Hydraulic Pump operation or incorrect hydraulic pressure behaviour.

---

## Applicability / Configuration

> **NOTE**
>
> All current tank installations use a single **Jettison Solenoid** controlled directly by the tank electrical system.  
> There are no alternate configurations or slave devices fitted.

---

## Preconditions / Notes
- System ON  
- Hydraulic Pump running continuously **or** abnormal hydraulic pressure behaviour observed  
- Pressure Switch and Hydraulic Pump Power Relay checks completed  

> **NOTE**
>
> The Jettison Solenoid is pressure-dependent.  
> Faults in the Jettison Solenoid circuit may present as:
> - Low or unstable hydraulic pressure
> - Continuous Hydraulic Pump operation
> - Uncommanded door movement

---

## Step 1 — Solenoid Power and Ground

**Question:**  
Is correct power and ground present at the Jettison Solenoid when the system is ON?

### Test Method
- Locate the **Jettison Solenoid** on the hydraulic manifold.
- Access the solenoid coil terminals or connector.
- With the system ON:
  - Check for **24–28 VDC** at the power terminal.
  - Check for a **solid ground** at the ground terminal.
- If required, remove the solenoid coil cap to access the terminals.

Refer to **Pic 27**.

---

### Result

- **YES — Power and ground present**
  - Wiring to the Jettison Solenoid is correct.
  - Proceed to **Step 2 — Solenoid Operation**.

- **NO — Power or ground missing**
  - Wiring or control fault upstream of the solenoid.
  - Inspect:
    - Jettison Switch
    - Isolair Display Box
    - Wiring between control unit and solenoid
  - Refer to **Diagram 6.2** and **Diagrams 6.3–6.5**.

---

## Step 2 — Solenoid Operation

**Question:**  
Does the Jettison Solenoid operate correctly when commanded?

### Test Method
- With the system ON:
  - Command the Jettison function.
  - Listen and feel for solenoid actuation (“click”).
- Observe hydraulic pressure response:
  - Pressure should change as expected when the solenoid is energised or de-energised.

---

### Result

- **YES — Solenoid operates correctly**
  - The Jettison Solenoid is serviceable.
  - If Hydraulic Pump continues to run with **low pressure**, proceed to  
    **Uncommanded Door Opening — Jettison Solenoid Check**.
  - If Hydraulic Pump continues to run with **high pressure**, proceed to  
    **Doors Switch Check**.

- **NO — Solenoid does not operate**
  - Faulty solenoid coil or internal solenoid valve.
  - Replace the Jettison Solenoid assembly.
  - Re-test system operation.

---

## Jettison Solenoid Replacement

> **CAUTION**
>
> Ensure all electrical connections are sealed against moisture ingress.  
> Failure to seal connectors may result in intermittent solenoid operation or repeat faults.

- After replacement:
  - Reconnect all wiring securely.
  - Confirm correct hydraulic pressure behaviour.
  - Re-test the full system.

---

## Next Action

- If Jettison Solenoid operation is confirmed correct →  
  Proceed to **Doors Switch Check**.
- If uncommanded door movement persists →  
  Proceed to **Uncommanded Door Opening** troubleshooting section.

