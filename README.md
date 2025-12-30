# Isolair Troubleshooting App (Project)

A mobile-friendly troubleshooting assistant derived from the **Isolair Fire Fighting Tank Troubleshooting Guide**.

This repo is intentionally split into:
- **docs/**: extracted Markdown knowledge (human-readable)
- **data/**: structured logic (YAML/JSON) used by the app
- **scripts/**: helpers to extract/validate/convert content
- **app/**: the future mobile/PWA application code
- **infra/**: Docker + tooling to keep the dev environment consistent

> ⚠️ **Safety / Advisory Disclaimer**
> This project is intended as an **advisory troubleshooting aid only**.
> It does **not** replace approved manuals, checklists, SOPs, or training.
> Always follow your organization’s approved procedures and documentation.

---

## Status

**Phase 1 (in progress):** Repository skeleton + PDF → Markdown extraction  
**Phase 2 (later):** YAML decision logic + validation  
**Phase 3 (later):** Mobile-first app (React/PWA)  
**Phase 4 (later):** Offline logging + Raspberry Pi kiosk testing

---

## Repository Layout

```text
isolair-troubleshooting-app/
├─ app/                  # (later) React/PWA app
├─ data/
│  ├─ schema/            # JSON Schema for validating structured data
│  ├─ yaml/              # (later) authored decision trees
│  └─ json/              # (later) compiled runtime data
├─ docs/
│  ├─ source_pdfs/       # original PDFs (source of truth)
│  ├─ extracted_md/      # cleaned markdown extracted from PDFs
│  └─ images/            # exported diagrams/images (later)
├─ infra/
│  ├─ docker/            # docker-compose/dev containers (later)
│  └─ ci/                # github actions (later)
└─ scripts/              # extraction + validation scripts (later)

---

## `.gitignore`

This is a safe, practical ignore set for your current structure + future Node/React + Python scripts:

```gitignore
# ===== OS / Editor =====
.DS_Store
Thumbs.db
*.swp
*~
.vscode/*
!.vscode/extensions.json
!.vscode/settings.json
!.vscode/launch.json

# ===== Logs / temp =====
*.log
*.tmp
tmp/
temp/
.cache/
dist/
build/

# ===== Node / Web =====
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
*.tsbuildinfo
.vite/

# ===== Env files =====
.env
.env.*
!.env.example

# ===== Python =====
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/
ENV/
env/
pip-wheel-metadata/

# ===== Coverage / test =====
coverage/
.nyc_output/

# ===== PDFs / derived exports =====
# Keep the source PDFs in git if you want versioned docs.
# Ignore large derived outputs if you generate them later:
docs/extracted_md/_exports/
docs/images/_exports/

