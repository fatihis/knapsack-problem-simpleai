#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function

from random import random, randint, choice, uniform, sample
from simpleai.search import SearchProblem, hill_climbing, genetic, hill_climbing_random_restarts
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer
'''
itmSize = input("Enter number of items")
itemSize = int(itmSize)
knapsackCapacity = input("Enter knapsack capacity")
weights = input("weights of each item (separate with '-' )")
values = input("values of each item (separate with '-' )")
'''

##FOR TESTING
weights = '12-16-13-11'
values = '15-14-13-12'
knapsackCapacity = '28'
itemSize = 4


def randomCharChange(str):
    s = list(str)
    randInt = randint(0, itemSize - 1)
    initNmber = s[randInt]
    if initNmber == '0':
        s[randInt] = '1'
    elif initNmber == '1':
        s[randInt] = '0'
    newState = "".join(s)
    print(newState)
    return newState


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


class knapsack(SearchProblem):
    def actions(self, state):
        changedState = randomCharChange(state)
        print('changed', changedState)
        return changedState;

    def result(self, state, action):
        print(state)
        return randomCharChange(state)

    def value(self, state):
        print('state ', state)
        listValues = string_to_list(values)
        lv = listValues[0]
        print('list value', lv)
        listWeights = string_to_list(weights)
        lw = listWeights[0]
        print('list weight', lw)
        listState = list(state)
        print('liststate', listState)
        totalValue = 0
        totalWeights = 0
        for i in range(len(lv)):
            print('list value item', lv[i])
            print('list state item', listState[i])

            totalValue = totalValue + int(lv[i]) * int(listState[i])
            totalWeights = totalWeights + int(lw[i]) * int(listState[i])

        if (totalWeights > int(knapsackCapacity)):
            print('over capacity')
            return 0
        else:
            print('value', totalValue)
            return totalValue

    def generate_random_state(self):
        numbers = '01'
        print(numbers)
        str = ''
        listStr = list(str)
        for i in range(itemSize):
            listStr.append(choice(numbers))

        print('liststr', listStr)
        resultStr = ''.join(listStr)
        return resultStr;

    def crossover(self, state1, state2):
        cut_point = randint(0, itemSize - 1)
        child = state1[:cut_point] + state2[cut_point:]
        return child

    def mutate(self, state):
        mutation = choice('01')
        mutation_point = randint(0, itemSize - 1)
        mutated = ''.join([state[i] if i != mutation_point else mutation
                           for i in range(len(state))])
        return mutated


problem = knapsack(initial_state='0101')
result = genetic(problem, mutation_chance=0.1,viewer=WebViewer())
print(result.state)
print(result.path())

'''
problem = knapsack(initial_state='0101')
result = hill_climbing(problem, viewer=ConsoleViewer())
print(result.state)
print(result.path())
'''
'''
problem = knapsack(initial_state='0101')
result = hill_climbing_random_restarts(problem, viewer=ConsoleViewer())
print(result.state)
print(result.path())
'''