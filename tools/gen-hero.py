#!/usr/bin/env python3
"""Generate assets/profile-hero.svg (1200x440).
Left: ascii agent loop. Right: ls -al repo listing + agent TUI card + detail grid,
cycling in sync with agent CLI commands typed at the prompt.
Agent icons use official brand artwork: simple-icons paths for
OpenAI/Claude/Gemini/Cursor, the xAI Grok slash, and oh-my-pi's own icon."""

FONT = 15
CHAR_W = 9                      # px per char at font-size 15 (0.6em mono)
X_PROMPT = 560
PROMPT_LEN = 25                 # "parkavenue9639@github:~$ " = 25 chars
X_TEXT = X_PROMPT + PROMPT_LEN * CHAR_W
Y = 424                         # prompt baseline
SLOT = 2.6                      # seconds per command
TYPE_FRAC = 0.62                # typing phase within a slot
GAP = 0.01                      # blank fraction between commands

# --- agents (index-matched: cmd <-> card) ---
CMDS = [
    'claude "fix flaky ci"',
    'codex --review HEAD~1',
    'gemini "draft the plan"',
    'cursor-agent "add tests"',
    'grok "explain this trace"',
    'omp pair on refactor',
]

# simple-icons v15 path data (24x24), simpleicons.org (CC0)
D_OPENAI = "M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"
D_CLAUDE = "m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z"
D_CURSOR = "M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23"
D_GEMINI = "M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"

AGENTS = [
    # name, vendor, border color, icon-markup (24x24 box)
    ('claude', 'anthropic', '#D97757', f'<path d="{D_CLAUDE}" fill="#D97757" />'),
    ('codex', 'openai', '#8a9bb5', f'<path d="{D_OPENAI}" fill="#e6edf3" />'),
    ('gemini', 'google', '#7a9df0', f'<path d="{D_GEMINI}" fill="url(#gemgrad)" />'),
    ('cursor-agent', 'cursor', '#8a9bb5', f'<path d="{D_CURSOR}" fill="#e6edf3" />'),
    ('grok', 'xai', '#5c6b7d',
     '<rect x="0" y="0" width="24" height="24" rx="5.5" fill="#111318" stroke="#3d4d73" stroke-width="0.8" />'
     '<polygon points="5.68,18.96 8.61,18.96 18.34,5.07 15.42,5.07" fill="#e6edf3" />'),
    ('omp', 'oh-my-pi', '#f97316',
     '<g transform="translate(0,3.1) scale(0.198)">'
     '<rect x="10" y="8" width="100" height="12" rx="2" fill="#fafafa" />'
     '<rect x="25" y="20" width="12" height="62" rx="2" fill="#fafafa" />'
     '<rect x="75" y="20" width="12" height="45" rx="2" fill="#fafafa" />'
     '<rect x="71" y="55" width="20" height="16" rx="3" fill="#f97316" /></g>'),
]

# --- ls -al entries: repos only; selection index = command index % len ---
ENTRIES = [
    ('drwxr-xr-x', 'external-agent-mcp/', '7'),
    ('drwxr-xr-x', 'jaeger-mcp/', '21'),
    ('drwxr-xr-x', 'jevloop/', '42'),
    ('drwxr-xr-x', 'loop-engineering/', '33'),
]

# --- permanent detail grid, 2 cols x 4 rows (repos live in ls, status on card) ---
DETAIL_L = [('os', 'macOS · Linux'), ('ai', 'langgraph · mcp · mlx'),
            ('llm', 'only when needed'), ('work', 'agents · mcp · tooling')]
DETAIL_R = [('stack', 'python · ts · fastapi'), ('loop', 'observe → execute → ledger'),
            ('fails', 'loudly, then stops'), ('rule', 'write less, bug less')]
DETAIL_Y = [150, 176, 202, 228]
X_COL2 = 880

X_LIST = 560
L_FONT, L_CHAR_W, L_STEP = 13.5, 8.1, 24
TOTAL_Y = 268
ROW_Y0 = 292

