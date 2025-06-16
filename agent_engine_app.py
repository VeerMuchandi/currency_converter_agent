import vertexai
import os
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp
from dotenv import load_dotenv
from agent import root_agent



def deploy_agent_engine_app():
    load_dotenv(override=True) 

    GOOGLE_CLOUD_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
    GOOGLE_CLOUD_LOCATION = os.environ["GOOGLE_CLOUD_LOCATION"]

    STAGING_BUCKET = f"gs://{GOOGLE_CLOUD_PROJECT}-agent-engine-deploy"
    AGENT_DISPLAY_NAME="Currency Analyst"
    


    vertexai.init(
        project=GOOGLE_CLOUD_PROJECT,
        location=GOOGLE_CLOUD_LOCATION,
        staging_bucket=STAGING_BUCKET,
    )

    app = AdkApp(
        agent=root_agent,
        enable_tracing=True,
    )

    #app.register_operations()

    with open('requirements.txt', 'r') as file:
        reqs = file.read().splitlines()

    agent_config =  {
        "agent_engine" : app,
        "display_name" : AGENT_DISPLAY_NAME,
        "requirements" : reqs+[
            "google-cloud-aiplatform[agent_engines,adk]",
        ],
        "extra_packages" : [
            "agent.py",
            "currencytool.py"
        ],
    }

    existing_agents=list(agent_engines.list(filter='display_name="Currency Analyst"'))

    if existing_agents:
         print(f"Number of existing agents found for {AGENT_DISPLAY_NAME}:" + str(len(list(existing_agents))))
    #     print(existing_agents[0].resource_name)
    #     print(existing_agents[1].resource_name)
        

    if existing_agents:
      #update the existing agent
      remote_app = existing_agents[0].update(**agent_config)
    else:
      #create a new agent
      remote_app = agent_engines.create(**agent_config)
    
    return None


if __name__ == "__main__":
    deploy_agent_engine_app()
