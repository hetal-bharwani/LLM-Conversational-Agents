from config import *
open_logs("concept_q&a")


# README: This script can be used to generate 5 short concepts that respond to the context retrieved by the RAG agent on the knowledge pool.

# concepts = """**Concept 1: The Whispering Grove**
# In the heart of the bustling city, a tranquil haven unfolds - The Whispering Grove. 
# This brutalist edifice takes inspiration from the organic world, weaving together nature and urbanity in an harmonious dance. 
# Its facade, etched with intricate patterns reminiscent of tree bark, invites the curious passerby to explore its depths. 
# A labyrinth of concrete columns, resembling mighty trunks, support a canopy of glass leaves, filtering sunlight into the building's core. 
# Here, within the sanctuary, functional zones are neatly arranged like blossoms on branches, providing the necessary nourishment for productivity and creativity to thrive.

# **Concept 2: The Elemental Fortress**
# Embracing raw power and primal energy, the Elemental Fortress stands as a testament to human resilience against the natural forces. 
# Inspired by ancient castles, its walls are formed of rough-hewn stone, each block meticulously placed to form an impenetrable shield. 
# Concrete battlements jut out from its surface, representing the relentless tide that crashes upon the shore, while timber balconies protrude like jagged tree limbs against the wind. 
# The interior is a series of intimate, functional spaces, where warmth and comfort contrast the fortress's rugged exterior.

# **Concept 3: The Timeless Library**
# A cathedral for the mind, The Timeless Library, is a sanctuary devoted to the preservation and celebration of knowledge. 
# Its facade is a tapestry of stacked gabion walls, each one holding volumes of wisdom, carefully bound in raw concrete. 
# A series of bridges link the library's distinct zones, creating an intricate web of connections that invite exploration. 
# The library's heart beats with the steady rhythm of ticking clocks, while shafts of sunlight stream through tall windows, casting long shadows that dance and flicker across the shelves. 
# Here, time stands still, allowing visitors to become lost in the infinite labyrinth of knowledge."""

concepts = """**Concept 1: The Fluttering Leaf** 
This concept explores the integration of nature into indoor spaces to create a dynamic environment that responds to changes in temperature. 
By incorporating living plants and green walls, the indoor space can adapt to thermal stimuli by absorbing or reflecting sunlight, providing shade or insulation as needed. The greenery also has a positive impact on human health and well-being through its ability to purify the air, increase humidity, and reduce stress levels.
**Concept 2: The Thermal Harp** 
This concept focuses on using innovative materials and technologies to create a building that can actively adapt to thermal stimuli in real-time. 
By incorporating shape-shifting surfaces, smart windows, and thermal energy storage systems, the building can change its form and appearance to optimize indoor temperature and comfort levels. 
The design is inspired by the harp, which uses strings to create music in response to the musician's actions. 
In this case, the building's "strings" are the materials that can be manipulated to create a comfortable environment.
**Concept 3: The Elemental Pavilion**
This concept explores the use of traditional architectural techniques to create a building that is adaptable to thermal stimuli while also celebrating the beauty and essence of each element (water, earth, air, and fire). 
The pavilion's design incorporates natural materials such as stone, wood, and bamboo, which can regulate indoor temperature and humidity levels. 
The layout of the building is inspired by the principles of feng shui, a traditional Chinese practice that focuses on harmonizing with the natural world."""

questions = """ 1. What are the names of all interior spaces in this building?
                2. What is the most important aspect of the interior spaces in this building?
                3. What are the materials used for this building?"""    

# questions = """ 1. If you were a visitor, what would be the most striking aspect when you walk inside the building?
#                 2. If you were a photographer, what aspect of the building would you focus on for your photograhs?
#                 3. If you had to convince a guest to stay in the building, what aspect of the building would you focus on?""" 

# questions = """ 1. When a visitor walks into the main lobby, what does it see?
#                 2. What do the rooms look like?
#                 3. How would you describe what a visitor sees when he looks at the building from afar?"""  

def question_concept(questions: str, concepts: str)-> str:
    # client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """ 
                       You are a world renowed architect. You answer questions about building design concepts.
                       """,
            },
            {
                "role": "user",
                "content": f"""You are given a set of questions and brief summaries of building design concepts.
                Answer the questions for each of the concepts. Be imaginative and creative in your answers:
                #CONCEPTS#: {concepts}
                #QUESTION#: {questions}
                """,
            },
        ],
        max_tokens=450,
    )
    return response.choices[0].message.content


answer = question_concept(questions, concepts)
print(answer)


close_logs()