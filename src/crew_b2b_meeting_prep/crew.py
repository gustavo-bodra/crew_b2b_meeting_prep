from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import EXASearchTool, SerperDevTool, PDFSearchTool, WebsiteSearchTool
from crew_b2b_meeting_prep.tools import EmailTool

@CrewBase
class CrewB2BMeetingPrepCrew():
	"""CrewB2BMeetingPrep crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher_news(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher_news'],
			tools=[SerperDevTool(), WebsiteSearchTool()],
			verbose=True,
			# max_iter=15
		)

	@agent
	def researcher_corp(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher_corp'],
			tools=[SerperDevTool(), PDFSearchTool(), WebsiteSearchTool()],
			verbose=True,
			# max_iter=15
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			# max_iter=15
			# tools=[EmailTool()]
		)

	@task
	def research_task_news(self) -> Task:
		return Task(
			config=self.tasks_config['research_task_news'],
			agent=self.researcher_news()
		)

	@task
	def research_task_corp(self) -> Task:
		return Task(
			config=self.tasks_config['research_task_corp'],
			agent=self.researcher_corp()
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			output_file='output/company_dossie.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewB2BMeetingPrep crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			verbose=2,
			process=Process.hierarchical,
			# planning=True,
			# memory=True,
			manager_agent=Agent(config=self.agents_config['supervisor'], verbose=True),
		)