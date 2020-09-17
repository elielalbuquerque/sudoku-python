import matplotlib.pyplot as plt
import numpy as np

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
    def __init__(self,max_level):
        self.all_results_aStar = []
        self.all_results_bfs = []
        self.max_level=max_level

    def generate_calcs(self):
        file_bfs = open(f'tests/analysis_bfs.txt', 'w').close()
        file_aStar = open(f'tests/analysis_aStar.txt', 'w').close()
        for file_id in range (1, self.max_level+1):
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


def plot_bar(names, values, label, xlabel, ylabel,suptitle,file_name):
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.bar(names, values, label = label)
    plt.legend()
    plt.suptitle(suptitle)
    plt.savefig(f'plots/{file_name}.png')
    ##plt.show()
    plt.clf()


def plot_line(names, values, label, xlabel, ylabel,suptitle,file_name):
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.plot(names, values, label = label)
    plt.plot(names, values,'bo')
    plt.legend()
    plt.suptitle(suptitle)
    plt.savefig(f'plots/{file_name}.png')
    ##plt.show()
    plt.clf()


def plot_steps():
    test = AnalysisResultsAll(5)
    test.generate_calcs()
    names = [1,2,3,4,5]
    values_median_steps_bfs = []
    values_median_steps_aStar = []
    for i in range (5):
        values_median_steps_bfs.append(test.all_results_bfs[i].median_steps)
    for i in range (5):
        values_median_steps_aStar.append(test.all_results_aStar[i].median_steps)
    plot_line(names,values_median_steps_bfs,'BFS','Level','Steps','Steps Number Evolution by Level in BFS','bfs_steps_line')
    plot_bar(names,values_median_steps_bfs,'BFS','Level','Steps','Steps Number Evolution by Level in BFS','bfs_steps_bar')
    plot_line(names,values_median_steps_aStar,'aStar','Level','Steps','Steps Number Evolution by Level in aStar','aStar_steps_line')
    plot_bar(names,values_median_steps_aStar,'aStar','Level','Steps','Steps Number Evolution by Level in aStar','aStar_steps_bar')


def plot_time():
    test = AnalysisResultsAll(5)
    test.generate_calcs()
    names = [1,2,3,4,5]
    values_median_time_bfs = []
    values_median_time_aStar = []
    for i in range (5):
        values_median_time_bfs.append(test.all_results_bfs[i].median_execution_time)
    for i in range (5):
        values_median_time_aStar.append(test.all_results_aStar[i].median_execution_time)
    plot_line(names,values_median_time_bfs,'BFS','Level','Time (s)','Median Time evolution in BFS','bfs_time_line')
    plot_bar(names,values_median_time_bfs,'BFS','Level','Time (s)','Median Time evolution in BFS','bfs_time_bar')
    plot_line(names,values_median_time_aStar,'aStar','Level','Time (s)','Median Time evolution in aStar','aStar_time_line')
    plot_bar(names,values_median_time_aStar,'aStar','Level','Time (s)','Median Time evolution in aStar','aStar_time_bar')


def plot_steps_group():
    test = AnalysisResultsAll(5)
    test.generate_calcs()
    names = [1,2,3,4,5]
    values_median_steps_bfs = []
    values_median_steps_aStar = []
    for i in range (5):
        values_median_steps_bfs.append(test.all_results_bfs[i].median_steps)
    for i in range (5):
        values_median_steps_aStar.append(test.all_results_aStar[i].median_steps)
    plt.plot(names,values_median_steps_bfs,label='BFS')
    plt.plot(names,values_median_steps_bfs,'bo')
    plt.plot(names,values_median_steps_aStar,label='aStar')
    plt.plot(names,values_median_steps_aStar,'bo')
    plt.ylabel('Steps Number')
    plt.xlabel('Difficulty Level')
    plt.title("Median Steps Evolution by Level")
    plt.legend()
    plt.savefig('plots/group_steps_line.png')
    ###plt.show()
    plt.clf()


    x = np.arange(len(names))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values_median_steps_bfs, width, label='BFS')
    rects2 = ax.bar(x + width/2, values_median_steps_aStar, width, label='aStar')
    ax.set_ylabel('Steps Number')
    ax.set_xlabel('Difficulty Level')
    ax.legend()
    
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(f'{height:.2f}'),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig('plots/group_steps_bar.png')
    ###plt.show()
    plt.clf()


def plot_time_group():
    test = AnalysisResultsAll(5)
    test.generate_calcs()
    names = [1,2,3,4,5]
    values_median_time_bfs = []
    values_median_time_aStar = []
    for i in range (5):
        values_median_time_bfs.append(test.all_results_bfs[i].median_execution_time)
    for i in range (5):
        values_median_time_aStar.append(test.all_results_aStar[i].median_execution_time)
    plt.plot(names,values_median_time_bfs,label='BFS')
    plt.plot(names,values_median_time_bfs,'bo')
    plt.plot(names,values_median_time_aStar,label='aStar')
    plt.plot(names,values_median_time_aStar,'bo')
    plt.ylabel('Execution Time (s)')
    plt.xlabel('Difficulty Level')
    plt.title("Median Time Evolution by Level")
    plt.legend()
    plt.savefig('plots/group_time_line.png')
    ###plt.show()
    plt.clf()


    x = np.arange(len(names))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values_median_time_bfs, width, label='BFS')
    rects2 = ax.bar(x + width/2, values_median_time_aStar, width, label='aStar')
    ax.set_ylabel('Execution Time (s)')
    ax.set_xlabel('Difficulty Level')
    ax.legend()
    
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(f'{height:.3f}'),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig('plots/group_time_bar.png')
    ###plt.show()
    plt.clf()


def main():
    plot_steps()
    plot_time()
    plot_steps_group()
    plot_time_group()


if __name__ == "__main__":
    main()