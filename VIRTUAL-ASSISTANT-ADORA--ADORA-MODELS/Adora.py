import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

from Listen import Listen  
from Speak import Say

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents from JSON file
with open("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/intents.json", "r") as json_data:
    intents = json.load(json_data)

# Load pre-trained model and data
FILE = "C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/FINAL-PROJECT-main/TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

# Load the model
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Your virtual assistant's name
Name = "Adora"

def Main():
    sentence = Listen()  # Assuming this function captures user input

    if sentence == 'bye':
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                Say(reply)


if __name__ == "__main__":
    Main()


