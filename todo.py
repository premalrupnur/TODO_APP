#!/usr/bin/python3
import argparse
import sys
import time
import datetime


def todo(args):
    # condition for displaying help
    if(args.o[0]=='help'):
        help = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics\n"
        return help
    
    # Addition of new todo
    if(args.o[0]=='add'):
        try:
            with open('todo.txt',"a") as f:
                f.write(args.o[1]+'\n')
                return f'Added todo: "{args.o[1]}"'
        except:
            return 'Error: Missing todo string. Nothing added!'
        
    #Deleting a todo 
    if(args.o[0]=='del' and len(sys.argv)==2):
        return 'Error: Missing NUMBER for deleting todo.'
    
    if(args.o[0]=='del' and len(sys.argv)==3):
        with open('todo.txt',"r") as f:
            reads = f.readlines()
        if(len(reads)==0 or int(sys.argv[2])<1 or int(sys.argv[2])>len(reads)):
            return f'Error: todo #{args.o[1]} does not exist. Nothing deleted.'
        else:
            reads.pop(int(args.o[1]))
            with open('todo.txt',"w") as f:
                for read in reads:
                    f.write(read)
            return f'Deleted todo #{args.o[1]}\n'
    
    #Displaying the todos
    if(args.o[0]=='ls'):
        with open('todo.txt','r') as f:
            reads = f.readlines()
        if(len(reads)==0):
            return 'There are no pending todos!\n'
        else:
            reads.reverse()
            str1=''
            count = len(reads)
            for read in reads:
                str1+=f'[{count}] {read}'
                count = count-1
            return str1
       
    #Marking todos as done
    if(args.o[0]=='done' and len(sys.argv)==2):
        return f'Error: Missing NUMBER for marking todo as done.\n'
    
    if(args.o[0]=='done' and len(sys.argv)==3):
        with open('todo.txt',"r") as f:
                reads = f.readlines()
        if(len(reads)==0 or int(sys.argv[2])<1 or int(sys.argv[2])>len(reads)):
                return f'Error: todo #{sys.argv[2]} does not exist.'
        else:
            with open('done.txt',"a") as f:
                f.write(reads[int(sys.argv[2])-1])
            with open('todo.txt',"r") as f:
                reads = f.readlines()
                reads.pop(int(args.o[1])-1)
            with open('todo.txt',"w") as f:    
                for read in reads:
                    f.write(read)
            return f'Marked todo #{sys.argv[2]} as done.'

    #Reporting the todos to user
    if(args.o[0]=='report'):
        with open('todo.txt','r') as f:
            reads = f.readlines()
        with open('done.txt','r') as f1:
            reads1 = f1.readlines()
        return f'{time.strftime("%Y-%m-%d")} Pending : {len(reads)} Completed : {len(reads1)} '
        
        
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('o', nargs='+')
    if len(sys.argv)==1:
        print("Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics\n")
        sys.exit(1)
    args=parser.parse_args()
    sys.stdout.write(str(todo(args)))
    
