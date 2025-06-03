# BANGLA_WORD_BANK46000
 This is a huge collection of Bangla words with labeled data.
 
![Screenshot 2025-03-18 113524](https://github.com/user-attachments/assets/ad3b896a-2bd0-4401-b659-6f4cc0883ff0)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BANGLA_WORD_BANK46000</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1, h2, h3 {
            text-align: center;
        }
        code {
            background: #eee;
            padding: 2px 4px;
            font-size: 90%;
            border-radius: 4px;
        }
        pre {
            background: #333;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }
        .section {
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        a {
            color: #007acc;
        }
        footer {
            text-align: center;
            font-style: italic;
            margin-top: 40px;
        }
    </style>
</head>
<body>

<h1>🇧🇩 BANGLA_WORD_BANK46000</h1>
<p style="text-align:center;"><strong>A comprehensive structured vocabulary database for the Bangla language</strong><br/>Part of the <strong>BongoVandar</strong> project</p>

<div class="section">
    <h2>📖 Project Overview</h2>
    <ul>
        <li>🅰️ 46 Bangla letters</li>
        <li>🌍 4 Origins: তৎসম, তদ্ভব, দেশীয়, বিদেশি</li>
        <li>📚 5 Word Types: Noun, Verb, Adjective, Pronoun, Indeclinable</li>
    </ul>
    <p>Each entry includes label, origin, synonyms, and example sentences. All are stored in structured <strong>JSON</strong> format using <strong>PostgreSQL JSONB</strong>.</p>
</div>

<div class="section">
    <h2>🌟 Key Features</h2>
    <ul>
        <li>✅ Coverage of <strong>46,000+</strong> unique words</li>
        <li>✅ JSON-formatted structured entries</li>
        <li>✅ Origin and type classification</li>
        <li>✅ Built-in <code>Django</code> web interface for word management</li>
        <li>✅ Frontend: <code>HTML + CSS</code>, Backend: <code>Django</code>, DB: <code>PostgreSQL</code></li>
    </ul>
</div>

<div class="section">
    <h2>🗂️ Directory Structure</h2>
    <pre><code>BANGLA_WORD_BANK46000/
├── manage.py
├── shabdabhandar/
│   ├── settings.py
│   └── urls.py
├── vocabulary/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/
│       └── vocabulary/
│           ├── base.html
│           ├── word_list.html
│           └── add_word.html
├── static/
│   └── css/
│       └── styles.css
├── json/
│   └── vocabulary.json
├── insert_json_data.py
└── README.md</code></pre>
</div>

<div class="section">
    <h2>⚙️ Setup Instructions</h2>
    <h3>🔧 Requirements</h3>
    <ul>
        <li>Python 3.x</li>
        <li>PostgreSQL</li>
        <li>Django</li>
    </ul>

    <h3>🚀 Installation</h3>
    <pre><code>git clone https://github.com/sadatpro/BANGLA_WORD_BANK46000.git
cd BANGLA_WORD_BANK46000
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scriptsctivate
pip install -r requirements.txt</code></pre>

    <h3>🗃️ Database Setup</h3>
    <pre><code>CREATE DATABASE shabdabhandar;</code></pre>

    <h3>🔄 Migrations & Data Import</h3>
    <pre><code>python manage.py makemigrations
python manage.py migrate
python insert_json_data.py</code></pre>

    <h3>🌐 Run Server</h3>
    <pre><code>python manage.py runserver</code></pre>
    <p>Visit: <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a></p>
</div>

<div class="section">
    <h2>🧱 JSON Structure</h2>
    <pre><code>{
  "শব্দভাণ্ডার": {
    "অ": {
      "তৎসম": {
        "বিশেষ্য": [
          {
            "লেবেল": "সাধারণ বিশেষ্য",
            "মূল": "অমৃত",
            "সমার্থক": ["পানীয়", "অমৃতরস"],
            "উৎপত্তি": "সংস্কৃত",
            "উদাহরণ": "দেবতারা অমৃত পান করেন।"
          }
        ]
      }
    }
  }
}</code></pre>
</div>

<div class="section">
    <h2>📌 Future Roadmap</h2>
    <ul>
        <li>🔍 Filter/search by letter, origin, type</li>
        <li>📱 Mobile app with Flutter or React Native</li>
        <li>⚙️ REST API using Django REST Framework</li>
        <li>🎨 Frontend upgrade with Bootstrap or React</li>
        <li>🧠 NLP model integration</li>
    </ul>
</div>

<div class="section">
    <h2>🤝 Contribution</h2>
    <ul>
        <li>Fork the repo and open a Pull Request</li>
        <li>Add words to <code>vocabulary.json</code></li>
        <li>Run <code>insert_json_data.py</code> to import</li>
        <li>Report issues and suggest features</li>
    </ul>
</div>

<div class="section">
    <h2>📄 License</h2>
    <p><strong>MIT License</strong><br/>See <code>LICENSE</code> for details</p>
</div>

<div class="section">
    <h2>📬 Contact</h2>
    <p><strong>GitHub:</strong> <a href="https://github.com/sadatpro" target="_blank">SadatPro</a></p>
    <p><strong>Email:</strong> sadatmahmud1@outlook.com</p>
</div>

<footer>Empowering Bangla language through open-source lexicons 🇧🇩</footer>

</body>
</html>

