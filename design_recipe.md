# Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

```
 ┌───────────────────────────────────────────────┐  ┌───────────────────┐
 │Diary:                                         │  │ToDoList:          │
 │                                               │  │                   │
 │diary_entries (attribute)                      │  │todos (attribute)  │
 │                                               │  │                   │
 │def add_entry(self, entry)                     │  │def add(self, todo)│
 │def list_entries(self)                         │  └───────────────────┘
 │def select_best_entry_for_time(self, wpm, mins)│           │           
 │def list_mobile_numbers(self)                  │           │           
 └─────────────┬─────────────────────────────────┘  ┌────────▼───────┐   
               │                                    │ToDo:           │   
               │                                    │                │   
 ┌─────────────▼──────────────────┐                 │todo (attribute)│   
 │DiaryEntry:                     │                 └────────────────┘   
 │                                │                                      
 │entry (attribute)               │                                      
 │mobile_numbers (attribute)      │                                      
 │                                │                                      
 │def extract_mobile_numbers(self)│                                      
 └────────────────────────────────┘                                      
```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   diary_entries: list of instances of diary_entry

    def __init__(self):
        pass

    def add_entry(self, entry):
        # Parameters:
        #   entry: an instance of diary_entry
        # Side-effects:
        #   Adds the diary entry to the diary_entries property
        pass

    def list_entries(self):
        # Returns:
        #   diary_entries
        pass

    def select_best_entry_for_time(self, wpm, mins):
        # Parameters:
        #   wpm: integer representing reading speed
        #   mins: integer representing available minutes
        # Returns:
        #   diary_entry entry with closest word count below wpm * mins
        pass

    def list_mobile_numbers(self):
        # Returns:
        #   list of mobile numbers extracted from all diary entries
        pass

class DiaryEntry:
    # User-facing properties:
    #   entry: string
    #   mobile_numbers: list of strings

    def __init__(self, entry):
        # Parameters:
        #   entry: string
        # Side-effects:
        #   Sets the entry property
        pass

    def extract_mobile_numbers(self):
        # Returns:
        #   A list of mobile numbers extracted from the entry
        pass

class ToDoList:
    # User-facing properties:
    #   todos: list of instances of ToDo

    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: instance of ToDo
        # Side-effects:
        #   adds ToDo instance to the todos property
        pass

class ToDo:
    #User-facing properties:
    #   todo: string
        def __init__(self, todo)
        # Parameters:
        #   todo: string
        # Side-effects:
        #   sets the todo property
        pass
```