# Folder: data/raw

## 📍 Purpose
Holds all unprocessed telecom datasets — directly collected or simulated.

---

## 📂 Contents & Lineage
| File | Description | Generated From | Used In |
|------|--------------|----------------|---------|
| `telecom_data_messy_python.csv` | Primary raw dataset with inconsistencies | External source / simulated generator | Phase 2A & 2B notebooks |
| `telecom_data_messy_sql.csv` | SQL-exported variant of raw data | From BigQuery / DB exports | Phase 2A audit + SQL validation |
| `telecom_data_sample.csv` | Smaller subset for teaching demos | Extracted manually from messy dataset | Used in mini-handbooks & quick labs |
| `.gitkeep` | Folder placeholder | — | — |

---

## 🧩 Notes
- Keep this directory **read-only** to preserve data integrity.  
- Version any modifications via DVC tags.

_Last Updated: 2025-10-13_
