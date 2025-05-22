# 🗓️🤖 Daily Task Automator with OpenAI GPT-4o-mini

This is a lightweight tool that reads a list of tasks from a `.txt` file, sends them to OpenAI's GPT-4o-mini model, and receives an analysis that includes:

- ✅ Task description  
- 📊 Task complexity  
- ⏱️ Estimated time to complete each task  

The generated response is printed to the console and saved to `tasks_response.txt` for future reference.

---

## 🚀 Features

- Upload your own `.txt` file with tasks
- Automatically analyze tasks using a powerful LLM
- Clear, concise, and structured output
- Easily customizable and extendable

---

## 🧩 Example Workflow

1. **Upload a `tasks.txt` file**  
   (e.g., contains a list like: `Write report`, `Clean dataset`, `Deploy app`)
2. **Run the script**
3. **Receive analysis**  
   Example output:
   ```
   - Task: Write a report
     Draft: ...
     Complexity: Medium
     Time Estimate: 2 hours

   - Task: Clean dataset
     Describe: ...
     Complexity: High
     Time Estimate: 3 hours
   ```

---

## 📁 Project Structure

```
├── tasks.txt                # Your input task file
├── tasks_response.txt       # Output file with LLM's analysis
├── main.py                  # Main script to upload and process tasks
├── helper_functions.py      # Contains OpenAI interaction functions
├── .env                     # File with your OpenAI API key
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-analyzer.git
cd task-analyzer
```

### 2. Install dependencies

```bash
pip install openai python-dotenv
```

### 3. Create a `.env` file

In the project root directory, add your OpenAI API key to a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Prepare your task list

Create a `tasks.txt` file with one task per line.

### 5. Run the script

```bash
python main.py
```

---

## 🧠 Powered By

- [OpenAI GPT-4o-mini](https://platform.openai.com/)
- Python 3.8+
- `openai`, `dotenv` libraries

---

## 🙌 Contributing

Feel free to fork the repo, suggest improvements, or submit pull requests!

---

## ✨ Future Improvements

- Web UI using Streamlit  
- Support for multiple file formats (.csv, .docx)  
- Prioritization and scheduling of tasks  
