from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape

from radp.config.paths import TEMPLATE_DIR
from radp.runtime import Runtime

from .runtime import get_runtime

jinja_env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=select_autoescape(["html", "xml"]),
    cache_size=0,
)
router = APIRouter(prefix="/web", tags=["web"])


@router.get("/certificates", response_class=HTMLResponse)
def certificates(request: Request, runtime: Runtime = Depends(get_runtime)):
    report_service = runtime.report()

    rows = report_service.build_certificates_inventory()

    template = jinja_env.get_template("certificates.html")
    html = template.render(request=request, certificate_report_rows=rows)
    return HTMLResponse(content=html)


@router.get("", response_class=HTMLResponse)
def home(num_items: int = 20, runtime: Runtime = Depends(get_runtime)):
    report_service = runtime.report()

    rows = report_service.build_first_page_view()

    html = f"""
    <html>
        <head><title>RADS Explorer</title></head>
        <body>
            <h1>Перечень первых {num_items} сертификатов</h1>
            <ul>
    """

    for c in rows.items:
        html += f"<li>{c.id} ({c.serial_number}): {c.name_attributes.commonName}</li>"

    html += """
            </ul>
        </body>
    </html>
    """

    return html
