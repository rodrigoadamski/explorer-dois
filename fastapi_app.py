import os
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

try:
    from supabase import create_client, Client
except Exception:  # pragma: no cover - supabase optional
    create_client = None
    Client = None  # type: ignore


load_dotenv()

app = FastAPI(title="External API", version="0.1.0")


def get_supabase_client() -> "Client":
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")
    if not url or not key:
        raise RuntimeError("SUPABASE_URL/SUPABASE_ANON_KEY não configurados")
    if create_client is None:
        raise RuntimeError("Biblioteca supabase não instalada")
    return create_client(url, key)


@app.get("/api/reports", response_model=List[Dict[str, Any]])
def list_reports() -> List[Dict[str, Any]]:
    """Retorna denúncias da tabela 'reports_report' (Django ORM -> tabela)."""
    try:
        supa = get_supabase_client()
        # Ajuste o nome da tabela se necessário
        resp = supa.table("reports_report").select("*").order("criado_em", desc=True).execute()
        return resp.data or []
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc))


class AlertIn(BaseModel):
    source: str
    title: str
    description: str | None = None
    severity: str | None = None


@app.post("/webhooks/alerts")
def webhook_alerts(payload: AlertIn) -> Dict[str, str]:
    """Webhook simples que pode acionar integrações (Telegram/WhatsApp/Slack)."""
    # Aqui você pode enviar para Slack/Telegram/Twilio usando variáveis do .env
    # Exemplo (pseudo): requests.post(os.getenv("SLACK_WEBHOOK_URL"), json={...})
    return {"status": "received", "title": payload.title}


@app.get("/api/alerts", response_model=List[Dict[str, Any]])
def list_alerts() -> List[Dict[str, Any]]:
    """Retorna dados oficiais coletados (placeholder até a criação da tabela)."""
    return []


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "fastapi_app:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8001)),
        reload=True,
    )

