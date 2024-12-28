import os
from typing import List, Dict
from dataclasses import dataclass
from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

@dataclass
class AgentResponse:
    content: str
    sources: List[str]
    tool_calls: List[Dict]

class AgentSystem:
    def __init__(self):
        load_dotenv()
        self.init_agents()
        
    def init_agents(self):
        # Web Agent with search capabilities
        self.web_agent = Agent(
                                name="Web Agent",
                                role="Search and analyze web information",
                                model=Groq(api_key=os.getenv('GROQ_API_KEY')),
                                tools=[
                                    DuckDuckGo(fixed_max_results=5),
                                    GoogleSearch(
                                        fixed_language='english',
                                        fixed_max_results=5
                                        # fixed_time_period='10m'  # Last 10 months
                                    )
                                ],
                                instructions=[
                                        "Always include sources",
                                        "Prioritize recent information",
                                        "Cross-reference multiple sources",
                                        "Highlight conflicting information if found"
                                ],
                                show_tool_calls=True,
                                markdown=True,
                            )
        
        # Finance Agent with financial tools
        self.finance_agent = Agent(
                                    name="Finance Agent",
                                    role="Comprehensive financial analysis",
                                    model=Groq(api_key=os.getenv('GROQ_API_KEY')),
                                    tools=[
                                        YFinanceTools(
                                            stock_price=True,
                                            analyst_recommendations=True,
                                            company_info=True,
                                            # financial_statements=True,
                                            # balance_sheet=True,
                                            # cash_flow=True
                                        )
                                    ],
                                    instructions=[
                                            "Use tables to display data",
                                            "Include key financial metrics",
                                            "Highlight significant changes",
                                            "Add brief market context"
                                    ],
                                    show_tool_calls=True,
                                    markdown=True,
                                )
        
        # Team Agent with coordination
        self.agent_team = Agent(
                                team=[self.web_agent, self.finance_agent],
                                model=Groq(api_key=os.getenv('GROQ_API_KEY')),
                                instructions=[
                                        "Combine insights from both agents",
                                        "Highlight contradictions",
                                        "Provide comprehensive analysis",
                                        "Include all sources",
                                        "Use tables for numerical data"
                                ],
                                show_tool_calls=True,
                                markdown=True,
                            )
        
    
    def get_stock_analysis(self, ticker: str) -> AgentResponse:
        """Get comprehensive stock analysis."""
        prompt = f"""Analyze {ticker}:
                    1. Latest analyst recommendations
                    2. Recent news and market sentiment
                    3. Key financial metrics
                    4. Market position and competitive analysis"""
        
        response: RunResponse = self.agent_team.run(prompt)
        content = response.content
        sources = []
        if hasattr(response, 'sources'):
            sources = response.sources  

        return AgentResponse(
            content=content,
            sources=sources,
            tool_calls=response.tool_calls if hasattr(response, 'tool_calls') else []
        )
    
    def get_market_news(self, topic: str) -> AgentResponse:
        """Get focused market news analysis."""
        prompt = f"Analyze recent market news about {topic}, focus on impact and trends"
        response: RunResponse = self.web_agent.run(prompt)
        content = response.content
        sources = []
        if hasattr(response, 'sources'):
            sources = response.sources  

        return AgentResponse(
            content=content,
            sources=sources,
            tool_calls=response.tool_calls if hasattr(response, 'tool_calls') else []
        )