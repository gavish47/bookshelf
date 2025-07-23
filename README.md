📚 Bookshelf – Book Management Web App

[🌐 Visit Live Site →](https://bookshelf1.store)

Bookshelf is a full-stack Django-based web application that allows users to explore, add, update, and manage books. It features secure user authentication, a clean book management UI, and RESTful APIs for external integration.

🚀 Features

- 🔐 **User Authentication**
  - Sign up / login / logout
  - Secure session management via Django Auth

- 📖 **Book Management**
  - Add, edit, and delete books (admin only)
  - Title, author, description, full content, and buy link
  - Dynamic detail pages for each book

- 📄 **Admin Panel**
  - Full Django admin interface for managing books and users

- 🔎 **Book Browsing**
  - View all books on the homepage
  - Responsive layout using Bootstrap

- 🧩 **REST API (via Django REST Framework)**
  - API endpoints for listing, creating, editing, and deleting books
  - Token-based authentication for secure access

---

 🖼️ Live Preview

 Homepage Screenshot
<img width="1920" height="1080" alt="Screenshot 2025-07-23 130637" src="https://github.com/user-attachments/assets/bd3a5c31-0948-48ff-acad-a025d1d0c9f3" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 130648" src="https://github.com/user-attachments/assets/9e219558-ff99-43c2-9a95-0a8237ba9b0b" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 130707" src="https://github.com/user-attachments/assets/5e65833e-fcb1-42fc-bea8-d71481a05044" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 130659" src="https://github.com/user-attachments/assets/3978efa3-0e15-4e42-82da-854e6c7eeaa6" />


> *(Ensure the screenshot exists at the above URL or update it based on where you host the image.)*

 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (development)
- **Authentication:** Django's built-in system
- **Deployment:** [bookshelf1.store](https://bookshelf1.store)

⚙️ Project Structure

```

bookshelf/
├── aujla/            # Django project settings
├── karanaujla/              # Core app: models, views, URLs
├── templates/            # HTML templates
├── static/               # CSS and images
├── db.sqlite3            # Database file
└── manage.py

````
 🧪 Local Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/gavish47/bookshelf.git
   cd bookshelf
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install the requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access locally** at [http://127.0.0.1:8000](http://127.0.0.1:8000)

 🔐 Admin Panel

To create a superuser:

```bash
python manage.py createsuperuser
```

Then log in at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🔗 API Endpoints

| Endpoint           | Method | Description              |
| ------------------ | ------ | ------------------------ |
| `/api/books/`      | GET    | List all books           |
| `/api/books/<id>/` | GET    | Retrieve a specific book |
| `/api/books/`      | POST   | Add a new book (auth)    |
| `/api/books/<id>/` | PUT    | Update a book (auth)     |
| `/api/books/<id>/` | DELETE | Delete a book (auth)     |

> For secure access, use token-based authentication with DRF.
 🌱 Future Enhancements

* Add search/filter functionality
* Book reviews and ratings
* Pagination and sorting
* User book library (My Books)
* Deployment on Render/Vercel with PostgreSQL

 👤 Author

**Gavish **
🎓 B.Tech CSE | 🔧 Full-Stack Developer
📧 [gavish4768@gmail.com](mailto:gavishwalia47@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/gavish27/)
🔗 [GitHub](https://github.com/gavish47)


