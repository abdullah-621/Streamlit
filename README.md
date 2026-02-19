1. python -m venv myenv -> Virtual Environment Create

2. myenv\Scripts\activate -> Environment Activate

3. pip install streamlit -> Streamlit Install



🧠 Real Life Example

আগে তুমি করতা:

python -m venv myenv
myenv\Scripts\activate
pip install fastapi
pip install uvicorn


এখন uv দিয়ে:

uv venv
uv pip install fastapi uvicorn
uv run uvicorn main:app --reload