# Handpicked by Haiku for You

You can try out Handpicked by Haiku for You at [https://handpicked-by-haiku-for-you.onrender.com/](https://handpicked-by-haiku-for-you.onrender.com/).


Handpicked by Haiku for You is a 2 page flask app that generates personalized recommendations and visualizations based on user input. It leverages the knowledge base of Claude Haiku to create engaging and informative content tailored to the user's preferences.

I structure the outputs by providing with few shot examples in the system prompt. 

I made the prompt mainly via chatting with Claude Opus and using the [metaprompt notebook](https://colab.research.google.com/drive/1SoAajN8CBYTl79VyTwxtxncfCWlHlyy9).

The diagrams are rendered using [mermaid](https://mermaid.js.org/) and [markmap](https://markmap.js.org/)

## Features

- **Personalized Recommendations**: Enter your favorite items (e.g., movies, books, songs) and get personalized recommendations in the form of a visually appealing Mermaid flowchart diagram
- **Markmap Visualizations**: Generate interactive and dynamic mindmaps based on your queries using the Markmap feature
- **Flexible Input**: Combine different types of items (e.g., books and songs) to get cross-domain recommendations.
- **Targeted Recommendations**: Specify the type of recommendations you're looking for (e.g., movies, restaurants) to get more focused results.
- **Download Options**: Easily download the generated Mermaid diagrams and Markmap visualizations as high-quality images.


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



## License

This project is licensed under the [MIT License](LICENSE).