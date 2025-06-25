# Wellness Landing Page - Replit Guide

## Overview

This is a Flask-based wellness landing page focused on spiritual services related to the Holy Land. The application is a single-page website with a contact form for users interested in prayer services at the Stone of Anointing in Jerusalem. The site is built with Flask backend, Bootstrap frontend, and includes form validation and responsive design.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Entry Point**: `main.py` serves as the WSGI entry point
- **Application Logic**: `app.py` contains the main Flask application
- **Form Handling**: Flask-WTF with WTForms for form validation
- **Session Management**: Flask's built-in session handling with secret key

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **CSS Framework**: Bootstrap 5.3.0 via CDN
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Playfair Display and Inter)
- **JavaScript**: Vanilla JavaScript for smooth scrolling and animations
- **Responsive Design**: Mobile-first approach with Bootstrap grid system

### Development Environment
- **Python Version**: 3.11
- **Package Manager**: UV (modern Python package manager)
- **Deployment**: Gunicorn WSGI server
- **Platform**: Replit with Nix environment

## Key Components

### Application Structure
```
/
├── app.py              # Main Flask application
├── main.py            # WSGI entry point
├── forms.py           # Form definitions (duplicate of app.py forms)
├── templates/
│   └── index.html     # Main page template
├── static/
│   ├── css/
│   │   └── style.css  # Custom styles
│   └── js/
│       └── main.js    # Frontend interactions
└── pyproject.toml     # Python dependencies
```

### Form Handling
- **ContactForm**: Handles user inquiries with fields for name, email, phone, and message
- **Validation**: Server-side validation with Russian language error messages
- **Security**: CSRF protection via Flask-WTF
- **User Feedback**: Flash messages for form submission confirmation

### Styling and UI
- **Design System**: Custom CSS variables for consistent theming
- **Color Scheme**: Blue primary (#4A90E2), green secondary (#7BC142), orange accent (#F5A623)
- **Typography**: Serif headings (Playfair Display) and sans-serif body text (Inter)
- **Animations**: CSS transitions and JavaScript scroll animations
- **Navigation**: Fixed header with smooth scrolling to sections

## Data Flow

1. **User Request**: User accesses the landing page
2. **Template Rendering**: Flask renders `index.html` with ContactForm instance
3. **Form Submission**: User submits contact form via POST request
4. **Validation**: Flask-WTF validates form data server-side
5. **Success Response**: Flash message displayed and user redirected to prevent resubmission
6. **Error Handling**: Validation errors displayed inline with form fields

## External Dependencies

### Python Packages
- **flask**: Web framework
- **flask-wtf**: Form handling and CSRF protection
- **wtforms**: Form validation
- **email-validator**: Email validation
- **flask-sqlalchemy**: Database ORM (included but not currently used)
- **psycopg2-binary**: PostgreSQL adapter (included but not currently used)
- **gunicorn**: Production WSGI server

### Frontend Dependencies (CDN)
- **Bootstrap 5.3.0**: CSS framework
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts**: Playfair Display and Inter fonts

### Development Dependencies
- **OpenSSL**: Security library
- **PostgreSQL**: Database system (configured but not used)

## Deployment Strategy

### Production Configuration
- **Server**: Gunicorn WSGI server
- **Binding**: 0.0.0.0:5000 (all interfaces)
- **Scaling**: Autoscale deployment target
- **Process Management**: Replit workflows for development and production

### Environment Configuration
- **Session Secret**: Environment variable `SESSION_SECRET` with fallback
- **Debug Mode**: Enabled in development, should be disabled in production
- **Logging**: Basic logging configuration for debugging

### Development Workflow
- **Run Command**: Gunicorn with reload for development
- **Port Waiting**: Configured to wait for port 5000
- **Parallel Execution**: Workflow supports parallel task execution

## Changelog

```
Changelog:
- June 25, 2025. Initial setup
- June 25, 2025. Added email notification system for contact form submissions
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

## Notes for Code Agent

- The application currently has database dependencies (SQLAlchemy, PostgreSQL) configured but not implemented
- Forms are defined in both `app.py` and `forms.py` (duplication that could be cleaned up)
- No actual form processing is implemented - submissions just show a success message
- The site content is in Russian, targeting Russian-speaking users interested in spiritual services
- CSS uses modern features like CSS custom properties and backdrop-filter
- JavaScript includes intersection observer for scroll animations
- The application is ready for database integration if needed for storing contact form submissions