## 2025-05-04 — Flask API Calculator Rebuild

### What I built:
- Implemented `/calculate` route in Flask
- Uses `POST` method to accept JSON input: `{ "op": "add", "a": 3, "b": 4 }`
- Returns result with: `{ "result": 7 }`
- Function dispatch via `operations = { "add": lambda a,b: a+b, ... }`

### Concepts reinforced:
- `@app.route(..., methods=['POST'])` syntax
- `request.json` for POST payload extraction
- Function dispatch using a dict of lambdas
- Using `.get()` on a dictionary to avoid branching
- Understanding how `op_func(data['a'], data['b'])` works

### Reflection:
- Rebuilding without memorization pressure helped retention
- Avoided premature over-engineering (e.g. status codes, type checks)
- Recognized how early structure (if/elif) clarified the use of `lambda`
- Still unclear on how to *remember* vs how to *retrace*
- Felt fear of forgetting, but realized redoing small tasks is how to build fluency