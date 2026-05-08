from flask import Flask, render_template_string

app = Flask(__name__)

html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kanye West Fan Page</title>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: #0d0d0d;
      color: white;
      overflow-x: hidden;
    }

    header {
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      background: linear-gradient(135deg, #111, #222, #000);
      animation: backgroundMove 8s infinite alternate;
    }

    @keyframes backgroundMove {
      from {
        background-position: left;
      }
      to {
        background-position: right;
      }
    }

    h1 {
      font-size: 5rem;
      text-transform: uppercase;
      animation: fadeIn 2s ease;
    }

    p {
      margin-top: 20px;
      width: 70%;
      line-height: 1.8;
      color: #d1d1d1;
      font-size: 1.2rem;
      animation: slideUp 2s ease;
    }

    .btn {
      margin-top: 30px;
      padding: 15px 35px;
      border: none;
      border-radius: 30px;
      background: white;
      color: black;
      font-weight: bold;
      cursor: pointer;
      transition: 0.3s;
    }

    .btn:hover {
      transform: scale(1.1);
      background: #cfcfcf;
    }

    section {
      padding: 80px 10%;
    }

    .albums {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
      margin-top: 40px;
    }

    .card {
      background: #1b1b1b;
      padding: 25px;
      border-radius: 20px;
      transition: 0.4s;
      text-align: center;
    }

    .card:hover {
      transform: translateY(-10px);
      background: #292929;
    }

    .card h2 {
      margin-bottom: 10px;
    }

    footer {
      text-align: center;
      padding: 30px;
      border-top: 1px solid rgba(255,255,255,0.1);
      color: #888;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
    }

    @keyframes slideUp {
      from {
        opacity: 0;
        transform: translateY(50px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @media(max-width: 768px) {
      h1 {
        font-size: 3rem;
      }

      p {
        width: 90%;
        font-size: 1rem;
      }
    }
  </style>
</head>
<body>

  <header>
    <h1>Kanye West</h1>
    <p>
      Rapper, producer, designer, and cultural icon. Kanye West changed modern music forever with creativity and innovation.
    </p>

    <button class="btn" onclick="scrollToAlbums()">Explore Albums</button>
  </header>

  <section id="albums">
    <h1 style="font-size:3rem; text-align:center;">Legendary Albums</h1>

    <div class="albums">
      <div class="card">
        <h2>Graduation</h2>
        <p>One of Kanye's most iconic and futuristic hip-hop albums.</p>
      </div>

      <div class="card">
        <h2>Donda</h2>
        <p>A powerful and emotional album dedicated to his mother.</p>
      </div>

      <div class="card">
        <h2>808s & Heartbreak</h2>
        <p>An album that influenced a generation of melodic rap artists.</p>
      </div>

      <div class="card">
        <h2>The College Dropout</h2>
        <p>The album that introduced Kanye's genius to the world.</p>
      </div>
    </div>
  </section>

  <footer>
    Kanye West Fan Website • Built With Python & Flask
  </footer>

  <script>
    function scrollToAlbums() {
      document.getElementById('albums').scrollIntoView({
        behavior: 'smooth'
      });
    }
  </script>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)


