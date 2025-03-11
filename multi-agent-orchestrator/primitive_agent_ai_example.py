### With this current example
### The current form of python script shows a very primitive example of AI agent (no more than a google API call on message)
### A chat if it should interact with google calendar and create a date if the answer is "oui".
### It's a very primitive way of showing a AI agent
### We could guess that using tools like N8N could make it more powerful with evoluted agents which can interact with models output/input in a more advanced way
### and separated scripts dedicated for tooling instead of all in a script that our example is showing

from google_auth_oauthlib import flow as google_flow
from googleapiclient.discovery import build as google_build
from ollama.tokenizer import get_encoder
from typing import Dict, Any
import os

# Chargez le modèle localement
manager = ModelManager()
model = manager["mistral/mistral-base-multilingual"]
encoder = get_embeddings(model)

# Créez une chaîne de langage pour créer un rendez-vous sur Google Calendar
calendar_template = PromptTemplate.from_string("Assistant: J'ai pris en compte votre demande de rencontrer le {date} à {time}. Confirmé ?")
action_template = PromptTemplate.from_string("Assistant: Pour créer un rendez-vous, dois-je autoriser l'application Google Calendar ?")

def action(response: Dict[str, Any]) -> str:
    if response["confirm"] == "oui":
        # Récupérez les informations de connexion de l'utilisateur pour se connecter à Google Calendar
        flow = google_flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file="path/to/credentials.json", scopes=[CalendarScopes]
        )
        credentials = flow.run()

        # Créez un service Google Calendar avec les informations de connexion de l'utilisateur
        service = google_build(
            "calendar",
            credentials=credentials,
            discoveryServiceUrl="https://calendar.googleapis.com/discovery/v2/apis/calendar/v3/rest"
        )

        # Créez un nouveau rendez-vous avec les informations spécifiées par l'utilisateur
        event = {
            "summary": "Rendez-vous",
            "location": "Mon bureau",
            "description": "Nouveau rendez-vous",
            "start": {"dateTime": "2022-11-15T14:00:00"},
            "end": {"dateTime": "2022-11-15T15:00:00"}
        }

        # Créez l'événement dans le calendrier de l'utilisateur
        created_event = service.events().insert(calendarId="primary", body=event).execute()

        return "Rendez-vous créé avec succès"
    else:
        return "Rendez-vous pas créé"

# Créez une chaîne de langage pour l'assistant qui détermine si l'utilisateur veut créer un rendez-vous ou non
chain = LLMChain(llm=model, action=action, calendar_template=calendar_template, action_template=action_template)
