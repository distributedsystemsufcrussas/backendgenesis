
from fastapi import APIRouter, Depends

import datetime

from app.api.deps import get_current_active_user
# Roteador para dados do painel principal (Dashboard)
router_dashboard = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)