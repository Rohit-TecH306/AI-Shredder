<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>AI Shredder & Redaction Tool — README</title>
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#7c3aed;
      --accent-2:#06b6d4;
      --text:#e6eef8;
      --glass: rgba(255,255,255,0.03);
      --code-bg:#071029;
      --mono: "SFMono-Regular", "Consolas", "Liberation Mono", Menlo, monospace;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%}
    body{
      margin:0;
      background: linear-gradient(180deg, #071123 0%, #071229 50%, #06131c 100%);
      color:var(--text);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.5;
      padding:28px;
      box-sizing:border-box;
    }

    .container{
      max-width: 1000px;
      margin: 0 auto;
    }

    header {
      display:flex;
      gap:18px;
      align-items:center;
      margin-bottom:22px;
    }
    .logo{
      width:64px;height:64px;
      display:grid;place-items:center;
      border-radius:12px;
      background:linear-gradient(135deg,var(--accent),var(--accent-2));
      box-shadow: 0 6px 24px rgba(124,58,237,0.18), inset 0 -6px 18px rgba(0,0,0,0.15);
      font-weight:700;font-size:20px;
    }
    h1{margin:0;font-size:28px}
    .subtitle{color:var(--muted);margin-top:6px;font-size:14px}

    .hero {
      background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
      border-radius:12px;
      padding:18px;
      box-shadow: 0 8px 30px rgba(2,6,23,0.6);
      margin-bottom:20px;
    }

    .badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
    .badge{
      background:var(--glass);
      color:var(--text);
      padding:6px 10px;border-radius:999px;font-size:13px;border:1px solid rgba(255,255,255,0.03)
    }

    main{
      display:grid;
      grid-template-columns: 1fr 320px;
      gap:20px;
      align-items:start;
    }

    .card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:12px;
      padding:18px;
      box-shadow: 0 8px 24px rgba(2,6,23,0.6);
      border:1px solid rgba(255,255,255,0.02);
    }

    .content h2{
      margin-top:0;margin-bottom:8px;font-size:18px;
      display:flex;align-items:center;gap:10px;
    }
    .muted{color:var(--muted);font-size:13px;margin-bottom:12px}

    pre.code {
      background:var(--code-bg);
      padding:14px;
      border-radius:10px;
      overflow:auto;
      font-family:var(--mono);
      font-size:13px;
      border:1px solid rgba(255,255,255,0.02);
      position:relative;
      color:#cfe7ff;
      margin:12px 0;
    }

    .code .copy-btn{
      position:absolute;
      top:10px;right:10px;
      background:rgba(255,255,255,0.04);
      border:1px solid rgba(255,255,255,0.03);
      color:var(--text);
      padding:6px 8px;border-radius:8px;
      cursor:pointer;font-size:12px;
    }

    .file-tree{
      font-family:var(--mono);
      font-size:13px;
      background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);
      padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.02);
      color:var(--muted);
    }
    .file-tree code{color:var(--muted)}
    .section {
      margin-bottom:18px;
    }

    ul{padding-left:18px}
    li{margin:8px 0}

    .cta-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
    .btn{
      display:inline-flex;align-items:center;gap:8px;
      padding:10px 14px;border-radius:10px;border:0;cursor:pointer;
      background:linear-gradient(90deg,var(--accent),var(--accent-2));
      color:white;font-weight:600;
      box-shadow: 0 6px 18px rgba(124,58,237,0.18);
    }
    .btn.ghost{
      background:transparent;border:1px solid rgba(255,255,255,0.04);
      color:var(--text);font-weight:600;
    }

    footer{margin-top:20px;color:var(--muted);font-size:13px;text-align:center}

    @media (max-width:980px){
      main{grid-template-columns:1fr}
      .container{padding:18px}
    }

    /* small helpers */
    .kbd{
      background:rgba(255,255,255,0.03);
      padding:2px 8px;border-radius:6px;border:1px solid rgba(255,255,255,0.02);
      font-family:var(--mono);font-size:12px;color:var(--text)
    }

    .tag{display:inline-block;padding:4px 8px;font-size:12px;border-radius:999px;background:rgba(255,255,255,0.02);color:var(--muted);border:1px solid rgba(255,255,255,0.02)}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">AI</div>
      <div>
        <h1>AI Shredder &amp; Redaction Tool</h1>
        <div class="subtitle">Detect, score, and redact sensitive information with configurable confidence thresholds.</div>
        <div class="badges">
          <div class="badge">MIT</div>
          <div class="badge">Python • PyTorch</div>
          <div class="badge">Confidence Scoring</div>
        </div>
      </div>
    </header>

    <div class="hero card">
      <div style="display:flex;justify-content:space-between;gap:12px;align-items:center">
        <div>
          <strong style="font-size:16px">Overview</strong>
          <div class="muted">An AI-powered tool for detecting, evaluating, and redacting sensitive text (PII/PHI/etc.).</div>
        </div>
        <div class="tag">Ready to paste — HTML README</div>
      </div>

      <div style="margin-top:12px;color:var(--muted);font-size:14px">
        Use this file as a project homepage, or convert the content back into <code>README.md</code>.
      </div>
    </div>

    <main>
      <section class="card content">
        <div class="section">
          <h2>✨ Features</h2>
          <div class="muted">Capabilities included in this repository</div>
          <ul>
            <li>🔍 <strong>Entity Detection</strong> — Names, identifiers, and other sensitive fields.</li>
            <li>📝 <strong>Redaction Strategies</strong> — Mask, remove, or hash detected entities.</li>
            <li>📊 <strong>Confidence Scoring</strong> — Per-entity score (0–1) and configurable thresholds.</li>
            <li>⚡ <strong>Training &amp; Inference</strong> — Train models and run redaction pipelines.</li>
            <li>🧪 <strong>Testing Suite</strong> — Test inference behavior and thresholds.</li>
          </ul>
        </div>

        <div class="section">
          <h2>📂 Repository Structure</h2>
          <div class="muted">Project layout (placeholders reflect repo)</div>
          <pre class="code file-tree"><code>
