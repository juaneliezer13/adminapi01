from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from src.adapters.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from src.adapters.export.csv_exporter import CSVExporter

router = APIRouter()


@router.get("/export/users", tags=["Export"], summary="Export users as CSV")
def export_users(db: Session = Depends(get_db)):
    repo = SQLAlchemyUserRepository(db)

    users = repo.list_all()

    exporter = CSVExporter()
    csv_bytes = exporter.export_users_csv(users)
    return Response(content=csv_bytes, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=users.csv"})
