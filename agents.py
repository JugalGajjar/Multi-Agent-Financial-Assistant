from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.googlesearch import GoogleSearch

# Load API keys from environment variables
from dotenv import load_dotenv
load_dotenv()

# Define agents for web search
web_search_agent = Agent(
    name="Web Search Agent",
    description="An agent that can search the web for latest information.",
    tools=[GoogleSearch()],
    model=Groq(id="llama3-8b-8192"),
    instructions="Always include the source of the information you find in your response. If you cannot find the information, say so.",
    show_tool_calls=True,
    markdown=True
)

# Define agents for finance queries
finance_agent = Agent(
    name="Finance Agent",
    description="An agent that can answer questions about finance and stock market.",
    tools=[YFinanceTools(
        stock_price=True,
        historical_prices=True,
        stock_fundamentals=True,
        analyst_recommendations=True,
        company_news=True,
        company_info=True
    )],
    model=Groq(id="llama3-8b-8192"),
    instructions="Always provide the latest stock prices and financial news. If you cannot find the information, say so. Use table format for stock data.",
    show_tool_calls=True,
    markdown=True
)

# Define a multi-task agent that can perform both web search and finance queries
multi_agent = Agent(
    name="Multi-Task Agent",
    description="An agent that can perform multiple tasks including web search and finance queries.",
    model=Groq(id="llama3-8b-8192"),
    team=[web_search_agent, finance_agent],
    instructions=(
        "If the task involves the web, include the source(s) in one line as a list separated by commas."
        "If the task involves finance or stock data, provide the latest prices, news, and tables, and include the source(s) in one line as a list separated by commas."
        "If any data is unavailable, say 'Unable to fetch data' and do not include any source."
    ),
    show_tool_calls=True,
    markdown=True
)