AI_Shredder_and_Redaction_Tool/
├── data/                    # Datasets / sample inputs
├── logs/                    # Logs from training, inference, or evaluation
├── models/                  # Saved models
├── Redaction/               # Core redaction logic
├── utils/                   # Helper functions
├── dataset.py               # Data loading & preprocessing
├── evaluate.py              # Model evaluation & metrics
├── generate_test_labels.py  # Generate test labels
├── inference.py             # Run inference & redaction
├── model.py                 # Model architecture
├── test_inference.py        # Inference testing
├── train.py                 # Training script
└── README.md
          </code></pre>
        </div>

        <div class="section">
          <h2>🚀 Getting Started</h2>
          <div class="muted">Quick setup guide</div>

          <strong>1. Installation</strong>
          <pre class="code" id="cmd-install"><button class="copy-btn copy" data-target="cmd-install">Copy</button><code>git clone https://github.com/prachishende007/AI_Shredder_and_Redaction_Tool.git
cd AI_Shredder_and_Redaction_Tool
pip install -r requirements.txt</code></pre>
          <div class="muted">If `requirements.txt` is missing, install essentials like <code>torch</code>, <code>transformers</code>, <code>scikit-learn</code>, and <code>pytest</code>.</div>

          <strong style="display:block;margin-top:10px">2. Training</strong>
          <pre class="code" id="cmd-train"><button class="copy-btn copy" data-target="cmd-train">Copy</button><code>python train.py --epochs 10 --batch_size 32 --save_dir models/</code></pre>

          <strong style="display:block;margin-top:10px">3. Inference / Redaction</strong>
          <pre class="code" id="cmd-infer"><button class="copy-btn copy" data-target="cmd-infer">Copy</button><code>python inference.py --input "John Doe’s SSN is 123-45-6789" --threshold 0.85</code></pre>

          <div class="muted">Example output (conceptual)</div>
          <pre class="code"><button class="copy-btn copy">Copy</button><code>Cleaned Text:
████ ███’s SSN is █████████

