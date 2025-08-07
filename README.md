# 🌐 My Django Web App

A simple Django-based web application for adding tasks to a checklist

---

## 📦 Requirements

- Python 3.8+
- pip

---

## 🛠️ Local Setup

Follow these steps to run the app locally:

```bash
# 1. Clone the repo
git clone https://github.com/manish0x11/checklist
cd checklist

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate


# 6. Run the server
python manage.py runserver
