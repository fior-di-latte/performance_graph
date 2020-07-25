import argparse
from os import system, getcwd
from os.path import exists
from datetime import datetime
from path import Path

def make_graph(args, opt_folder, output_fn):
       # create graph picture
       system(f'python -m cProfile -o profile {args.fn}; '  # profiling
              f'gprof2dot -f pstats -p  {getcwd()} {opt_folder} -e 0.5 -n 0.35 -o graph.dot profile; '  # graph
              f'dot graph.dot -Tpng -o {output_fn} ; '  # export to png
              f'rm profile graph.dot')  # delete everything except output

#TODO if script to test is on highest level , folder is empty variable, which is a problem
if __name__== '__main__':
       # current time
       time = str(datetime.now()).split('.')[0].split(' ')
       time = '-'.join(time)[:-3]
       # TODO enhance arparser
       # CLI interface
       parser = argparse.ArgumentParser(description='Enter file name. Use this script from project root.')
       parser.add_argument('fn', help='specify file')
       args = parser.parse_args()
       input_str = args.fn               # target file name w/o parent folder
       entire_path = Path(getcwd()) / input_str
       script_name = str(entire_path.name)
       assert exists(entire_path), 'Input file not found.'
       folder = input_str[:-len(script_name)-1]
       opt_folder = f'-p {folder}' if len(folder) > 1 else ""
       output_fn = f'{entire_path.parent / script_name.split(".")[0]}-{time}.png'     # file name of output png
       make_graph(args, opt_folder, output_fn)            # invoke make_graph fn

       # TODO make sure gprof2dot is in the dependencies, specify versions
       # TODO readme
       #--root="main_copy:9:<module>"