CARD_X, CARD_Y, CARD_W, CARD_H = 880, 268, 278, 128
ICON_TX, ICON_TY = 904, 298
NAME_X, NAME_Y = 946, 308
VEND_X, VEND_Y = 946, 332

CYCLE = SLOT * len(CMDS)
LBL_W = 8                       # detail label column width, chars


def fmt(x):
    return ('%f' % x).rstrip('0').rstrip('.')


def gate(i):
    t0 = fmt(i / len(CMDS))
    t1 = fmt((i + 1) / len(CMDS) - GAP)
    return (f'<animate attributeName="opacity" calcMode="discrete" '
            f'values="0;1;0;0" keyTimes="0;{t0};{t1};1" '
            f'dur="{fmt(CYCLE)}s" begin="0s" repeatCount="indefinite" />')


def command_parts(i, cmd):
    n = len(cmd)
    begin = fmt(i * SLOT)
    widths = [0] + [CHAR_W * k for k in range(1, n + 1)]
    w_vals = ';'.join(fmt(w) for w in widths)
    w_kts = ';'.join(fmt(TYPE_FRAC * k / n) for k in range(n + 1))
    xs = [X_TEXT + CHAR_W * k for k in range(n + 1)]
    x_vals = ';'.join(fmt(x) for x in xs)

    clip = f'''    <clipPath id="cmd{i}">
      <rect x="{X_TEXT}" y="{Y - 13}" width="0" height="22">
        <animate attributeName="width" calcMode="discrete" values="{w_vals}" keyTimes="{w_kts}" dur="{fmt(SLOT)}s" begin="{begin}s" repeatCount="indefinite" />
      </rect>
    </clipPath>'''
    body = f'''  <g>
    {gate(i)}
    <text x="{X_TEXT}" y="{Y}" class="mono val" font-size="{FONT}" clip-path="url(#cmd{i})">{cmd}</text>
    <text x="{X_TEXT}" y="{Y}" class="mono cursor" font-size="{FONT}" filter="url(#glow)">▮<animate attributeName="x" calcMode="discrete" values="{x_vals}" keyTimes="{w_kts}" dur="{fmt(SLOT)}s" begin="{begin}s" repeatCount="indefinite" /></text>
  </g>'''
    return clip, body


def slot_group(i):
    perms, name, size = ENTRIES[i % len(ENTRIES)]
    aname, vendor, border, mark = AGENTS[i]
    line = f'{perms}  {name:<21}{size:>4}'
    y = ROW_Y0 + (i % len(ENTRIES)) * L_STEP
    box_w = 6 + len(line) * L_CHAR_W + 3   # hug the actual text width
    return f'''  <g opacity="0">
    {gate(i)}
    <rect x="{X_LIST - 6}" y="{y - 13}" width="{fmt(box_w)}" height="17" rx="3" fill="#63e7ff" fill-opacity="0.12" stroke="#63e7ff" stroke-opacity="0.3" />
    <text x="{X_LIST}" y="{y}" class="mono node" font-size="{L_FONT}" xml:space="preserve">{line}</text>
    <g filter="url(#glow)">
      <rect x="{CARD_X}" y="{CARD_Y}" width="{CARD_W}" height="{CARD_H}" rx="12" fill="#0a101a" stroke="{border}" stroke-opacity="0.55" stroke-width="1.5" />
      <g transform="translate({ICON_TX},{ICON_TY})">{mark}</g>
      <text x="{NAME_X}" y="{NAME_Y}" class="mono val" font-size="16">{aname}</text>
      <text x="{VEND_X}" y="{VEND_Y}" class="mono dim" font-size="12">{vendor}</text>
      <circle cx="{CARD_X + CARD_W - 18}" cy="{CARD_Y + 18}" r="4" fill="#00ff9c" class="pulse" />
    </g>
  </g>'''


def detail_line(x, y, label, value):
    pad = ' ' * (LBL_W - len(label))
    return (f'    <text x="{x}" y="{y}" class="mono" font-size="13" xml:space="preserve">'
            f'<tspan class="lbl">{label}{pad}</tspan><tspan class="val">{value}</tspan></text>')


