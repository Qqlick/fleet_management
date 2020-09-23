Fleet Management API


CICD with db migrations with alembic: <https://github.com/Qqlick/fleet_management/commit/72ba5d7983edc0e3100407fca0f83a468720f80a/checks?check_suite_id=255192822>

Stack:
- Flask, Flask-restplus
- SQLAlchemy
- Alembic
- Zappa
- AWS Lambda as backend, AWS API Gateway, AWS Secret Manager
- MySQL
- Pytest
- Github actions as CICD pipeline
