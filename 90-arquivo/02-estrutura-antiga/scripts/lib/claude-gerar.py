"""
claude-gerar.py — Integração com a API do Claude para geração de conteúdo via Telegram.
Detecta frente, carrega briefing do agente, gera e ajusta conteúdo em multi-turno.
"""
import json
import os
import re
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path

VAULT   = Path(os.environ.get("TG_VAULT_PATH", ""))
SECRETS = Path(os.environ.get("TG_SECRETS_PATH", ""))

# ── Mapeamento frente → slug do agente ───────────────────────────────────────

_FRENTE_MAP = {
    "saúde":          "saude-sao-sebastiao",
    "saude":          "saude-sao-sebastiao",
    "sms":            "saude-sao-sebastiao",
    "secretaria":     "saude-sao-sebastiao",
    "sindss":         "sindss",
    "sindicato":      "sindss",
    "câmara":         "camara",
    "camara":         "camara",
    "lógika":         "logika",
    "logika":         "logika",
    "rogério":        "rogerio",
    "rogerio":        "rogerio",
    "além da foto":   "alem-da-foto",
    "alem da foto":   "alem-da-foto",
    "além-da-foto":   "alem-da-foto",
    "lives":          "lives-louvor",
    "louvor":         "lives-louvor",
    "vereadores":     "vereadores",
    "josi":           "vereadores",
    "vando":          "vereadores",
    "manoel":         "vereadores",
}

_SLUG_LABEL = {
    "saude-sao-sebastiao": "Saúde",
    "sindss":              "SINDSS",
    "camara":              "Câmara",
    "logika":              "Lógika",
    "rogerio":             "Rogério",
    "alem-da-foto":        "Além da Foto",
    "lives-louvor":        "Lives de Louvor",
    "vereadores":          "Vereadores",
}

# Arquivos de equipe/gestão por frente (carregados junto ao agente)
_FRENTE_EQUIPE = {
    "saude-sao-sebastiao": "[F1] 5-Frentes/Saude-Sao-Sebastiao/EQUIPE DE GESTÃO.md",
}

