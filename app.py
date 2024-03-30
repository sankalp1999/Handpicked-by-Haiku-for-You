from flask import Flask, render_template, request
import anthropic
import os
import requests, json
app = Flask(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
SYSTEM_PROMPT = '''
Given your three favorite items (could be anything from movies, TV shows, books, anime or music artists to cuisine, city, country name, brand name):
1. {$ITEM1}
2. {$ITEM2}
3. {$ITEM3}

And the optional type of recommendations you want :
4. {$RECTYPE}

Create a visually appealing Mermaid flowchart diagram with the following elements:
- Use your 3 favorite items as the initial nodes in the flowchart, represented as stadium-shaped nodes ([]).
- Create additional nodes representing recommendations based on connections and similarities between your favorite items, such as:
  - Themes, genres, and styles
  - Directors, actors, authors, and artists
  - Tone, atmosphere, and creative elements
- Represent recommendation nodes as subroutine-shaped nodes {{}}.
- Use cylindrical nodes [()] for recommendations that combine elements from multiple favorite items.
- Draw curved arrows (===>) connecting the initial nodes to the relevant recommendation nodes.
- Make sure you recommend items you are sure about, do not give misinformation.
- Label each arrow briefly describing the connection (e.g., "Philosophical sci-fi", "Tarantino-esque dialogue", "Dystopian themes", "Jazz influences").
- Inside each recommendation node, include the titles of 1-3 specific items you would recommend based on that connection.
- The recommendation node should necessarily contain a title and not random descriptions.
- The recommendation should be of the type specified in {$RECTYPE}. If no type is specified, the recommendation can be any of movie, music, anime, or book wherever you find a connection.
- Format recommendation item titles as "Title<br> Year" while making SURE YOU DO NOT USE PARENTHESES in names. Simply Mention as Name Year.
- If a recommendation item title contains parentheses, replace them with underscores to avoid Mermaid syntax errors.
- Apply style classes to distinguish node types:
  - classDef favItem fill:#f9d, stroke:#333, stroke-width:2px;
  - classDef mainRec fill:#bfb, stroke:#333, stroke-width:2px;
- Attach the styles to the appropriate nodes, e.g., A:::favItem.
- Adjust the layout direction for different sections:
  - Favorite items flowing from left to right
  - Recommendations extending top to bottom from each favorite
  - Combined recommendations going from bottom to top
- Use meaningful variable names for nodes and format arrow labels with breaks and spacing.
- Organize and explain sections of the flowchart using comments %%.
- Double-check the Mermaid syntax for errors and parenthesis in title name.

Output the complete Mermaid flowchart diagram inside triple backticks using below example and make sure not include parentheses and any kind of quotes in the titles. Also no explanation is required.:

Example 1 (Movie recommendations):
```mermaid
graph LR
%% Favorite songs
A([Shape of You<br>Ed Sheeran]) ====> B([Show Me How<br>Men I Trust])
B ====> C([Perfect Girl<br>Mareux])

%% Movie recommendations
A ====> D{{La La Land<br>2016}}
D -.->|Romantic| E{{The Notebook<br>2004}}
B ====> F{{Lost in Translation<br>2003}}
F -.->|Quirky Indie| G{{Eternal Sunshine of the Spotless Mind<br>2004}}
C ====> H{{Drive<br>2011}}
H -.->|Retro Aesthetic| I{{Blade Runner 2049<br>2017}}

%% Combined recommendations
A & B ==> J[(500 Days of Summer<br>2009)]
B & C ==> K[(Her<br>2013)]

%% Styling
classDef favItem fill:#f9d, stroke:#333, stroke-width:2px;
classDef mainRec fill:#bfb, stroke:#333, stroke-width:2px;
A:::favItem; B:::favItem; C:::favItem;
D:::mainRec; F:::mainRec; H:::mainRec;
```

Example 2 (Book recommendations):
```mermaid
graph LR
%% Favorite songs
A([Shape of You<br>Ed Sheeran]) ====> B([Show Me How<br>Men I Trust])
B ====> C([Perfect Girl<br>Mareux])

%% Book recommendations
A ====> D{{The Rosie Project<br>Graeme Simsion}}
D -.->|Unconventional Romance| E{{Eleanor & Park<br>Rainbow Rowell}}
B ====> F{{Murakami<br>Norwegian Wood}}
F -.->|Introspective| G{{The Perks of Being a Wallflower<br>Stephen Chbosky}}
C ====> H{{Neuromancer<br>William Gibson}}
H -.->|Cyberpunk| I{{Snow Crash<br>Neal Stephenson}}

%% Combined recommendations
A & B ==> J[(The Unbearable Lightness of Being<br>Milan Kundera)]
B & C ==> K[(Do Androids Dream of Electric Sheep<br>Philip K. Dick)]

%% Styling
classDef favItem fill:#f9d, stroke:#333, stroke-width:2px;
classDef mainRec fill:#bfb, stroke:#333, stroke-width:2px;
A:::favItem; B:::favItem; C:::favItem;
D:::mainRec; F:::mainRec; H:::mainRec;
```

Example 3 (Food recommendations):
```mermaid
graph TD
%% Favorite items
A([McDonalds]) ====> B([Shape of You<br>Ed Sheeran])
B ====> C([Permutation City<br>Greg Egan])

%% Food recommendations
A ====> D{{Burger King}}
D -.->|Fast Food| E{{Wendys}}
E -.->|Chicken Sandwiches| F{{KFC}}
A ====> G{{Pizza Hut}}
G -.->|Italian-American| H{{Dominos Pizza}}
B ====> I{{Romantic Dinner<br>Spaghetti and Meatballs}}
I -.->|Intimate Dining| J{{Fondue for Two}}
J -.->|Interactive Cooking| K{{Korean BBQ}}
B ====> L{{Picnic in the Park<br>Charcuterie Board}}
L -.->|Al Fresco Dining| M{{Food Truck Festival}}
C ====> N{{Molecular Gastronomy<br>Alinea Restaurant}}
N -.->|Futuristic Cuisine| O{{Heston Blumenthals<br>The Fat Duck}}
O -.->|Experimental Dining| P{{elBulli<br>Ferran Adria}}
C ====> Q{{Themed Restaurant<br>Sci-Fi Dine-In Theater}}
Q -.->|Immersive Dining| R{{Ninja New York}}

%% Combined recommendations
A & B ==> S[(Candlelit Drive-Thru<br>In-N-Out Burger)]
S -.->|Elevated Fast Food| T[(Gourmet Food Truck<br>Kogi BBQ)]
B & C ==> U[(Sci-Fi Themed Cafe<br>Nebulon 42)]
U -.->|Futuristic Dining| V[(Virtual Reality Restaurant<br>Sublimotion)]
A & C ==> W[(3D Printed Food<br>Food Ink)]

%% Styling
classDef favItem fill:#f9d, stroke:#333, stroke-width:2px;
classDef mainRec fill:#bfb, stroke:#333, stroke-width:2px;
classDef combRec fill:#e0e0e0, stroke:#333, stroke-width:2px;
A:::favItem; B:::favItem; C:::favItem;
D:::mainRec; G:::mainRec; I:::mainRec; L:::mainRec; N:::mainRec; Q:::mainRec;
S:::combRec; U:::combRec; W:::combRec;
```


Example 4 (Title name contained parenthesis replaced by underscore)
```mermaid
graph LR

%% Favorite items
A([Filter Coffee]) ====> B([Dosa]) 
B ====> C([Idli])

%% Restaurant recommendations
A ====> D{{Brahmin's Coffee Bar}}
D -.->|South Indian Classics| E{{Vidyarthi Bhavan}}
E -.->|Iconic Dosa| F{{CTR _Chitra Refreshment House_}}
A ====> G{{Shri Sagar - CTR}}  
G -.->|Filter Coffee Connoisseur| H{{Cafe Madras}}
B ====> I{{Veena Stores}}
I -.->|Masala Dosa| J{{Shri Sagar - CTR}}
B ====> K{{Janatha Deluxe}}
K -.->|Fluffy Idli| L{{Vidyarthi Bhavan}}  
C ====> M{{Shri Sagar - CTR}}
M -.->|Authentic Idli| N{{Brahmin's Coffee Bar}}
C ====> O{{Vidyarthi Bhavan}}
O -.->|Comfort Food| P{{Janatha Deluxe}}

%% Combined recommendations
A & B ==> Q[(Koshy's)]
Q -.->|Quintessential Bangalore Eatery| R[(Mavalli Tiffin Rooms _MTR_)]
B & C ==> S[(Taaza Thindi)]
S -.->|Breakfast Delights| T[(Shri Sagar - CTR)]

%% Styling
classDef favItem fill:#f9d, stroke:#333, stroke-width:2px;
classDef mainRec fill:#bfb, stroke:#333, stroke-width:2px;
classDef combRec fill:#e0e0e0, stroke:#333, stroke-width:2px;
A:::favItem; B:::favItem; C:::favItem;
D:::mainRec; G:::mainRec; I:::mainRec; K:::mainRec; M:::mainRec; O:::mainRec; 
Q:::combRec; S:::combRec;
```

```

'''

print(API_KEY)

def replace_parentheses(string):
    return string.replace('(', '_').replace(')', '_')

# system="Given your three favorite movies:\n\n1. {$MOVIE1}\n\n2. {$MOVIE2}\n\n3. {$MOVIE3}\n\nCreate a Mermaid flowchart diagram with the following elements:\n\n- Use your 3 favorite movies as the initial nodes in the flowchart\n\n- Create additional nodes representing movie recommendations based on connections and similarities between your favorite movies, such as:\n\n-- Themes and genres\n\n-- Directors and actors\n\n-- Style, tone, and cinematography\n\n- Draw arrows connecting the initial movie nodes to the relevant recommendation nodes\n\n- Label each arrow briefly describing the connection (e.g., \"Philosophical sci-fi\", \"Tarantino-esque dialogue\")\n\n- Inside each recommendation node, include the titles of 1-3 specific movies you would recommend based on that connection\n\n- You can create recommendation nodes based on combinations of your initial favorite movies if you notice overarching connections between them\n\n- Use proper Mermaid syntax, with your favorite movies and recommendations represented as nodes\n\n- mention movie names as movie_name year\n\n- make graph aesthetic if you can\n\n- check syntax again\n\nOutput the complete Mermaid flowchart diagram inside triple backticks like this (note it is an example):\n\n```mermaid\n\ngraph TD\n\nA((Favorite Movies))\n\nA --> B{$MOVIE1}\n\nA --> C{$MOVIE2}\n\nA --> D{$MOVIE3}\n\nB --> E[Recommendation1]\n\nE --> E1[Movie Title]\n\nE --> E2[Movie Title]\n\nB --> F[Recommendation2]\n\nF --> F1[Movie Title]\n\nF --> F2[Movie Title]\n\nC --> G[Recommendation1]\n\nG --> G1[Movie Title]\n\nG --> G2[Movie Title]\n\nC --> H[Recommendation2]\n\nH --> H1[Movie Title]\n\nH --> H2[Movie Title]\n\nD --> I[Recommendation1]\n\nI --> I1[Movie Title]\n\nI --> I2[Movie Title]\n\nD --> J[Recommendation2]\n\nJ --> J1[Movie Title]\n\nJ --> J2[Movie Title]\n\nB --> K{Combined Recommendation}\n\nC --> K\n\nK --> K1[Movie Title]\n\nK --> K2[Movie Title]\n\nC --> L{Combined Recommendation}\n\nD --> L\n\nL --> L1[Movie Title]\n\nL --> L2[Movie Title]",
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        movie1 = replace_parentheses(request.form['movie1'])
        movie2 = replace_parentheses(request.form['movie2'])
        movie3 = replace_parentheses(request.form['movie3'])
        rectype = ''
        if 'rectype' in request.form:
          rectype = replace_parentheses(request.form['rectype'])

        # client = anthropic.Anthropic(api_key=API_KEY)

        # message = client.messages.create(
        #     model="claude-3-haiku-20240307",
        #     # model="claude-3-opus-20240229",
        #     max_tokens=1000,
        #     temperature=0,
            
        #     system = SYSTEM_PROMPT,
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": [
        #                 {
        #                     "type": "text",
        #                     "text": f"my favourite movies are {movie1}, {movie2} and {movie3}. I want recommendations for {rectype} \n"
        #                 }
        #             ]
        #         }
        #     ]
        # )

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "picked-by-haiku-for-you.onrender.com", # Optional, for including your app on openrouter.ai rankings.
                "X-Title": "Handpicked by Haiku", # Optional. Shows in rankings on openrouter.ai.
            },
            data=json.dumps({
                "model": "anthropic/claude-3-haiku", # Optional
                "messages": [
                {"role": "system", "content":  f"{SYSTEM_PROMPT}"},
                
                {"role": "user", "content": f"my favourite movies are {movie1}, {movie2} and {movie3}. I want recommendations for {rectype} \n"}
                ]
            })
            )

        # print(mermaid_code)
        # mermaid_code = mermaid_code.split("```mermaid")[1].split("```")[0].strip()
        # print(mermaid_code)


        response_json = json.loads(response.content)
        mermaid_code = response_json['choices'][0]['message']['content']
        print(mermaid_code)
        mermaid_code = mermaid_code.split("```mermaid")[1].split("```")[0].strip()
        # print(mermaid_code)
        return render_template('index.html', mermaid_code=mermaid_code)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()