clips, bodies = zip(*(command_parts(i, c) for i, c in enumerate(CMDS)))

listing = ['    <text x="%d" y="%d" class="mono dim" font-size="%s">total 4</text>' % (X_LIST, TOTAL_Y, L_FONT)]
for i, (perms, name, size) in enumerate(ENTRIES):
    line = f'{perms}  {name:<21}{size:>4}'
    y = ROW_Y0 + i * L_STEP
    listing.append(f'    <text x="{X_LIST}" y="{y}" class="mono file" font-size="{L_FONT}" xml:space="preserve">{line}</text>')
listing = '\n'.join(listing)

slots = '\n'.join(slot_group(i) for i in range(len(CMDS)))
detail = '\n'.join([detail_line(X_LIST, y, l, v) for (l, v), y in zip(DETAIL_L, DETAIL_Y)]
                   + [detail_line(X_COL2, y, l, v) for (l, v), y in zip(DETAIL_R, DETAIL_Y)])

# left ascii loop at font 20 (charW 12), 35-char lines
A_Y = [162, 206, 250, 294]

svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-labelledby="title desc">
  <title id="title">agent loop — observe, decide, guard, execute, ledger, repeat</title>
  <desc id="desc">A neofetch-style terminal card in neon: on the left, an ASCII agent loop with a glowing signal orbiting it; on the right, an ls -al listing of repos whose selection and an agent TUI card (official brand icons) cycle in sync with agent CLI commands typed at the prompt, over a permanent detail grid of stack and principles.</desc>
  <defs>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.4" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="gemgrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4e8cf5" />
      <stop offset="1" stop-color="#a05ce6" />
    </linearGradient>