Detected Entities:
[
  {"entity": "NAME", "value": "John Doe", "confidence": 0.91},
  {"entity": "SSN", "value": "123-45-6789", "confidence": 0.94}
]</code></pre>

          <strong style="display:block;margin-top:10px">4. Evaluation</strong>
          <pre class="code" id="cmd-eval"><button class="copy-btn copy" data-target="cmd-eval">Copy</button><code>python evaluate.py --predictions preds.json --ground_truth data/test.json</code></pre>

          <strong style="display:block;margin-top:10px">5. Testing</strong>
          <pre class="code" id="cmd-test"><button class="copy-btn copy" data-target="cmd-test">Copy</button><code>pytest test_inference.py</code></pre>
        </div>

        <div class="section">
          <h2>⚖️ Confidence Scoring</h2>
          <div class="muted">How confidence controls redaction</div>
          <p>
            Each detected entity receives a numeric confidence score in the range <code>[0.0, 1.0]</code>.
            Configure a threshold to decide whether to auto-redact or flag for manual review.
          </p>
          <pre class="code"><button class="copy-btn copy">Copy</button><code># Example: only redact if confidence ≥ 0.9
redactor = Redactor(confidence_threshold=0.9)</code></pre>
          <ul>
            <li>✅ Above threshold → auto-redact</li>
            <li>⚠️ Below threshold → flagged / logged for human review</li>
          </ul>
        </div>

        <div class="section">
          <h2>⚙️ Configuration</h2>
          <div class="muted">Optional <code>config.yml</code> suggestion</div>
          <pre class="code"><button class="copy-btn copy">Copy</button><code>model:
  checkpoint: "models/latest.pt"

redaction:
  threshold: 0.85
  strategy: mask   # options: mask, remove, hash
  mask_char: "█"

logging:
  level: INFO
  output: logs/
</code></pre>
        </div>

        <div class="section">
          <h2>🛣 Roadmap</h2>
          <div class="muted">Planned improvements</div>
          <ul>
            <li>Multi-language support</li>
            <li>Additional entity categories (financial, medical, legal)</li>
            <li>REST API &amp; Web UI for redaction services</li>
            <li>Redaction preview mode</li>
            <li>Model ensembles for improved accuracy</li>
          </ul>
        </div>

        <div class="section">
          <h2>🤝 Contributing</h2>
          <div class="muted">How to contribute</div>
          <ol>
            <li>Fork the repository</li>
            <li>Create a feature branch (<span class="kbd">git checkout -b feature-name</span>)</li>
            <li>Commit changes (<span class="kbd">git commit -m "Add feature"</span>)</li>
            <li>Push and open a Pull Request</li>
          </ol>
        </div>

        <div class="section">
          <h2>📜 License</h2>
          <div class="muted">Project license</div>
          <p>MIT License © 2025 [Your Name / Organization]</p>
        </div>

      </section>

      <aside class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <strong>Quick Links</strong>
          <span class="muted">Reference</span>
        </div>

        <div style="margin-bottom:12px">
          <div style="font-weight:700;margin-bottom:6px">Useful commands</div>
          <div style="font-size:13px;color:var(--muted)">
            <div style="margin-bottom:6px;"><code>python train.py</code> — train models</div>
            <div style="margin-bottom:6px;"><code>python inference.py</code> — run redaction</div>
            <div><code>python evaluate.py</code> — evaluate predictions</div>
          </div>
        </div>

        <div style="margin-bottom:12px">
          <div style="font-weight:700;margin-bottom:6px">File Tree</div>
          <div style="font-size:13px;color:var(--muted)">
            <pre style="margin:0;font-family:var(--mono);font-size:13px;white-space:pre-wrap">
