# Password Reset Application

This repository contains a simple password reset application implemented using Python and Flask.
It provides functionality for users to request a password reset and receive an email with instructions.

## Features

- User-friendly interface for requesting password resets
- Email notifications with reset instructions
- Template-based HTML emails

## Prerequisites

- Python 3.x
- Flask
- An SMTP server for sending emails

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rameshlinuxadmin/password_reset_app.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd password_reset_app
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up environment variables:**

   Create a `.env` file in the project root directory and add the following configurations:

   ```ini
   MAIL_SERVER=smtp.example.com
   MAIL_PORT=587
   MAIL_USERNAME=your_email@example.com
   MAIL_PASSWORD=your_email_password
   SECRET_KEY=your_secret_key
   ```

   - `MAIL_SERVER`: Your SMTP server address
   - `MAIL_PORT`: SMTP server port (e.g., 587 for TLS, 465 for SSL)
   - `MAIL_USERNAME`: Your email address used to send emails
   - `MAIL_PASSWORD`: Password for the email account
   - `SECRET_KEY`: A secret key for Flask session management

2. **Configure email templates:**

   The HTML templates for the application are located in the `templates` directory. Customize them as needed to match your application's branding and messaging.

## Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000`.

3. **Request a password reset:**

   Enter your email address in the provided form and submit. If the email is associated with an account, a password reset email will be sent.

## File Structure

- `app.py`: Main Flask application file handling routes and application logic.
- `password_reset_mail.py`: Module responsible for sending password reset emails.
- `templates/`: Directory containing HTML templates for the application.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
