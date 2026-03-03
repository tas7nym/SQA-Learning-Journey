# SQA-Learning-Journey

A hands-on introduction to **Software Quality Assurance (SQA)** — from core concepts to practical testing with Python.

---

## 📚 What is SQA?

Software Quality Assurance (SQA) is a set of activities that ensures software products and processes meet defined quality standards throughout the software development lifecycle (SDLC). SQA focuses on:

- **Preventing defects** rather than just finding them
- Establishing and following **processes and standards**
- **Verifying** (are we building the product right?) and **validating** (are we building the right product?)

---

## 🗺️ Learning Roadmap

### 1. Core Concepts
- [ ] Types of testing: Unit, Integration, System, Acceptance
- [ ] White-box vs Black-box testing
- [ ] Static vs Dynamic testing
- [ ] Test-Driven Development (TDD)

### 2. Practical Skills
- [ ] Writing unit tests with `pytest`
- [ ] Measuring code coverage
- [ ] Mocking dependencies
- [ ] Continuous Integration (CI) basics

### 3. Advanced Topics
- [ ] Performance testing
- [ ] Security testing basics
- [ ] Test automation frameworks
- [ ] Behaviour-Driven Development (BDD)

---

## 🏁 Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

```bash
pip install -r requirements.txt
```

### Running the Tests

```bash
pytest tests/ -v
```

To see a coverage report:

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

---

## 📁 Repository Structure

```
SQA-Learning-Journey/
├── src/
│   └── calculator.py        # Example module under test
├── tests/
│   └── test_calculator.py   # Unit tests demonstrating SQA practices
├── requirements.txt
└── README.md
```

---

## 🔑 Key SQA Principles

| Principle | Description |
|-----------|-------------|
| **Testing shows presence of bugs** | Tests can prove bugs exist, but not that software is bug-free |
| **Exhaustive testing is impossible** | Prioritise based on risk and importance |
| **Early testing saves money** | Bugs found early cost far less to fix |
| **Defect clustering** | A small number of modules contain most defects |
| **Pesticide paradox** | Repeating the same tests finds no new bugs — keep evolving your test suite |
| **Testing is context-dependent** | Different products need different testing approaches |
| **Absence-of-errors fallacy** | A bug-free system can still fail to meet user needs |

---

## 💡 Example: Unit Testing a Calculator

The `src/calculator.py` module is a deliberately simple example you can use to practise writing tests. Explore `tests/test_calculator.py` to see:

- Basic assertions
- Testing edge cases (e.g. division by zero)
- Parameterised tests with `pytest.mark.parametrize`
- How test naming communicates intent

---

## 📖 Further Reading

- [ISTQB Foundation Level Syllabus](https://www.istqb.org/certifications/certified-tester-foundation-level)
- [pytest documentation](https://docs.pytest.org/)
- [Google Testing Blog](https://testing.googleblog.com/)
- [The Art of Software Testing – Glenford Myers](https://www.wiley.com/en-us/The+Art+of+Software+Testing%2C+3rd+Edition-p-9781118031964)
