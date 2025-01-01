#!/usr/bin/env python
import sys
import warnings

from newsletter_gen.crew import NewsletterGen

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def load_html_template():
    with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
        html_template = file.read()
    return html_template


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': input("Please enter the topic for your newsletter:"),
        'personal_message': input("Please enter your personal message: "),
        'html_template': load_html_template()
    }
    NewsletterGen().crew().kickoff(inputs=inputs)