dataset.py
model.py
train.py
inference.py
evaluate.py
generate_test_labels.py
test_inference.py
utils/
Redaction/
data/
models/
logs/
            </pre>
          </div>
        </div>

        <div style="margin-bottom:6px">
          <div style="font-weight:700;margin-bottom:6px">Configuration Tips</div>
          <div class="muted" style="font-size:13px">
            Use a <code>config.yml</code> for thresholds &amp; checkpoints; keep logs in <code>logs/</code>.
          </div>
        </div>

        <div style="margin-top:14px" class="cta-row">
          <button class="btn" onclick="copyTextToClipboard('git clone https://github.com/prachishende007/AI_Shredder_and_Redaction_Tool.git')">Copy clone URL</button>
          <a class="btn ghost" href="#" onclick="window.print();return false;">Print</a>
        </div>
      </aside>
    </main>

    <footer>
      <div>Made with care • AI Shredder &amp; Redaction Tool</div>
      <div style="margin-top:6px;color:var(--muted)">Tip: Edit the license holder and any command-line arguments to match your codebase.</div>
    </footer>
  </div>

  <script>
    // Copy button logic
    document.querySelectorAll('.copy').forEach(btn=>{
      btn.addEventListener('click', async (e)=>{
        const parent = btn.closest('pre');
        const code = parent.querySelector('code').innerText;
        try {
          await navigator.clipboard.writeText(code);
          btn.innerText = 'Copied';
          setTimeout(()=>btn.innerText='Copy',1200);
        } catch(err){
          alert('Copy failed — select & copy manually.');
        }
      });
    });

    // Copy specific quick clone button
    function copyTextToClipboard(text){
      navigator.clipboard.writeText(text).then(()=> {
        const prev = document.activeElement;
        alert('Copied to clipboard');
      }, ()=> alert('Could not copy — please copy manually.'));
    }

    // Add copy button to any pre.code not already having .copy inside
    document.querySelectorAll('pre.code').forEach(pre=>{
      if (!pre.querySelector('.copy-btn')){
        const btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.innerText = 'Copy';
        btn.onclick = async ()=>{
          const code = pre.querySelector('code').innerText;
          try {
            await navigator.clipboard.writeText(code);
            btn.innerText = 'Copied';
            setTimeout(()=>btn.innerText='Copy',1200);
          } catch {
            alert('Copy failed — please copy manually.');
          }
        };
        pre.appendChild(btn);
      }
    });
  </script>
