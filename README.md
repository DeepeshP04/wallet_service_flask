# Headless Wallet Microservice

A headless microservice that simulates a single-wallet system supporting some key money operations.

## Folder Structure

```
wallet_service/
│
├── app.py
├── requirements.txt
├── README.md
│
├── instance/
│   └── wallet.db
│
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── ... (migration scripts)
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── extensions.py
│   ├── utils.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schema.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── wallet_services.py
│   │   └── report_services.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── wallet_routes.py
│       └── report_routes.py
│
└── venv/
    └── ... (virtual environment files)
```

## Dependencies

- flask
- flask-sqlalchemy
- flask-migrate
- marshmallow

## Database?  
I chose SQLite database for this wallet service. Why?

- **Simplicity:** SQLite is serverless and requires no setup, making it ideal for development, prototyping, and small-scale deployments.
- **Portability:** The database is stored in a single file, making it easy to move or back up.
- **Persistance:** Data such as balances, holds, and logs are persisted across server restarts because SQLite stores it on disk (wallet.db).
- **Sufficient for Use Case:** For a lightweight wallet microservice, SQLite provides all the necessary features without the overhead of a full RDBMS.

## API Endpoints

### Wallet Operations
- `POST /wallet/init` — Initialize a new wallet for a user.
- `POST /wallet/add_money` — Add money to a user's wallet.
- `POST /wallet/hold_money` — Place a hold on a specified amount in the wallet.
- `POST /wallet/release_hold` — Release eligible holds (after 10 minutes).
- `POST /wallet/reverse_hold` — Reverse a specific hold.

### Reporting
- `GET /report/wallet_balance` — Get the current balance for a user's wallet.
- `GET /report/hold_report` — Get the number of holds by status (active, released, reversed) for a user.
- `GET /report/wallet_operation_report` — Get the number of wallet operations (e.g., total adds, total holds) for a user.

---

**Note:** All endpoints expect and return JSON.