# Development Rules

## General Rules

- Keep code modular
- Separate API logic from UI logic
- No hardcoded mock data in production mode
- All time must be converted to Asia/Taipei (UTC+8)

---

## Frontend Rules

- Use vanilla HTML/CSS/JavaScript
- No frameworks unless explicitly requested
- Must support GitHub Pages deployment
- Must be responsive (mobile + desktop)

---

## Backend Rules

- Python 3.12
- FastAPI architecture
- Async HTTP requests (httpx)
- Clean service-layer separation

---

## API Integration Rules

### Football
Use API-Football as primary source

### NBA
Use API-Basketball

### MLB
Use MLB Stats API

---

## Data Handling Rules

- Normalize all matches into unified schema:
  {
    sport,
    league,
    home_team,
    away_team,
    home_score,
    away_score,
    match_time,
    status
  }

- status:
  - upcoming
  - finished

---

## UI Rules

- Always show:
  - sport badge
  - match time
  - teams
  - score if available
  - status label

---

## Performance Rules

- Cache API responses (backend phase)
- Avoid repeated fetch calls
- Render only filtered dataset
