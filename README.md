# 🏭 Smart Factory: IoT Production Analysis Dashboard
### (IoTデータによるスマートファクトリー化：製造分析ダッシュボード)

---

## 📌 Project Overview (プロジェクト概要)
This project aims to visualize real-time IoT data from the manufacturing floor (collected via **adFactory**) to achieve "Mieruka" (Visual Management) and efficiency. It transforms raw Excel data into actionable insights using Python and Streamlit.

本プロジェクトは、製造現場の設備から得られるリアルタイムデータ（**adFactory**経由）を活用し、工場の「見える化」と「効率化」を実現することを目的としています。PythonとStreamlitを用いることで、生のExcelデータを価値ある分析結果へと変換します。

---

## 📂 Directory Structure (ディレクトリ構成)
The project follows a **Modular Architecture** for high maintainability.
(本プロジェクトは、メンテナンス性を高めるために**モジュール化構造**を採用しています。)

```text
📁 production_dashboard/
├── 📄 app.py              # Main entry point (メインエントリポイント)
├── 📁 config/             # Global settings & styles (設定とスタイル)
├── 📁 data/               # Data loading & Caching (データ読み込みとキャッシュ)
├── 📁 services/           # Business logic & Metrics (計算ロジック)
├── 📁 charts/             # Plotly visualization modules (グラフ作成モジュール)
├── 📁 ui/                 # UI components & CSS (UIコンポーネント)
└── 📄 requirements.txt    # Library dependencies (依存ライブラリ)
🚀 Key Technical Features (主な技術的特徴)
1. High Performance with Caching (キャッシュによる高速化)
Utilizes st.cache_data to store processed data in memory, preventing redundant Excel reading and ensuring an instantaneous user experience. (st.cache_dataを活用し、処理済みデータをメモリに保存することで、Excelの再読み込みを防ぎ、即座なレスポンスを実現しています。)

2. Dynamic Process Detection (動的な工程検知)
Automatically identifies manufacturing processes from Excel columns. No manual code updates are required when processes change. (Excelの列から製造工程を自動的に認識します。工程の追加や名称変更があっても、コードを修正する必要はありません。)

3. Advanced Statistical Analysis (高度な統計分析)
Radar Chart (%): Normalizes all processes to a 100% baseline for easy deviation detection. (全ての工程を100%基準で正規化し、標準からの乖離を容易に把握できます。)

Box Plot (Variability): Visualizes "Baratsuki" (variability) to identify unstable operations. (「ばらつき」を可視化し、不安定な作業工程を特定します。)

🛠 Setup & Installation (セットアップ方法)
Environment (環境構築)
Bash
pip install -r requirements.txt
Run Application (実行)
Bash
streamlit run app.py
💡 Future Roadmap (今後の展望)
Direct DB Connection: Transition from Excel files to direct SQL integration with adFactory. (ExcelファイルからadFactoryのSQLデータベースへの直接連携。)

Automated Alerts: Real-time notifications for efficiency drops via Email or Slack. (効率低下時のメールやSlackによるリアルタイムアラート通知。)

👤 Author (作成者)
Name: [Your Name / 氏名]

Internship: Kanto Seiki Co., Ltd. (関東精機株式会社)

Period: Jan 2026 - Feb 2026

📝 Note for Successors (後継者へのメモ)
The code is strictly separated into logic and UI. When adding a new chart, please create a new file in the charts/ directory and import it into app.py. (コードはロジックとUIを厳格に分離しています。新しいグssラフを追加する場合は、charts/ディレクトリに新しいファイルを作成し、app.pyでインポートしてください。)