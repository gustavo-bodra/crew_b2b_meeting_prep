#!/usr/bin/env python
import sys
from crew_b2b_meeting_prep.crew import CrewB2BMeetingPrepCrew
from datetime import datetime


def run():
    inputs = {
        'company': 'Bauminas',
        'current_date': '2024-07-21' #datetime.today().strftime('%Y-%m-%d')
    }
    CrewB2BMeetingPrepCrew().crew().kickoff(inputs=inputs, planning=True)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company': 'Bauminas',
        'current_date': '2024-07-21'
    }
    try:
        CrewB2BMeetingPrepCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
