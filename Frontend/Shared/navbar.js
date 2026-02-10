document.getElementById("navbar").innerHTML = `
<nav style="
  padding:20px 8%;
  display:flex;
  justify-content:space-between;
  align-items:center;
  background:white;
  box-shadow:0 4px 12px rgba(0,0,0,0.05);
">
  <strong style="font-size:20px;color:#3aa6ff;">
    Karya<span style="color:#ff7a18;">Reksa</span>
  </strong>

  <div style="display:flex;gap:20px;">
    <a href="/Frontend/Home/index.html">Home</a>
    <a href="/Frontend/Services/index.html">Services</a>
    <a href="/Frontend/Courses/index.html">Courses</a>
    <a href="/Frontend/Media/index.html">Media</a>
    <a href="/Frontend/Store/index.html">Store</a>
  </div>
</nav>
`;
