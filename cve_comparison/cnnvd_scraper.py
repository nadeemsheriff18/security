from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_cnnvd():
    options = Options()
    # options.add_argument('--headless')  # optional
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.cnnvd.org.cn/home/loophole")
    with open("cnnvd_debug.html", "w", encoding="utf-8") as f:
       f.write(driver.page_source)

    '''
    try:
        # 🔍 Wait for at least 1 vulnerability card to appear
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-row.content-center.zhong-borde")))

        cards = driver.find_elements(By.CSS_SELECTOR, ".el-row.content-center.zhong-borde")
        print(f"✅ CNNVD cards found: {len(cards)}")

        data = []
        for card in cards:
            try:
                title = card.find_element(By.CSS_SELECTOR, "div:nth-child(1)").text.strip()
                cnnvd_id = card.find_element(By.CSS_SELECTOR, "div:nth-child(2)").text.strip()
                collection_time = card.find_element(By.CSS_SELECTOR, "div:nth-child(3)").text.strip()
                update_time = card.find_element(By.CSS_SELECTOR, "div:nth-child(4)").text.strip()

                data.append({
                    "source": "CNNVD",
                    "id": cnnvd_id.split(":")[-1].strip(),
                    "description": title,
                    "published": collection_time.split(":")[-1].strip()
                })
            except Exception as e:
                print("❌ Error parsing a card:", e)

        driver.quit()
        return data

    except Exception as e:
        print("❌ Timeout waiting for CNNVD elements:", e)
        driver.quit()
        return []
    '''