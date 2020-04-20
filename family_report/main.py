def kids(chore_sentence):
    def assignment_sentence(*args, **kwargs):
        original_sentence = chore_sentence(*args, **kwargs)
        return original_sentence + " by the kids"
    return assignment_sentence

def dad(chore_sentence):
    def assignment_sentence(*args, **kwargs):
        original_sentence = chore_sentence(*args, **kwargs)
        return original_sentence + " by Dad"
    return assignment_sentence

def mom(chore_sentence):
    def assignment_sentence(*args, **kwargs):
        original_sentence = chore_sentence(*args, **kwargs)
        return original_sentence + " by Mom"
    return assignment_sentence


@kids
def laundry():
    return "The dirty laundry was cleaned"

@dad
def garbage():
    return "The garbage was taken out"

@kids
def dust():
    return "The house was dusted"

@mom
def groom():
    return "The dog was brushed"


print(laundry())
print(garbage())
print(dust())
print(groom())
