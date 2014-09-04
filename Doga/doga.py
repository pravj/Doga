import argparse


class Doga:

    def __init__(self):
        self.desc = 'HTTP log monitoring console program'
        self.parser = argparse.ArgumentParser(description=(self.desc))