</body>
</html>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>AI Shredder & Redaction Tool — README</title>
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#7c3aed;
      --accent-2:#06b6d4;
      --text:#e6eef8;
      --glass: rgba(255,255,255,0.03);
      --code-bg:#071029;
      --mono: "SFMono-Regular", "Consolas", "Liberation Mono", Menlo, monospace;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%}
    body{
      margin:0;
      background: linear-gradient(180deg, #071123 0%, #071229 50%, #06131c 100%);
      color:var(--text);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.5;
      padding:28px;
      box-sizing:border-box;
    }

    .container{
      max-width: 1000px;
      margin: 0 auto;
    }

    header {
      display:flex;
      gap:18px;
      align-items:center;
      margin-bottom:22px;
    }
    .logo{
      width:64px;height:64px;
      display:grid;place-items:center;
      border-radius:12px;
      background:linear-gradient(135deg,var(--accent),var(--accent-2));
      box-shadow: 0 6px 24px rgba(124,58,237,0.18), inset 0 -6px 18px rgba(0,0,0,0.15);
      font-weight:700;font-size:20px;
    }
    h1{margin:0;font-size:28px}
    .subtitle{color:var(--muted);margin-top:6px;font-size:14px}

    .hero {
      background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
      border-radius:12px;
      padding:18px;
      box-shadow: 0 8px 30px rgba(2,6,23,0.6);
      margin-bottom:20px;
    }

    .badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
    .badge{
      background:var(--glass);
      color:var(--text);
      padding:6px 10px;border-radius:999px;font-size:13px;border:1px solid rgba(255,255,255,0.03)
    }

    main{
      display:grid;
      grid-template-columns: 1fr 320px;
      gap:20px;
      align-items:start;
    }

    .card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:12px;
      padding:18px;
      box-shadow: 0 8px 24px rgba(2,6,23,0.6);
      border:1px solid rgba(255,255,255,0.02);
    }

    .content h2{
      margin-top:0;margin-bottom:8px;font-size:18px;
      display:flex;align-items:center;gap:10px;
    }
    .muted{color:var(--muted);font-size:13px;margin-bottom:12px}

    pre.code {
      background:var(--code-bg);
      padding:14px;
      border-radius:10px;
      overflow:auto;
      font-family:var(--mono);
      font-size:13px;
      border:1px solid rgba(255,255,255,0.02);
      position:relative;
      color:#cfe7ff;
      margin:12px 0;
    }

    .code .copy-btn{
      position:absolute;
      top:10px;right:10px;
      background:rgba(255,255,255,0.04);
      border:1px solid rgba(255,255,255,0.03);
      color:var(--text);
      padding:6px 8px;border-radius:8px;
      cursor:pointer;font-size:12px;
    }

    .file-tree{
      font-family:var(--mono);
      font-size:13px;
      background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);
      padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.02);
      color:var(--muted);
    }
    .file-tree code{color:var(--muted)}
    .section {
      margin-bottom:18px;
    }

    ul{padding-left:18px}
    li{margin:8px 0}

    .cta-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
    .btn{
      display:inline-flex;align-items:center;gap:8px;
      padding:10px 14px;border-radius:10px;border:0;cursor:pointer;
      background:linear-gradient(90deg,var(--accent),var(--accent-2));
      color:white;font-weight:600;
      box-shadow: 0 6px 18px rgba(124,58,237,0.18);
    }
    .btn.ghost{
      background:transparent;border:1px solid rgba(255,255,255,0.04);
      color:var(--text);font-weight:600;
    }

    footer{margin-top:20px;color:var(--muted);font-size:13px;text-align:center}

    @media (max-width:980px){
      main{grid-template-columns:1fr}
      .container{padding:18px}
    }

    /* small helpers */
    .kbd{
      background:rgba(255,255,255,0.03);
      padding:2px 8px;border-radius:6px;border:1px solid rgba(255,255,255,0.02);
      font-family:var(--mono);font-size:12px;color:var(--text)
    }

    .tag{display:inline-block;padding:4px 8px;font-size:12px;border-radius:999px;background:rgba(255,255,255,0.02);color:var(--muted);border:1px solid rgba(255,255,255,0.02)}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">AI</div>
      <div>
        <h1>AI Shredder &amp; Redaction Tool</h1>
        <div class="subtitle">Detect, score, and redact sensitive information with configurable confidence thresholds.</div>
        <div class="badges">
          <div class="badge">MIT</div>
          <div class="badge">Python • PyTorch</div>
          <div class="badge">Confidence Scoring</div>
        </div>
      </div>
    </header>

    <div class="hero card">
      <div style="display:flex;justify-content:space-between;gap:12px;align-items:center">
        <div>
          <strong style="font-size:16px">Overview</strong>
          <div class="muted">An AI-powered tool for detecting, evaluating, and redacting sensitive text (PII/PHI/etc.).</div>
        </div>
        <div class="tag">Ready to paste — HTML README</div>
      </div>

      <div style="margin-top:12px;color:var(--muted);font-size:14px">
        Use this file as a project homepage, or convert the content back into <code>README.md</code>.
      </div>
    </div>

    <main>
      <section class="card content">
        <div class="section">
          <h2>✨ Features</h2>
          <div class="muted">Capabilities included in this repository</div>
          <ul>
            <li>🔍 <strong>Entity Detection</strong> — Names, identifiers, and other sensitive fields.</li>
            <li>📝 <strong>Redaction Strategies</strong> — Mask, remove, or hash detected entities.</li>
            <li>📊 <strong>Confidence Scoring</strong> — Per-entity score (0–1) and configurable thresholds.</li>
            <li>⚡ <strong>Training &amp; Inference</strong> — Train models and run redaction pipelines.</li>
            <li>🧪 <strong>Testing Suite</strong> — Test inference behavior and thresholds.</li>
          </ul>
        </div>

        <div class="section">
          <h2>📂 Repository Structure</h2>
          <div class="muted">Project layout (placeholders reflect repo)</div>
          <pre class="code file-tree"><code>
