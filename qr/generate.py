import os
import segno
from dotenv import load_dotenv

load_dotenv()

linkedin = os.getenv("LINKEDIN")
github = os.getenv("GITHUB")
website = os.getenv("WEBSITE")
resume = os.getenv("RESUME")

qrcode = segno.make_qr(f"{linkedin}")
qrcode.save(
    "linkedin.png",
    scale=10,
    light="lightblue",
)

qrcode = segno.make_qr(f"{github}")
qrcode.save(
    "github.png",
    scale=10,
)

qrcode = segno.make_qr(f"{website}")
qrcode.save(
    "website.png",
    scale=10,
    light="pink",
)

qrcode = segno.make_qr(f"{resume}")
qrcode.save(
    "resume.png",
    scale=10,
    light="lightgreen",
)

# https://segno.readthedocs.io/en/latest/colorful-qrcodes.html#module-names
