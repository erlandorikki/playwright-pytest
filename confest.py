import os
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            # Buat folder reports/screenshots jika belum ada
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            try:
                page.screenshot(path=screenshot_path)
                print(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"Failed to save screenshot: {e}")

            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(screenshot_path))
                rep.extra = extra
