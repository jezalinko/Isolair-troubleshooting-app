# Snorkel Pump Won’t Operate

**System:** Fire Tank – Snorkel Pump  
**Fault Condition:** Snorkel Pump will not operate  

> **Diagram Reference**
>
> Refer to **Diagram xx**  
> *(Current wiring shown; diagram to be added.)*

---

## Possible Causes
- Hydraulic pressure not within operating range
- Doors not fully closed
- Faulty Pressure Switch
- Faulty Snorkel Pump Power Relay
- Faulty Snorkel Pump motor, ECC, or power cable
- Faulty Pump Switch within the Cyclic Controller
- Wiring fault between controller, relay, and pump

---

## 1.1 — Quick Check

### Step 1 — Hydraulic Pressure

**Question:**  
Is the hydraulic pressure within the normal operating range  
(**850–1150 psi** on the Pressure Gauge)?

- **YES →** Proceed to **Step 2 — Door Status**
- **NO →** Proceed to **1.3 — Pressure Switch Check**

---

### Step 2 — Door Status

**Question:**  
Is the green **DOOR CLOSE** LED illuminated on the Isolair Display Box?

> **NOTE**
>
> The DOOR CLOSE LED illuminates when hydraulic pressure is in range and the doors are fully closed.  
> The snorkel pump will not operate unless the doors are confirmed closed.

- **YES →** Proceed to **1.2 — Snorkel Pump Motor Check**
- **NO →** Proceed to **1.3 — Pressure Switch Check**

---

## 1.2 — Snorkel Pump Motor Check

**Purpose:**  
Verify that power is reaching the snorkel pump and that the pump assembly and power cable are serviceable.

---

### Step 1 — Power at Pump Connector

**Question:**  
When the Pump Switch is triggered, is there power and ground at the snorkel pump power receptacle (tank side)?

#### Test Method
- Disconnect the **Snorkel Pump Anderson Plug (214)** from the tank receptacle.
- While another person triggers the **Pump Switch**:
  - Check for **24–28 VDC** at the tank-mounted receptacle.
  - Confirm a good ground at the other terminal.

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **YES →**
  - Pump assembly, ECC, or power cable is suspect.
  - Swap to the spare pump assembly to remain serviceable.
  - Tag removed pump/cable for workshop troubleshooting.
  - Proceed to **Step 2 — Cable Continuity Check** when practical.

- **NO →**
  - Pump motor is likely not the issue.
  - Proceed to **1.3 — Pressure Switch Check**.

---

### Step 2 — Cable Continuity Check

**Question:**  
Is there continuity through both the power and ground wires in the pump power cable?

#### Test Method
- Disconnect:
  - Pump Motor Milspec Plug
  - Anderson Plug from the tank
- Check continuity on both power and ground wires.
- Confirm Anderson plug contacts are fully locked in the housing.

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **YES →**
  - Power cable is serviceable.
  - Pump motor is faulty, most likely the **End Cap Controller (ECC)**.
  - Continue using spare pump.
  - Replace ECC as soon as possible.

  > **NOTE**
  >
  > All spare ECCs are programmed for **214 snorkels only**.  
  > ECC programming must be carried out by an authorised technician.

- **NO →**
  - Faulty power cable or Anderson plug.
  - Inspect and repair wiring or connectors.

---

## 1.3 — Pressure Switch Check

**Purpose:**  
Verify that the Pressure Switch is supplying power to the snorkel pump control circuit when hydraulic pressure is in range.

---

### Step 1 — Pressure Switch Output

**Question:**  
Is there **24–28 VDC** at the **High Pressure (N/O)** terminal of the Pressure Switch when:
- The system is ON, and
- Hydraulic pressure is within 850–1150 psi?

#### Test Method
- Measure voltage at the **High Pressure (N/O)** terminal.
- On Stauff Pressure Switches, this is **Terminal 4**.

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **YES →**
  - Pressure Switch is functioning correctly.
  - Proceed to **1.4 — Snorkel Pump Power Relay Check**.

