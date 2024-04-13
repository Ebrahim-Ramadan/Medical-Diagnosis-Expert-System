# Expert System for Disease Diagnosis

## Overview

This project implements an expert system for diagnosing diseases based on symptoms provided by the user. The system categorizes diseases into different organ systems and prompts the user to indicate their symptoms. Using this information, the system applies a set of rules to identify the most probable disease(s) affecting the user.

## Workflow

1. **User Input**: The user selects the organ system they are experiencing symptoms in.
2. **Symptom Assessment**: The system prompts the user to confirm the presence or absence of specific symptoms associated with diseases in the chosen organ system.
3. **Diagnosis**: Based on the symptoms provided by the user, the system applies a set of rules to determine the most probable disease(s) affecting the user.
4. **Output**: The system displays the most probable disease(s) identified based on the user's symptoms.

## Logic

The expert system is implemented using the `experta` library in Python. It consists of a set of rules defined in the `knowledge` class. Here's an overview of the key components:

- **Initialization**: The `__init__` method initializes the knowledge engine with disease categories, symptoms, and user choice.
- **Rule Execution**: The `disease` rule is triggered when the user initiates the diagnosis process. It prompts the user to confirm symptoms and determines the most probable disease(s) based on the input.
- **Result Display**: Depending on the outcome, the system displays the most probable disease(s) identified using the `matched` and `matched_diseases` rules. If no disease is identified, the `not_matched` rule is triggered.

## Scaling with Experta

The project leverages the Experta library, which provides a powerful framework for building expert systems. Here's how Experta facilitates scalability:

- **Rule-Based Logic**: Experta allows the definition of rules in a clear and structured manner, making it easy to add, modify, or remove rules as needed.
- **Efficient Rule Evaluation**: Experta's inference engine efficiently evaluates rules to determine the most appropriate action based on the provided facts and rules.
- **Fact-Based Reasoning**: The system utilizes facts to represent user input and intermediate states during the diagnosis process. This allows for flexible reasoning and decision-making based on the available information.
- **Modularity and Extensibility**: Experta supports modular design, enabling the organization of rules into separate classes or modules based on functionality or domain. This makes it straightforward to scale the system by adding new rules or expanding existing ones.

---

Feel free to customize and expand upon this draft to better fit your project's specifics and requirements!
