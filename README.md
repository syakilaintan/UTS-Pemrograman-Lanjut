
# Sistem Pemesanan Produk

Backend REST API menggunakan Python dan FastAPI.

## Fitur

- Melihat produk
- Menambah produk
- Mengubah produk
- Menghapus produk
- Membuat pesanan
- Melihat pesanan
- Mengubah status pesanan
- Validasi data
- API Key admin
- Automated testing

## Teknologi

- Python
- FastAPI
- Pydantic
- Pytest
- HTTPX

## Instalasi

```bash
python -m venv venv
```

Aktifkan virtual environment.

Windows:

```powershell
.\venv\Scripts\Activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

## Menjalankan aplikasi

```bash
uvicorn app.main:app --reload
```

Buka:

http://127.0.0.1:8000/docs

## Menjalankan testing

```bash
pytest -v
```

## API Key Admin

```text
X-API-Key: admin123
```

## Penyimpanan

Data masih menggunakan dictionary Python.
Data akan hilang ketika aplikasi dihentikan.
