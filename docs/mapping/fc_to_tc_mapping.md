# FC → TC Mapping (LOCKED)

This document defines every handoff from First Checks (FC) to Through Checks (TC) by canonical node ID.

---

## FC-0 — Start

- User selects Snorkel Pump Won’t Operate → fc_1_snorkel_pump_wont_operate
- User selects System Won’t Turn On → fc_2_system_wont_turn_on
- User selects Hydraulic Pump Continues To Run → fc_3_hydraulic_pump_continues_to_run
- User selects Uncommanded Door Opening → fc_4_uncommanded_door_opening
- User selects Leaking Doors → fc_5_leaking_doors

---

## FC-1 — Snorkel Pump Won’t Operate

- Step 3 (Pressure Switch changed) → NO → tc_pressure_switch_check
- Step 5 (Cyclic Controller changed) → NO → tc_snorkel_pump_power_relay_check
- Step 6 (Snorkel Pump substituted) → YES → tc_snorkel_pump_motor_check
- Step 6 (Snorkel Pump substituted) → NO → tc_snorkel_pump_wont_operate

Optional reference targets (not direct step handoffs yet):
- Reference / view detail → tc_cyclic_controller_pump_switch_check

---

## FC-2 — System Won’t Turn On

- Step 5 (Not on ground power) → tc_circuit_breaker_checks
- Step 6 (Pressure Switch changed) → NO → tc_tank_power_supply_check
- Step 7 (Still won’t turn on) → tc_circuit_breaker_checks

Additional escalation targets referenced by FC-2:
- If relay suspected → tc_hydraulic_pump_power_relay_check
- If wiring suspected → tc_wiring_continuity_checks

---

## FC-3 — Hydraulic Pump Continues To Run

- Step 2A → YES (switch set too low) → tc_pressure_switch_adjustment
- Step 2A → NO and pressure <1300 psi → tc_hydraulic_pump_output_pressure_adjustment
- Step 2A → NO and pressure >1300 psi → tc_pressure_switch_check
- Step 3 → YES (power/ground present) → tc_jettison_solenoid_check
- Step 3 → NO (power/ground missing) → tc_jettison_solenoid_check

Additional escalation targets referenced by FC-3:
- If relay suspected → tc_hydraulic_pump_power_relay_check

---

## FC-4 — Uncommanded Door Opening

- Step 2A (Cooling does not resolve) → tc_jettison_solenoid_check
- Step 2B (Controller swap does not resolve) → tc_jettison_switch_check
- Step 3A (Controller swap does not resolve) → tc_hydraulic_cross_over_check

Terminal outcomes referenced by FC-4:
- Internal door fault path → terminal_mechanical_investigation_required

---

## FC-5 — Leaking Doors

- Step 2 (Within allowable) → terminal_monitor_condition
- Step 3 (Exceeds allowable) → terminal_workshop_inspection_required
