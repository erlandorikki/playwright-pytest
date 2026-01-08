```sh
# Portfolio Testing Web dengan Playwright + Pytest

## Deskripsi  
Automated testing pada website [SauceDemo](https://www.saucedemo.com/):  
- Login (positive & negative case)  
- Checkout (positive & negative case pada form checkout)
- Logout (positive & negative case)

Menggunakan Playwright dengan pytest dan fitur parameterize untuk efisiensi test case.

## Tools dan Teknologi  
- Python  
- Playwright  
- Pytest  

## Cara Setup  
1. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

2. Struktur folder:  
    ```
    playwright_pytest_portfolio/    
    ├── reports/
    │   ├── screenshots/
    │   ├── test_login.html
    │   ├── test_checkout.html
    │   ├── test_logout.html
    ├── tests/
    │   ├── test_login.py
    │   └── test_checkout.py
    │   └── test_logout.py
    ├── confest.py
    ├── pytest.ini
    ├── README.md
    └── requirements.txt
    ```

## Cara Menjalankan Test  
- Jalankan semua test:  
    ```bash
    pytest
    ```

- Jalankan hanya test login:  
    ```bash
    pytest -m login
    ```

- Jalankan hanya test checkout:  
    ```bash
    pytest -m checkout
    ```

- Jalankan hanya test logout:  
    ```bash
    pytest -m logout
    ```

## Test Case
- Login sukses dengan username dan password valid  
- Gagal login dengan username salah  
- Gagal login dengan password salah  
- Gagal login dengan username & password kosong  

- Checkout sukses dengan data valid  
- Gagal checkout jika first name kosong  
- Gagal checkout jika last name kosong  
- Gagal checkout jika postal code kosong  
- Gagal checkout jika semua field kosong

- User berhasil logout dari menu dan kembali ke halaman login
- Setelah berhasil logout, user mencoba mengakses halaman /inventory.html langsung, namun diarahkan ke halaman login

---

Terima kasih!

```