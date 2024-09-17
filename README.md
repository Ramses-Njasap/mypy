# CSRF Token Case Sensitivity Test

## Overview

To address the issue where mypy complains of type errors.

mypy is a static type checker for Python. It ensures that your code adheres to type hints you provide. If mypy is complaining, it likely means that the type information is not clear, or it doesn't align with the expected type.

## Installation

### Prerequisites

- Python 3.x
- Django

### Setting Up the Django Backend

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/Ramses-Njasap/mypy.git
   cd mypy
   ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
    On windows

    ```bash
    venv\Scripts\activate
    ```

    On MacOs/Linux

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies**
    ```bash
    pip3 install -r requirements.txt
    ```

5. **Start the Django Development Server**
    ```bash
    python3 manage.py runserver
    ```

    This runs on PORT 8000, if using a different port change the PORT in the html file as well