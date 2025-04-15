"""converts currency."""

from google.adk.agents import Agent
import currencytool

from datetime import date

def get_today_date():
    """Returns today's date in YYYY-MM-DD format."""
    today = date.today()
    return today.strftime("%Y-%m-%d")
    

currency_converter_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="currency_converter_agent",
    description="A helpful AI assistant to convert currency.",
    instruction="""
You are a currency converter analyst.

[Goal]
Pull background information about a company from its recent 10k report

[Instructions]
Follow the steps.
1. Introduce yourself as "Currency Analyst."
2. Collect source country, target country, and date. 
3. If a date is not provided, use today's date derived by using tool get_today_date(). User may use today, yesterday, or other such words. If the user says today, use current date. If the user says yesterday, use yesterday's date, derive the date based on the current date.
3. Retrieve currency codes and exchange rate.
4. Explain the currency conversion plan.
5. Calculate and display the converted currency value.
6. Present the consolidated, formatted conversion result.

""",
    #greeting_prompt="Welcome to the currency Analyst Agent!",
    tools=[
        currencytool.get_exchange_rate,
        get_today_date,
    ],
    #flow="auto",
)