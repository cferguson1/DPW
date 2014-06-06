#Get names in array
character = []
name = character.append( raw_input("Pick a name: ") )
animal = character.append( raw_input("Pick an animal ") )
verb = character.append( raw_input("Pick a verb: ") )

number_one = raw_input("Pick a number (1-10)" )
number_two = raw_input("Pick another number (1-10)" )
number_three = raw_input("Pick one last number (1-72)" )
numbers = dict()
numbers = {"Duration":number_one, "Interval":number_two, "Measure":number_three}

#use a FUNCTION with a LOOP to get my "feels" sentence
def measure_feels(measurement):
    measurement = int(measurement)
    feelwords = []
    sentence = ''
    if measurement <= 36:
        feelwords.extend(["only ", str(measurement), " inches tall"])
    else:
        measurement *= 10
        feelwords.extend(["a whopping ", str(measurement), " pounds"])
    for word in feelwords:
        sentence += word
    return sentence;

def annoyance_level(duration, interval):
    level_words = []
    duration = int(duration)
    interval = int(interval)
    level_words.extend([duration, interval])
    score = duration + interval
    if score < 5:
        level_words.extend(["really", "getting a wedgie and shoved in the dumpster"])
    elif score < 15:
        level_words.extend(["super", "getting punch in the face and stuffed in a locker"])
    else:
        level_words.extend(["INCREDIBLY", "getting stuffed into a heavily used port-a-potty, buried alive in a thick layer of concrete, and left to die of starvation"])
    return level_words

feels = measure_feels(numbers["Measure"])
level = annoyance_level(numbers["Duration"], numbers["Interval"])


madlib = "" \
         "" \
         "One day there was a {character[1]} named {character[0]}. {character[0]}" \
         " had a problem because he was {feels}. Everyone thought he was a loser." \
         " So one day, {character[0]} decided he would try to make friends by doing" \
         " the only thing he's ever been good at. {character[2]}ing. He {character[2]}ed" \
         " and {character[2]}ed for {level[0]} days and {level[0]} nights with at least {level[1]} {character[2]}s" \
         " every minute. He was {level[2]} annoying and, as a result, ended up {level[3]}"

madlib = madlib.format(**locals())
print madlib


