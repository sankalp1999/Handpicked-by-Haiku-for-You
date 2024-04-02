# Handpicked by Haiku for You

Handpicked by Haiku for You is a web application that generates personalized recommendations and visualizations based on user input. It leverages the power of AI to create engaging and informative content tailored to the user's preferences.

## Features

- **Personalized Recommendations**: Enter your favorite items (e.g., movies, books, songs) and get personalized recommendations in the form of a visually appealing Mermaid flowchart diagram.
- **Markmap Visualizations**: Generate interactive and dynamic mindmaps based on your queries using the Markmap feature.
- **Flexible Input**: Combine different types of items (e.g., books and songs) to get cross-domain recommendations.
- **Targeted Recommendations**: Specify the type of recommendations you're looking for (e.g., movies, restaurants) to get more focused results.
- **Download Options**: Easily download the generated Mermaid diagrams and Markmap visualizations as high-quality images.

## Live Demo

Check out the live demo of Handpicked by Haiku for You at [https://handpicked-by-haiku-for-you.onrender.com/](https://handpicked-by-haiku-for-you.onrender.com/).

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Handpicked-by-Haiku-for-You.git
   cd Handpicked-by-Haiku-for-You
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set the required environment variables:
   - `OPENROUTER_API_KEY`: Your OpenRouter API key.
6. Run the Flask development server:
   ```
   flask run
   ```

7. Access the application in your web browser at `http://localhost:5000`.

## Deployment

To deploy the application using Gunicorn for a concurrent server:

1. Install Gunicorn:
   ```
   pip install gunicorn
   ```

2. Run the application using Gunicorn:
   ```
   gunicorn app:app
   ```



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).