"""Gera as páginas do site claro (index, casos) com cabeçalho, rodapé e pixel comuns.
Uso (da raiz do repo): python3 ferramentas/gerar.py
Os cases ficam em casos.js; aqui só a estrutura das páginas."""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PIXEL = (RAIZ / "ferramentas/_pixel.html").read_text()
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com" />\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />'
LINKS = [("index.html#areas", "Resultados"), ("casos.html", "Cases"), ("index.html#como", "Como funciona"), ("index.html#momento", "Para quem")]


def head(titulo, desc, url):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{titulo}</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="64x64" href="assets/favicon-64.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png" />
  <meta name="theme-color" content="#ffffff" />
  <meta property="og:title" content="{titulo}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="https://vertexdevs.org/assets/og-image.jpg" />
  <meta property="og:url" content="https://vertexdevs.org/{url}" />
  <meta property="og:type" content="website" />
  {FONTS}
  <link rel="stylesheet" href="site.css" />
{PIXEL}
</head>'''


def nav(atual):
    itens = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == atual else ""}>{t}</a>' for h, t in LINKS)
    return f'''<header class="nav"><div class="wrap">
    <a class="logo" href="index.html" aria-label="Vertex, início">VERTEX</a>
    <nav class="nav-links" aria-label="Principal">{itens}<a class="btn btn-primary btn-sm" href="consulta.html">Agendar conversa</a></nav>
  </div></header>'''


RODAPE = '''<footer class="footer"><div class="wrap">
    <span>© 2026 Vertex · Consultoria de IA aplicada · Brasil e Portugal</span>
    <nav aria-label="Rodapé"><a href="casos.html">Cases</a><a href="index.html#como">Como funciona</a><a href="consulta.html">Agendar conversa</a><a href="https://www.instagram.com/vertex.devs/" target="_blank" rel="noopener">Instagram</a></nav>
  </div></footer>'''

SHEET = '<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-labelledby="sheet-title" aria-hidden="true"><div class="sheet-body"></div></div>'
SCRIPTS = '<script src="casos.js"></script>\n  <script src="site.js"></script>\n  <script src="efeitos.js"></script>'

CURVA = '''<svg viewBox="0 0 900 300" role="img" aria-label="Piloto fica parado; resultado cresce mês a mês">
          <defs><linearGradient id="fillResult" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2f5bc4" stop-opacity=".18"/><stop offset="100%" stop-color="#2f5bc4" stop-opacity="0"/></linearGradient></defs>
          <g class="grid"><line x1="40" y1="250" x2="880" y2="250"/><line x1="40" y1="170" x2="880" y2="170"/><line x1="40" y1="90" x2="880" y2="90"/></g>
          <g class="axis"><text x="40" y="275">Mês 1</text><text x="300" y="275">Mês 3</text><text x="580" y="275">Mês 6</text><text x="830" y="275">Mês 12</text></g>
          <path class="pilot" d="M40 238 C 200 236, 320 232, 420 236 S 700 240, 880 237"/>
          <path class="area" d="M40 242 C 180 236, 260 212, 360 186 S 560 120, 680 88 S 820 46, 880 38 L 880 250 L 40 250 Z"/>
          <path class="result" d="M40 242 C 180 236, 260 212, 360 186 S 560 120, 680 88 S 820 46, 880 38"/>
          <circle class="dot" cx="880" cy="38" r="7"/>
          <g class="tag" transform="translate(600 200)"><rect width="240" height="34" rx="17"/><text x="18" y="22">Piloto: não chega ao caixa</text></g>
          <g class="tag" transform="translate(470 26)"><rect width="270" height="34" rx="17"/><text x="18" y="22">Resultado: medido todo mês</text></g>
        </svg>'''

INDEX = f'''{head("Vertex · Menos piloto. Mais resultado.", "Consultoria de IA que executa: colocamos IA para trabalhar no financeiro, fiscal, vendas, telefonia e atendimento, e medimos o retorno todo mês.", "")}
<body>
  <a class="skip" href="#principal">Pular para o conteúdo</a>
  {nav("index.html")}
  <main id="principal">

    <section class="hero">
      <div class="aurora" aria-hidden="true" data-aurora='{{"stops":["#9db8f5","#2f5bc4","#c9b8f2"],"lightMode":true,"height":0.5,"amplitude":0.9,"blend":0.6,"opacity":0.55,"speed":0.6}}'></div>
      <div class="wrap">
        <span class="eyebrow">Consultoria de IA aplicada</span>
        <h1 class="h1" data-blur>Menos piloto. <span class="grad">Mais resultado.</span></h1>
        <p class="lead">Colocamos IA para trabalhar na sua operação. E medimos o retorno em reais.</p>
        <div class="hero-cta"><a class="btn btn-primary" href="consulta.html">Agendar conversa</a><a class="btn btn-ghost" href="casos.html">Ver cases ›</a></div>
      </div>
      <div class="wrap">
        <div class="hero-chart curve">
          <div class="hero-chart-top">
            <div><div class="h3">95% dos pilotos de IA não chegam ao caixa.</div><div class="src">MIT, The GenAI Divide, 2025</div></div>
            <div class="legend"><span><i style="background:#b9b9c0"></i>Piloto</span><span><i style="background:#2f5bc4"></i>Com a Vertex</span></div>
          </div>
          {CURVA}
        </div>
      </div>
    </section>

    <section class="alt" aria-label="Números">
      <div class="wrap">
        <div class="stats">
          <div class="stat dark reveal"><b class="num" data-count="300" data-suffix="+">300+</b><span>sistemas em produção</span></div>
          <div class="stat reveal"><b class="num">2</b><span>países: Brasil e Portugal</span></div>
          <div class="stat reveal"><b class="num" data-count="22">22</b><span>cases com número, nesta página</span></div>
          <div class="stat reveal"><b class="num">100%</b><span>do código e dos acessos com você</span></div>
        </div>
      </div>
    </section>

    <section id="areas">
      <div class="wrap">
        <div class="head"><span class="eyebrow">Onde a IA paga a conta</span><h2 class="h2">Escolha a área. Veja o antes e o depois.</h2></div>
        <div class="tabs" id="area-tabs" role="tablist" aria-label="Áreas"></div>
        <div id="area-panels"></div>
      </div>
    </section>

    <section class="alt" id="cases">
      <div class="wrap">
        <div class="head"><span class="eyebrow">Cases</span><h2 class="h2">Cada projeto, um número.</h2><p class="lead">Sem nome de cliente. Com o resultado.</p></div>
        <div class="cases" id="cases-grid" data-destaque="true"></div>
        <div style="text-align:center;margin-top:2rem"><a class="btn btn-dark" href="casos.html">Ver todos os cases</a></div>
      </div>
    </section>

    <section id="momento">
      <div class="wrap">
        <div class="head center"><span class="eyebrow">Para quem</span><h2 class="h2">Em que momento sua empresa está?</h2></div>
        <div class="moments">
          <button class="moment reveal" type="button" data-m="ideia" aria-pressed="true"><span class="ico">01</span><h3>Ideia</h3><p>Sei que a IA pode ajudar. Não sei por onde começar.</p></button>
          <button class="moment reveal" type="button" data-m="rodando" aria-pressed="false"><span class="ico">02</span><h3>Processo rodando</h3><p>A operação funciona, mas custa caro e depende de gente.</p></button>
          <button class="moment reveal" type="button" data-m="time" aria-pressed="false"><span class="ico">03</span><h3>Time tradicional</h3><p>Meu time não é AI-first. Preciso que a IA entre sem travar nada.</p></button>
        </div>
        <div class="path" id="moment-path" aria-live="polite"></div>
      </div>
    </section>

    <section class="alt" id="como">
      <div class="wrap">
        <div class="head center"><span class="eyebrow">Como funciona</span><h2 class="h2">Do diagnóstico ao número.</h2></div>
        <div class="steps">
          <div class="step reveal"><span class="dot">1</span><b>Diagnóstico</b><span>Onde a IA paga a conta na sua operação.</span><em>2 semanas</em></div>
          <div class="step reveal"><span class="dot">2</span><b>Primeiro resultado</b><span>Um caso rodando de verdade, com número.</span><em>semanas, não trimestres</em></div>
          <div class="step reveal"><span class="dot">3</span><b>Escala</b><span>Novos casos todo trimestre.</span><em>contínuo</em></div>
          <div class="step reveal"><span class="dot">4</span><b>Retorno medido</b><span>Um relatório por mês: quanto a IA devolveu.</span><em>todo mês</em></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="head center"><span class="eyebrow">AI-first de verdade</span><h2 class="h2">Não vendemos piloto. Entregamos operação.</h2></div>
        <div class="versus">
          <div class="card reveal"><h3 class="h3">O que o mercado entrega</h3><ul>
            <li><span class="mark-x">✕</span>Demonstração bonita que não vai para a operação</li>
            <li><span class="mark-x">✕</span>Ferramenta antes do problema</li>
            <li><span class="mark-x">✕</span>Relatório e tchau</li>
            <li><span class="mark-x">✕</span>Sem número no fim do mês</li>
          </ul></div>
          <div class="card us reveal"><h3 class="h3">O que a Vertex entrega</h3><ul>
            <li><span class="mark-v">✓</span>IA rodando no processo real, com gente usando</li>
            <li><span class="mark-v">✓</span>Problema primeiro, ferramenta depois</li>
            <li><span class="mark-v">✓</span>Mão na massa até o resultado aparecer</li>
            <li><span class="mark-v">✓</span>Retorno medido em reais, todo mês</li>
          </ul></div>
        </div>
      </div>
    </section>

    <section class="alt cta">
      <div class="wrap">
        <h2 class="h2">Qual processo vai dar resultado primeiro?</h2>
        <a class="btn btn-primary" href="consulta.html">Agendar conversa</a>
      </div>
    </section>
  </main>
  {RODAPE}
  {SHEET}
  {SCRIPTS}