- **NO →**
  - Pressure Switch faulty or not closing correctly.
  - Replace Pressure Switch.
  - Seal against water ingress using **DC4 silicone grease**.
  - Re-test system.

---

## 1.4 — Snorkel Pump Power Relay Check

**Purpose:**  
Verify that the Snorkel Pump Power Relay is switching correctly and supplying power to the pump.

---

### Step 1 — Relay Output

**Question:**  
Is there **24–28 VDC** at the **large output terminal** of the Snorkel Pump Power Relay **only when the Pump Switch is triggered**?

#### Test Method
- Trigger Pump Switch.
- Listen for relay click.
- Measure voltage at the large output terminal.

Refer to **Pic xx**  
*(Image to be updated.)*

---

### Result

- **YES →**
  - Relay is switching correctly.
  - Verify power at the Snorkel Pump Anderson Plug.
  - If no power present, proceed to **Step 2 — Power Wire Continuity**.

- **NO →**
  - Relay not switching.
  - Proceed to **Step 3 — Relay Control Circuit**.

---

### Step 2 — Power Wire Continuity

**Question:**  
Is there continuity between the relay large output terminal and the Anderson plug power pin?

#### Test Method
- Perform continuity check between relay output and Anderson plug.

Refer to **Pic xx**  
*(Image to be updated.)*

- **YES →** Power wire serviceable  
- **NO →** Repair wiring between relay and Anderson plug

---

### Step 3 — Relay Control Circuit

#### Control Power

**Question:**  
Is control power present at the relay coil?

##### Test Method
- Remove one control wire.
- Check for **24–28 VDC** at the remaining small terminal.

Refer to **Pic xx**  
*(Image to be updated.)*

- **NO →** Wiring fault from Pressure Switch (return to **1.3**)  
- **YES →** Proceed to **Step 3 — Data Plug Ground**

---

## 1.5 — Cyclic Controller Pump Switch Check

> **Operational Policy**
>
> In the field, the Cyclic Controller is replaced as a complete unit.  
> Individual switch repair is **workshop only**.

---

### Step 1 — Pump Switch Function

**Question:**  
Does the snorkel pump operate when the Pump Switch is triggered in **either direction**?

#### Test Method
- Trigger pump switch in both directions.
- Observe pump response.

Refer to **Pic xx**  
*(Image to be updated.)*

- **YES →**
  - Pump Switch partially functional.
  - Replace or repair Cyclic Controller at next maintenance.

- **NO →**
  - Replace Cyclic Controller with spare.
  - Re-test system.

---

### Step 2 — Cyclic Controller Output

**Question:**  
Is there continuity between **pins 6 and 8** on the DB9 connector when the Pump Switch is triggered?

#### Test Method
- Measure continuity across DB9 pins while actuating Pump Switch.

Refer to **Pic xx**  
*(Image to be updated.)*

- **YES →** Proceed to **Step 3 — Data Plug Ground**  
- **NO →** Repair or replace Pump Switch in workshop

---

### Step 3 — Data Plug Ground

**Question:**  
Is there ground at **slot M** on the 24-pin data plug receptacle when the Pump Switch is triggered?

#### Test Method
- Measure ground at slot M during Pump Switch actuation.

Refer to **Pic xx**  
*(Image to be updated.)*

- **NO →** Fault in Isolair Display Box or wiring  
- **YES →** Proceed to **Step 4 — Tank Wiring**

---

### Step 4 — Tank Wiring

**Question:**  
Is there continuity between **pin M** on the data plug and the ground control terminal of the Snorkel Pump Power Relay?

#### Test Method
- Perform continuity check between data plug and relay ground terminal.

Refer to **Pic xx**  
*(Image to be updated.)*

> **NOTE**
>
> Slave relays are no longer fitted.  
> Testing is performed directly at the Snorkel Pump Power Relay.

- **YES →** Re-check relay operation (Section **1.4**)  
- **NO →** Repair tank wiring or connector pins

---

## Final Action

- If snorkel pump operates → Return system to service  
- If fault persists → Re-evaluate wiring, pump assembly, or control logic