AI_Shredder_and_Redaction_Tool/
├── data/                    # Datasets / sample inputs
├── logs/                    # Logs from training, inference, or evaluation
├── models/                  # Saved models
├── Redaction/               # Core redaction logic
├── utils/                   # Helper functions
├── dataset.py               # Data loading & preprocessing
├── evaluate.py              # Model evaluation & metrics
├── generate_test_labels.py  # Generate test labels
├── inference.py             # Run inference & redaction
├── model.py                 # Model architecture
├── test_inference.py        # Inference testing
├── train.py                 # Training script
└── README.md
          </code></pre>
        </div>

        <div class="section">
          <h2>🚀 Getting Started</h2>
          <div class="muted">Quick setup guide</div>

          <strong>1. Installation</strong>
          <pre class="code" id="cmd-install"><button class="copy-btn copy" data-target="cmd-install">Copy</button><code>git clone https://github.com/prachishende007/AI_Shredder_and_Redaction_Tool.git
cd AI_Shredder_and_Redaction_Tool
pip install -r requirements.txt</code></pre>
          <div class="muted">If `requirements.txt` is missing, install essentials like <code>torch</code>, <code>transformers</code>, <code>scikit-learn</code>, and <code>pytest</code>.</div>

          <strong style="display:block;margin-top:10px">2. Training</strong>
          <pre class="code" id="cmd-train"><button class="copy-btn copy" data-target="cmd-train">Copy</button><code>python train.py --epochs 10 --batch_size 32 --save_dir models/</code></pre>

          <strong style="display:block;margin-top:10px">3. Inference / Redaction</strong>
          <pre class="code" id="cmd-infer"><button class="copy-btn copy" data-target="cmd-infer">Copy</button><code>python inference.py --input "John Doe’s SSN is 123-45-6789" --threshold 0.85</code></pre>

          <div class="muted">Example output (conceptual)</div>
          <pre class="code"><button class="copy-btn copy">Copy</button><code>Cleaned Text:
████ ███’s SSN is █████████

Detected Entities:
[
  {"entity": "NAME", "value": "John Doe", "confidence": 0.91},
  {"entity": "SSN", "value": "123-45-6789", "confidence": 0.94}
]</code></pre>

          <strong style="display:block;margin-top:10px">4. Evaluation</strong>
          <pre class="code" id="cmd-eval"><button class="copy-btn copy" data-target="cmd-eval">Copy</button><code>python evaluate.py --predictions preds.json --ground_truth data/test.json</code></pre>

          <strong style="display:block;margin-top:10px">5. Testing</strong>
          <pre class="code" id="cmd-test"><button class="copy-btn copy" data-target="cmd-test">Copy</button><code>pytest test_inference.py</code></pre>
        </div>

        <div class="section">
          <h2>⚖️ Confidence Scoring</h2>
          <div class="muted">How confidence controls redaction</div>
          <p>
            Each detected entity receives a numeric confidence score in the range <code>[0.0, 1.0]</code>.
            Configure a threshold to decide whether to auto-redact or flag for manual review.
          </p>
          <pre class="code"><button class="copy-btn copy">Copy</button><code># Example: only redact if confidence ≥ 0.9
redactor = Redactor(confidence_threshold=0.9)</code></pre>
          <ul>
            <li>✅ Above threshold → auto-redact</li>
            <li>⚠️ Below threshold → flagged / logged for human review</li>
          </ul>
        </div>

        <div class="section">
          <h2>⚙️ Configuration</h2>
          <div class="muted">Optional <code>config.yml</code> suggestion</div>
          <pre class="code"><button class="copy-btn copy">Copy</button><code>model:
  checkpoint: "models/latest.pt"

redaction:
  threshold: 0.85
  strategy: mask   # options: mask, remove, hash
  mask_char: "█"

logging:
  level: INFO
  output: logs/
