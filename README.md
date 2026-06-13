# 🔒 MediTrust Security Audit & Remediation

A web application security assessment project conducted on **MediTrust**, a medical record management system built with PHP and MySQL. This project focuses on identifying, analyzing, and mitigating common web application vulnerabilities based on the **OWASP Testing Checklist**.

![OWASP](https://img.shields.io/badge/OWASP-Testing%20Checklist-red)
![PHP](https://img.shields.io/badge/PHP-8.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Selenium](https://img.shields.io/badge/Selenium-Automated%20Testing-green)

---

## 📖 Project Overview

This project was developed as part of a Web Application Security assessment. The main objective was to perform a security audit on the MediTrust application, identify critical vulnerabilities, implement secure coding practices, and verify the effectiveness of the applied security controls through automated testing.

The assessment focused on authentication, patient search functionality, patient medical records, and access control mechanisms.

---

## 🎯 Objectives

- Identify security vulnerabilities using the OWASP Testing Checklist.
- Analyze the impact and severity of discovered vulnerabilities.
- Apply secure coding practices to mitigate identified risks.
- Verify security improvements through automated testing.
- Improve the overall security posture of the application.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| PHP | Backend Development |
| MySQL | Database Management |
| HTML/CSS | User Interface |
| Selenium WebDriver | Automated Security Testing |
| Git & GitHub | Version Control |
| OWASP Testing Checklist | Security Assessment Framework |

---

## 🔍 Security Findings

The following vulnerabilities were identified during the security audit:

| No | Vulnerability | OWASP Category | Risk Level |
|----|---------------|----------------|------------|
| 1 | SQL Injection (Login) | A03:2021 - Injection | Critical |
| 2 | SQL Injection (Search) | A03:2021 - Injection | Critical |
| 3 | Stored Cross-Site Scripting (XSS) | A03:2021 - Injection | High |
| 4 | Broken Authentication | A07:2021 | High |
| 5 | Broken Access Control (IDOR) | A01:2021 | High |

---

## 🔧 Security Improvements Implemented

### ✅ SQL Injection Prevention

Before:

```php
$query = "SELECT * FROM users WHERE username='$username'";
```

After:

```php
$stmt = $conn->prepare(
    "SELECT * FROM users WHERE username=?"
);

$stmt->bind_param("s", $username);
$stmt->execute();
```

---

### ✅ Cross-Site Scripting (XSS) Prevention

Before:

```php
echo $row['diagnosis'];
```

After:

```php
echo htmlspecialchars(
    $row['diagnosis'],
    ENT_QUOTES,
    'UTF-8'
);
```

---

### ✅ Authentication Hardening

Implemented session validation on protected pages:

```php
session_start();

if(!isset($_SESSION['user']))
{
    header("Location: login.php");
    exit();
}
```

---

### ✅ Access Control Protection

Implemented session-based user identification:

```php
$user_id = $_SESSION['user_id'];
```

This prevents unauthorized access through URL parameter manipulation.

---

## 🧪 Automated Security Testing

Security verification was performed using **Selenium WebDriver** to simulate common attack scenarios.

### Test Coverage

- SQL Injection Login Bypass
- SQL Injection on Search Functionality
- Stored XSS
- Broken Authentication
- Broken Access Control (IDOR)

### Sample Output

```text
==================================================
PENGUJIAN KEAMANAN MEDITRUST
==================================================

[TEST 1] SQL Injection Login
PASS - SQL Injection berhasil ditolak

[TEST 2] SQL Injection Search
PASS - Query berjalan aman

[TEST 3] Cross Site Scripting (XSS)
PASS - XSS berhasil dicegah

[TEST 4] Broken Authentication
PASS - Dashboard terlindungi

[TEST 5] IDOR
PASS - Akses dibatasi oleh session

Pengujian selesai.
```

---

## 📂 Project Structure

```text
MediTrust/
│
├── config/
│   └── database.php
│
├── db/
│   └── setup.sql
│
├── includes/
│   ├── header.php
│   └── footer.php
│
├── index.php
├── login.php
├── logout.php
├── dashboard.php
├── detail_pasien.php
├── edit_profil.php
├── search.php
├── test_security.py
│
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/SatriyaViar/Security-MediTrans.git
```

### 2. Import Database

Import:

```text
db/setup.sql
```

into your MySQL database.

### 3. Configure Database

Edit:

```text
config/database.php
```

and adjust the database credentials.

### 4. Run Application

Using PHP built-in server:

```bash
php -S localhost:8000
```

Open:

```text
http://localhost:8000
```

---

## ▶️ Run Automated Security Test

Install Selenium:

```bash
pip install selenium
```

Run:

```bash
python test_security.py
```

---

## 📊 Security Audit Summary

| Category | Status |
|-----------|----------|
| SQL Injection | Fixed |
| Stored XSS | Fixed |
| Broken Authentication | Fixed |
| IDOR | Fixed |
| Automated Security Testing | Implemented |

---

## 📚 References

- OWASP Top 10 (2021)
- OWASP Web Security Testing Guide (WSTG)
- PHP Official Documentation
- Selenium Documentation

---

## 👨‍💻 Author

**Satriya Viar**

Information Systems Business Student | Web Developer | Cybersecurity Enthusiast

Passionate about secure software development, web security, vulnerability assessment, quality assurance, and OWASP-based security testing.

---

⭐ If you find this project useful, feel free to give it a star.
