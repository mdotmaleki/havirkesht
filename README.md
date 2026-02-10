# پروژه درس پایگاه داده پیشرفته
# توسعه دهنده: میثم ملکی
# شماره دانشجویی: 40411415015
# نیمسال اول سال 1404 - 1405

پروژه **HAVIRKESHT** یک سرویس بک‌اند مبتنی بر **FastAPI** است که برای مدیریت داده‌های کشاورزی، مناطق، کاربران و عملیات مدیریتی طراحی شده است.  
این سرویس با ساختار ماژولار، امنیت مبتنی بر JWT، و معماری قابل توسعه پیاده‌سازی شده است.

---

## تکنولوژی‌های استفاده‌شده

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **PostgreSQL**
- **SQLAlchemy**
- **Alembic**
- **Pydantic**
- **Nginx**
- **Docker**
- **Cloudflare (SSL + CDN)**

---

## احراز هویت
این پروژه از JWT برای احراز هویت استفاده می‌کند:

رمزنگاری پسورد ها با استفاده از الگوریتم bcrypt انجام می شود

محافظت از مسیرها با OAuth2PasswordBearer انجام می شود

---

## مستندات پروژه
مستندات API
پس از اجرای پروژه، مستندات خودکار FastAPI در مسیرهای زیر در دسترس هستند:

Swagger UI
https://meysam-maleki.ir/docs

OpenAPI JSON
https://meysam-maleki.ir/openapi.json

---

## مدیریت دامنه با Cloudflare
![Clouflare](images/cloudflare.png)

---

---

## قرار دادن پروژه در Github Repository
![Github](images/github.png)

---

## اعمال تغییرات در سرور به صورت خودکار (CI/CD)
![CI/CD](images/CI-CD.png)

---

##  ساختار کلی پروژه
![Structure](images/structure.png)

---

## نصب وابستگی ها
pip install -r requirements.txt
![Requirements](images/requirements.png)

---

## اجرای سرور توسعه
uvicorn app.main:app --reload

---

