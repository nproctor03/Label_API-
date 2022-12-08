import faiss
import pickle
import numpy as np
from faiss import read_index
import traceback




def label_image(list):

    try:
        #convert embedding to numpy array
        emb = np.array(list).astype('float32')
        #print(emb)
        #pass into faiss indexes to get labels
        has_beard = label_beard(emb)
        print("1")
        generation = label_generation(emb)
        print("2")
        hair_type = label_hair_type(emb)
        print("3")
        mouth_opened_or_closed = label_mouth_opened(emb)
        print("4")
        nationality = label_nationality(emb)
        print("5")
        sex = label_sex(emb)
        print("6")
        glasses = label_wearing_glasses(emb)
        print("7")
        hat = label_wearing_hat(emb)

        labels = [has_beard, generation, hair_type, mouth_opened_or_closed, nationality, sex, glasses, hat]
        status ="Success"
        return status, labels
    
    except Exception as e: 
        print(e)
        status = "Fail"
        message = "There was an error processing your request"
        return status, message





def label_beard(embedding):

    try:
        
        print("beard entered")
        index = faiss.read_index('Label_API-\\data\\beard\\beard.index')
        print("index file read")
        with open("Label_API-\\data\\beard\\beard_dict", "rb") as file:
            dictionary = pickle.load(file)

        print("about to search index")
        D, I = index.search(embedding, 1)
     
        print(I)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)

        



def label_generation(embedding):

    try:
        index = faiss.read_index('Label_API-\data\generations\generations.index')
        with open("Label_API-\\data\\generations\\generations_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)

    

def label_hair_type(embedding):

    try:
        index = faiss.read_index('Label_API-\data\hair\hair.index')
        with open("Label_API-\\data\\hair\\hair_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label  
    except Exception as e:
        print(e)

      

def label_mouth_opened(embedding):

    try:
        index = faiss.read_index('Label_API-\data\mouthopened\mouthopened.index')
        with open("Label_API-\\data\\mouthopened\\mouthopened_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label  

    except Exception as e:
        print(e)

       

def label_nationality(embedding):

    try:
        index = faiss.read_index('Label_API-\\data\\nationalities\\nationalities.index')
        with open("Label_API-\\data\\nationalities\\nationalities_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)




def label_profession(embedding):

    try:
        index = faiss.read_index('Label_API-\data\Professions\professions.index')
        with open("Label_API-\\data\\Professions\\professions_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label  

    except Exception as e:
        print(e)


def label_sex(embedding):

    try:
        index = faiss.read_index('Label_API-\data\sexes\sexes.index')
        with open("Label_API-\\data\\sexes\\sexes_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label  
    
    except Exception as e:
        print(e)


def label_wearing_glasses(embedding):
    try:
        index = faiss.read_index('Label_API-\data\wearing_glasses\wearing_glasses.index')
        with open("Label_API-\\data\\wearing_glasses\\wearingglasses_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label  
    
    except Exception as e:
        print(e)


def label_wearing_hat(embedding):
    try:
        index = faiss.read_index('Label_API-\data\wearing_hat\wearing_hat.index')
        with open("Label_API-\\data\\wearing_hat\\hat_dict", "rb") as file:
                dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label  

    except Exception as e:
        print(e)
