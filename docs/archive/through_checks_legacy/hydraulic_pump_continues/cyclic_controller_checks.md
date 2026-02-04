## Cyclic Controller Input Checks  
*(Door Switch and Jettison Switch)*

**System:** Hydraulic Pump Continues To Run  
**Source:** troubleshooting_guide.pdf (pp. 48–50)

---

## Purpose
Verify that Cyclic Controller inputs (Door Switch and Jettison Switch) are not commanding unintended hydraulic or jettison functions, resulting in continuous Hydraulic Pump operation.

---

## Applicability / Configuration

> **NOTE**
>
> The Door Switch and Jettison Switch are internal to the **Cyclic Controller**.  
> Both switches influence hydraulic and jettison logic and are evaluated together.
>
> The Cyclic Controller is replaced as a complete unit in the field.  
> Individual switch repair is carried out **only in the workshop**.

---

## Preconditions / Notes
- System ON  
- Hydraulic Pump continues to run, or abnormal pressure behaviour observed  
- Pressure Switch, Hydraulic Pump Power Relay, and Jettison Solenoid checks completed  

---

## Step 1 — Door Switch Input Check

**Question:**  
Is the Cyclic Controller Door Switch input correctly indicating door position?

### Test Method
- Locate the **small DB9 connector** on the Cyclic Controller.
- With the **Jettison Switch in the normal (UP) position**:
  - Measure continuity between **pins 9 and 4**.
- Observe Door Switch state:
  - **Doors NOT triggered (closed):** No continuity expected
  - **Doors triggered (open):** Continuity expected

Refer to **Pic 28** and **Diagram 6.1**.

---

### Result

- **YES — Door Switch input behaves correctly**
  - Proceed to **Step 2 — Jettison Switch Input Check**.

- **NO — Door Switch input incorrect**
  - Door Switch within the Cyclic Controller is faulty.
  - Replace the Cyclic Controller.
  - Re-test system operation.

---

## Step 2 — Jettison Switch Input Check

**Question:**  
Is the Cyclic Controller Jettison Switch input operating correctly?

### Test Method
- With the **Jettison Switch in the normal (UP) position**:
  - Check continuity between **pins 9 and 5** on the DB9 connector.
- Move the Jettison Switch to the **EMERGENCY (DOWN)** position:
  - Continuity should be **broken** between pins 9 and 5.

Refer to **Pic 28** and **Diagram 6.1**.

---

### Result

- **YES — Jettison Switch input correct**
  - Proceed to **Step 3 — Jettison Power Feed Verification**.

- **NO — Jettison Switch input incorrect**
  - Jettison Switch within the Cyclic Controller is faulty.
  - Replace the Cyclic Controller.
  - Re-test system operation.

---

## Step 3 — Jettison Power Feed Verification

**Question:**  
Is power correctly supplied from the Cyclic Controller to the Jettison Solenoid circuit?

### Test Method
- With the system ON:
  - Measure for **24–28 VDC** at **pin ‘G’** on the **24-pin Milspec data plug receptacle**.
- The main power connector must remain connected.

Refer to **Pic 23** and **Diagram 6.2**.

---

### Result

- **YES — Power present**
  - Cyclic Controller output and upstream wiring are correct.
  - If Hydraulic Pump continues to run:
    - With **high pressure** → Re-check **Doors Switch logic**
    - With **low pressure** → Proceed to **Uncommanded Door Opening** section

- **NO — Power absent**
  - Faulty Cyclic Controller or wiring between:
    - Cyclic Controller (DB25 connector)
    - Data Plug (pin ‘G’)
  - Replace Cyclic Controller or repair wiring as required.
  - Re-test system operation.

---

## Next Action

- If Cyclic Controller inputs are confirmed correct →  
  Re-evaluate hydraulic pressure behaviour and proceed to remaining checks as applicable.
- If any Cyclic Controller input fails →  
  Replace the Cyclic Controller and re-test the system.

