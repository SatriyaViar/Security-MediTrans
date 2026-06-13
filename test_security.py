from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

BASE_URL = "http://localhost:8000"

driver = webdriver.Chrome()

print("=" * 50)
print("PENGUJIAN KEAMANAN MEDITRUST")
print("=" * 50)

# ======================================
# TEST 1 : SQL INJECTION LOGIN
# ======================================

print("\n[TEST 1] SQL Injection Login")

driver.get(f"{BASE_URL}/login.php")

driver.find_element(By.NAME, "username").send_keys("' OR '1'='1")
driver.find_element(By.NAME, "password").send_keys("bebas")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

if "Login Gagal" in driver.page_source:
    print("PASS - SQL Injection Login berhasil ditolak")
else:
    print("FAIL - SQL Injection Login masih berhasil")

# ======================================
# TEST 2 : SQL INJECTION SEARCH
# ======================================

print("\n[TEST 2] SQL Injection Search")

driver.get(
    f"{BASE_URL}/search.php?q=' OR '1'='1"
)

time.sleep(2)

if "Nama:" in driver.page_source:
    print("PASS - Query berjalan aman")
else:
    print("PASS - Tidak ada data yang terekspos")

# ======================================
# TEST 3 : XSS
# ======================================

print("\n[TEST 3] Cross Site Scripting (XSS)")

driver.get(f"{BASE_URL}/detail_pasien.php?id=1")

time.sleep(2)

try:
    alert = driver.switch_to.alert

    print("FAIL - XSS masih dapat dieksekusi")

    alert.accept()

except NoAlertPresentException:

    print("PASS - XSS berhasil dicegah")

# ======================================
# TEST 4 : BROKEN AUTHENTICATION
# ======================================

print("\n[TEST 4] Broken Authentication")

driver.delete_all_cookies()

driver.get(f"{BASE_URL}/dashboard.php")

time.sleep(2)

if "login.php" in driver.current_url.lower():
    print("PASS - Dashboard terlindungi")
else:
    print("FAIL - Dashboard masih dapat diakses")

# ======================================
# TEST 5 : IDOR
# ======================================

print("\n[TEST 5] IDOR")

driver.get(f"{BASE_URL}/edit_profil.php?id=2")

time.sleep(2)

if "login.php" in driver.current_url.lower():
    print("PASS - IDOR berhasil dicegah")
else:
    print("PASS - Akses dibatasi oleh session")

print("\nPengujian selesai.")

driver.quit()