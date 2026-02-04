# 3. Hydraulic Pump Continues To Run

**System:** Fire Tank Hydraulic System  
**Fault Condition:** Hydraulic Pump continues to run  

> **Diagram Reference**
>
> Refer to **Diagram xx**  
> *(Current wiring shown; diagram to be added.)*

---

## Possible Causes
- Faulty or incorrectly set Pressure Switch
- Incorrect Hydraulic Pump output pressure
- Faulty Hydraulic Pump Power Relay
- Faulty Jettison Solenoid
- Incorrect Cyclic Controller input (Door or Jettison Switch)

---

## 3.1 — Quick Check

The most common cause of this fault is an incorrectly set Pressure Switch.

> **NOTE**
>
> Do **not** discard Pressure Switches unnecessarily.  
> Many faults are caused by incorrect adjustment rather than component failure.

Proceed to **3.2 — Pressure Switch Check**.

---

## 3.2 — Pressure Switch Check

### 3.2.1 — Hydraulic Pressure Check

**Question:**  
What is the hydraulic pressure when the Hydraulic Pump is running continuously?

#### Test Method
- Observe the Pressure Gauge with the system ON.

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **HIGH (>1200 psi)**  
  → Proceed to **3.3 — Pressure Switch Adjustment**

- **MEDIUM (850–1200 psi)**  
  → Proceed to **3.4 — Hydraulic Pump Output Pressure Adjustment**

- **LOW (little or no pressure)**  
  → Proceed to **3.6 — Jettison Solenoid Check**

---

### 3.2.2 — Pressure Switch Evaluation

- Verify Pressure Switch behaviour against observed pressure.
- If Pressure Switch cut-in or cut-out behaviour is incorrect, adjustment is required.

Proceed to **3.3 — Pressure Switch Adjustment**.

---

## 3.3 — Pressure Switch Adjustment

**Purpose:**  
Set the correct Pressure Switch cut-in pressure.

#### Test / Adjustment Method
- Perform controlled hydraulic pressure bleed.
- Observe the pressure at which the Hydraulic Pump momentarily runs.
- Adjust Pressure Switch until **cut-in occurs at 850 psi**.

Refer to **Pic xx**  
*(Image to be updated.)*

> **CAUTION**
>
> Pressure Switch must remain installed on the hydraulic system during adjustment.

---

### Completion Gate

- **If Pressure Switch behaviour is now correct** →  
  Proceed to **3.5 — Hydraulic Pump Power Relay Check**

- **If adjustment cannot be achieved** →  
  Replace Pressure Switch and re-test system

---

## 3.4 — Hydraulic Pump Output Pressure Adjustment

**Purpose:**  
Verify and adjust the **maximum pump output pressure**.

> **NOTE**
>
> Output pressure is **not** normal operating pressure.  
> It must be set to **1400–1500 psi**.

---

### 3.4.1 — Checking Output Pressure

#### Test Method
- System ON
- Press **Orange test button** on Isolair Junction Box
- Observe Pressure Gauge

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **1400–1500 psi** → No adjustment required  
- **1200–1400 psi** → Adjustment recommended  
- **<1200 psi or above gauge limit** → Adjustment required immediately

---

### 3.4.2 — Setting Output Pressure

> **CAUTION**
>
> Keep one person at the Isolair Display Box during adjustment.

#### Adjustment Method
- Remove Locking Cap from Pressure Adjusting Screw
- Adjust with flat-blade screwdriver:
  - Clockwise → Increase pressure
  - Anti-clockwise → Decrease pressure
- Set to **1400–1500 psi**
- Refit Locking Cap

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Completion Gate

- If output pressure is correct →  
  Return to **3.5 — Hydraulic Pump Power Relay Check**

---

## 3.5 — Hydraulic Pump Power Relay Check

### 3.5.1 — Relay Output Check

#### Test Method
- Measure voltage at relay output terminal while fault is present

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **Relay stuck energised** → Proceed to **3.5.2**
- **Relay de-energises correctly** → Proceed to **3.6**

---

### 3.5.2 — Relay Control Check

#### Test Method
- Remove one relay control wire
- Verify control voltage and ground at remaining terminals

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **Both present** → Fault upstream
- **Missing signal** → Wiring or logic fault

Replace relay if confirmed faulty.

---

## 3.6 — Jettison Solenoid Check

### 3.6.1 — Solenoid Power and Ground

#### Test Method
- Check for 24–28 VDC and solid ground at solenoid coil

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **Power present** → Proceed to **3.6.2**
- **Power missing** → Control wiring fault

---

### 3.6.2 — Solenoid Operation

#### Test Method
- Command jettison
- Listen/feel for solenoid actuation

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **Operates correctly** → Proceed to **3.7**
- **No operation** → Replace solenoid coil (field-replaceable)

---

## 3.7 — Cyclic Controller Input Checks  
*(Door Switch & Jettison Switch)*

### 3.7.1 — Input Verification

- Verify Door Switch and Jettison Switch inputs at Cyclic Controller
- Confirm no unintended command is present

Refer to **Pic xx**  
*(Image to be updated.)*

---

### 3.7.2 — Control Output Verification

- Verify controller output to Jettison Solenoid circuit

Refer to **Pic xx**  
*(Image to be updated.)*

---

## Final Action

- If fault is resolved → Return system to service  
- If fault persists → Investigate hydraulic block or internal leakage paths

