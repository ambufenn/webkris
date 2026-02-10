# webkris
## 📁 Struktur Folder
```text
karya-reksa/
│
├── Frontend/                  # Seluruh tampilan website (UI)
│   │
│   ├── Home/                  # Halaman utama (gateway)
│   │   ├── index.html
│   │   ├── home.css
│   │   └── home.js
│   │
│   ├── Services/              # Layanan profesional
│   │   ├── index.html
│   │   └── services.js
│   │
│   ├── Courses/               # Platform pembelajaran
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── courses.js
│   │
│   ├── Media/                 # Media & konten (YouTube, dsb)
│   │   ├── index.html
│   │   └── media.js
│   │
│   ├── Store/                 # Produk / clothing line
│   │   ├── index.html
│   │   └── store.js
│   │
│   ├── Shared/                # Komponen bersama
│   │   ├── navbar.js
│   │   ├── footer.js
│   │   ├── theme.css
│   │   └── global.js
│   │
│   └── Assets/                # Aset statis
│       ├── images/
│       └── icons/
│
├── Backend/                   # Backend (dikembangkan bertahap)
│   │
│   ├── main.py                # Entry backend (production nanti)
│   │
│   ├── Api/                   # Endpoint API per fitur
│   │   ├── courses.py
│   │   ├── services.py
│   │   ├── media.py
│   │   └── store.py
│   │
│   ├── Models/                # Model data
│   │   ├── course.py
│   │   └── user.py
│   │
│   ├── Database/              # Database config & schema
│   │   ├── db.py
│   │   └── schema.sql
│   │
│   └── requirements.txt
│
├── main.py                    # ⚠️ STREAMLIT (sementara, DEV ONLY)
│
└── README.md


##versi github.io
```text
karya-reksa/
│
├── index.html              # ✅ ENTRY POINT GitHub Pages
│
├── Frontend/
│   │
│   ├── Home/
│   │   ├── index.html
│   │   ├── home.css
│   │   └── home.js
│   │
│   ├── Services/
│   │   ├── index.html
│   │   └── services.js
│   │
│   ├── Courses/
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── courses.js
│   │
│   ├── Media/
│   │   ├── index.html
│   │   └── media.js
│   │
│   ├── Store/
│   │   ├── index.html
│   │   └── store.js
│   │
│   ├── Shared/
│   │   ├── navbar.js
│   │   ├── footer.js
│   │   ├── theme.css
│   │   └── global.js
│   │
│   └── Assets/
│       ├── image/
│       │   └── dora.png     # ⚠️ BUKAN images
│       └── icons/
│
├── Backend/                # ❌ TIDAK dipakai GitHub Pages
│   ├── main.py
│   ├── Api/
│   ├── Models/
│   ├── Database/
│   └── requirements.txt
│
├── main.py                 # Streamlit DEV ONLY
│
└── README.md

