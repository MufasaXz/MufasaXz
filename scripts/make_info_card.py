"""
Generate info-card.svg with a big animated typing effect:
'Just a noob'
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")

W, H = 480, 376
PAD = 24
TITLEBAR_H = 30

BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#c9d1d9"
GREEN = "#3fb950"
ACCENT = "#22d3ee"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace">
  <defs>
    <linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{BG2}"/>
      <stop offset="1" stop-color="{BG}"/>
    </linearGradient>
    <clipPath id="cmd-clip">
      <rect x="28" y="55" height="30" width="0">
        <animate attributeName="width" from="0" to="360" begin="0.2s" dur="0.7s" fill="freeze"/>
      </rect>
    </clipPath>
    <clipPath id="text-clip">
      <rect x="28" y="145" height="55" width="0">
        <animate attributeName="width" from="0" to="270" begin="1.0s" dur="1.2s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <!-- Window Frame -->
  <rect width="{W}" height="{H}" rx="12" fill="url(#ibg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>
  <line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>

  <!-- Window Controls -->
  <circle cx="20" cy="15" r="5" fill="#ff5f56"/>
  <circle cx="36" cy="15" r="5" fill="#ffbd2e"/>
  <circle cx="52" cy="15" r="5" fill="#27c93f"/>
  <text x="{W/2}" y="19" fill="{MUTED}" font-size="12" text-anchor="middle">mufasaxz@github: ~$ whoami</text>

  <!-- Terminal Command line -->
  <g clip-path="url(#cmd-clip)">
    <text x="28" y="76" font-size="14" font-weight="700">
      <tspan fill="{GREEN}">mufasaxz</tspan><tspan fill="{MUTED}">@</tspan><tspan fill="{ACCENT}">github</tspan><tspan fill="{MUTED}">:~$</tspan> <tspan fill="{INK}">cat status.txt</tspan>
    </text>
  </g>

  <!-- Sub-prompt arrow -->
  <text x="28" y="185" font-size="34" font-weight="800" fill="{GREEN}">&gt;</text>

  <!-- Big Animated Text: Just a noob -->
  <g clip-path="url(#text-clip)">
    <text x="60" y="185" font-size="36" font-weight="800" fill="{ACCENT}" letter-spacing="1">Just a noob</text>
  </g>

  <!-- Cursor during typing -->
  <rect x="60" y="152" width="18" height="38" fill="{ACCENT}" opacity="0">
    <animate attributeName="x" from="60" to="295" begin="1.0s" dur="1.2s" fill="freeze"/>
    <set attributeName="opacity" to="0.9" begin="1.0s"/>
    <set attributeName="opacity" to="0" begin="2.2s"/>
  </rect>

  <!-- Blinking Cursor after typing -->
  <rect x="298" y="152" width="18" height="38" fill="{ACCENT}" opacity="0">
    <set attributeName="opacity" to="1" begin="2.2s"/>
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite" begin="2.2s"/>
  </rect>
</svg>
'''

with open(OUT, "w") as f:
    f.write(svg)
print("wrote", OUT, len(svg), "bytes;", W, "x", H)
