import traceback


# Task 1: Diary
try:
    # Track first prompt
    first_prompt = True

    # Create text string to track
    text = ""

    # Open file
    with open("diary.txt", "w") as file:
        # Continually prompt the user
        while True:
            if first_prompt:
                text = input("What happened today? ")
                text += "\n"
                # Set first_prompt to false after the first prompt
                first_prompt = False
            else:
                # Follow up prompt    
                text = input("What else? ")
                text += "\n"

            # Write text to file
            file.write(text)

            # Create break condition
            if "done for now" in text:
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
