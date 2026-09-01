from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WA Badak Python Dashboard</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #0f172a; color: #ffffff; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; box-sizing: border-box; }
        .card { background-color: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3); width: 100%; max-width: 400px; text-align: center; border: 1px solid #334155; box-sizing: border-box; }
        h1 { color: #4ade80; margin-bottom: 5px; font-size: 24px; margin-top: 0; }
        .subtitle { color: #94a3b8; font-size: 12px; margin-top: 0; margin-bottom: 20px; }
        .status-container { margin-bottom: 25px; }
        .status-label { font-size: 14px; color: #94a3b8; display: block; margin-bottom: 5px; }
        .status-badge { background-color: rgba(74, 222, 128, 0.15); color: #4ade80; border: 1px solid rgba(74, 222, 128, 0.3); padding: 6px 16px; border-radius: 50px; font-size: 14px; font-weight: bold; display: inline-block; }
        .form-group { text-align: left; border-top: 1px solid #334155; padding-top: 20px; }
        h3 { color: #cbd5e1; margin-bottom: 15px; font-size: 16px; margin-top: 5px; }
        label { font-size: 12px; color: #94a3b8; display: block; margin-bottom: 5px; }
        input, textarea { width: 100%; padding: 10px; background-color: #334155; border: 1px solid #475569; border-radius: 6px; color: white; font-size: 14px; margin-bottom: 15px; box-sizing: border-box; }
        input:focus, textarea:focus { outline: none; border-color: #4ade80; }
        textarea { height: 80px; resize: none; }
        button { width: 100%; background-color: #22c55e; color: #0f172a; padding: 12px; border: none; border-radius: 6px; font-weight: bold; font-size: 14px; cursor: pointer; transition: background 0.2s; }
        button:hover { background-color: #4ade80; }
        #status-kirim { font-size: 12px; margin-top: 12px; font-weight: bold; text-align: center; }
        .text-yellow { color: #facc15; }
        .text-green { color: #4ade80; }
    </style>
</head>
<body>

    <div class="card">
        <h1>🤖 WA Badak Python</h1>
        <p class="subtitle">Pydroid 3 Web Controller</p>
        
        <div class="status-container">
            <span class="status-label">Status Web Server:</span>
            <span class="status-badge">Berjalan Lancar ✅</span>
        </div>

        <div class="form-group">
            <h3>Kirim Pesan Cepat</h3>
            
            <label>Nomor Tujuan (Gunakan Kode Negara)</label>
            <input type="text" id="nomor" placeholder="Contoh: 628123456789">
            
            <label>Isi Pesan</label>
            <textarea id="pesan" placeholder="Ketik pesan di sini..."></textarea>
            
            <button onclick="kirimWA()">Buka & Kirim via WhatsApp</button>
            
            <div id="status-kirim"></div>
        </div>
    </div>

    <script>
        function kirimWA() {
            const nomor = document.getElementById('nomor').value.trim();
            const pesan = encodeURIComponent(document.getElementById('pesan').value);
            const statusBox = document.getElementById('status-kirim');

            if(!nomor || !pesan) {
                alert('Nomor dan pesan tidak boleh kosong!');
                return;
            }

            statusBox.innerText = "⏳ Membuka WhatsApp...";
            statusBox.className = "text-yellow";

            // Menggunakan api whatsapp resmi langsung
            const urlWA = `https://whatsapp.com{nomor}&text=${pesan}`;
            
            // FIX: Menggunakan window.location.href agar langsung pindah aplikasi tanpa keblokir pop-up browser
            window.location.href = urlWA;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("\n🌐 Web Dashboard Berhasil Diperbarui!")
    print("👉 Silakan buka kembali di browser HP kamu: http://127.0.0.1:5000\n")
    app.run(host='0.0.0.0', port=5000, debug=True)