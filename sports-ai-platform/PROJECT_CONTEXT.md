# Sports AI Platform

## Overview

This project is a sports data aggregation and analytics platform focusing on:

- Football (Soccer)
- NBA Basketball
- MLB Baseball

The system provides:

- Live scores
- Match schedules
- Final results
- Team information
- UTC+8 time normalization
- Basic match filtering

No betting, no payment, no gambling execution.

---

## Data Sources

### Football
- API: API-Football
- Coverage: major global leagues (EPL, La Liga, UCL, World Cup)

### NBA
- API: API-Basketball

### MLB
- API: MLB Stats API (official public endpoints)

---

## Core Features

- Multi-sport aggregation
- Date filtering
- Sport category filtering
- Match status filtering (upcoming / finished)
- UTC+8 timezone display
- Responsive web UI

---

## Architecture

Frontend:
- Static site (GitHub Pages)

Backend (Phase 2):
- FastAPI (Python)

Database (Phase 2):
- PostgreSQL

---

## Timezone Rule

All match times must be displayed in:

UTC+8 (Asia/Taipei)

All API timestamps must be converted before rendering.

---

## Future Expansion

- AI match prediction system
- Team performance index
- Historical head-to-head analysis
- Win probability model
