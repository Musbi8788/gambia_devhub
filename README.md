# Gambia DevHub

A hackathon project built during the **MyFarm Dev Hackathon**. Gambia DevHub is a community-driven platform where developers in The Gambia can share, learn, and collaborate.

🌍 Live Demo: [https://gambia-devhub.onrender.com/](https://gambia-devhub.onrender.com/)

## Features
- Django backend (Python)
- SQLite database
- Bootstrap frontend
- User-friendly interface
- Hackathon-ready MVP

## Tech Stack
- **Backend:** Django
- **Database:** SQLite
- **Frontend:** Bootstrap
- **Deployment:** Render (with Gunicorn)

## Installation & Setup

Clone the repository:
```bash
git clone https://github.com/your-username/gambia-devhub.git
cd gambia-devhub
```

Create & activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py migrate
```

Run the development server:
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deployment
We use **Render** for deployment.

Gunicorn command:
```bash
gunicorn gambia_devhub.wsgi
```

## Contributing
We are looking for collaborators! 🎉

1. Fork the repo
2. Create your branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push (`git push origin feature-name`)
5. Open a Pull Request

## License
For **hackathon/demo purposes only**. Not a free software license.

