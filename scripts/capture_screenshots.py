"""
Capture all 5 application screenshots for the Jeju Tourism RAG Assistant.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "reports" / "figures" / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

PORT = 8506

print(f"Starting Streamlit server on port {PORT}...")
proc = subprocess.Popen([
    sys.executable, '-m', 'streamlit', 'run', 'app.py',
    '--server.headless=true', f'--server.port={PORT}', '--browser.gatherUsageStats=false'
])
time.sleep(3)

try:
    opts = Options()
    opts.add_argument('--headless=new')
    opts.add_argument('--window-size=1400,980')
    driver = webdriver.Chrome(options=opts)
    
    print(f"Connecting to http://localhost:{PORT} ...")
    driver.get(f'http://localhost:{PORT}')
    
    # Wait until 'Stop' button disappears
    print("Waiting for Streamlit initial execution...")
    for _ in range(35):
        time.sleep(1)
        stop_btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'Stop')]")
        if not stop_btns:
            # Check if main content is present
            headers = driver.find_elements(By.XPATH, "//*[contains(text(), 'Jeju Tourism AI Assistant')]")
            if headers:
                break

    print("App loaded. Capturing Tab 1: Dashboard...")
    time.sleep(2)
    driver.save_screenshot(str(SCREENSHOTS_DIR / "01_dashboard.png"))
    print("Saved 01_dashboard.png")

    # Tab 2: Document Management
    print("Navigating to Tab 2: Document Management...")
    tab2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Document Management')]")
    tab2.click()
    time.sleep(3)
    driver.save_screenshot(str(SCREENSHOTS_DIR / "02_document_management.png"))
    print("Saved 02_document_management.png")

    # Tab 3: AI Chat Assistant
    print("Navigating to Tab 3: AI Chat Assistant...")
    tab3 = driver.find_element(By.XPATH, "//*[contains(text(), 'AI Chat Assistant')]")
    tab3.click()
    time.sleep(2)
    # Click Hallasan button
    try:
        hallasan_btn = driver.find_element(By.XPATH, "//button[contains(., 'Hallasan Summit Trails')]")
        hallasan_btn.click()
        print("Clicked Hallasan example button, generating answer...")
        # Wait until generation finishes (Stop button disappears)
        time.sleep(2)
        for _ in range(25):
            time.sleep(1)
            stop_btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'Stop')]")
            if not stop_btns:
                break
        time.sleep(2)
    except Exception as e:
        print("Error clicking Hallasan button:", e)

    driver.save_screenshot(str(SCREENSHOTS_DIR / "03_chat_assistant.png"))
    print("Saved 03_chat_assistant.png")

    # Tab 4: Retrieval Inspector
    print("Navigating to Tab 4: Retrieval Inspector...")
    tab4 = driver.find_element(By.XPATH, "//*[contains(text(), 'Retrieval Inspector')]")
    tab4.click()
    time.sleep(2)
    try:
        search_btn = driver.find_element(By.XPATH, "//button[contains(., 'Execute Similarity Search')]")
        search_btn.click()
        print("Clicked Execute Similarity Search...")
        time.sleep(3)
    except Exception as e:
        print("Error clicking search button:", e)

    driver.save_screenshot(str(SCREENSHOTS_DIR / "04_retrieval_inspector.png"))
    print("Saved 04_retrieval_inspector.png")

    # Tab 5: Evaluation & Analytics
    print("Navigating to Tab 5: Evaluation & Analytics...")
    tab5 = driver.find_element(By.XPATH, "//*[contains(text(), 'Evaluation & Analytics')]")
    tab5.click()
    time.sleep(3)
    driver.save_screenshot(str(SCREENSHOTS_DIR / "05_evaluation_dashboard.png"))
    print("Saved 05_evaluation_dashboard.png")

    driver.quit()
    print("All screenshots successfully captured!")

except Exception as ex:
    print("Fatal exception during capture:", ex)
finally:
    proc.terminate()
