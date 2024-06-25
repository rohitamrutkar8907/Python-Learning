def shout(text):
    return text.upper()
  
def whisper(text):
    return text.lower()
  
def greet(a):
    # storing the function in a variable
    greeting = a("""Hi, I am created by a function passed as an argument.""")
    print (greeting) 
  
greet(shout)
greet(whisper)