# Mapeamento slug → pasta dentro de [F1] 5-Frentes/
_FRENTE_F1_DIR = {
    "saude-sao-sebastiao": "[F1] 5-Frentes/Saude-Sao-Sebastiao",
    "camara":              "[F1] 5-Frentes/Camara-Municipal",
    "sindss":              "[F1] 5-Frentes/SINDSS",
    "logika":              "[F1] 5-Frentes/Logika-Creative",
    "alem-da-foto":        "[F1] 5-Frentes/Alem-da-Foto",
    "vereadores":          "[F1] 5-Frentes/Outros-Vereadores",
    "lives-louvor":        "[F1] 5-Frentes/Lives-Louvor-Reflexao",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def detectar_frente(texto: str):
    """Retorna (slug, label) ou (None, None) se não detectar."""
    t = texto.lower()
    for key in sorted(_FRENTE_MAP, key=len, reverse=True):
        if key in t:
            slug = _FRENTE_MAP[key]
            return slug, _SLUG_LABEL.get(slug, slug)
    return None, None


def _carregar_contexto_editorial(slug: str) -> str:
    """Lê todos os .md da pasta CONTEXTO EDITORIAL do Fluxo 1 da frente."""
    f1_rel = _FRENTE_F1_DIR.get(slug)
    if not f1_rel:
        return ""

    ctx_dir = VAULT / f1_rel / "CONTEXTO EDITORIAL"
    if not ctx_dir.is_dir():
        return ""

    partes = []
    for arq in sorted(ctx_dir.glob("*.md")):
        try:
            partes.append(f"### {arq.stem}\n{arq.read_text(encoding='utf-8')}")
        except Exception:
            pass
    return "\n\n".join(partes)


def _carregar_banco_referencias(slug: str) -> str:
    """Lê todos os .md da pasta 12 - BANCO DE REFERENCIAS do Fluxo 1 da frente."""
    f1_rel = _FRENTE_F1_DIR.get(slug)
    if not f1_rel:
        return ""

    banco_dir = VAULT / f1_rel / "12 - BANCO DE REFERENCIAS"
    if not banco_dir.is_dir():
        return ""

    partes = []
    # Guia condensado primeiro (prefixo 00), depois o restante em ordem
    for arq in sorted(banco_dir.glob("*.md")):
        try:
            partes.append(f"### {arq.stem}\n{arq.read_text(encoding='utf-8')}")
        except Exception:
            pass
    return "\n\n".join(partes)


def _carregar_identidade_autor() -> str:
    """Lê o arquivo de identidade do autor — contexto base para toda geração."""
    try:
        return (VAULT / "memory" / "agents" / "_jadielson-identidade.md").read_text(encoding="utf-8")
    except Exception:
        return ""


def _carregar_curadoria_pack() -> str:
    """Lê a curadoria do prompts-pack — frameworks e fórmulas extraídos dos melhores arquivos."""
    try:
        return (VAULT / "memory" / "databases" / "prompts-pack" / "00 - CURADORIA BOT.md").read_text(encoding="utf-8")
    except Exception:
        return ""


def carregar_agente(slug: str) -> str:
    """Carrega briefing do agente + contexto editorial completo do Fluxo 1."""
    secoes = []

    identidade = _carregar_identidade_autor()
    if identidade:
        secoes.append(
            "━━━ IDENTIDADE DO AUTOR ━━━\n"
            "Quem está por trás desta comunicação — leia para calibrar autenticidade e tom:\n\n"
            + identidade
        )

    agent_path = VAULT / "memory" / "agents" / slug
    agent_file = VAULT / "memory" / "agents" / f"{slug}.md"

    if agent_path.is_dir():
        # Pasta com múltiplos arquivos (ex: vereadores/)
        partes = []
        for arq in sorted(agent_path.glob("*.md")):
            try:
                partes.append(f"### {arq.stem}\n{arq.read_text(encoding='utf-8')}")
            except Exception:
                pass
        if partes:
            secoes.append("\n\n".join(partes))
    else:
        try:
            secoes.append(agent_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    ctx_editorial = _carregar_contexto_editorial(slug)
    if ctx_editorial:
        secoes.append(
            "━━━ CONTEXTO EDITORIAL COMPLETO (Fluxo 1) ━━━\n"
            "Use as expressões, hashtags e estruturas EXATAS abaixo:\n\n"
            + ctx_editorial
        )

    banco_refs = _carregar_banco_referencias(slug)
    if banco_refs:
        secoes.append(
            "━━━ BANCO DE REFERÊNCIAS — MELHORES RESULTADOS ━━━\n"
            "Exemplos reais aprovados. Use como inspiração direta de estrutura, tom e expressões:\n\n"
            + banco_refs
        )

    # Equipe e gestão da frente
    equipe_rel = _FRENTE_EQUIPE.get(slug)
    if equipe_rel:
        try:
            equipe_txt = (VAULT / equipe_rel).read_text(encoding="utf-8")
            secoes.append(
                "━━━ EQUIPE E GESTÃO ━━━\n"
                "Use estes nomes quando o usuário pedir menção a gestores, coordenadores ou autoridades:\n\n"
                + equipe_txt
            )
        except Exception:
            pass

    # Pessoas-chave transversais (prefeito, etc.) — de memory/context/people.md
    try:
        people_txt = (VAULT / "memory" / "context" / "people.md").read_text(encoding="utf-8")
        secoes.append(
            "━━━ PESSOAS-CHAVE DO MUNICÍPIO ━━━\n"
            "Referência para nomes de autoridades municipais:\n\n"
            + people_txt
        )
    except Exception:
        pass

    # Frameworks e fórmulas do prompts-pack — alternativas de forma quando contexto específico não resolve
    curadoria = _carregar_curadoria_pack()
    if curadoria:
        secoes.append(
            "━━━ FRAMEWORKS DE FORMA E PERSUASÃO ━━━\n"
            "Use como alternativa de estrutura, ângulo ou fórmula quando necessário. "
            "Sempre adapte ao contexto e tom da frente — nunca aplique direto sem calibrar:\n\n"
            + curadoria
        )

    return "\n\n".join(secoes)


def _api_key() -> str:
    for env_path in [SECRETS / "anthropic.env",
                     VAULT / "scripts" / ".secrets" / "anthropic.env"]:
        try:
            for line in Path(env_path).read_text().splitlines():
                line = line.strip()
                if line.startswith("ANTHROPIC_API_KEY"):
                    val = line.split("=", 1)[1].strip().strip('"')
                    if val and val != "sua-chave-aqui":
                        return val
        except Exception:
            pass
    return os.environ.get("ANTHROPIC_API_KEY", "")


def _regras_frente(slug: str) -> str:
    """Regras técnicas específicas por frente (hashtags, emojis, fechamento)."""
    if slug == "saude-sao-sebastiao":
        return (
            "\n\n━━━ REGRAS TÉCNICAS — SAÚDE SÃO SEBASTIÃO ━━━\n"
            "LIMITE DE CARACTERES:\n"
            "- LEGENDA inteira (texto + emojis + hashtags) = alvo 450–499 chars, nunca abaixo de 450\n"
            "- As 3 hashtags fixas somam ~65 chars — planeje o texto com ~380–420 chars\n"
            "- Use cada char disponível: seja imersivo, persuasivo, específico\n\n"
            "HASHTAGS (sempre ao final da LEGENDA, dentro dos 499):\n"
            "- EXATAMENTE 3 hashtags — nem mais, nem menos\n"
            "- Use APENAS estas três: #agentefazcomcoracao #saudesaosebastiaoal #maistrabalhomaisavanco\n"
            "- NUNCA adicione hashtags extras — nem de tema, nem de serviço\n"
            "- NUNCA: #SãoSebastião #Saúde #GestaoPública #emulti #fisioterapia ou qualquer outra\n\n"
            "EMOJIS:\n"
            "- Máximo 2 emojis discretos (💚🏥)\n"
            "- Sem exclamações em série, sem cascata de emojis\n\n"
            "ASSINATURA — REGRA DE INTEGRAÇÃO:\n"
            "- NUNCA escreva 'Saúde a gente faz com coração.' como linha isolada\n"
            "- Injete a essência da assinatura NA última frase do fechamento\n"
            "- Exemplos de integração natural:\n"
            "  '...porque saúde a gente faz com coração.'\n"
            "  '...cuidar com coração é o que a saúde pede.'\n"
            "  '...presença de quem faz saúde com coração.'"
        )
    if slug == "camara":
        return (
            "\n\n━━━ REGRAS TÉCNICAS — CÂMARA ━━━\n"
            "- Tom sóbrio, sem emojis excessivos\n"
            "- Hashtags: minúsculas sem acento\n"
            "- Nunca mencionar partido ou liderança de governo"
        )
    if slug == "sindss":
        return (
            "\n\n━━━ REGRAS TÉCNICAS — SINDSS ━━━\n"
            "- Hashtags: minúsculas sem acento (ex: #sindss #servidorpublico)\n"
            "- Presidente: Ceiça\n"
            "- Sexta: reservada para depoimentos de servidores"
        )
    return ""


def _system_prompt(slug: str, tipo: str = "legenda") -> str:
    agente_ctx = carregar_agente(slug)
    label      = _SLUG_LABEL.get(slug, slug)

    # Regras de protagonismo por frente
    protagonismo = {
        "saude-sao-sebastiao": (
            "A SECRETARIA DE SAÚDE DE SÃO SEBASTIÃO é sempre o SUJEITO da narrativa — não a Prefeitura, não o prefeito.\n"
            "❌ NUNCA como sujeito: 'A Prefeitura realizou...' / 'O prefeito entregou...' / 'A gestão do prefeito...'\n"
            "✅ SEMPRE como sujeito: 'A Secretaria de Saúde...' / 'A equipe da Saúde...' / 'O serviço de saúde...'\n\n"
            "MENÇÃO DE NOMES — REGRA DA PIRÂMIDE INVERTIDA:\n"
            "Nomes de coordenadores, secretário e prefeito estão disponíveis na seção EQUIPE E GESTÃO.\n"
            "USE-OS por padrão no fechamento da narrativa — não espere o usuário pedir.\n"
            "Posição obrigatória: último parágrafo da narrativa, antes do CTA.\n"
            "✅ Ex: '...ação coordenada por Alanderson, sob a secretaria de Felipe Regueira.'\n"
            "✅ Ex: '...com o apoio do secretário Felipe Regueira e do prefeito Charles.'\n"
            "✅ Ex: '...iniciativa da equipe de Alissandra, coordenadora da EMULTI.'\n"
            "❌ NUNCA abrir o texto com nome de gestor — fato e serviço sempre primeiro.\n"
            "❌ NUNCA omitir nomes quando o pedido mencionar gestores, coordenadores ou autoridades."
        ),
        "camara": (
            "A CÂMARA MUNICIPAL DE SÃO SEBASTIÃO é sempre o sujeito da narrativa.\n"
            "❌ NUNCA: 'O poder público...' / 'A administração...' / 'O governo...'\n"
            "✅ SEMPRE: 'A Câmara Municipal...' / 'Os vereadores...' / 'O parlamento municipal...'"
        ),
        "sindss": (
            "O SINDSS — Sindicato dos Servidores de São Sebastião — é sempre o protagonista.\n"
            "❌ NUNCA: genérico sindical ou governo\n"
            "✅ SEMPRE: 'O SINDSS...' / 'O sindicato...' / 'A entidade...'"
        ),
        "logika": (
            "A LÓGIKA CREATIVE / LÓGIKA FILMS é sempre o sujeito.\n"
            "❌ NUNCA: 'Uma agência...' / 'Profissionais de...'\n"
            "✅ SEMPRE: 'A Lógika...' / 'A Lógika Films...' / 'Nossa equipe...'"
        ),
    }.get(slug, f"A frente {label} é sempre o protagonista — nunca diluir em referência genérica.")

    base_escrever = (
        "━━━ COMO ESCREVER ━━━\n"
        "1. CONTE UMA HISTÓRIA — cada parágrafo avança a narrativa, não repete\n"
        "2. Abertura: pelo serviço ou fato concreto — NUNCA pelo nome do gestor\n"
        "3. Arco: contexto → ação → detalhes específicos → logística → significado\n"
        "4. Emoção vem dos detalhes reais (nomes de procedimentos, números, lugares)\n"
        "5. Feche com frase de compromisso — curta, com força\n"
        "6. Linguagem viva, com ritmo — nunca texto de diário oficial\n\n"
    )

    exemplo_estilo = (
        "━━━ EXEMPLO DO ESTILO ESPERADO ━━━\n"
        "O trabalho iniciado no Saúde em Movimento segue avançando e agora transforma triagem em resposta concreta para a população.\n\n"
        "Como desdobramento das ações do programa, 17 pacientes seguem para Palmeira dos Índios para cirurgias — histerectomia, colecistectomia, hérnia, postectomia e laqueadura. Esse avanço foi possível após o mutirão de consultas com cirurgião geral, realizado na semana passada no Espaço Cuidar, etapa fundamental para avaliar cada caso.\n\n"
        "Mais do que deslocar pacientes, essa ação representa continuidade de cuidado, organização da fila e compromisso com quem aguardava.\n\n"
        "Seguimos trabalhando para dar mais agilidade à assistência e transformar espera em cuidado de verdade.\n\n"
        "━━━ FIM DO EXEMPLO ━━━\n\n"
    )

    if tipo == "legenda":
        estrutura = (
            "━━━ SAÍDA — LEGENDA PRONTA PARA POSTAR ━━━\n"
            "Entregue APENAS o texto da legenda — sem título, sem prefixo '**LEGENDA**', sem seção.\n"
            "A resposta deve estar pronta para copiar e colar diretamente no Instagram ou Facebook.\n\n"
            "Estrutura interna (blocos separados por linha em branco):\n"
            "  BLOCO 1 — Gancho (máx 2 linhas): frase de impacto que para o scroll\n"
            "  BLOCO 2 — Desenvolvimento (máx 3 linhas): o que aconteceu, quem, como\n"
            "  BLOCO 3 — Fechamento (máx 2 linhas): impacto + assinatura INTEGRADA na frase\n"
            "    → A assinatura 'Saúde a gente faz com coração.' NÃO aparece sozinha\n"
            "    → Injete-a na última frase: ex: '...porque saúde a gente faz com coração.'\n"
            "  BLOCO 4 — CTA (1 linha + emoji): provoca comentário, tag ou reação\n"
            "    → Ex: 'Você estava lá? Conta nos comentários! 👇'\n"
            "  BLOCO 5 — Hashtags (1 linha, colada ao bloco 4): exatamente as hashtags da frente\n\n"
            "Tamanho alvo: 450–499 caracteres (tudo incluso). NUNCA entregue abaixo de 450.\n\n"
        )
        regras_finais = (
            "━━━ REGRAS FINAIS ━━━\n"
            "- Sempre em português brasileiro\n"
            "- Nunca invente dados — use [DADO] se necessário\n"
            "- Se pedir ajuste: aplique e reenvie a legenda completa (sem títulos de seção)\n"
            "- Alvo: 450–499 chars — não entregue abaixo de 450"
        )
    elif tipo == "headline":
        estrutura = (
            "━━━ SAÍDA — 3 HEADLINES PRONTAS ━━━\n"
            "Entregue APENAS as 3 variações de headline — sem título, sem prefixo, sem explicação.\n"
            "Prontas para copiar e colar no WhatsApp, story ou manchete de post.\n\n"
            "Formato exato (uma por linha):\n"
            "1. [headline]\n"
            "2. [headline]\n"
            "3. [headline]\n\n"
            "Regras por variação:\n"
            "  1 — impacto direto (fato + número ou resultado)\n"
            "  2 — ângulo emocional (quem se beneficia)\n"
            "  3 — chamada à ação (convite ou pergunta)\n"
            "Máx 80 chars por headline. Sem ponto final. Sem emojis.\n\n"
        )
        regras_finais = (
            "━━━ REGRAS FINAIS ━━━\n"
            "- Sempre em português brasileiro\n"
            "- Nunca invente dados — use [DADO] se necessário\n"
            "- Se pedir ajuste: reenvie as 3 headlines sem títulos de seção\n"
            "- Máx 80 chars por linha"
        )
    else:  # roteiro
        estrutura = (
            "━━━ SAÍDA — ROTEIRO PRONTO ━━━\n"
            "Entregue APENAS o roteiro — sem título, sem prefixo, sem seção separadora.\n"
            "Pronto para copiar e usar na gravação.\n\n"
            "Estrutura (use estes marcadores exatos, em MAIÚSCULAS, sem asteriscos):\n\n"
            "GANCHO (0–3s):\n"
            "[frase de abertura — para o scroll em 3 segundos]\n\n"
            "DESENVOLVIMENTO:\n"
            "[corpo narrativo em 3 parágrafos — contexto, ação, resultado]\n\n"
            "FECHAMENTO + CTA:\n"
            "[frase de encerramento com força + chamada à ação]\n\n"
            "SUGESTÕES DE B-ROLL:\n"
            "- [imagem 1]\n"
            "- [imagem 2]\n"
            "- [imagem 3]\n\n"
            "Tom: narrativa em 3 atos, linguagem viva, sem jargão institucional.\n\n"
        )
        regras_finais = (
            "━━━ REGRAS FINAIS ━━━\n"
            "- Sempre em português brasileiro\n"
            "- Nunca invente dados — use [DADO] se necessário\n"
            "- Se pedir ajuste: reenvie o roteiro completo sem prefixos extras\n"
            "- Gancho: máx 1 frase · Desenvolvimento: 3 parágrafos · CTA: 1 frase"
        )

    return (
        f"Você é o ghostwriter de comunicação de Jadielson Davi dos Santos, "
        f"Diretor de Comunicação em São Sebastião/AL.\n\n"
        f"Você escreve para a frente: {label}\n\n"

        f"━━━ PROTAGONISMO — REGRA INVIOLÁVEL ━━━\n"
        f"{protagonismo}\n\n"

        f"━━━ BRIEFING DO AGENTE — LEIA E APLIQUE INTEGRALMENTE ━━━\n"
        f"{agente_ctx}\n\n"

        + base_escrever
        + exemplo_estilo
        + estrutura
        + _regras_frente(slug)
        + "\n\n"
        + regras_finais
    )

# ── API call ──────────────────────────────────────────────────────────────────

def gerar(messages: list, frente_slug: str, tipo: str = "legenda") -> str:
    """
    Chama a API do Claude e retorna o texto gerado.
    messages = lista de {role, content} para suportar multi-turno.
    tipo = "legenda" | "headline" | "roteiro"
    """
    api_key = _api_key()
    if not api_key:
        return "❌ Chave da API do Claude não configurada em scripts/.secrets/anthropic.env"

    payload = json.dumps({
        "model":      "claude-sonnet-4-6",
        "max_tokens": 2000,
        "system":     _system_prompt(frente_slug, tipo),
        "messages":   messages,
    }, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key":         api_key,
            "anthropic-version": "2023-06-01",
            "content-type":      "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            data = json.loads(resp.read())
            return data["content"][0]["text"].strip()
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:300]
        return f"❌ Erro na API ({e.code}):\n{body}"
    except Exception as e:
        return f"❌ Erro: {str(e)[:200]}"

# ── Salvar no vault ───────────────────────────────────────────────────────────

def salvar_draft(frente_slug: str, pedido: str, conteudo: str) -> str:
    """Salva o conteúdo aprovado em memory/outputs/<frente>/drafts/. Retorna o caminho."""
    hoje  = date.today().isoformat()
    slug  = re.sub(r"[^a-z0-9\s]", "", pedido.lower())
    slug  = "-".join(slug.split()[1:6])  # pula a frente, pega 5 palavras do pedido
    slug  = slug[:50] or "conteudo"

    dest_dir = VAULT / "memory" / "outputs" / frente_slug / "drafts"
    dest_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{hoje}-{slug}.md"
    dest     = dest_dir / filename

    # Evita sobrescrita
    counter = 1
    while dest.exists():
        dest = dest_dir / f"{hoje}-{slug}-{counter}.md"
        counter += 1

    label = _SLUG_LABEL.get(frente_slug, frente_slug)
    texto = (
        f"---\n"
        f"tipo: draft\n"
        f"frente: {frente_slug}\n"
        f"gerado-por: claude-telegram\n"
        f"revisado: false\n"
        f"data: {hoje}\n"
        f"pedido: \"{pedido[:120].replace(chr(34), chr(39))}\"\n"
        f"---\n\n"
        f"# {label} — {slug.replace('-', ' ').title()}\n\n"
        f"{conteudo}\n"
    )

    dest.write_text(texto, encoding="utf-8")
    return str(dest.relative_to(VAULT))
