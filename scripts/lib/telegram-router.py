"""
telegram-router.py — Roteador de comandos e callbacks do bot Telegram.
Despacha para telegram-commands.py (Fases 2–4).
"""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent

CAPTURE_PREFIXES = {
    "/t", "/tarefa",
    "/c", "/compromisso",
    "/r", "/reuniao", "/reunião",
    "/g", "/gravacao", "/gravação",
    "/n", "/nota", "/captura",
    "/p", "/publicacao", "/publicação",
    "/i", "/inbox",
}

INTERACTIVE_COMMANDS = {
    "/start", "/menu", "/status", "/agenda",
    "/buscar", "/confirmar", "/cancelar", "/repetir", "/gerar", "/projeto",
    "/tpd", "/tpg",
}


# Módulos carregados UMA VEZ no startup — evita EDEADLK do OneDrive por recarga por mensagem.
# telegram-polling.sh copia scripts/lib/*.py para /tmp/tg-lib antes de iniciar; preferimos essas
# cópias pois estão fora do escopo de sync do OneDrive.
_LIB_TMP = Path("/tmp/tg-lib")

def _lib_path(fname):
    p = _LIB_TMP / fname
    return p if p.exists() else _HERE / fname

def _load_once(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_cmds_mod = _load_once("telegram_commands", _lib_path("telegram-commands.py"))
_sm_mod   = _load_once("state_manager",     _lib_path("state-manager.py"))

def _cmds(): return _cmds_mod
def _sm():   return _sm_mod


def route_message(chat_id, text, send_fn):
    """
    Retorna True se a mensagem foi tratada (não chamar lógica de captura).
    Retorna False para cair na captura normal.
    """
    parts = text.strip().split(None, 1)
    cmd   = parts[0].lower() if parts else ""
    args  = parts[1] if len(parts) > 1 else ""

    cmds = _cmds()

    # Texto livre com estado ativo — verifica primeiro
    if not text.startswith("/"):
        if cmds.handle_free_text(chat_id, text):
            return True
        return False  # sem estado ativo → cai na captura normal

    # Comandos de captura → cai na lógica existente
    if cmd in CAPTURE_PREFIXES:
        return False

    # Comandos interativos
    if cmd == "/start":
        cmds.cmd_start(chat_id, args)
        return True
    if cmd == "/menu":
        cmds.cmd_menu(chat_id, args)
        return True
    if cmd == "/status":
        cmds.cmd_status(chat_id, args)
        return True
    if cmd == "/agenda":
        cmds.cmd_agenda(chat_id, args)
        return True
    if cmd == "/buscar":
        cmds.cmd_buscar(chat_id, args)
        return True
    if cmd == "/confirmar":
        cmds.cmd_confirmar(chat_id, args)
        return True
    if cmd == "/cancelar":
        cmds.cmd_cancelar(chat_id, args)
        return True
    if cmd == "/repetir":
        cmds.cmd_repetir(chat_id, args)
        return True
    if cmd == "/gerar":
        cmds.cmd_gerar(chat_id, args)
        return True
    if cmd == "/projeto":
        cmds.cmd_projeto(chat_id, args)
        return True
    if cmd == "/tpd":
        cmds.cmd_tpd(chat_id, args)
        return True
    if cmd == "/tpg":
        cmds.cmd_tpg(chat_id, args)
        return True

    # Comando desconhecido → ignora silenciosamente
    if text.startswith("/"):
        return True

    return True


def route_callback(chat_id, callback_data, answer_fn):
    """
    Roteia callback de botão inline.
    answer_fn() remove o "loading" do botão — deve ser chamado sempre.
    """
    answer_fn()

    sm = _sm()
    if sm.is_state_expired(chat_id):
        sm.clear_state(chat_id)

    _cmds().handle_callback(chat_id, callback_data)
