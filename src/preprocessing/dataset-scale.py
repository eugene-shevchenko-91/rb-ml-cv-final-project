from pathlib import Path
from PIL import Image

S = 320
# S = 240
SRC = Path("../../data/chest_xray")
DST = Path(f"../../data/chest_xray_{S}")

for f in SRC.rglob("*.jpeg"):
    rel = f.relative_to(SRC)
    out = (DST / rel).with_suffix(".jpeg")
    out.parent.mkdir(parents=True, exist_ok=True)

    # Grayscale
    im = Image.open(f).convert("L")
    # Downscale
    im.thumbnail((S, S), Image.LANCZOS)
    im.save(out, "JPEG", quality=95, optimize=True)
