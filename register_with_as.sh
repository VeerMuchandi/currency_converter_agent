# export PROJECT_NUMBER="121968733869"
# export PROJECT_ID="agentspace-demo-1145-b"
# export AS_APP="neuravibeapp_1738849257936"

export PROJECT_NUMBER="977834784893"
export PROJECT_ID="spark-demo-1114"
export AS_APP="neuravibeenterprisesearch_1732204320742"

#REASONING_ENGINE="projects/121968733869/locations/us-central1/reasoningEngines/2893290081701855232"
export REASONING_ENGINE="projects/${PROJECT_ID}/locations/us-central1/reasoningEngines/4712040643717758976" #new name. We should do a list query to make sure it exists
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
    {
      "displayName": "Corporate Analyst",
      "vertexAiSdkAgentConnectionInfo": {
        "reasoningEngine": "projects/spark-demo-1114/locations/us-central1/reasoningEngines/1508714671262138368"
      },
      "toolDescription": "The agent can analyze a corporation given its ticker symbol and generates a report from SEC 10K report and other sources",
      "icon": {
        "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
      },
      "id": "corp_analyst_agent"
    },
    ]
  }'

    