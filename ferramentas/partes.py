"""Aplica as partes comuns do site (cabeçalho, rodapé, planos) em todas as páginas.
Uso: python3 ferramentas/partes.py   (idempotente; roda da raiz do repo)"""
import re, pathlib

PAGINAS = ["index.html", "oferta.html", "metodo.html", "produtos.html", "estudio.html", "cartografia.html"]
LINKS = [("oferta.html", "A Oferta"), ("metodo.html", "O Método"), ("produtos.html", "A Prova"),
         ("estudio.html", "O Estúdio"), ("guilherme/", "O Fundador")]
WHATS = "5521920509475"

def nav(atual):
    itens = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if h == atual else ""}>{t}</a>' for h, t in LINKS)
    return f'''<header class="site-header">
    <nav aria-label="Navegação principal">
      <a class="wordmark" href="index.html">VERTEX</a>
      <div class="nav-links">
{itens}
        <a class="btn btn-ghost btn-sm" href="consulta.html">Agendar conversa</a>
      </div>
    </nav>
  </header>'''

RODAPE = '''<footer class="site-footer">
    <div class="footer-inner">
      <span class="wordmark">VERTEX</span>
      <nav class="footer-nav" aria-label="Rodapé">
        <a href="oferta.html">A Oferta</a>
        <a href="cartografia.html">A Cartografia</a>
        <a href="metodo.html">O Método</a>
        <a href="produtos.html">A Prova</a>
        <a href="estudio.html">O Estúdio</a>
        <a href="https://www.instagram.com/vertex.devs/" target="_blank" rel="noopener">@vertex.devs</a>
      </nav>
      <p>Tecnologia com dono. · Engenharia no seu ponto mais alto. · © 2026 Vertex Devs · Brasil &amp; Portugal</p>
    </div>
  </footer>'''

PLANOS = [
    ("Conselho", "R$ 6.000", "por mês", False, "Para quem tem fornecedores e sistemas, mas não tem time técnico.",
     ["Reunião quinzenal e canal direto", "Decisões de tecnologia e governança de fornecedores", "Relatório mensal e registro de decisões"]),
    ("Diretoria", "R$ 14.000", "por mês", True, "Para quem precisa decidir e construir.",
     ["Presença semanal e canal direto", "Até 40 horas por mês da engenharia da casa", "Plantão de incidente em horário comercial", "Conselho trimestral com os sócios"]),
    ("Diretoria plena", "desde R$ 26 mil", "por mês", False, "Para quem tem time interno ou operação crítica.",
     ["Lidera e contrata o time interno", "Squad dedicado da casa", "Plantão estendido"]),
]

def planos():
    cards = []
    for nome, preco, per, rec, para, itens in PLANOS:
        li = "".join(f"<li>{i}</li>" for i in itens)
        flag = '<span class="plan-flag">Recomendada</span>' if rec else '<span class="plan-flag" aria-hidden="true"></span>'
        cards.append(f'''        <article class="plan{' plan--featured' if rec else ''}" data-reveal>
          {flag}
          <h3>{nome}</h3>
          <p class="plan-for">{para}</p>
          <ul>{li}</ul>
        </article>''')
    return '<div class="plans" data-partes="planos">\n' + "\n".join(cards) + "\n      </div>"

for p in PAGINAS:
    f = pathlib.Path(p)
    if not f.exists():
        continue
    s = f.read_text()
    s = re.sub(r"<header class=\"site-header\">.*?</header>|<!--NAV-->", lambda m: nav(p), s, count=1, flags=re.S)
    s = re.sub(r"<footer class=\"site-footer\">.*?</footer>|<!--FOOTER-->", RODAPE, s, count=1, flags=re.S)
    s = re.sub(r'<div class="plans" data-partes="planos">.*?\n      </div>|<!--PLANS-->', lambda m: planos(), s, flags=re.S)
    f.write_text(s)

# WhatsApp profissional (21) no lugar do antigo 48, em todo HTML e JS
for f in list(pathlib.Path(".").glob("*.html")) + list(pathlib.Path(".").glob("*.js")):
    s = f.read_text()
    n = s.replace("wa.me/554892044331", f"wa.me/{WHATS}")
    if n != s:
        f.write_text(n)
print("ok")
