# webkris
## 📁 Struktur Folder

karya-reksa/
│
├── frontend/                  # Seluruh tampilan website (UI)
│   │
│   ├── home/                  # Halaman utama (gateway)
│   │   ├── index.html
│   │   ├── home.css
│   │   └── home.js
│   │
│   ├── services/              # Layanan profesional
│   │   ├── index.html
│   │   └── services.js
│   │
│   ├── courses/               # Platform pembelajaran
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── courses.js
│   │
│   ├── media/                 # Media & konten (YouTube, dsb)
│   │   ├── index.html
│   │   └── media.js
│   │
│   ├── store/                 # Produk / clothing line
│   │   ├── index.html
│   │   └── store.js
│   │
│   ├── shared/                # Komponen bersama
│   │   ├── navbar.js
│   │   ├── footer.js
│   │   ├── theme.css
│   │   └── global.js
│   │
│   └── assets/                # Aset statis
│       ├── images/
│       └── icons/
│
├── backend/                   # Backend (dikembangkan bertahap)
│   │
│   ├── main.py                # Entry backend (production nanti)
│   │
│   ├── api/                   # Endpoint API per fitur
│   │   ├── courses.py
│   │   ├── services.py
│   │   ├── media.py
│   │   └── store.py
│   │
│   ├── models/                # Model data
│   │   ├── course.py
│   │   └── user.py
│   │
│   ├── database/              # Database config & schema
│   │   ├── db.py
│   │   └── schema.sql
│   │
│   └── requirements.txt
│
├── main.py                    # ⚠️ STREAMLIT (sementara, DEV ONLY)
│
└── README.md
