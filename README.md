# Late Show API

A Flask REST API for managing late-night show episodes, guests, and appearances.

## Quick Start

```bash
pip install -r requirements.txt
python3 seed.py
python3 app.py
# API available at http://localhost:5555
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message with all endpoints |
| GET | `/episodes` | List all episodes |
| GET | `/episodes/<id>` | Get episode with appearances |
| DELETE | `/episodes/<id>` | Delete an episode |
| GET | `/guests` | List all guests |
| POST | `/appearances` | Create appearance |

## Example Requests

```bash
# Get all episodes
curl http://localhost:5555/episodes

# Get episode with appearances
curl http://localhost:5555/episodes/1

# Create appearance
curl -X POST http://localhost:5555/appearances \
  -H "Content-Type: application/json" \
  -d '{"rating": 5, "episode_id": 2, "guest_id": 3}'
```

## Models

- **Episode**: id, date, number
- **Guest**: id, name, occupation
- **Appearance**: id, rating (1-5), episode_id, guest_id

## Validation

- Rating must be integer 1-5
- episode_id and guest_id must reference existing records
- Cascade delete enabled for appearances

## Files

- `app.py` - Flask application
- `seed.py` - Database seeder
- `requirements.txt` - Dependencies
