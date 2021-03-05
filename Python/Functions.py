#!/usr/bin/env python

# Functions ...


#print("Let's run a function");

''' we don\'t need any parameters, but they go here '''
'''
def get_info(): #{

    print("This is inside the function");
#}

get_info();

print("this is outside the function");
'''

def get_info():

    user_input = input("What should we say?\n");
    print("Let's say: \t" + user_input);

get_info();
