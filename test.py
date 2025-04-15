import vertexai
import json
from vertexai.preview import reasoning_engines

PROJECT_ID="agentspace-demo-1145-b"
#PROJECT_ID = "spark-demo-1114"
LOCATION = "us-central1"
vertexai.init(
      project=PROJECT_ID,
      location=LOCATION,
      # api_endpoint="us-central1-aiplatform.googleapis.com",
  )
engines = reasoning_engines.ReasoningEngine.list(filter='display_name="Currency Analyst"')

if not engines:
    print("Reasoning engine for currency Analyst missing")
    exit

print ("Reasoning engine: " + engines[0].resource_name)

engine = reasoning_engines.ReasoningEngine(engines[0].resource_name)


#session = engine.create_session(session_id="session1")

sessions_data = engine.list_sessions(user_id="user1")
print (sessions_data)


# Check if the response is a string and if so, attempt to parse as JSON
if isinstance(sessions_data, str):
  try:
    sessions_data = json.loads(sessions_data)
  except json.JSONDecodeError as e:
      print(f"Error decoding JSON: {e}")
      print(f"Received string: {sessions_data}")
      #Handle the error case. maybe return or exit
      exit()
      

# Now check if it's a dictionary with a 'session_ids' key
if isinstance(sessions_data, dict) and 'session_ids' in sessions_data:
    session_ids = sessions_data['session_ids']
    if not session_ids:  # Check if the list is empty
        print("Creating new session")
        session = engine.create_session(user_id="user1")
        
    else:
        print(f"Existing sessions found: {session_ids}")
        session = engine.get_session(user_id="user1", session_id=session_ids[0])
else:
    print(
        "Unexpected format for session data. Expected a dictionary with a 'session_ids' key."
    )
    print(f"Received: {sessions_data}")
    # Handle the error case. maybe return or exit
    exit()

from google.genai import types
for event in engine.stream_query(
    user_id="user1",
    session_id=session["id"],
    message="what was the conversion rate between usd and inr on 21st march 2025"):
    print(event)


agent_context = '{"message":{"role":"user","parts":[{"text":"How were you built?"}]},"events":[{"content":{"role":"user","parts":[{"text":"how were you built ?"}]},"author":"AgentSpace_root_agent"},{"content":{"role":"model","parts":[{"functionCall":{"name":"agentspaceak","args":{"question":"How were you built?"},"id":"14076651604820872102"}}]},"invocation_id":"14076651604820871801","author":"AgentSpace_root_agent","id":"14076651604820872102"}]}'

for response in engine.streaming_agent_run_with_events(request_json=agent_context):
    print(response)

