"""Generate the local SVG hobby icons used by the game."""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "hobbies")

ICONS = {
    "reading": """
      <path d="M100 62c-16-12-36-16-56-12v76c20-4 40 0 56 12" fill="#ffd27d"/>
      <path d="M100 62c16-12 36-16 56-12v76c-20-4-40 0-56 12" fill="#ffd27d"/>
      <path d="M100 62v76"/>
      <path d="M56 78c14-2 26 0 36 6M56 98c14-2 26 0 36 6M108 84c12-6 24-8 36-6M108 104c12-6 24-8 36-6" stroke="#8a93bd" stroke-width="5"/>
    """,
    "swimming": """
      <circle cx="70" cy="72" r="16" fill="#ffd27d"/>
      <path d="M86 84c22 2 36 14 48 30" stroke="#3d7bff" stroke-width="13"/>
      <path d="M96 78c12-18 28-20 42-10" stroke="#ff8a2b" stroke-width="13"/>
      <path d="M28 126c12-10 24-10 36 0s24 10 36 0 24-10 36 0 24 10 36 0" stroke="#22c55e" stroke-width="7"/>
      <path d="M28 150c12-10 24-10 36 0s24 10 36 0 24-10 36 0 24 10 36 0" stroke="#3d7bff" stroke-width="7"/>
    """,
    "painting": """
      <path d="M100 44c34 0 60 24 60 54 0 24-20 38-44 38-10 0-16-6-26-6s-16 6-26 6c-24 0-44-14-44-38 0-30 26-54 60-54z" fill="#ffd27d"/>
      <circle cx="70" cy="88" r="8" fill="#ef4444" stroke="none"/>
      <circle cx="100" cy="74" r="8" fill="#3d7bff" stroke="none"/>
      <circle cx="128" cy="92" r="8" fill="#22c55e" stroke="none"/>
      <circle cx="150" cy="70" r="10" fill="#ffffff"/>
      <path d="M138 150l38-38M166 122l12 12M150 138l12 12" stroke="#8b5cf6" stroke-width="10"/>
    """,
    "cycling": """
      <circle cx="56" cy="136" r="26"/>
      <circle cx="146" cy="136" r="26"/>
      <path d="M56 136l30-44h34l26 44M86 92l18 44M120 92l-16 44M104 92l-2-22"/>
      <circle cx="102" cy="54" r="14" fill="#ffd27d"/>
      <path d="M102 70l-10 22M102 70l18 22M100 76l26-10"/>
    """,
    "cooking": """
      <path d="M60 76c0-18 14-30 30-30 8 0 14 4 18 10 6-8 14-12 24-10 14 2 22 14 22 30" fill="#ffffff"/>
      <path d="M58 76h88v24H58z" fill="#ffffff"/>
      <path d="M48 110h108l-10 48H58z" fill="#ff8a2b"/>
      <path d="M40 110h124"/>
      <path d="M74 136h56" stroke="#ffffff" stroke-width="7"/>
    """,
    "dancing": """
      <circle cx="100" cy="54" r="16" fill="#ffd27d"/>
      <path d="M100 70v44M100 82L64 60M100 82l36-22M100 114L74 154M100 114l28 40"/>
      <path d="M150 84V50l16-6v34" fill="#3d7bff"/>
      <circle cx="146" cy="84" r="6" fill="#3d7bff" stroke="none"/>
      <circle cx="162" cy="78" r="6" fill="#3d7bff" stroke="none"/>
    """,
    "singing": """
      <rect x="84" y="46" width="32" height="64" rx="16" fill="#ef4444"/>
      <path d="M92 110h16v22H92z" fill="#ffd27d"/>
      <path d="M100 132v24M78 158h44"/>
      <path d="M148 88V52l16-6v36" fill="#3d7bff"/>
      <circle cx="144" cy="88" r="6" fill="#3d7bff" stroke="none"/>
      <circle cx="160" cy="82" r="6" fill="#3d7bff" stroke="none"/>
    """,
    "gardening": """
      <path d="M44 92h60l-8 46H52z" fill="#3d7bff"/>
      <path d="M104 100l30-18 8 12-28 20" fill="#3d7bff"/>
      <path d="M56 92c0-16 24-16 24 0"/>
      <path d="M150 146V96" stroke="#22c55e" stroke-width="8"/>
      <circle cx="150" cy="80" r="9" fill="#ffd27d" stroke="none"/>
      <circle cx="150" cy="60" r="9" fill="#ff6b9a" stroke="none"/>
      <circle cx="170" cy="80" r="9" fill="#ff6b9a" stroke="none"/>
      <circle cx="150" cy="100" r="9" fill="#ff6b9a" stroke="none"/>
      <circle cx="130" cy="80" r="9" fill="#ff6b9a" stroke="none"/>
      <path d="M150 120c-16-8-24-20-24-34M150 120c16-8 24-20 24-34" stroke="#22c55e" stroke-width="5"/>
    """,
    "fishing": """
      <path d="M44 156L116 44" stroke="#8b5cf6" stroke-width="8"/>
      <path d="M116 44c24 6 32 26 26 48" stroke="#8b5cf6" stroke-width="4"/>
      <path d="M142 92v30" stroke="#5a6188" stroke-width="3"/>
      <path d="M124 126c14-14 38-14 52 0-14 14-38 14-52 0z" fill="#3d7bff"/>
      <path d="M124 126l-14-12v24z" fill="#3d7bff"/>
      <circle cx="166" cy="122" r="3" fill="#ffffff" stroke="none"/>
      <path d="M34 160c12-8 24-8 36 0s24 8 36 0" stroke="#22c55e" stroke-width="6"/>
    """,
    "hiking": """
      <path d="M26 150l46-68 26 38 18-24 58 54z" fill="#94a3d8"/>
      <path d="M72 82l14 20-14 8-12-10z" fill="#ffffff"/>
      <circle cx="100" cy="58" r="13" fill="#ffd27d"/>
      <path d="M100 72v34M100 82l-22 14M100 82l20 16M100 106l-16 36M100 106l18 36"/>
    """,
    "sketching": """
      <rect x="38" y="36" width="104" height="124" rx="10" fill="#ffffff"/>
      <path d="M56 132l28-34 20 18 18-26 14 42z" fill="#22c55e" stroke-width="5"/>
      <circle cx="68" cy="64" r="8" fill="#ffd27d" stroke-width="4"/>
      <path d="M126 150l40-40 12 12-40 40-16 4z" fill="#ff8a2b"/>
      <path d="M166 110l12-12 12 12-12 12z" fill="#ffd27d"/>
    """,
    "sewing": """
      <rect x="48" y="70" width="60" height="72" rx="10" fill="#8b5cf6"/>
      <path d="M48 84h60M48 128h60" stroke="#ffffff" stroke-width="6"/>
      <path d="M78 142c0 18 30 18 30 0" stroke="#ef4444" stroke-width="5"/>
      <path d="M126 142L166 52" stroke="#5a6188" stroke-width="6"/>
      <circle cx="166" cy="52" r="6"/>
      <path d="M126 142c-14 8-22 20-18 32" stroke="#ef4444" stroke-width="5"/>
    """,
    "jogging": """
      <circle cx="88" cy="50" r="15" fill="#ffd27d"/>
      <path d="M88 66l-6 38 26 18M82 104l-24 26M108 122l16 30M82 78l-28 8M82 78l30-8"/>
      <path d="M132 150h30" stroke="#22c55e" stroke-width="7"/>
    """,
    "yoga": """
      <circle cx="100" cy="52" r="14" fill="#ffd27d"/>
      <path d="M100 66v38M100 78L64 100M100 78l36 22"/>
      <path d="M100 104c-28 0-46 16-46 30h92c0-14-18-30-46-30z" fill="#8b5cf6"/>
      <path d="M64 100l-12-8M136 100l12-8"/>
    """,
    "chess": """
      <path d="M64 148h72l8-64H56z" fill="#94a3d8"/>
      <path d="M56 84h88v16H56z" fill="#94a3d8"/>
      <path d="M64 84V60h12v12h16V60h16v12h16V60h12v24" fill="#94a3d8"/>
      <path d="M56 148h88v12H56z" fill="#94a3d8"/>
    """,
    "soccer": """
      <circle cx="100" cy="100" r="60" fill="#ffffff"/>
      <path d="M100 70l28 20-11 32H83L72 90z" fill="#26325b" stroke="none"/>
      <path d="M100 70V44M128 90l26-8M117 122l16 22M83 122l-16 22M72 90L46 82"/>
      <path d="M44 82c-8 14-8 30 0 44M156 82c8 14 8 30 0 44M83 144h34"/>
    """,
    "tennis": """
      <ellipse cx="76" cy="84" rx="34" ry="44" transform="rotate(-25 76 84)" fill="#22c55e"/>
      <ellipse cx="76" cy="84" rx="22" ry="30" transform="rotate(-25 76 84)" fill="#f4f7ff" stroke-width="5"/>
      <path d="M100 112l46 46" stroke="#8b5cf6" stroke-width="10"/>
      <circle cx="146" cy="146" r="18" fill="#ffd27d"/>
      <path d="M132 136c10 8 18 18 24 30M160 134c-10 10-16 20-18 30" stroke="#ffffff" stroke-width="4"/>
    """,
    "guitar": """
      <path d="M78 118c-22 0-34-16-34-34s14-32 32-32c14 0 24 8 30 20 6-12 16-20 30-20 18 0 32 14 32 32s-12 34-34 34c-14 0-24-8-28-18-4 10-14 18-28 18z" fill="#ff8a2b"/>
      <circle cx="106" cy="104" r="12" fill="#26325b" stroke="none"/>
      <path d="M106 74L146 34M140 40l12 12" stroke="#8b5cf6" stroke-width="12"/>
      <path d="M96 92l28 28M104 84l28 28" stroke="#ffffff" stroke-width="3"/>
    """,
    "drums": """
      <path d="M70 126h60v34H70z" fill="#ef4444"/>
      <ellipse cx="100" cy="126" rx="30" ry="10" fill="#ffffff"/>
      <path d="M70 126v34M130 126v34"/>
      <path d="M44 84h32v26H44zM124 84h32v26h-32z" fill="#3d7bff"/>
      <ellipse cx="60" cy="84" rx="16" ry="6" fill="#ffffff"/>
      <ellipse cx="140" cy="84" rx="16" ry="6" fill="#ffffff"/>
      <path d="M36 70h48M116 70h48" stroke="#ffd27d" stroke-width="8"/>
      <path d="M60 70v14M140 70v14" stroke-width="5"/>
    """,
    "camping": """
      <path d="M100 48L36 152h128z" fill="#22c55e"/>
      <path d="M100 48v104M100 48l-30 104M100 48l30 104" stroke="#ffffff" stroke-width="5"/>
      <path d="M100 48l34 12-34 14z" fill="#ff8a2b"/>
      <path d="M36 152h128"/>
      <path d="M166 108v44M166 108l-12-8v20" stroke-width="5"/>
    """,
}


def wrap(inner):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <rect x="6" y="6" width="188" height="188" rx="44" fill="#f4f7ff"/>
  <g fill="none" stroke="#26325b" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
{inner.strip()}
  </g>
</svg>
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, inner in ICONS.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(wrap(inner))
    print(f"Wrote {len(ICONS)} hobby icons to {OUT}")


if __name__ == "__main__":
    main()
