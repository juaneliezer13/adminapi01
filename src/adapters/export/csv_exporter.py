from src.application.export.export_service import ExportServicePort
from typing import List
from src.domain.entities.user import User
import csv
import io


class CSVExporter(ExportServicePort):
    def export_users_csv(self, users: List[User]) -> bytes:
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(["id", "email", "full_name"])
        for u in users:
            writer.writerow([u.id or "", u.email, u.full_name])
        return buf.getvalue().encode("utf-8")
