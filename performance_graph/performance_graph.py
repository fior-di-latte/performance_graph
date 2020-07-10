import argparse
from os import system, getcwd
from datetime import datetime


def make_graph(script_name, folder, output_fn):
       # create graph picture
       system(f'python -m cProfile -o profile {args.fn}; '  # profiling
              f'gprof2dot -f pstats -p  {getcwd()} -p {folder} -e 0.5 -n 0.35 -o graph.dot profile; '  # graph
              f'dot graph.dot -Tpng -o {output_fn} ; '  # export to png
              f'rm profile graph.dot')  # delete everything except output

if __name__== '__main__':
       # current time
       time = str(datetime.now()).split('.')[0].split(' ')
       time = '-'.join(time)[:-3]

       # TODO enhance arparser
       # CLI interface
       parser = argparse.ArgumentParser(description='Enter file name.')
       parser.add_argument('fn', help='specify file')
       args = parser.parse_args()

       script_name = args.fn.split('/')[-1]                  # target file name w/o parent folder
       folder = args.fn[:-len(script_name)-1]                # parent folder
       output_fn = f'{args.fn.split(".")[0]}-{time}.png'     # file name of output png
       make_graph(script_name, folder, output_fn)            # invoke make_graph fn



       # TODO make sure gprof2dot is in the dependencies, specify versions
       # TODO add pyinstaller in setup
       # TODO readme
       # TODO PATHLIB
       #--root="main_copy:9:<module>"
