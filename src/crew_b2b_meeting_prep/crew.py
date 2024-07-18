from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from src.crew_b2b_meeting_prep.tools import EmailTool

@CrewBase
class CrewB2BMeetingPrepCrew():
	"""CrewB2BMeetingPrep crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			tools=[EmailTool()]
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher()
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			# output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewB2BMeetingPrep crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			verbose=2,
			process=Process.hierarchical,
			manager_agent=Agent(config=self.agents_config['supervisor'], verbose=True),
		)