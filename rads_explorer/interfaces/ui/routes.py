from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from rads_explorer.container.container import get_container

router = APIRouter(prefix="/ui", tags=["UI"])


@router.get("", response_class=HTMLResponse)
def home(num_items: int = 20):
    container = get_container()
    report_service = container.report_service()

    rows = report_service.build_certificates_inventory()

    html = f"""
    <html>
        <head><title>RADS Explorer</title></head>
        <body>
            <h1>Перечень первых {num_items} сертификатов</h1>
            <ul>
    """

    for c in rows[:num_items]:
        html += f"<li>{c.serial_number}: {c.common_name}</li>"

    html += """
            </ul>
        </body>
    </html>
    """

    return html
