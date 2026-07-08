"""
state-manager.py — Gerencia estado conversacional do bot Telegram.
Estado persiste em scripts/state/telegram-state.json. Expira em 1h.
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

STATE_FILE = Path(__file__).parent.parent / "state" / "telegram-state.json"
TTL_HOURS = 1


def _load():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _is_expired(entry):
    expira = entry.get("expira_em")
    if not expira:
        return False
    try:
        return datetime.fromisoformat(expira) < datetime.now()
    except Exception:
        return True


def get_state(chat_id):
    state = _load()
    entry = state.get(str(chat_id), {})
    if _is_expired(entry):
        clear_state(chat_id)
        return {}
    return entry


def set_state(chat_id, **kwargs):
    state = _load()
    cid = str(chat_id)
    if cid not in state:
        state[cid] = {}
    state[cid].update(kwargs)
    state[cid]["expira_em"] = (datetime.now() + timedelta(hours=TTL_HOURS)).isoformat()
    _save(state)


def clear_state(chat_id):
    """Limpa estado de fluxo mas preserva ultima_captura."""
    state = _load()
    cid = str(chat_id)
    ultima = state.get(cid, {}).get("ultima_captura")
    state[cid] = {}
    if ultima:
        state[cid]["ultima_captura"] = ultima
    _save(state)


def get_last_capture(chat_id):
    state = _load()
    return state.get(str(chat_id), {}).get("ultima_captura")


def set_last_capture(chat_id, capture):
    state = _load()
    cid = str(chat_id)
    if cid not in state:
        state[cid] = {}
    state[cid]["ultima_captura"] = {
        **capture,
        "timestamp": datetime.now().isoformat(),
    }
    _save(state)


def is_state_expired(chat_id):
    state = _load()
    return _is_expired(state.get(str(chat_id), {}))
