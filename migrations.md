# Database Migrations

## Configuration

1. Install Alembic:
```bash
uv add alembic
```

2. Initialize Alembic in the project:
```bash
uv run alembic init alembic
```

3. Create a `.env` file in the project root:
```
DATABASE_URL="postgresql://postgres@localhost:5431/fastapi_yt"
```

4. Update `alembic/env.py` to load your models and database URL:
```python
from app.database.db import Base
from app.config.app_config import AppConfig

config.set_main_option("sqlalchemy.url", AppConfig.database_url)
target_metadata = Base.metadata
```


## Run all pending migrations
```bash
uv run alembic upgrade head
```

## Revert last migration
```bash
uv run alembic downgrade -1
```

## Create a new migration
1. Modify your schema files in `app/database/schema/`
2. Generate the migration:
```bash
uv run alembic revision --autogenerate -m "description of changes"
```
3. Apply it:
```bash
uv run alembic upgrade head
```

## Check current migration status
```bash
uv run alembic current
```

## View migration history
```bash
uv run alembic history
```

## Downgrade to a specific revision
```bash
uv run alembic downgrade <revision_id>
```

## Upgrade to a specific revision
```bash
uv run alembic upgrade <revision_id>
```

## Show pending migrations
```bash
uv run alembic heads
```

## Show migration SQL without applying
```bash
uv run alembic upgrade head --sql
```

## Stamp the database with a revision (without running migrations)
```bash
uv run alembic stamp <revision_id>
```
