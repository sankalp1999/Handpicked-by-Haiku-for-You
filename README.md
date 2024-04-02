# Handpicked by Haiku for You

You can try out Handpicked by Haiku for You at [https://handpicked-by-haiku-for-you.onrender.com/](https://handpicked-by-haiku-for-you.onrender.com/).


Handpicked by Haiku for You is a flask app that generates personalized recommendations and visualizations based on user input. It leverages the knowledge base of Claude Haiku to 
provide the recommendations based on the user's taste and then generate structured text output that can be rendered as diagrams.


The system prompt was made mainly via chatting with Claude Opus and using the [metaprompt notebook](https://colab.research.google.com/drive/1SoAajN8CBYTl79VyTwxtxncfCWlHlyy9).

The diagrams are rendered using [mermaid](https://mermaid.js.org/) and [markmap](https://markmap.js.org/)

See `app.py` for both the system prompts. (They are ugly)

See the files in `templates/` for the rendering code

Mermaid uses just a CDN to render. The trick for markmap is [here](https://markmap.js.org/api/modules/markmap_autoloader.html)

Markmap's benefit is very less syntax validation is required.


## Features

- **Personalized Recommendations**: Enter your favorite items (e.g., movies, books, songs) and get personalized recommendations in the form of a visually appealing Mermaid flowchart diagram
- **Markmap Visualizations**: Generate interactive and dynamic mindmaps based on your queries using the Markmap feature
- **Flexible Input**: Combine different types of items (e.g., books and songs) to get cross-domain recommendations.
- **Targeted Recommendations**: Specify the type of recommendations you're looking for (e.g., movies, restaurants) to get more focused results.
- **Download Options**: Easily download the generated Mermaid diagrams and Markmap visualizations as high-quality images.


## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/sankalp1999/Handpicked-by-Haiku-for-You.git
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