# pyllm

pyllm minimizes the effort needed to use LLMs within classical python software. It abstracts away complexities related to schema declaration, parsing, and validation. The library lets you seamlessly integrate LLMs into your Python code with minimal boilerplate.

## Features

- Simple API for LLM interactions
- Schema validation with Pydantic
- Support for structured inputs and outputs
- Reusable function prototypes
- Type safety through Pydantic models and enums

## Installation

```bash
pip install pyllm
```

## Basic Usage

### Simple Text Generation

```python
from pyllm import llm

# Simple text generation
hello = llm("say hello in 10 different languages")
print(hello)
```

### Structured Output with Pydantic Models

```python
from pydantic import BaseModel
from pyllm import llm

class Anything(BaseModel):
    name: str
    description: str = None

class Attributes(BaseModel):
    short_description: str
    is_sentient: bool
    origin: str
    abilities: list[str]
    weaknesses: list[str]

# Get structured information about Batman
batman = llm(
    "Explain powers",
    INPUT=Anything(name="Batman"),
    OUTPUT=Attributes,
)
print(batman.short_description)
print(batman.abilities)
```

### Using Enums for Controlled Vocabularies

```python
import enum
from pydantic import BaseModel
from pyllm import llm

class Origin(str, enum.Enum):
    COMICS = "comics"
    REAL_LIFE = "real_life"
    OTHER = "other"

class Attributes(BaseModel):
    short_description: str
    is_sentient: bool
    origin: Origin  # Using enum for controlled values
    abilities: list[str]
    weaknesses: list[str]

superman = llm(
    "Explain powers",
    INPUT=Anything(name="Superman"),
    OUTPUT=Attributes,
)
print(superman.origin)  # Will be one of the enum values
```

### Creating Reusable Function Prototypes

```python
from pydantic import BaseModel
from pyllm import llm

class Outcome(BaseModel):
    would_win: bool
    reason: str
    short_story_what_happend: str
    long_story_what_happend: str

# Create a reusable function prototype
battle = llm(
    [
        "Suppose the CHALLENGER and the OPPONENT duel, which one would win",
        "short story should be under 50 words, long story should be under 200 words",
        "reason should analyze the abilities and weaknesses",
        "if CHALLENGER would win, set would_win to True, otherwise False",
    ],
    create_prototype=True,
    OUTPUT=Outcome,
)

# Use the prototype with different inputs
match1 = battle(
    CHALLENGER=superman,
    OPPONENT=batman,
)

# Another match with different participants
kryptonite = Anything(name="kryptonite", description="A ton of those green rocks")
match2 = battle(
    CHALLENGER=kryptonite,
    OPPONENT=superman,
)
```

## Next Steps

Future development will include:

- [ ] Support for multiple LLM service providers
- [ ] Performance benchmarking
- [ ] LLM Parallelization (Multi-agent)
- [ ] Chain of LLM