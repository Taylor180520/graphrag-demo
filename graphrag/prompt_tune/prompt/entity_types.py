# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity types generation."""

ENTITY_TYPE_GENERATION_PROMPT = """
The goal is to study the connections and relations between the entity types and their features in order to understand all available information from the text.
The user's task is to {task}.
As part of the analysis, you want to identify the entity types present in the following text.
The entity types must be relevant to the user task.
Avoid general entity types such as "other" or "unknown".
This is VERY IMPORTANT: Do not generate redundant or overlapping entity types. For example, if the text contains "company" and "organization" entity types, you should return only one of them.
Don't worry about quantity, always choose quality over quantity. And make sure EVERYTHING in your answer is relevant to the context of entity extraction.
And remember, it is ENTITY TYPES what we need.
Return the entity types in as a list of comma sepparated of strings.
=====================================================================
EXAMPLE SECTION: The following section includes example output. These examples **must be excluded from your answer**.

EXAMPLE 1
Task: Understand and interpret the methodology and learn its formula.
Text: Sensitivity analysis calculates how responsive a decision is to changes in any of the variables used in making that decision. It looks at one variable at a time and measures how much the variable can change by (in percentage terms) before affecting the decision. The smaller the percentage, the more sensitive the decision is to that variable. Sensitivity % = Profit + Variable. 
RESPONSE:
methodologies, formulas
END OF EXAMPLE 1

EXAMPLE 2
Task: Identify the quiz's question and its corresponding answer, the key concepts, formulas, methodologies, and examples shared in the educational content.
Text: Quiz: Calculate the net present value (NPV) using the provided formula. Example: The formula for NPV considers the time value of money.
RESPONSE:
quizzes, formulas, examples
END OF EXAMPLE 2

EXAMPLE 3
Task: Identify the key concepts, methodologies, features, examples and quizzes related to the chapter.
Text: Chapter 8 discusses about decision-making under risk and uncertainty, including the concept of expected value and the methodology of sensitivity analysis, and their advantages and limitations.
RESPONSE:
concepts, methodologies, features
END OF EXAMPLE 3
======================================================================

======================================================================
REAL DATA: The following section is the real data. You should use only this real data to prepare your answer. Generate Entity Types only.
Task: {task}
Text: {input_text}
RESPONSE:
{{<entity_types>}}
"""

ENTITY_TYPE_GENERATION_JSON_PROMPT = """
The goal is to study the connections and relations between the entity types and their features in order to understand all available information from the text.
The user's task is to {task}.
As part of the analysis, you want to identify the entity types present in the following text.
The entity types must be relevant to the user task.
Avoid general entity types such as "other" or "unknown".
This is VERY IMPORTANT: Do not generate redundant or overlapping entity types. For example, if the text contains "company" and "organization" entity types, you should return only one of them.
Don't worry about quantity, always choose quality over quantity. And make sure EVERYTHING in your answer is relevant to the context of entity extraction.
Return the entity types in JSON format with "entities" as the key and the entity types as an array of strings.
=====================================================================
EXAMPLE SECTION: The following section includes example output. These examples **must be excluded from your answer**.

EXAMPLE 1
Task: Understand and interpret the methodology and learn its formula.
Text: Sensitivity analysis calculates how responsive a decision is to changes in any of the variables used in making that decision. It looks at one variable at a time and measures how much the variable can change by (in percentage terms) before affecting the decision. The smaller the percentage, the more sensitive the decision is to that variable. Sensitivity % = Profit + Variable. 
JSON RESPONSE:
{{"entity_types": [methodologies, formulas] }}
END OF EXAMPLE 1

EXAMPLE 2
Task: Identify the quiz's question and its corresponding answer, the key concepts, formulas, methodologies, and examples shared in the educational content.
Text: Quiz: Calculate the net present value (NPV) using the provided formula. Example: The formula for NPV considers the time value of money.
JSON RESPONSE:
{{"entity_types": [quizzes, formulas, examples] }}
END OF EXAMPLE 2

EXAMPLE 3
Task: Identify the key concepts, methodologies, features, examples and quizzes related to the chapter.
Text: Chapter 8 discusses about decision-making under risk and uncertainty, including the concept of expected value and the methodology of sensitivity analysis, and their advantages and limitations.
JSON RESPONSE:
{{"entity_types": [concepts, methodologies, features] }}
END OF EXAMPLE 3
======================================================================

======================================================================
REAL DATA: The following section is the real data. You should use only this real data to prepare your answer. Generate Entity Types only.
Task: {task}
Text: {input_text}
JSON response:
{{"entity_types": [<entity_types>] }}
"""
