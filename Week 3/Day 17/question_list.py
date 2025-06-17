from question import Question

class QuestionList:
    def __init__(self) -> None:
        self.questions = [
            Question("Is the capital of Australia Sydney? ", False),
            Question("Can humans survive in space without a spacesuit? ", False),
            Question("Is water made up of two hydrogen atoms and one oxygen atom? ", True),
            Question("Was Albert Einstein awarded the Nobel Prize for the theory of relativity? ", False),
            Question("Is the Great Wall of China visible from space with the naked eye? ", False),
            Question("Does the Amazon rainforest produce about 20% of the world's oxygen? ", True),
            Question("Is lightning hotter than the surface of the sun? ", True),
            Question("Did dinosaurs and humans live at the same time? ", False),
            Question("Is the boiling point of water lower at higher altitudes? ", True),
            Question("Do penguins live in the Arctic? ", False)
        ]
