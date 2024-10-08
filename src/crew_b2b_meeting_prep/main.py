#!/usr/bin/env python
import sys
from crew_b2b_meeting_prep.crew import CrewB2BMeetingPrepCrew
from datetime import datetime


def run():
    inputs = {
        'company': 'Bauminas',
        'today': datetime.now().strftime('%Y-%m-%d')
        # 'today': '2024-09-20'
    }
    CrewB2BMeetingPrepCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company': 'Bauminas',
        'today': datetime.now().strftime('%Y-%m-%d')
        # 'today': '2024-09-20'
    }
    try:
        CrewB2BMeetingPrepCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