</body>
</html>
'''

CASOS = f'''{head("Cases · Vertex", "Cases de IA aplicada em financeiro, fiscal, aquisição de clientes, telefonia, WhatsApp e operação. Sem nome de cliente, com o número.", "casos.html")}
<body>
  <a class="skip" href="#principal">Pular para o conteúdo</a>
  {nav("casos.html")}
  <main id="principal">
    <section class="hero" style="padding-bottom:2rem">
      <div class="wrap">
        <span class="eyebrow">Cases</span>
        <h1 class="h1" style="max-width:14ch">Cada projeto, <span class="grad">um número.</span></h1>
        <p class="lead">Sem nome de cliente. Com o resultado. Filtre pela sua área ou pelo seu momento.</p>
      </div>
    </section>
    <section class="alt" style="padding-top:3rem">
      <div class="wrap">
        <div class="filters"><div class="filter-row" id="filter-area"></div><div class="filter-row" id="filter-momento"></div></div>
        <p class="count" id="cases-count" aria-live="polite"></p>
        <div class="cases" id="cases-grid"></div>
      </div>
    </section>
    <section class="cta">
      <div class="wrap"><h2 class="h2">O próximo case pode ser o seu.</h2><a class="btn btn-primary" href="consulta.html">Agendar conversa</a></div>
    </section>
  </main>
  {RODAPE}
  {SHEET}
  {SCRIPTS}
</body>
</html>
'''

(RAIZ / "index.html").write_text(INDEX)
(RAIZ / "casos.html").write_text(CASOS)
print("ok")

# ---------- consulta: mantém o formulário (consulta.js depende dele) e troca a moldura ----------
import re
_c = (RAIZ / "consulta.html").read_text()
_form = re.search(r'<main id="principal" class="consulta-main">.*?</main>', _c, re.S).group(0)
_form = _form.replace('<div class="hero-guilloche" aria-hidden="true"></div>', '')
CONSULTA = f'''{head("Agendar conversa · Vertex", "Seis perguntas rápidas para a gente entender onde a IA pode dar resultado na sua empresa.", "consulta.html")}
<body>
  <a class="skip" href="#principal">Pular para o conteúdo</a>
  {nav("consulta.html")}
  {_form}
  <script defer src="https://cdn.jsdelivr.net/npm/gsap@3.12.7/dist/gsap.min.js"></script>
  <script defer src="consulta.js"></script>
</body>
</html>
'''
(RAIZ / "consulta.html").write_text(CONSULTA)
print("consulta ok")
