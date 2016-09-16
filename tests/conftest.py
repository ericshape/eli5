# -*- coding: utf-8 -*-
import pytest
from sklearn.datasets import fetch_20newsgroups

CATEGORIES = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
CATEGORIES_BINARY = [
    'alt.atheism',
    'comp.graphics',
]
SIZE = 100


def _get_newsgroups(binary=False, remove_chrome=False, test=False, size=SIZE):
    remove = ('headers', 'footers', 'quotes') if remove_chrome else []
    categories = CATEGORIES_BINARY if binary else CATEGORIES
    subset = 'test' if test else 'train'
    data = fetch_20newsgroups(subset=subset, categories=categories,
                              shuffle=True, random_state=42,
                              remove=remove)
    return data.data[:size], data.target[:size], data.target_names


@pytest.fixture(scope="session")
def newsgroups_train():
    return _get_newsgroups(remove_chrome=True)


@pytest.fixture(scope="session")
def newsgroups_train_binary():
    return _get_newsgroups(binary=True, remove_chrome=True)
