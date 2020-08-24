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
        return(f'{self.median_execution_time} {self.median_steps} {self.max_steps} {self.min_steps} '
        f'{self.max_execution_time} {self.min_execution_time}')

class AnalysisResultsAll:
    def __init__(self):
        self.all_results_aStar = []
        self.all_results_bfs = []

    def generate_cals(self):
        print(f"Gerando tests analysis")
        file_bfs = open(f'tests/analysis_bfs.txt', 'w').close()
        file_aStar = open(f'tests/analysis_aStar.txt', 'w').close()
        for file_id in range (1, 10):
            test_aStar = AnalysisResults(f'tests/results/aStar_{file_id}.txt')
            test_aStar.load_results()
            test_aStar.calc()
            self.all_results_aStar.append(test_aStar)
            print (test_aStar, file=open(f'tests/analysis_aStar.txt', "a"))
            test_bfs = AnalysisResults(f'tests/results/bfs_{file_id}.txt')
            test_bfs.load_results()
            test_bfs.calc()
            self.all_results_bfs.append(test_bfs)
            print (test_bfs, file=open(f'tests/analysis_bfs.txt', "a"))








def main():
    test = AnalysisResultsAll()
    test.generate_cals()
    # test.load_results()
    # test.calc()
    # print(test)


if __name__ == "__main__":
    main()