__CLIPS__
    <style>
      .mono { font-family: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
      .box  { fill: #2e4a6b; }
      .node { fill: #63e7ff; }
      .hl   { fill: #ff5fd2; font-weight: 700; }
      .note { fill: #8a7dff; }
      .lbl  { fill: #9d7bff; }
      .val  { fill: #d9e4ff; }
      .dim  { fill: #3d4d73; }
      .file { fill: #6b8098; }
      .user { fill: #00ff9c; font-weight: 700; }
      .pulse  { animation: soft 2s ease-in-out infinite; }
      .tick   { fill: #ff5fd2; animation: soft 2.4s ease-in-out infinite; }
      .flow   { fill: #ff5fd2; opacity: 0; animation: travel 2.4s linear infinite; }
      .f1 { animation-delay: 0s; }  .f2 { animation-delay: .4s; }
      .f3 { animation-delay: .8s; } .f4 { animation-delay: 1.2s; }
      .f5 { animation-delay: 1.6s; }.f6 { animation-delay: 2s; }
      .comet { fill: none; stroke: #5cf6ff; stroke-width: 2.5; stroke-linecap: round; stroke-dasharray: 4 96; animation: orbit 2.4s linear infinite; }
      .cursor { fill: #00ff9c; animation: blink 1.1s steps(1, end) infinite; }
      @keyframes blink  { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
      @keyframes soft   { 0%, 100% { opacity: 1; } 50% { opacity: .3; } }
      @keyframes travel { 0%, 8% { opacity: 0; } 16%, 30% { opacity: 1; } 42%, 100% { opacity: 0; } }
      @keyframes orbit  { to { stroke-dashoffset: -100; } }
      @media (prefers-reduced-motion: reduce) {
        .pulse, .tick, .cursor { animation: none; }
        .flow { animation: none; opacity: 0; }
        .comet { animation: none; }
      }
    </style>
  </defs>

  <rect x="1" y="1" width="1198" height="438" rx="14" fill="#05070d" stroke="#223457" stroke-width="2" />

  <!-- left: orbit ring around the ascii loop -->
  <rect x="58" y="128" width="450" height="188" rx="20" fill="none" stroke="#14283f" stroke-width="1.5" />
  <rect x="58" y="128" width="450" height="188" rx="20" pathLength="100" class="comet" filter="url(#glow)" />

  <!-- left: ascii loop -->
  <g class="mono" font-size="20">
    <text x="72" y="__A0__" xml:space="preserve"><tspan class="box">╭─▶ observe ──▶ </tspan><tspan class="box">      </tspan><tspan class="box"> ──▶ </tspan><tspan class="node">guard</tspan><tspan class="box"> ─┐</tspan></text>
    <text x="72" y="__A1__" xml:space="preserve"><tspan class="box">│                 ┆ </tspan><tspan class="note">llm, if needed</tspan><tspan class="box">│</tspan></text>
    <text x="72" y="__A2__" xml:space="preserve"><tspan class="box">▲                                 ▼</tspan></text>
    <text x="72" y="__A3__" xml:space="preserve"><tspan class="box">╰─ </tspan><tspan class="node">repeat</tspan><tspan class="box"> ◀── </tspan><tspan class="node">ledger</tspan><tspan class="box"> ◀── </tspan><tspan class="node">execute</tspan><tspan class="box"> ─┘</tspan></text>
  </g>

  <!-- decide: separate glowing layer -->
  <text x="72" y="__A0__" class="mono hl" font-size="20" xml:space="preserve" filter="url(#glow)">                decide</text>

  <!-- travelling signal: neon arrows pulsing in flow order -->
  <g class="mono" font-size="20" xml:space="preserve">
    <text x="72" y="__A0__" class="flow f1" xml:space="preserve">              ▶</text>
    <text x="72" y="__A0__" class="flow f2" xml:space="preserve">                         ▶</text>
    <text x="72" y="__A2__" class="flow f3" xml:space="preserve">                                  ▼</text>
    <text x="72" y="__A3__" class="flow f4" xml:space="preserve">                     ◀</text>
    <text x="72" y="__A3__" class="flow f5" xml:space="preserve">          ◀</text>
    <text x="72" y="__A2__" class="flow f6" xml:space="preserve">▲</text>
    <text x="72" y="__A1__" class="tick" xml:space="preserve">                  ┆</text>
  </g>

  <!-- right: neofetch header -->
  <text x="560" y="90" class="mono" font-size="17" filter="url(#glow)"><tspan class="user">parkavenue9639</tspan><tspan class="dim">@</tspan><tspan class="node">github</tspan></text>
  <text x="560" y="118" class="dim mono" font-size="15">__SEP__</text>

  <!-- right: permanent detail grid -->
__DETAIL__

  <!-- right: ls -al listing (repos) -->
__LISTING__

  <!-- right: selection + agent TUI card, cycling with the prompt -->
__SLOTS__

  <!-- right: terminal prompt -->
  <text x="560" y="__PY__" class="mono" font-size="15" xml:space="preserve"><tspan class="user">parkavenue9639</tspan><tspan class="dim">@</tspan><tspan class="node">github</tspan><tspan class="dim">:</tspan><tspan class="lbl">~</tspan><tspan class="dim">$ </tspan></text>

  <!-- typewriter prompt: agent cli commands -->
__BODY__
</svg>
'''
svg = (svg.replace('__CLIPS__', '\n'.join(clips))
          .replace('__LISTING__', listing)
          .replace('__SLOTS__', slots)
          .replace('__DETAIL__', detail)
          .replace('__SEP__', '─' * 21)
          .replace('__A0__', str(A_Y[0])).replace('__A1__', str(A_Y[1]))
          .replace('__A2__', str(A_Y[2])).replace('__A3__', str(A_Y[3]))
          .replace('__PY__', str(Y))
          .replace('__BODY__', '\n'.join(bodies)))
assert '__' not in svg, 'unreplaced placeholder'

with open('/Users/luchong/PycharmProjects/parkavenue9639/assets/profile-hero.svg', 'w') as f:
    f.write(svg)
print('written', len(svg), 'bytes; canvas 1200x440, slot', SLOT, 's, cycle', CYCLE, 's')
