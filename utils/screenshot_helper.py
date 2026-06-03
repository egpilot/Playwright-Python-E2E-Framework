"""Screenshot capture helper, integrates with Allure."""
from pathlib import Path
from datetime import datetime
import allure

SCREENSHOT_DIR = Path(__file__).resolve().parent.parent / "reports" / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


def capture(page, name: str = "screenshot") -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    path = SCREENSHOT_DIR / f"{name}_{ts}.png"
    page.screenshot(path=str(path), full_page=True)
    try:
        allure.attach.file(
            str(path),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass
    return path
