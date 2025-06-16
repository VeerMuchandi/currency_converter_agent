# export PROJECT_NUMBER="121968733869"
# export PROJECT_ID="agentspace-demo-1145-b"
# export AS_APP="neuravibeapp_1738849257936"

export PROJECT_NUMBER="512193404802"
export PROJECT_ID="google.com:solution-store"
export AS_APP="googlesalesagentspaceapp_1744915757093"
export REASONING_ENGINE_ID="2935300221975920640"

#REASONING_ENGINE="projects/121968733869/locations/us-central1/reasoningEngines/2893290081701855232"
export REASONING_ENGINE="projects/${PROJECT_NUMBER}/locations/us-central1/reasoningEngines/${REASONING_ENGINE_ID}" #new name. We should do a list query to make sure it exists
export AGENT_DISPLAY_NAME="Currency Converter"
export AGENT_DESCRIPTION="This agent can convert currency from one to another given the currencies, amount and the date"
export AGENT_ID="currency_converter_agent"

echo "REASONING_ENGINE: $REASONING_ENGINE"
echo "PROJECT_NUMBER: $PROJECT_NUMBER"
echo "PROJECT_ID: $PROJECT_ID"

curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "x-goog-user-project: ${PROJECT_ID}" \
https://discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${AS_APP}/assistants/default_assistant?updateMask=agent_configs -d '{
    "name": "projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${AS_APP}/assistants/default_assistant",
    "displayName": "Default Assistant",
    "agentConfigs": [{
      "displayName": "'"${AGENT_DISPLAY_NAME}"'",
      "vertexAiSdkAgentConnectionInfo": {
        "reasoningEngine": "'"${REASONING_ENGINE}"'"
      },
      "toolDescription": "'"${AGENT_DESCRIPTION}"'",
      "icon": {
        "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
      },
      "id": "'"${AGENT_ID}"'"
    },
    ]
  }'

    