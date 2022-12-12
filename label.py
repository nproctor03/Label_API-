import pickle
import faiss
import numpy as np


def label_image(image_embedding):
    """
    _summary_

    Args:
        list (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        # convert embedding to numpy array
        emb = np.array(image_embedding).astype('float32')
        # print(emb)
        # pass into faiss indexes to get labels
        has_beard = label_beard(emb)
        generation = label_generation(emb)
        hair_type = label_hair_type(emb)
        mouth_opened_or_closed = label_mouth_opened(emb)
        nationality = label_nationality(emb)
        sex = label_sex(emb)
        glasses = label_wearing_glasses(emb)
        hat = label_wearing_hat(emb)

        labels = [has_beard, generation, hair_type,
                  mouth_opened_or_closed, nationality, sex, glasses, hat]
        status = "Success"

        return status, labels

    except Exception as e:
        print(e)
        status = "Fail"
        message = "There was an error processing your request"
        return status, message


def label_beard(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:

        #print("beard entered")
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\beard\\beard.index')
        #print("index file read")
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\beard\\beard_dict", "rb") as file:
            dictionary = pickle.load(file)

       # print("about to search index")
        D, I = index.search(embedding, 1)

        # print(I)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_generation(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        index = faiss.read_index(
            "D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\generations\\generations.index")
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\generations\\generations_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_hair_type(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\hair\\hair.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\hair\\hair_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label
    except Exception as e:
        print(e)
        return "error"


def label_mouth_opened(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\mouthopened\\mouthopened.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\mouthopened\\mouthopened_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_nationality(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\nationalities\\nationalities.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\nationalities\\nationalities_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_profession(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\Professions\\professions.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\Professions\\professions_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_sex(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\sexes\\sexes.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\sexes\\sexes_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_wearing_glasses(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\wearing_glasses\\wearing_glasses.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\wearing_glasses\\wearingglasses_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"


def label_wearing_hat(embedding):
    """
    _summary_

    Args:
        embedding (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        index = faiss.read_index(
            'D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\wearing_hat\\wearing_hat.index')
        with open("D:\\Projects\\FlaskWebAPIs\\Label_API\\Label_API-\\data\\wearing_hat\\hat_dict", "rb") as file:
            dictionary = pickle.load(file)

        D, I = index.search(embedding, 1)
        label = dictionary[I[0][0]]
        return label

    except Exception as e:
        print(e)
        return "error"
