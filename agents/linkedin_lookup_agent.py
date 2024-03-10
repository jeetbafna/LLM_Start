from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# from langchain.agents import initialize_agent, Tool, AgentType
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin profile page.
        Your answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the LinkedIn profile URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    # agent = initialize_agent(
    #     tools=tools_for_agent,
    #     llm=llm,
    #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True,
    # )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]

    # linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linked_profile_url
