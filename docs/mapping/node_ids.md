# Canonical Node IDs (LOCKED)

This file defines the canonical IDs used by YAML and the application.

## Rules
- IDs are lowercase snake_case
- IDs are stable once committed (do not rename casually)
- Markdown may change wording freely; YAML references IDs only

---

## FC Entry Nodes (First Checks)

- fc_0_start
- fc_1_snorkel_pump_wont_operate
- fc_2_system_wont_turn_on
- fc_3_hydraulic_pump_continues_to_run
- fc_4_uncommanded_door_opening
- fc_5_leaking_doors

---

## TC Entry Nodes (Through Checks)

> These are the top-level “entry points” referenced from First Checks.

- tc_snorkel_pump_wont_operate
- tc_system_wont_turn_on
- tc_hydraulic_pump_continues_to_run
- tc_uncommanded_door_opening
- tc_leaking_doors

---

## Shared Through Check Nodes (Cross-referenced)

> These are referenced by multiple FC/TC flows.

- tc_pressure_switch_check
- tc_pressure_switch_adjustment
- tc_hydraulic_pump_output_pressure_adjustment
- tc_snorkel_pump_power_relay_check
- tc_snorkel_pump_motor_check
- tc_cyclic_controller_pump_switch_check
- tc_circuit_breaker_checks
- tc_tank_power_supply_check
- tc_hydraulic_pump_power_relay_check
- tc_wiring_continuity_checks
- tc_jettison_solenoid_check
- tc_jettison_switch_check
- tc_hydraulic_cross_over_check

---

## Terminal Nodes (Standard Outcomes)

> Use these for end states that do not continue into a Through Check.

- terminal_replace_cyclic_controller
- terminal_replace_pressure_switch
- terminal_replace_snorkel_pump
- terminal_adjust_pressure_switch
- terminal_adjust_pump_output_pressure
- terminal_monitor_condition
- terminal_mechanical_investigation_required
- terminal_workshop_inspection_required
- terminal_fault_not_present

> Definitions:
> - terminal_mechanical_investigation_required = internal door fault suspected; mechanical inspection required (no further app steps)
> - terminal_workshop_inspection_required = workshop-level procedure required (rigging/adjustment/tear-down)

