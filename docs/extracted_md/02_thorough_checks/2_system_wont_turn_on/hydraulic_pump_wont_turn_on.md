# 2. System Won’t Turn On  
*(Hydraulic Pump Will Not Run)*

**System:** Fire Tank Hydraulic System  

> **Diagram Reference**
>
> Refer to **Diagram xx**  
> *(Current wiring shown; diagram to be added.)*

---

## 2.0 Purpose
Determine why the Fire Tank system will not power up or run the Hydraulic Pump.

---

## 2.1 Applicability / Configuration

> **NOTE**
>
> This procedure applies to **current tank configurations only**:
> - No Slave Relays fitted
> - Current Stauff Pressure Switches
> - Single Hydraulic Pump Power Relay
> - Cyclic Controller providing all operator inputs

---

## 2.2 Initial Power Confirmation (Quick Check)

**Question:**  
Is power reaching the Isolair Tank System?

### Check
- Is the **ON/OFF switch** on the Isolair Display Box set to **ON**?
- Are **both circuit breakers** on the Isolair Display Box **IN**?
- Is the **Jettison Switch** on the Cyclic Controller in the **NORMAL (UP)** position?
- Are **any LEDs illuminated** on the Isolair Display Box?

> **NOTE**
>
> When power is present, at minimum the **FSC** and **Pump Temp** LEDs will illuminate.

---

### Result

- **YES — LEDs illuminated**
  - Power is reaching the system.
  - Proceed to **2.4 — Control System Check**.

- **NO — No LEDs illuminated**
  - No power is reaching the system.
  - Proceed to **2.3 — Power Supply Check**.

---

## 2.3 Power Supply Check

### 2.3.1 Circuit Breakers

**Question:**  
Have any Isolair system circuit breakers tripped?

#### Test Method
- Check **all aircraft circuit breakers** supplying the Isolair system.

Refer to **Pic xx**  
*(Image to be updated.)*

---

#### Result

- **YES — Circuit breaker tripped**
  - Reset circuit breaker.
  - Re-test system.

- **NO — All circuit breakers set**
  - Proceed to **2.3.2 — Tank Power Input Check**.

---

### 2.3.2 Tank Power Input Check

**Question:**  
Is power present at the tank power input?

#### Test Method
- With the system ON, measure voltage at the **large power input terminal** of the  
  **Hydraulic Pump Power Relay**.
- Voltage should be **24–28 VDC**.

Refer to **Pic 7** and **Pic 18**  
*(Images to be updated if required.)*

---

#### Result

- **YES — Power present**
  - Tank is receiving power.
  - Proceed to **2.4 — Control System Check**.

- **NO — No power present**
  - Fault in aircraft power supply or Isolair Display Box.
  - Replace the Isolair Display Box and re-test.
  - If still inoperative, investigate aircraft **Main Power Relay Assembly**.

---

## 2.4 Control System Check

> **NOTE**
>
> If power is present but the system will not operate, the fault lies in the  
> **control logic**, not the power supply.

---

### 2.4.1 Cyclic Controller Check

**Question:**  
Does the system operate when a known serviceable **spare Cyclic Controller** is installed?

#### Test Method
- Install the spare Cyclic Controller.
- Ensure the Jettison Switch is in the **NORMAL (UP)** position.
- Attempt system operation.

Refer to **Pic xx**  
*(Image to be updated.)*

---

#### Result

- **YES — System operates**
  - Original Cyclic Controller faulty.
  - Replace controller to remain serviceable.
  - Repair faulty switch(es) in workshop as required.

- **NO — System still inoperative**
  - Cyclic Controller is likely serviceable.
  - Proceed to **2.4.2 — Pressure Switch Power Check**.

---

### 2.4.2 Pressure Switch Power Check

**Question:**  
Is power present at the **Pressure Switch common supply** when the system is ON?

#### Test Method
- Measure voltage at the Pressure Switch common terminal.
- Voltage should be **24–28 VDC**.

Refer to **Pic xx**  
*(Image to be updated.)*

---

#### Result

- **YES — Power present**
  - Proceed to **2.4.3 — Hydraulic Pump Power Relay Check**.

- **NO — No power present**
  - Wiring fault between Isolair Display Box and Pressure Switch.
  - Investigate wiring using **Diagram xx**.

---

### 2.4.3 Hydraulic Pump Power Relay Check

Proceed with **Hydraulic Pump Power Relay Check**  
*(Modern single-path procedure).*

---

## 2.5 Next Action

- If system power is restored →  
  Re-test full tank operation.
- If fault persists →  
  Continue troubleshooting using applicable system sections.
