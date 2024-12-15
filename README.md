# SkillSync Project

**SkillSync** is a collaborative learning platform designed to enhance team productivity and streamline communication. It combines group management, real-time discussion boards, task tracking, and resource sharing to create an intuitive and efficient platform for collaborative work.

## **Features**

### 1. **Group Management**

- Create, join, and manage groups.
- View and edit group details.
- Manage group members with roles and permissions.

### 2. **Real-Time Discussion Boards**

- Real-time messaging with WebSocket support.
- Threaded discussions for better organization.
- Reactions and attachments in messages.

### 3. **Task Tracking**

- Assign and manage tasks with deadlines and priority levels.
- View tasks in a Kanban board format.
- Track task completion and progress.

### 4. **Resource Sharing**

- Upload and share documents, links, and other resources.
- Categorize and organize shared resources for easy access.

## **Technology Stack**

### **Backend**

- **Django**: For building RESTful APIs.
- **Django Channels**: For real-time WebSocket communication.
- **PostgreSQL**: As the primary database.
- **Redis**: For caching and real-time data.

### **Frontend**

- **React.js**: For building a responsive and dynamic user interface.
- **React-Bootstrap**: For pre-styled components.

### **Deployment**

- **Azure App Service**: For hosting the web application.
- **Azure Blob Storage**: For storing uploaded files.
- **Docker**: For containerizing the application.

## **Setup Instructions**

### **Prerequisites**

- Python 3.10+
- Node.js 22+
- PostgreSQL
- Docker (optional for deployment)

### **Backend Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/skillsync.git
   cd skillsync/backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the backend server:
   ```bash
   python manage.py runserver
   ```

### **Frontend Setup**

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

### **Running with Docker**

1. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

## **Usage**

1. Access the platform at ` http://localhost:5173` (Frontend).
2. Backend APIs run at `http://localhost:8000`.

## **Contributing**

We welcome contributions! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add your message here"
   git push origin feature-name
   ```
4. Open a pull request.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.
