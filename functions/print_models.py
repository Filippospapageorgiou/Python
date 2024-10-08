


def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)

def show_complete_models(completed_models):
    print("All models\n")
    for model in completed_models:
        print(f"All models completed : {model}")


unprinted_designs = ['phone case' , 'robot pendant' , 'dog']
completed_models = []

print_models(unprinted_designs[:],completed_models) #[:] xrisimopoiei ena antigrafo tis listas gia na min tropoipish tin dikia mas
show_complete_models(completed_models)



def show_messages(messages):
    for msg in messages:
        print(f"{msg}")


messages = ['hello' , 'world' , '!' , '!']
show_messages(messages)







