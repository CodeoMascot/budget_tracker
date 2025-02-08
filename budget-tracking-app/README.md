# Budget Tracking Application

## Overview
The Budget Tracking Application is a web application designed to help users manage their finances by tracking expenses, creating budgets, and visualizing spending trends. The application allows users to set one-time and recurring budgets, categorize expenses, and generate reports to gain insights into their financial habits.

## Tech Stack
- **Frontend**: React (Next.js, TypeScript)
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: OAuth (Google, GitHub, or email-based login)
- **State Management**: React Query or Context API
- **Styling**: Tailwind CSS or Chakra UI
- **Deployment**: Docker, AWS/GCP with managed PostgreSQL database

## Core Features
- **User Authentication**: Sign up, login, and logout using OAuth or email.
- **Budget Management**:
  - Create one-time and recurring budgets.
  - Monthly recurring budgets auto-renew with leftover amounts carried forward.
  - Track budget usage.
- **Expense Tracking**:
  - Add, edit, and delete expenses.
  - Categorize expenses (food, shopping, travel, etc.).
  - Attach receipts (optional).
- **Reports & Insights**:
  - Monthly spending summary (budget vs actual).
  - Display trends over time with interactive charts.
- **User Dashboard**:
  - Overview of total budgets, expenses, and remaining balance.
  - Notifications for budgets nearing their limits.
- **Admin Panel (Future Scope)**:
  - Manage users and set global budget categories.

## Non-Functional Requirements
- **Performance**: Backend API should respond in under 200ms.
- **Security**: Use JWT-based authentication, enforce HTTPS, and prevent SQL injection.
- **Scalability**: Design APIs to handle multi-user access with efficient DB queries.

## Deliverables
- API documentation using Swagger or FastAPI's built-in OpenAPI.
- PostgreSQL schema design (tables: users, budgets, expenses, categories).
- CI/CD pipeline setup for automated deployment.

## Getting Started
1. Clone the repository.
2. Set up the backend and frontend environments.
3. Configure the database and environment variables.
4. Run the application using Docker Compose.

## Setup and Running the Project

### Prerequisites
- Node.js (v14 or higher)
- Python (v3.8 or higher)
- PostgreSQL
- Docker (optional, for containerized deployment)

### Backend Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/budget-tracking-app.git
    cd budget-tracking-app/backend
    ```
2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the PostgreSQL database and update the `DATABASE_URL` in the `.env` file.
5. Run the database migrations:
    ```sh
    alembic upgrade head
    ```
6. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```sh
    cd ../frontend
    ```
2. Install the dependencies:
    ```sh
    npm install
    ```
3. Create a `.env.local` file and add the necessary environment variables.
4. Start the Next.js development server:
    ```sh
    npm run dev
    ```

### Running with Docker
1. Ensure Docker is installed and running.
2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

The application should now be running and accessible at `http://localhost:3000` for the frontend and `http://localhost:8000` for the backend.

## License
This project is licensed under the MIT License.