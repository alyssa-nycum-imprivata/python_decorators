# def kids(chore):
#     def assignment_sentence(*args, **kwargs):
#         original_sentence = chore(*args, **kwargs)
#         return original_sentence + " by the kids"
#     return assignment_sentence

# def dad(chore):
#     def assignment_sentence(*args, **kwargs):
#         original_sentence = chore(*args, **kwargs)
#         return original_sentence + " by Dad"
#     return assignment_sentence

# def mom(chore):
#     def assignment_sentence(*args, **kwargs):
#         original_sentence = chore(*args, **kwargs)
#         return original_sentence + " by Mom"
#     return assignment_sentence

# decorator for DRY code 
def assignment(person):
    def decorator(chore):
        def assignment_sentence(*args, **kwargs):
            original_sentence = chore(*args, **kwargs)
            return original_sentence + " by " + person
        return assignment_sentence
    return decorator

@assignment("the kids")
def laundry():
    return "The dirty laundry was cleaned"

@assignment("Dad")
def garbage():
    return "The garbage was taken out"

@assignment("the kids")
def dust():
    return "The house was dusted"

@assignment("Mom")
def groom():
    return "The dog was brushed"


print(laundry())
print(garbage())
print(dust())
print(groom())
