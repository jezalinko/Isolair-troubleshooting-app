# First Check — HYDRAULIC PUMP CONTINUES TO RUN

**Source:** troubleshooting_guide.pdf  
**Document:** McDav-FFTTG  
**Revision:** 03  
**Pages:** 15  

---

## Symptom
- Hydraulic Pump continues to run  

---

## Preconditions / Notes
- The most common cause of this fault is an incorrectly set Pressure Switch.

> **IMPORTANT**  
> Do not discard Pressure Switches unnecessarily — many faults are resolved by adjustment.

---

## Decision Steps

### Step 1 — Hydraulic Pressure Check
**Question:**  
What is the observed Hydraulic Pressure on the gauge?

Select the appropriate range:

- **High (>1150 psi)** → Proceed to Step 2A  
- **Medium (850–1150 psi)** → Proceed to Step 2B  
- **Low (<850 psi, often ~50 psi)** → Proceed to Step 2C  

---

### Step 2A — High Pressure Path (>1150 psi)
**Action:**  
Change Pressure Switch.

**Question:**  
Does the Hydraulic Pump now operate correctly?

- **YES →**
  - Pressure Switch was set too low  
  - Re-adjust Pressure Switch (do not discard)  
  - Perform **Pressure Switch Adjustment** (through checks)

- **NO →**
  - Re-check Hydraulic Pressure  

  > **NOTE**  
  > Normal operating pressure differs from maximum pump output pressure.

  - **If pressure is below 1300 psi →**
    - Re-adjust Hydraulic Pump output pressure  
    - Perform **Hydraulic Pump Output Pressure Adjustment**

  - **If pressure is above 1300 psi →**
    - Hydraulic Pump Power Relay may be faulty  
    - Perform **Pressure Switch Check**

---

### Step 2B — Medium Pressure Path (850–1150 psi)
**Action:**  
Adjust Hydraulic Pump output pressure.

**Question:**  
Does the Hydraulic Pump now operate correctly?

- **YES →**
  - Output pressure was set too low  

- **NO →**
  - Proceed to Step 2A  

---

### Step 2C — Low Pressure Path (<850 psi)
**Action:**  
Change Cyclic Controller.

**Question:**  
Does the Hydraulic Pump now operate correctly?

- **YES →**
  - Most likely a faulty Jettison Switch  
  - Replace Cyclic Controller  

- **NO →**
  - Proceed to Step 3  

---

### Step 3 — Jettison Solenoid Electrical Check
**Question:**  
With system power ON, is there power and ground at the Jettison Solenoid terminals?  
*(At least one wire must be removed when checking.)*

- **YES →**
  - Jettison Solenoid valve or coil likely faulty  
  - Perform **Jettison Solenoid Check** (from Uncommanded Door Opening)

- **NO →**
  - Wiring fault suspected  
  - Perform **Jettison Solenoid Check** (through checks)

---

## Outcomes & Diagnoses
- **Pressure Switch incorrectly set** — Perform Pressure Switch Adjustment  
- **Faulty Pressure Switch** — Replace Pressure Switch  
- **Faulty Hydraulic Pump Power Relay** — Replace relay  
- **Faulty Jettison Switch** — Replace Cyclic Controller  
- **Faulty Jettison Solenoid** — Perform Jettison Solenoid Check  
- **Wiring fault** — Perform Jettison Solenoid Check  

---

## References
- Pressure Switch Check  
- Pressure Switch Adjustment  
- Hydraulic Pump Output Pressure Adjustment  
- Hydraulic Pump Power Relay Check  
- Jettison Solenoid Check  
- Wiring Diagram — refer to aircraft IPC  