</code></pre>
        </div>

        <div class="section">
          <h2>🛣 Roadmap</h2>
          <div class="muted">Planned improvements</div>
          <ul>
            <li>Multi-language support</li>
            <li>Additional entity categories (financial, medical, legal)</li>
            <li>REST API &amp; Web UI for redaction services</li>
            <li>Redaction preview mode</li>
            <li>Model ensembles for improved accuracy</li>
          </ul>
        </div>

        <div class="section">
          <h2>🤝 Contributing</h2>
          <div class="muted">How to contribute</div>
          <ol>
            <li>Fork the repository</li>
            <li>Create a feature branch (<span class="kbd">git checkout -b feature-name</span>)</li>
            <li>Commit changes (<span class="kbd">git commit -m "Add feature"</span>)</li>
            <li>Push and open a Pull Request</li>
          </ol>
        </div>

        <div class="section">
          <h2>📜 License</h2>
          <div class="muted">Project license</div>
          <p>MIT License © 2025 [Your Name / Organization]</p>
        </div>

      </section>

      <aside class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <strong>Quick Links</strong>
          <span class="muted">Reference</span>
        </div>

        <div style="margin-bottom:12px">
          <div style="font-weight:700;margin-bottom:6px">Useful commands</div>
          <div style="font-size:13px;color:var(--muted)">
            <div style="margin-bottom:6px;"><code>python train.py</code> — train models</div>
            <div style="margin-bottom:6px;"><code>python inference.py</code> — run redaction</div>
            <div><code>python evaluate.py</code> — evaluate predictions</div>
          </div>
        </div>

        <div style="margin-bottom:12px">
          <div style="font-weight:700;margin-bottom:6px">File Tree</div>
          <div style="font-size:13px;color:var(--muted)">
            <pre style="margin:0;font-family:var(--mono);font-size:13px;white-space:pre-wrap">
dataset.py
model.py
train.py
inference.py
evaluate.py
generate_test_labels.py
test_inference.py
utils/
Redaction/
data/
models/
logs/
            </pre>
          </div>
        </div>

        <div style="margin-bottom:6px">
          <div style="font-weight:700;margin-bottom:6px">Configuration Tips</div>
          <div class="muted" style="font-size:13px">
            Use a <code>config.yml</code> for thresholds &amp; checkpoints; keep logs in <code>logs/</code>.
          </div>
        </div>

        <div style="margin-top:14px" class="cta-row">
          <button class="btn" onclick="copyTextToClipboard('git clone https://github.com/prachishende007/AI_Shredder_and_Redaction_Tool.git')">Copy clone URL</button>
          <a class="btn ghost" href="#" onclick="window.print();return false;">Print</a>
        </div>
      </aside>
    </main>

    <footer>
      <div>Made with care • AI Shredder &amp; Redaction Tool</div>
      <div style="margin-top:6px;color:var(--muted)">Tip: Edit the license holder and any command-line arguments to match your codebase.</div>
    </footer>
  </div>

  <script>
    // Copy button logic
    document.querySelectorAll('.copy').forEach(btn=>{
      btn.addEventListener('click', async (e)=>{
        const parent = btn.closest('pre');
        const code = parent.querySelector('code').innerText;
        try {
          await navigator.clipboard.writeText(code);
          btn.innerText = 'Copied';
          setTimeout(()=>btn.innerText='Copy',1200);
        } catch(err){
          alert('Copy failed — select & copy manually.');
        }
      });
    });

    // Copy specific quick clone button
    function copyTextToClipboard(text){
      navigator.clipboard.writeText(text).then(()=> {
        const prev = document.activeElement;
        alert('Copied to clipboard');
      }, ()=> alert('Could not copy — please copy manually.'));
    }

    // Add copy button to any pre.code not already having .copy inside
    document.querySelectorAll('pre.code').forEach(pre=>{
      if (!pre.querySelector('.copy-btn')){
        const btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.innerText = 'Copy';
        btn.onclick = async ()=>{
          const code = pre.querySelector('code').innerText;
          try {
            await navigator.clipboard.writeText(code);
            btn.innerText = 'Copied';
            setTimeout(()=>btn.innerText='Copy',1200);
          } catch {
            alert('Copy failed — please copy manually.');
          }
        };
        pre.appendChild(btn);
      }
    });
  </script>
</body>
</html>
