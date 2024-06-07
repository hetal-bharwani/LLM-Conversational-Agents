# from config import *
# open_logs("concept_tasks")


# # README: This script uses one concept you want to investigate further.
# # Choose between "local" or "openai" mode in config.py

# concept = """**Concept 1: The Fluttering Leaf**
# This concept explores the integration of nature into indoor spaces to create a dynamic environment that responds to changes in temperature. 
# By incorporating living plants and green walls, the indoor space can adapt to thermal stimuli by absorbing or reflecting sunlight, providing shade or insulation as needed. 
# The greenery also has a positive impact on human health and well-being through its ability to purify the air, increase humidity, and reduce stress levels.
# tasks = """ 1. First, list out the names of all interior spaces in this building.
#             2. Second, explain how they are connected and one can move from space to space across the building.
#             3. Third, describe what a visitor will see and find inside each of the spaces."""  

# def question_concept(tasks: str, concept: str)-> str:
#     # client = OpenAI(api_key=OPENAI_API_KEY)
#     response = client.chat.completions.create(
#         model=completion_model,
#         messages=[
#             {
#                 "role": "system",
#                 "content": """ 
#                        You are a world renowed architect. You answer questions about building design concepts.""",
#             },
#             {
#                 "role": "user",
#                 "content": 
#                         f"""You are given a set of tasks and a brief summaries of a building design concept.
#                         Be imaginative and creative in your answers:
#                         #CONCEPTS#: {concept}
#                         #TASKS#: {tasks}
#                         """,
#             },
#         ],
#         #max_tokens=450,
#     )
#     return response.choices[0].message.content


# answer = question_concept(tasks, concept)
# print(answer)

# close_logs()

from config import *
open_logs("concept_tasks")

# README: This script uses one concept you want to investigate further.
# Choose between "local" or "openai" mode in config.py

concept = """**Concept 1: The Fluttering Leaf**
This concept explores the integration of nature into indoor spaces to create a dynamic environment that responds to changes in temperature. 
By incorporating living plants and green walls, the indoor space can adapt to thermal stimuli by absorbing or reflecting sunlight, providing shade or insulation as needed. 
The greenery also has a positive impact on human health and well-being through its ability to purify the air, increase humidity, and reduce stress levels."""

tasks = """ 
1. First, list out the names of all interior spaces in this building.
2. Second, explain how they are connected and one can move from space to space across the building.
3. Third, describe what a visitor will see and find inside each of the spaces.
"""  

def question_concept(tasks: str, concept: str) -> str:
    prompt = (
        "You are a world-renowned architect. You answer questions about building design concepts.\n\n"
        f"You are given a set of tasks and brief summaries of a building design concept.\n"
        f"Be imaginative and creative in your answers:\n"
        f"#CONCEPTS#: {concept}\n"
        f"#TASKS#: {tasks}\n"
    )
    response = client.completions.create(
        model=completion_model,
        prompt=prompt,
        max_tokens=450,
    )
    return response.choices[0].text.strip()

answer = question_concept(tasks, concept)
print(answer)

close_logs()

