__version__ = '1.0'
import sys
import ast
def main():
    """
    The console_scripts Entry Point in setup.py
    """

    def check_line_limit(value):
        ivalue = int(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError("%s is an invalid line limit" % value)
        return ivalue
            def check_percentage_limit(value):
        ivalue = float(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError("%s is an invalid percentage limit" % value)
        return ivalue
parser = ArgParser(description='A simple plagiarism detection tool for python code')
    parser.add_argument('files', type=file, nargs=2,
                        help='the input files')
for func_diff_info in func_ast_diff_list:
            if len(func_diff_info.info_ref.func_ast_lines) >= args.l and func_diff_info.plagiarism_percent >= args.p:
                print(func_diff_info)


if __name__ == '__main__':
    main()
 [bdist_wheel]
universal = 1

    
    
    
    
    
