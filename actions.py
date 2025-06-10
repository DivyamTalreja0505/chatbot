import os
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionCallAIAPI(Action):
    def name(self) -> Text:
        return "action_call_ai_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        user_message = tracker.latest_message.get('text')
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            dispatcher.utter_message(text="Sorry, I can't process your request right now.")
            return []
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-3.5-turbo",  # or "gpt-4"
            "messages": [{"role": "user", "content": user_message}],
            "max_tokens": 150
        }

        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
        else:
            reply = "Sorry, I couldn't process your request at the moment."

        dispatcher.utter_message(text=reply)
        return []
