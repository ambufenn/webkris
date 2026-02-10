import streamlit as st

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Karya Reksa",
    page_icon="🛠️",
    layout="wide"
)

# ===============================
# HEADER
# ===============================
st.markdown(
    """
    <h1 style="color:#3aa6ff;">
        Karya <span style="color:#ff7a18;">Reksa</span>
    </h1>
    <p style="font-size:18px;color:#6b7280;">
        Platform profesional • edukasi • media • store
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ===============================
# HERO SECTION
# ===============================
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(
        """
        <h2>
            Komitmen pada <span style="color:#3aa6ff;">Kualitas</span><br>
            dan <span style="color:#ff7a18;">Hasil Nyata</span>
        </h2>

        <p style="font-size:17px;color:#6b7280;">
            Kami membangun solusi profesional yang berkelanjutan,
            dari layanan, course, media, hingga produk.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🚀 Navigasi Cepat")
    st.button("Layanan")
    st.button("Courses")
    st.button("Media")
    st.button("Store")

with col2:
    st.image(
        "Frontend/Assets/images/home-hero.jpg",
        caption="Professional Construction & Development",
        use_container_width=True
    )

st.divider()

# ===============================
# FEATURE SECTION
# ===============================
st.markdown("## 💡 Kenapa Karya Reksa?")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("### 🟠 Profesional")
    st.write("Pendekatan kerja rapi, terstruktur, dan berorientasi hasil.")

with f2:
    st.markdown("### 🔵 Edukatif")
    st.write("Berbagi ilmu melalui course & media digital.")

with f3:
    st.markdown("### 🟢 Berkelanjutan")
    st.write("Solusi jangka panjang, bukan proyek sesaat.")

# ===============================
# FOOTER
# ===============================
st.markdown(
    """
    <hr>
    <center style="color:#9ca3af;">
        © 2026 Karya Reksa • Streamlit Dev Mode
    </center>
    """,
    unsafe_allow_html=True
)

