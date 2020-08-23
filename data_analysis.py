class Result:
    def __init__(self,execution_time,steps):
        self.execution_time = execution_time
        self.steps = steps

    def __str__(self):
        return(f'{self.execution_time}, {self.steps}')

class AnalysisResults:

    def __init__(self,relative_file_path):
        self.relative_file_path = relative_file_path
        self.results = []
        self.median_steps = 0
        self.max_steps = 0
        self.min_steps = 0
        self.median_execution_time = 0
        self.max_execution_time = 0
        self.min_execution_time = 0




    def load_results(self):
        with open(self.relative_file_path, 'r') as file:
            for line in file:
                line_list = line.split()
                result = Result(float(line_list[0]),int(line_list[1]))
                self.results.append(result)


    def calc(self):
        sum_execution_time = 0
        sum_steps = 0
        for element in self.results:
            sum_execution_time += element.execution_time
            sum_steps += element.steps
            if element.steps > self.max_steps:
                self.max_steps = element.steps
            if element.steps < self.min_steps:
                self.min_steps = element.steps
            if element.execution_time > self.max_execution_time:
                self.max_execution_time = element.execution_time
            if element.execution_time < self.min_execution_time:
                self.min_execution_time = element.execution_time
            

        self.median_execution_time = sum_execution_time / len(self.results)
        self.median_steps = sum_steps / len(self.results)

    def __str__(self):
        return(f'Median execution time: {self.median_execution_time}, Median steps {self.median_steps}'
        f'\n Max and Min steps: {self.max_steps}, {self.min_steps}'
        f'\n Max and Min execution time: {self.max_execution_time}, {self.min_execution_time}')
        # for element in self.results:
        #     print(f'{element.execution_time}, {element.steps}\n')

def main():
    test = AnalysisResults('tests/results/aStar_1.txt')
    test.load_results()
    test.calc()
    print(test)



if __name__ == "__main__":
    main()