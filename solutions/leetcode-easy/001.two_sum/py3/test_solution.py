from typing import List
from solution import Solution
import pytest

@pytest.fixture
def solution_given() -> Solution:
    return Solution()


"""
Constraint Tests for Given Input.
"""

def test_raise_error_for_extreme_nums_length(solution_given: Solution)-> None:
    """
    Test if the solution raises an error when the length of nums is too extreme (either too short or exceeds the allowed limit).
    """
    with pytest.raises(ValueError):
        solution_given.two_sum([1000], 9);
    with pytest.raises(ValueError):
        given_arr: List[int] = list(range(1,10**5));
        solution_given.two_sum(given_arr, 9);

def test_raise_error_for_extreme_num_values(solution_given: Solution)-> None:
    """
    Test if the solution raises an error when elements in nums are too extreme (values outside the allowed range).
    """
    with pytest.raises(ValueError):
        solution_given.two_sum([1, 10**17], 9);

def test_raise_error_for_extreme_target_value(solution_given: Solution)-> None:
    """
    Test if the solution raises an error when the target value is too extreme (outside the allowed range).
    """
    with pytest.raises(ValueError):
        solution_given.two_sum([1,2], 10**17);

"""
Test Cases given by LeetCode
"""
def test_case_one(solution_given: Solution)-> None:
    """
    two_sum([2, 7, 11, 15])
    >>> [0, 1]
    """
    given_nums: List[int] = [2, 7, 11, 15];
    given_target: int = 9;
    result: List[int] = solution_given.two_sum(given_nums, given_target);
    assert result == [0, 1], f"Expect result should be [0, 1], but got {result}"

def test_case_two(solution_given: Solution)-> None:
    """
    two_sum([3, 2, 4])
    >>> [1, 2]
    """
    given_nums: List[int] = [3, 2, 4];
    given_target: int = 6;
    result: List[int] = solution_given.two_sum(given_nums, given_target);
    assert result == [1, 2], f"Expect result should be [1, 2], but got {result}"

def test_case_three(solution_given: Solution)-> None:
    """
    two_sum([3, 3])
    >>> [0, 1]
    """
    given_nums: List[int] = [3, 3];
    given_target: int = 6;
    result: List[int] = solution_given.two_sum(given_nums, given_target);
    assert result == [0, 1], f"Expect result should be [0, 1], but got {result}"
