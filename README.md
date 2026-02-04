# Isolair Troubleshooting App

A **field troubleshooting companion and decision-support aide** derived from the  
*Isolair Fire Fighting Tank Troubleshooting Guide*.

This project converts existing troubleshooting knowledge into **structured, validated decision logic** that can be used in the field to assist experienced tank technicians during fault isolation and follow-up.

> ⚠️ **Safety / Advisory Disclaimer**
>
> This project is an **advisory decision-support tool only**.
> It does **not** replace approved manuals, maintenance data, SOPs, or formal training.
> Always follow your organisation’s approved documentation and procedures.
> The technician remains responsible for all maintenance decisions.

---

## Project Status

### Phase 1 — Knowledge Extraction ✅ **Complete**
- PDF troubleshooting guides extracted and cleaned into Markdown
- Legacy material archived for traceability

### Phase 2 — Decision Logic (YAML)
- **First Checks (FC-0 → FC-5):** ✅ **Complete and validated**
- **Through Checks (TC-1 → TC-5):** ⏳ **Next stage**

> First Checks provide rapid in-field fault isolation.  
> Through Checks will provide deeper, component-level troubleshooting paths.

### Phase 3 — Application Layer ⏳ *Planned*
- Mobile-friendly UI (PWA)
- Offline/online operation
- Technician-entered context (aircraft, tank asset / serial number)

### Phase 4 — Reporting & History ⏳ *Planned*
- Post-troubleshooting report submission
- Asset-based fault history
- Inspection follow-up support for annual maintenance

---

## Repository Structure

```text
isolair-troubleshooting-app/
├─ app/                    # Early scaffolding for future mobile/PWA app
├─ data/
│  ├─ schema/              # JSON schema for validating troubleshooting logic
│  └─ yaml/
│     └─ first_checks/     # Authoritative FC-0 → FC-5 YAML decision trees
├─ docs/
│  ├─ first_checks/        # Human-readable First Check documentation
│  ├─ through_checks/      # Human-readable Through Check documentation
│  └─ archive/             # Legacy / extracted reference material
├─ scripts/
│  ├─ validate_yaml.py     # YAML logic validator
│  └─ run_check.py         # CLI troubleshooting runner (Field / Workshop modes)
├─ dev_archive/            # One-off and legacy development scripts
├─ infra/                  # Docker / tooling (future use)
└─ README.md
```

## First Checks (Current Capability)

The following **First Check (FC)** modules are complete and validated:

- **FC-0** — Start / Fault Selection  
- **FC-1** — Snorkel Pump Won’t Operate  
- **FC-2** — System Won’t Turn On  
- **FC-3** — Hydraulic Pump Continues To Run  
- **FC-4** — Uncommanded Door Opening  
- **FC-5** — Leaking Doors  

Each First Check:

- Uses canonical node IDs
- Passes schema and logic validation
- Cleanly hands off to relevant Through Checks where required

---

## CLI Usage (Developer / Power User)

### Validate YAML Logic

Ensure a First Check or Through Check YAML file is structurally valid:

```bash
python3 scripts/validate_yaml.py data/yaml/first_checks/fc_3_hydraulic_pump_continues_to_run.yaml
```

### Run the Troubleshooting Flow (CLI)

Launch an interactive troubleshooting session:

```bash
python3 scripts/run_check.py data/yaml/first_checks/fc_0_start.yaml
```
### Runtime Controls

- `y / n` → Answer **Yes / No**
- `b` → Go back one step
- `c` → Toggle **Field ⇄ Workshop** context
- `q` → Quit

Field vs Workshop context controls how much detail is displayed, reducing cognitive load during live operations.

---

## Source Documentation

This project is derived from company troubleshooting documentation.

- PDF source material may be stored locally for reference
- Commit status of source PDFs is intentionally **neutral**
- Markdown documentation reflects extracted and cleaned knowledge only

---

## Contribution Notes

This repository is currently:

- Maintained as an internal engineering project
- Structured for future collaboration
- Not yet open for general external contributions

> Contribution guidelines may be added once the Through Check logic and application layer are stabilised.

---

## Design Philosophy

- **Field-first:** Fast fault isolation under operational pressure
- **Advisory, not authoritative:** Supports judgement, does not replace it
- **Traceable:** Every decision maps back to documented logic
- **Expandable:** Designed to grow into reporting, history, and analytics

---

## Licence / Usage

> Internal engineering and decision-support use only.  
> Distribution or operational use is subject to organisational approval.


