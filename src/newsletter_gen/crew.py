from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.custom_tool import SearchAndContents, FindSimilar, GetContents
import streamlit as st
from crewai.agents.parser import AgentAction, AgentFinish

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class NewsletterGen():
	"""NewsletterGen crew"""

	def step_callback(self, agent_output, agent_name):
		st.write(f"Agent name: {agent_name}")
		st.write(f"Agent type: {type(agent_output)}")
		if isinstance(agent_output, AgentAction):
			with st.expander("Thought / Tool / Tool input"):
				st.write(f"Thought: {agent_output.thought}")
				st.write(f"Tool: {agent_output.tool}")
				st.write(f"Tool input: {agent_output.tool_input}")
			with st.expander("Text"):
				st.write(agent_output.text)
			with st.expander("Result"):
				st.write(agent_output.result)
		
		elif isinstance(agent_output, AgentFinish):
			with st.expander("Thought"):
				st.write(agent_output.thought)
			with st.expander("Output"):
				st.write(agent_output.output)
			with st.expander("Text"):
				st.write(agent_output.text)

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[
				SearchAndContents(),
				FindSimilar(),
				GetContents()
			],
			verbose=True,
			step_callback=lambda step : self.step_callback(step, "Research Agent")
		)

	@agent
	def editor(self) -> Agent:
		return Agent(
			config=self.agents_config['editor'],
			tools=[
				SearchAndContents(),
				FindSimilar(),
				GetContents()
			],
			verbose=True,
			step_callback=lambda step : self.step_callback(step, "Editor Agent")
		)
	
	@agent
	def designer(self) -> Agent:
		return Agent(
			config=self.agents_config['designer'],
			verbose=True,
			allow_delegation=False,
			step_callback=lambda step : self.step_callback(step, "Designer Agent")
		)
	
	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher(),
			output_file="tasks/research_task.md"
		)

	@task
	def edit_task(self) -> Task:
		return Task(
			config=self.tasks_config['edit_task'],
			agent=self.editor(),
			output_file='tasks/edit_task.md'
		)
	
	@task
	def newsletter_task(self) -> Task:
		return Task(
			config=self.tasks_config['newsletter_task'],
			agent=self.designer(),
			output_file='tasks/newsletter_task.html'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the NewsletterGen crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
