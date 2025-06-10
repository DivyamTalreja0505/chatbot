# Scholarship Guidance Chatbot

A multilingual scholarship guidance chatbot developed in collaboration with Hochschule Rhein-Waal (HSRW University). The chatbot leverages Rasa and GPT-3.5 to provide personalized, accurate, and context-aware support to students across various programs and countries.

---

## Features

- **Multilingual Support:** Assists students in multiple languages, ensuring accessibility for a diverse user base.  
- **Data-Driven Responses:** Utilized scraped and consolidated data from government and private scholarship websites to create a comprehensive, domain-specific dataset.  
- **Hybrid Response System:** Combines LLM-driven dynamic Q&A with rule-based flows to simplify complex application procedures.  
- **Iterative Improvement:** Conducted qualitative evaluations (accuracy, relevance, fallback success rate) and incorporated user feedback to enhance response quality.  
- **Scalable Deployment:** Deployed via a scalable backend with REST APIs for real-time access and seamless integration into existing student support systems.  
- **Enhanced User Trust:** Implemented prompt engineering, fallback strategies, and validation logic to improve response reliability and user engagement.  

---

## Technologies Used

- **Rasa:** Open-source conversational AI framework  
- **GPT-3.5:** Language model for dynamic, context-aware responses  
- **Python:** Backend development and data processing  
- **REST API:** Deployment and integration  
- **Web Scraping:** Data collection from scholarship websites  

---

## Collaboration & Development

- Partnered with **Hochschule Rhein-Waal (HSRW University)** to develop a tailored, multilingual chatbot.  
- Scraped and consolidated data from multiple sources to ensure accurate and relevant responses.  
- Integrated large language models with rule-based flows for a balanced, effective user experience.  
- Conducted continuous evaluation and improvement cycles based on user feedback and qualitative metrics.  
- Deployed the solution in a scalable environment for reliable, real-time support.  

---
## Deployment & How to Start

 1. **Install Dependencies**
Make sure you have Python installed. Then, install the required Python packages:
```bash
pip install rasa requests
```

2. **Run the Rasa Server**
In your terminal, start the Rasa server:
```bash
rasa run
```
3. **Run the Actions Server (if using custom actions)**
Open another terminal and start the actions server:
'''bash
rasa run actions
```
 4. **Test the Chatbot**
Use rasa shell to interact directly via command line:
'''bash
rasa shell
```
## How to Test the Chatbot

1. **Set Up the Environment:**  
   - Ensure the backend server hosting the Rasa chatbot and API is running.  
   - Verify that the custom actions server (if used) is active.

2. **Use a REST Client:**  
   - Tools like Postman or cURL can be used to send POST requests to your chatbot's API endpoint.  
   - Example cURL command:  
     ```bash
     curl -X POST -H "Content-Type: application/json" \
          -d '{"sender": "test_user", "message": "Hello"}' \
          http://localhost:5005/webhooks/rest/webhook
     ```

3. **Test Different Scenarios:**  
   - Greet the chatbot: "Hi", "Hello"  
   - Ask specific FAQs: "What is the application deadline?"  
   - Ask complex or unrecognized questions: "Tell me about the scholarship funding"  
   - Verify responses are accurate, relevant, and fallback triggers work correctly.

4. **Evaluate Responses:**  
   - Check if the chatbot responds appropriately based on the intent.  
   - Confirm that fallback responses invoke the GPT-3.5 API for unrecognized questions.

5. **Iterate and Improve:**  
   - Collect feedback from test users.  
   - Adjust intents, stories, or fallback strategies as needed.

---

## Contact & Support

For further information or collaboration opportunities, please contact:  
**Divyam Talreja**  
**Email:** Divyam.Manojkumar-Talreja@hsrw.org
**Organization:** Hochschule Rhein-Waal (HSRW University)  

---

*Note: Replace placeholder contact details with your actual information.*
