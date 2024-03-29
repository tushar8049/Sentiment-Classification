import tarfile
import sys
import os
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
from torch import optim


# Task 1: Load the data
# For this task you will load the data, create a vocabulary and encode the reviews with integers

def read_file(path_to_dataset):
    """
    :param path_to_dataset: a path to the tar file (dataset)
    :return: two lists, one containing the movie reviews and another containing the corresponding labels
    """

    if not tarfile.is_tarfile(path_to_dataset):
        sys.exit("Input path is not a tar file")
    dirent = tarfile.open(path_to_dataset)
    """
    COMPLETE THE REST OF THE METHOD
    """
    dirent.close()


def preprocess(text):
    """
    :param text: list of sentences or movie reviews
    :return: a dict of all tokens you encounter in the dataset. i.e. the vocabulary of the dataset
    Associate each token with a unique integer
    """

    if type(text) is not list:
        sys.exit("Please provide a list to the method")
    """
    COMPLETE THE REST OF THE METHOD
    """


def encode_review(vocab, text):
    """
    :param vocab: the vocabulary dictionary you obtained from the previous method
    :param text: list of movie reviews obtained from the previous method
    :return: encoded reviews
    """

    if type(vocab) is not dict or type(text) is not list:
        sys.exit("Please provide a list to the method")
    """
    COMPLETE THE REST OF THE METHOD
    """


def encode_labels(labels): # Note this method is optional (if you have not integer-encoded the labels)
    """
    :param labels: list of labels associated with the reviews
    :return: encoded labels
    """

    if type(labels) is not list:
        sys.exit("Please provide a list to the method")
    """
    COMPLETE THE REST OF THE METHOD
    """


def pad_zeros(encoded_reviews, seq_length = 200):
    """
    :param encoded_reviews: integer-encoded reviews obtained from the previous method
    :param seq_length: maximum allowed sequence length for the review
    :return: encoded reviews after padding zeros
    """

    if type(encoded_reviews) is not list:
        sys.exit("Please provide a list to the method")
    """
    COMPLETE THE REST OF THE METHOD
    """

# Task 2: Load the pre-trained embedding vectors
# For this task you will load the pre-trained embedding vectors from Word2Vec

def load_embedding_file(embedding_file, token_dict):
    """
    :param embedding_file: path to the embedding file
    :param token_dict: token-integer mapping dict obtained from previous step
    :return: embedding dict: embedding vector-integer mapping
    """

    if not os.path.isfile(embedding_file):
        sys.exit("Input embedding path is not a file")
    if type(token_dict) is not dict:
        sys.exit("Input a dictionary!")

# Task 3: Create a TensorDataset and DataLoader

def create_data_loader(encoded_reviews, labels, batch_size = 32):
    """
    :param encoded_reviews: zero-paddded integer-encoded reviews
    :param labels: integer-encoded labels
    :param batch_size: batch size for training
    :return: DataLoader object
    """

    if type(encoded_reviews) is not list or type(labels) is not list:
        sys.exit("Please provide a list to the method")
    """
    COMPLETE THE REST OF THE METHOD
    """


# Task 4: Define the Baseline model here

# This is the baseline model that contains an embedding layer and an fcn for classification
class BaseSentiment(nn.Module):
    def __init__(self):
        super(BaseSentiment).__init__()

    def forward (self, input_words):
        pass


# Task 5: Define the RNN model here

# This model contains an embedding layer, an rnn and an fcn for classification
class RNNSentiment(nn.Module):
    def __init__(self):
        super(RNNSentiment).__init__()

    def forward(self, input_words):
        pass

# Task 6: Define the RNN model here

# This model contains an embedding layer, self-attention and an fcn for classification
class AttentionSentiment(nn.Module):
    def __init__(self):
        super(RNNSentiment).__init__()

    def forward(self, input_words):
        pass

"""
ALL METHODS AND CLASSES HAVE BEEN DEFINED! TIME TO START EXECUTION!!
"""

# Task 7: Start model training and testing

# Instantiate all hyper-parameters and objects here

# Define loss and optimizer here

# Training starts!!

# Testing starts!!



# Implicit Task 8: Get creative!!